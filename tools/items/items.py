"""Compiles the Shinobi Modpack's item registry, shops and crafting from the tables in tools/items/.

Every item id in the pack lives in catalogue/*.tsv (ITEMS.md). Shops, stock, jobs, services, stations, recipes
and kits are their own tables; outfits come from the wardrobe's collections and clans. The compiled JSON in
data/items/ is what Phase 0's Shinobi Life (and the life:economy module today) reads.

    python tools/items/items.py            # write data/items/*.json and docs/items/CATALOGUE.md
    python tools/items/items.py --check    # validate the tables and verify the compiled files are current
    python tools/items/items.py --stats    # counts by category, slice and art, and crafting savings

Never hand-edit the compiled files (economy.json is hand-edited: it is tuning, not compiled).

Catalogue columns:
  id        bare snake_case id, unique pack-wide; the registry name is <mod>:<id> (vanilla= / vf= rows reuse an
            existing item and only give it a price)
  category  tool weapon gear container consumable food ingredient scroll material furniture station keepsake
            curio key gift collectible pet currency outfit
  group     a sub-group for the catalogue and shop shelves
  rank      the first rank that uses it: any academy genin chunin jonin anbu kage
  slice     the first slice that needs it: beta1 beta2 beta2_5 beta3 later
  stack     1, 3, 16 or 64
  price     base buy price in ryo; 0 if it is never sold (given, crafted, found)
  sources   ways to get it besides shops, recipes and kits (those are added from their tables):
            kit:<kit> quest[:<id>] mission:<rank> salvage:<place> gather:<spot> drop:<enemy> event:<event>
            clan:<clan> (sold or given by that clan once its welcome quest is done) home:<place> service:<id>
            loot (a loot table in loot.tsv) vanilla vf
  use       what it does, in a sentence (tooltips are lang keys in Phase 0; this is the design text)
  gift      gift tags it satisfies for the bond engine's personalities (food:ramen, item:scroll ...)
  art       sprite (authored), tint:<base> (a palette variant of a sprite), icon (a simple sprite still to draw),
            model (a 3D held model), block (a Konoha block), wardrobe (from the wardrobe), vanilla, vf
  props     k=v;k=v: mechanics for the owning session (food=, buff=, durability=, block=, set=, sell= ...)
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = ROOT / 'data/items'
DOC = ROOT / 'docs/items/CATALOGUE.md'
WARDROBE = ROOT / 'tools/wardrobe'
PERSONALITY = ROOT / 'life/bonds/src/main/java/dev/shinobi/life/bond/Personality.java'

CATEGORIES = ('tool', 'weapon', 'gear', 'container', 'consumable', 'food', 'ingredient', 'scroll', 'material',
              'furniture', 'station', 'keepsake', 'curio', 'key', 'gift', 'collectible', 'pet', 'currency', 'outfit')
RANKS = ('any', 'academy', 'genin', 'chunin', 'jonin', 'anbu', 'kage')
SLICES = ('beta1', 'beta2', 'beta2_5', 'beta3', 'later')
STACKS = (1, 3, 16, 64)
ARTS = ('sprite', 'icon', 'model', 'block', 'wardrobe', 'vanilla', 'vf')
RESTOCKS = ('daily', '3d', 'weekly', 'once')
STATIONS_VF = {'cooking.pot', 'cooking.oven', 'cooking.prep'}
VESSELS = {'bowl', 'glass_bottle'}
# The mod that registers each category (props mod= overrides). ROADMAP §4: tools and techniques are Combat's;
# ryo, shops, crafting, food, furniture and pets are Life's; quests are Progression's; the wardrobe is Village's.
MOD_BY_CATEGORY = {'tool': 'shinobi_combat', 'weapon': 'shinobi_combat', 'gear': 'shinobi_combat',
                   'key': 'shinobi_progression', 'outfit': 'narutominecraft'}
OUTFIT_PRICES = {'academy': 100, 'civilian': 120, 'genin': 180, 'chunin': 320, 'jonin': 480, 'anbu': 0, 'kage': 0}
OUTFIT_SLICES = {'academy': 'beta1', 'civilian': 'beta1', 'genin': 'beta1', 'chunin': 'beta3', 'jonin': 'later',
                 'anbu': 'later', 'kage': 'later'}
# Gift ids the bond engine names that are vanilla items, not ours (Personality.java).
VANILLA_GIFTS = {'item:spider_eye', 'item:note_block', 'item:compass', 'item:amethyst_shard', 'item:glass', 'item:dirt',
                 'item:seeds', 'item:bone_meal', 'item:poisonous_potato', 'item:fishing_rod', 'item:gravel',
                 'item:iron_ingot', 'item:gold_nugget', 'item:spyglass', 'item:shield', 'item:planks', 'item:tnt',
                 'item:poppy', 'item:dandelion', 'item:rotten_flesh', 'item:dead_bush', 'item:bell'}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def table(path):
    """Rows of a TSV with a header line; '#' lines are comments and '-' is empty."""
    lines = [line for line in path.read_text(encoding='utf-8').splitlines() if line.strip() and not line.startswith('#')]
    rows = []
    for n, row in enumerate(csv.DictReader(lines, delimiter='\t', quoting=csv.QUOTE_NONE), start=2):
        if None in row or any(v is None for v in row.values()):
            err(f'{path.name}: row {n} has the wrong number of columns: {row}')
            continue
        rows.append({k: ('' if v == '-' else v) for k, v in row.items()})
    return rows


def props(text):
    out = {}
    for part in filter(None, text.split(';')):
        key, _, value = part.partition('=')
        out[key.strip()] = value.strip() if value else 'yes'
    return out


def split(text):
    return [s for s in text.split(';') if s]


def rank_index(rank):
    return RANKS.index(rank) if rank in RANKS else 0


def slice_index(s):
    return SLICES.index(s) if s in SLICES else len(SLICES)


# -- loading ------------------------------------------------------------------------------------------------------

def load_items():
    items = {}
    for path in sorted((HERE / 'catalogue').glob('*.tsv')):
        for row in table(path):
            iid = row['id']
            if iid in items:
                err(f'{path.name}: duplicate id {iid}')
            if not re.fullmatch(r'[a-z][a-z0-9_]*', iid):
                err(f'{path.name}: bad id {iid!r}')
            p = props(row['props'])
            art = row['art']
            category = row['category']
            item = {
                'id': iid, 'name': row['name'], 'category': category, 'group': row['group'],
                'rank': row['rank'], 'slice': row['slice'], 'stack': int(row['stack'] or 1),
                'price': int(row['price'] or 0), 'sources': split(row['sources']), 'use': row['use'],
                'gifts': split(row['gift']), 'art': art, 'props': p, 'file': path.name,
            }
            item['mod'] = p.pop('mod', None) or MOD_BY_CATEGORY.get(category, 'shinobi_life')
            if 'vanilla' in p:
                item['registry'], item['new'] = p['vanilla'], False
            elif 'vf' in p:
                item['registry'], item['new'] = p['vf'], False
            else:
                item['registry'], item['new'] = f"{item['mod']}:{iid}", True
            for key, allowed, label in (('category', CATEGORIES, 'category'), ('rank', RANKS, 'rank'), ('slice', SLICES, 'slice')):
                if item[key] not in allowed:
                    err(f'{path.name}: {iid} has an unknown {label} {item[key]!r}')
            if item['stack'] not in STACKS:
                err(f'{path.name}: {iid} stacks to {item["stack"]}')
            base = art.split(':')[0]
            if base not in ARTS + ('tint',):
                err(f'{path.name}: {iid} has an unknown art kind {art!r}')
            items[iid] = item
    for item in items.values():
        if item['art'].startswith('tint:') and item['art'][5:] not in items:
            err(f"{item['id']}: tint base {item['art'][5:]} is not an item")
    return items


def load_outfits():
    outfits = []
    for kind, folder in (('collection', 'collections'), ('clan', 'clans')):
        for path in sorted((WARDROBE / folder).glob('*.json')):
            data = json.loads(path.read_text(encoding='utf-8'))
            for o in data.get('outfits', []):
                rank = o.get('rank', 'genin')
                pieces = [o[k] for k in ('top', 'bottom', 'headwear', 'mask', 'extra') if o.get(k)]
                outfits.append({
                    'id': f"{data['id']}.{o['id']}", 'name': o['name'], 'source': f"{kind}:{data['id']}", 'rank': rank,
                    'pieces': pieces, 'palettes': o.get('palettes', []),
                    'price': OUTFIT_PRICES.get(rank, 200), 'slice': OUTFIT_SLICES.get(rank, 'later'),
                    'sold_at': 'tailor' if kind == 'collection' and OUTFIT_PRICES.get(rank, 0) else
                               ('tailor:clan_members' if OUTFIT_PRICES.get(rank, 0) else 'given'),
                })
    return outfits


def load_variants():
    variants = defaultdict(dict)
    for row in table(HERE / 'variants.tsv'):
        variants[row['item']][row['variant']] = {'name': row['name'], 'rank': row['rank'], 'slice': row['slice'],
                                                  'price': int(row['price'] or 0), 'notes': row['notes']}
    return variants


def ingredients(text):
    """'a*2;b' -> [('a', 2), ('b', 1)]"""
    out = []
    for part in split(text):
        name, _, n = part.partition('*')
        out.append((name, int(n or 1)))
    return out


# -- checks -------------------------------------------------------------------------------------------------------

def check_loot(items, loot):
    tables = defaultdict(list)
    for row in loot:
        if row['item'] not in items:
            err(f"loot {row['table']}: unknown item {row['item']}")
        if not re.fullmatch(r'\d+(-\d+)?', row['count']) or int(row['weight'] or 0) <= 0:
            err(f"loot {row['table']}: bad weight or count for {row['item']}")
        tables[row['table']].append(row)
    for item in items.values():
        if 'loot' in item['sources'] and not any(r['item'] == item['id'] for r in loot):
            err(f"{item['id']}: says it is loot but no loot table drops it")
    return tables


def check_all(items, shops, stock, jobs, services, stations, recipes, kits, variants, outfits, economy):
    shop_ids = {s['id'] for s in shops}
    job_ids = {j['id'] for j in jobs}
    station_ids = {s['id'] for s in stations} | STATIONS_VF

    for s in shops:
        for key in ('opens', 'closes'):
            if not re.fullmatch(r'\d\d:\d\d', s[key]):
                err(f"shop {s['id']}: {key} {s[key]!r} is not HH:MM")
        if not s['keeper'].startswith('role:'):
            err(f"shop {s['id']}: keeper must be a role")
        if not s['interior']:
            err(f"shop {s['id']}: no interior blocks")
        if s['slice'] not in SLICES:
            err(f"shop {s['id']}: slice {s['slice']}")
        if s['haggle'] not in ('no', 'yes', 'pawn'):
            err(f"shop {s['id']}: haggle {s['haggle']}")
    for row in stock:
        iid, shop = row['item'], row['shop']
        if shop not in shop_ids:
            err(f'stock: unknown shop {shop}')
            continue
        if iid not in items:
            err(f'stock: {shop} sells unknown item {iid}')
            continue
        if row['restock'] not in RESTOCKS:
            err(f"stock: {shop}/{iid} restock {row['restock']}")
        if row['pool'] not in ('core', 'rot'):
            err(f"stock: {shop}/{iid} pool {row['pool']}")
        item = items[iid]
        shop_slice = next(s['slice'] for s in shops if s['id'] == shop)
        if row['slice'] and slice_index(row['slice']) < slice_index(item['slice']):
            err(f"stock: {shop} sells {iid} in {row['slice']}, before the item exists ({item['slice']})")
        if row['slice'] and slice_index(row['slice']) < slice_index(shop_slice):
            warn(f"stock: {shop}/{iid} is listed for {row['slice']} but the shop opens in {shop_slice}")
        if row['variant'] and iid in variants and row['variant'] not in variants[iid]:
            err(f"stock: {shop} sells {iid} variant {row['variant']} which variants.tsv lacks")
        if not row['price'] and not item['price'] and iid not in variants and iid != 'folded_outfit':
            err(f'stock: {shop} sells {iid}, which has no price')
    sold = {r['item'] for r in stock}
    for row in recipes:
        if row['station'] not in station_ids:
            err(f"recipe {row['id']}: unknown station {row['station']}")
        for name, n in ingredients(row['inputs']) + [(row['output'], 1)]:
            if name not in items:
                err(f"recipe {row['id']}: unknown item {name}")
        slots = ingredients(row['inputs'])
        if row['station'] in STATIONS_VF:
            used = sum(n for name, n in slots if name not in VESSELS or row['station'] != 'cooking.pot')
            if used > 6:
                err(f"recipe {row['id']}: {used} grid slots at a VF station (6 at most; x*2 takes two slots)")
        elif len(slots) > 6:
            err(f"recipe {row['id']}: {len(slots)} slots (6 at most)")
        unlock = row['unlock']
        if unlock.startswith('job:'):
            _, job, n = unlock.split(':')
            if job not in job_ids:
                err(f"recipe {row['id']}: unlock names unknown job {job}")
        elif unlock.startswith('book:') and unlock[5:] not in items:
            err(f"recipe {row['id']}: unlock names unknown book {unlock[5:]}")
        elif unlock == 'blueprint' and items.get(row['output'], {}).get('category') not in ('furniture', 'station'):
            err(f"recipe {row['id']}: blueprints are for furniture")
        out = items.get(row['output'])
        if out and slice_index(row['slice']) < slice_index(out['slice']):
            err(f"recipe {row['id']}: in {row['slice']} but {out['id']} is {out['slice']}")
    for job in jobs:
        if job['shop'] not in shop_ids:
            err(f"job {job['id']}: unknown shop {job['shop']}")
        for step in split(job['teaches']):
            n, _, what = step.partition(':')
            kind, _, ref = what.partition(':')
            if kind == 'recipe' and ref not in {r['id'] for r in recipes}:
                err(f"job {job['id']}: teaches unknown recipe {ref}")
            if kind == 'blueprint' and ref not in items:
                err(f"job {job['id']}: teaches a blueprint for unknown item {ref}")
    for sv in services:
        p = sv['provider']
        if not (p in shop_ids or p.startswith('place:') or p in ('housing_office', 'clan_registry', 'travel_desk')):
            err(f"service {sv['id']}: unknown provider {p}")
    for k in kits:
        if k['item'] not in items:
            err(f"kit {k['kit']}: unknown item {k['item']}")
    for st in stations:
        if st['home_item'] and st['home_item'] not in items:
            err(f"station {st['id']}: home item {st['home_item']} is not an item")

    crafted = {r['output'] for r in recipes}
    kitted = {k['item'] for k in kits}
    for item in items.values():
        iid = item['id']
        if not (iid in sold or iid in crafted or iid in kitted or item['sources']):
            err(f'{iid}: no way to get it (no shop, recipe, kit or source)')
        if item['price'] == 0 and iid in sold and iid not in variants and iid != 'folded_outfit' and \
                not any(r['item'] == iid and r['price'] for r in stock):
            err(f'{iid}: sold but has no price')
        if item['category'] == 'furniture' and item['new'] and not ({'block', 'vanilla_block'} & set(item['props'])):
            err(f'{iid}: furniture needs a block= request (or vanilla_block=)')

    # Crafting must never be a way to print ryo: what a crafted piece sells back for stays under what its inputs cost.
    for row in recipes:
        out = items.get(row['output'])
        if not out:
            continue
        cost = sum(max(items[n]['price'], sell_value(items[n], economy)) * k for n, k in ingredients(row['inputs']) if n in items)
        back = sell_value(out, economy) * int(row['count'] or 1)
        if back and back >= cost:
            err(f"recipe {row['id']}: sells back for {back}, its inputs cost {cost}: a craft-and-sell loop")

    # Every gift the bond engine's personalities name must be something you can give.
    if PERSONALITY.exists():
        named = set(re.findall(r'"((?:food|item):[a-z_]+)"', PERSONALITY.read_text(encoding='utf-8')))
        tagged = {g for item in items.values() for g in item['gifts']}
        for gift in sorted(named - tagged - VANILLA_GIFTS):
            err(f'gift {gift} (bond personalities) is met by no item')

    starter = [i for i in items.values() if i['props'].get('set') == 'starter']
    if not starter:
        err('no set=starter furniture: the economy is tuned around it')
    for wish, w in economy.get('wishes', {}).items():
        if wish.startswith('_'):
            continue
        for key in w.get('items', {}):
            iid, _, variant = key.partition('@')
            if iid not in items:
                err(f'economy.json wish {wish}: unknown item {iid}')
            elif variant and variant not in variants.get(iid, {}):
                err(f'economy.json wish {wish}: unknown variant {key}')
        if w.get('kind') == 'service' and w['id'] not in {s['id'] for s in services}:
            err(f"economy.json wish {wish}: unknown service {w['id']}")
    for name, profile in economy.get('profiles', {}).items():
        for sl, meals in profile['meals'].items():
            for meal in meals:
                if meal not in items and meal not in economy.get('meal_bundles', {}):
                    err(f'economy.json profile {name}: unknown meal {meal}')
    if not any(o['rank'] == 'academy' for o in outfits):
        err('no academy outfits in the wardrobe')
    if 'festival' in {r['variant'] for r in stock if r['item'] == 'folded_outfit'}:
        warn('folded_outfit variant "festival" (yukata): the wardrobe has no festival outfits yet (asked of the wardrobe owner)')


def sell_value(item, economy):
    if 'sell' in item['props']:
        return int(item['props']['sell'])
    share = economy['sell_back'].get(item['category'], economy['sell_back']['default'])
    return int(item['price'] * share)


# -- compile ------------------------------------------------------------------------------------------------------

def compile_all():
    items = load_items()
    variants = load_variants()
    outfits = load_outfits()
    shops = table(HERE / 'shops.tsv')
    stock = table(HERE / 'stock.tsv')
    jobs = table(HERE / 'jobs.tsv')
    services = table(HERE / 'services.tsv')
    stations = table(HERE / 'stations.tsv')
    recipes = table(HERE / 'recipes.tsv')
    kits = table(HERE / 'kits.tsv')
    loot = table(HERE / 'loot.tsv')
    economy = json.loads((OUT / 'economy.json').read_text(encoding='utf-8'))
    check_all(items, shops, stock, jobs, services, stations, recipes, kits, variants, outfits, economy)
    tables = check_loot(items, loot)
    for row in loot:
        src = 'loot:' + row['table']
        if row['item'] in items and src not in items[row['item']]['sources']:
            items[row['item']]['sources'].append(src)
    for item in items.values():
        if 'loot' in item['sources']:
            item['sources'].remove('loot')

    # Merge where each item comes from.
    for row in stock:
        if row['item'] in items:
            src = f"shop:{row['shop']}"
            if src not in items[row['item']]['sources']:
                items[row['item']]['sources'].append(src)
    for row in recipes:
        if row['output'] in items:
            station = row['station'].split('.')[0]
            src = f'craft:{station}'
            if src not in items[row['output']]['sources']:
                items[row['output']]['sources'].append(src)
    for k in kits:
        if k['item'] in items and k['kit'] not in items[k['item']]['sources']:
            items[k['item']]['sources'].append(k['kit'])

    order = {c: i for i, c in enumerate(CATEGORIES)}
    item_list = []
    for item in sorted(items.values(), key=lambda i: (order[i['category']], i['group'], i['id'])):
        entry = {k: item[k] for k in ('id', 'registry', 'new', 'name', 'mod', 'category', 'group', 'rank', 'slice',
                                      'stack', 'price')}
        entry['sell'] = sell_value(item, economy)
        entry['sources'] = item['sources']
        entry['use'] = item['use']
        if item['gifts']:
            entry['gifts'] = item['gifts']
        entry['art'] = item['art']
        if item['props']:
            entry['props'] = item['props']
        if item['id'] in variants:
            entry['variants'] = variants[item['id']]
        item_list.append(entry)

    files = {}
    files['items.json'] = {'format': 1, '_doc': 'Compiled by tools/items/items.py from tools/items/catalogue/*.tsv. Do not edit.',
                           'count': len(item_list), 'items': item_list}
    files['outfits.json'] = {'format': 1, '_doc': 'Every wardrobe outfit as a folded_outfit variant; compiled from tools/wardrobe collections and clans.',
                             'count': len(outfits), 'prices': OUTFIT_PRICES, 'outfits': outfits}

    def stock_entry(r):
        e = {'item': r['item']}
        for key in ('variant', 'rank', 'slice'):
            if r[key]:
                e[key] = r[key]
        e['qty'] = int(r['qty']) if r['qty'] else None
        e['restock'] = r['restock']
        if r['price']:
            e['price'] = int(r['price'])
        e['pool'] = r['pool']
        return e

    shop_list = []
    for s in shops:
        entry = {k: s[k] for k in ('id', 'name', 'district', 'keeper')}
        entry['staff'] = split(s['staff'])
        entry['hours'] = {'opens': s['opens'], 'closes': s['closes'], 'closed': s['closed'] or None}
        for k in ('slice', 'rank', 'standing', 'haggle'):
            entry[k] = s[k]
        entry['markup'] = float(s['markup'])
        entry['rotating'] = int(s['rotating'])
        entry['orders'] = split(s['orders'])
        entry['interior'] = split(s['interior'])
        entry['stock'] = [stock_entry(r) for r in stock if r['shop'] == s['id']]
        entry['jobs'] = [j['id'] for j in jobs if j['shop'] == s['id']]
        shop_list.append(entry)
    files['shops.json'] = {
        'format': 1, '_doc': 'Compiled from tools/items/shops.tsv, stock.tsv, jobs.tsv and services.tsv. Do not edit.',
        'shops': shop_list,
        'jobs': [{'id': j['id'], 'shop': j['shop'], 'rank': j['rank'], 'slice': j['slice'], 'window': j['window'],
                  'hours': int(j['hours']), 'pay': int(j['pay']), 'task': j['task'],
                  'teaches': [{'after': int(t.split(':', 1)[0]), 'what': t.split(':', 1)[1]} for t in split(j['teaches'])]}
                 for j in jobs],
        'services': [{'id': s['id'], 'provider': s['provider'], 'rank': s['rank'], 'slice': s['slice'],
                      'price': int(s['price']) if s['price'] else None, 'effect': s['effect'], 'note': s['note']}
                     for s in services],
    }

    def recipe_entry(r):
        inputs = ingredients(r['inputs'])
        e = {'id': r['id'], 'station': r['station']}
        if r['station'] == 'cooking.pot':
            vessel = [n for n, _ in inputs if n in VESSELS]
            inputs = [(n, k) for n, k in inputs if n not in VESSELS]
            e['vessel'] = vessel[0] if vessel else None
        e['inputs'] = [{'item': n, 'count': k} for n, k in inputs]
        e['output'] = {'item': r['output'], 'count': int(r['count'])}
        e['time'] = int(r['time'])
        e['rank'] = r['rank']
        e['slice'] = r['slice']
        e['unlock'] = r['unlock'] or None
        e['difficulty'] = int(r['difficulty'] or 0)
        return e

    files['recipes.json'] = {
        'format': 1, '_doc': 'Compiled from tools/items/stations.tsv and recipes.tsv. Do not edit. Cooking recipes become VF hearth_recipe data in Phase 0.',
        'stations': [{'id': s['id'], 'name': s['name'], 'blocks': split(s['blocks']), 'public': split(s['public']),
                      'home_item': s['home_item'] or None, 'slice': s['slice'], 'rank': s['rank'],
                      'max_grade': s['max_grade'], 'screen': s['screen'], 'why': s['why']} for s in stations],
        'recipes': [recipe_entry(r) for r in recipes],
    }
    kit_map = defaultdict(list)
    for k in kits:
        kit_map[k['kit']].append({'item': k['item'], 'count': int(k['count']), 'when': k['when'], 'note': k['note'] or None})
    described = {r['block']: r for r in table(HERE / 'blocks.tsv')}
    requests = {}
    for item in items.values():
        block = item['props'].get('block')
        if block and (item['new'] or block not in requests):
            r = requests.setdefault(block, {'block': f'block:{block}', 'kind': 'furniture' if item['category'] != 'keepsake' else 'display',
                                            'item': None, 'description': '', 'used_by': []})
            if item['category'] == 'keepsake':
                r['used_by'].append(f"item:{item['id']}")
            else:
                r['item'], r['description'] = f"item:{item['id']}", item['use']
    for s in shops:
        for entry in split(s['interior']):
            b, _, variant = entry.partition('@')
            r = requests.setdefault(b, {'block': f'block:{b}', 'kind': 'interior', 'item': None, 'description': '', 'used_by': []})
            r['used_by'].append(f"shop:{s['id']}" + (f'@{variant}' if variant else ''))
    for st in stations:
        for b in split(st['blocks']):
            if b.startswith('villagefriends:'):
                continue
            r = requests.setdefault(b, {'block': f'block:{b}', 'kind': 'station', 'item': None, 'description': '', 'used_by': []})
            r['used_by'].append(f"station:{st['id']}")
    for b, r in requests.items():
        d = described.get(b)
        if d:
            r['kind'], r['description'] = d['kind'], d['description']
        elif not r['description']:
            err(f'block {b} is requested but blocks.tsv does not describe it')
    for b in described:
        if b not in requests:
            warn(f'blocks.tsv describes {b}, which nothing uses')
    files['block_requests.json'] = {'format': 1, '_doc': 'Blocks asked of the Konoha build session (its tools/konoha/blocks.json owns them). Compiled from the catalogue, shops.tsv, stations.tsv and blocks.tsv.',
                                    'count': len(requests), 'blocks': sorted(requests.values(), key=lambda r: (r['kind'], r['block']))}
    files['loot.json'] = {'format': 1, '_doc': 'Loot tables (curios, salvage, drops, gathering, festival prizes), compiled from tools/items/loot.tsv. Do not edit.',
                          'tables': {t: [{'item': r['item'], 'weight': int(r['weight']), 'count': r['count']} for r in rows]
                                     for t, rows in sorted(tables.items())}}
    files['kits.json'] = {'format': 1, '_doc': 'Compiled from tools/items/kits.tsv. Do not edit.', 'kits': kit_map}
    return files, items, outfits, shops, stock, recipes, jobs, services, stations, variants, economy


def dumps(data):
    return json.dumps(data, indent=1, ensure_ascii=False) + '\n'


# -- the generated catalogue ----------------------------------------------------------------------------------------

def catalogue_md(items, outfits, shops, stock, recipes, stations, jobs, services):
    out = ['# Item catalogue', '',
           'Generated by `python tools/items/items.py` from the tables in `tools/items/`. Do not edit: change the',
           'tables and rerun. The design is in [ITEMS.md](../../ITEMS.md).', '']
    counts = Counter(i['category'] for i in items.values())
    out += ['| Category | Items |', '|---|---|'] + [f'| {c} | {counts[c]} |' for c in CATEGORIES if counts[c]]
    out += [f'| outfits (wardrobe, as `folded_outfit` variants) | {len(outfits)} |', '']
    for cat in CATEGORIES:
        rows = sorted((i for i in items.values() if i['category'] == cat), key=lambda i: (i['group'], i['id']))
        if not rows:
            continue
        out += [f'## {cat}', '', '| Id | Name | Group | Rank | Slice | Stack | Price | Sources | Use |',
                '|---|---|---|---|---|---|---|---|---|']
        for i in rows:
            src = ', '.join(i['sources'])
            out.append(f"| `{i['id']}` | {i['name']} | {i['group']} | {i['rank']} | {i['slice']} | {i['stack']} | "
                       f"{i['price'] or '—'} | {src} | {i['use']} |")
        out.append('')
    out += ['## Shops', '']
    for s in shops:
        out += [f"### {s['name']} (`{s['id']}`)", '',
                f"{s['district']}; {s['opens']} to {s['closes']}" + (f", closed {s['closed']}" if s['closed'] else '') +
                f"; from {s['slice']}; keeper `{s['keeper']}`; discount by `{s['standing']}` standing; haggle: {s['haggle']}.", '',
                '| Item | Variant | Rank | Slice | Qty | Restock | Pool |', '|---|---|---|---|---|---|---|']
        for r in stock:
            if r['shop'] == s['id']:
                out.append(f"| `{r['item']}` | {r['variant'] or ''} | {r['rank'] or ''} | {r['slice'] or ''} | "
                           f"{r['qty'] or '∞'} | {r['restock']} | {r['pool']} |")
        out.append('')
    out += ['## Recipes', '']
    for st in [s['id'] for s in stations] + sorted(STATIONS_VF):
        rows = [r for r in recipes if r['station'] == st or (st == 'cooking' and False)]
        if not rows:
            continue
        out += [f'### {st}', '', '| Recipe | Inputs | Output | Rank | Slice | Unlock |', '|---|---|---|---|---|---|']
        for r in rows:
            ins = ', '.join(f'{n} ×{k}' if k > 1 else n for n, k in ingredients(r['inputs']))
            out.append(f"| `{r['id']}` | {ins} | {r['output']} ×{r['count']} | {r['rank']} | {r['slice']} | {r['unlock'] or '—'} |")
        out.append('')
    return '\n'.join(out) + '\n'


# -- stats ----------------------------------------------------------------------------------------------------------

def art_class(item):
    art = item['art']
    if not item['new'] or art in ('vanilla', 'vf'):
        return 'reused'
    if art.startswith('tint:'):
        return 'tint'
    return art


def stats(items, outfits, shops, stock, recipes):
    print(f'{len(items)} items ({sum(1 for i in items.values() if i["new"])} new), {len(outfits)} outfits, '
          f'{len(shops)} shops, {len(stock)} stock lines, {len(recipes)} recipes')
    by = Counter((i['category']) for i in items.values())
    print('by category: ' + ', '.join(f'{c} {by[c]}' for c in CATEGORIES if by[c]))
    sl = Counter(i['slice'] for i in items.values())
    print('by slice:    ' + ', '.join(f'{s} {sl[s]}' for s in SLICES))
    art = Counter(art_class(i) for i in items.values())
    beta = Counter(art_class(i) for i in items.values() if i['slice'] != 'later')
    print('art (all / beta): ' + ', '.join(f'{k} {art[k]}/{beta[k]}' for k in ('sprite', 'tint', 'icon', 'model', 'block', 'wardrobe', 'reused')))
    print('crafting, input cost against the shop price:')
    for r in recipes:
        out = items[r['output']]
        cost = sum(items[n]['price'] * k for n, k in ingredients(r['inputs']))
        value = out['price'] * int(r['count'])
        if value:
            print(f"  {r['id']:24} {cost:5} for {value:5}  ({cost / value:4.0%})")


def main(argv):
    files, items, outfits, shops, stock, recipes, jobs, services, stations, variants, economy = compile_all()
    doc = catalogue_md(items, outfits, shops, stock, recipes, stations, jobs, services)
    for w in warnings:
        print('warning:', w)
    if errors:
        for e in errors:
            print('error:', e)
        print(f'{len(errors)} errors')
        return 1
    if '--stats' in argv:
        stats(items, outfits, shops, stock, recipes)
        return 0
    if '--check' in argv:
        stale = [name for name, data in files.items() if not (OUT / name).exists() or (OUT / name).read_text(encoding='utf-8') != dumps(data)]
        if not DOC.exists() or DOC.read_text(encoding='utf-8') != doc:
            stale.append(str(DOC.relative_to(ROOT)))
        if stale:
            print('stale (rerun python tools/items/items.py): ' + ', '.join(stale))
            return 1
        print(f'ok: {len(items)} items, {len(outfits)} outfits, {len(shops)} shops, {len(recipes)} recipes')
        return 0
    OUT.mkdir(parents=True, exist_ok=True)
    for name, data in files.items():
        (OUT / name).write_text(dumps(data), encoding='utf-8')
    DOC.parent.mkdir(parents=True, exist_ok=True)
    DOC.write_text(doc, encoding='utf-8')
    print(f'wrote {len(files)} files to {OUT.relative_to(ROOT)} and {DOC.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
