"""Regression checks for portable generated-output validation."""
import io
import json
import math
from pathlib import Path
import tempfile
import unittest

from PIL import Image

from output_checks import matches


def png(image, level=6):
    buffer = io.BytesIO()
    image.save(buffer, 'PNG', compress_level=level)
    return buffer.getvalue()


class OutputChecksTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)

    def test_png_compression_changes_preserve_pixels(self):
        image = Image.new('RGBA', (16, 16), (20, 40, 60, 255))
        path = self.root / 'image.png'
        path.write_bytes(png(image, 0))
        self.assertNotEqual(path.read_bytes(), png(image, 9))
        self.assertTrue(matches(path, png(image, 9)))

    def test_png_rejects_changed_pixel_alpha_size_or_mode(self):
        original = Image.new('RGBA', (2, 2), (10, 20, 30, 255))
        path = self.root / 'image.png'
        path.write_bytes(png(original))
        changed = original.copy()
        changed.putpixel((0, 0), (11, 20, 30, 255))
        alpha = original.copy()
        alpha.putpixel((0, 0), (10, 20, 30, 254))
        for image in (changed, alpha, original.resize((3, 3)), original.convert('RGB')):
            with self.subTest(mode=image.mode, size=image.size):
                self.assertFalse(matches(path, png(image)))

    def test_json_accepts_native_math_roundoff_and_formatting(self):
        path = self.root / 'mesh.json'
        path.write_text(json.dumps({'pivot': [2.2943057454041846], 'name': 'mesh'}, indent=2) + '\r\n')
        self.assertTrue(matches(path, json.dumps({'name': 'mesh', 'pivot': [2.294305745404184]}).encode()))

    def test_json_rejects_real_changes_keys_order_and_types(self):
        path = self.root / 'mesh.json'
        path.write_text(json.dumps({'value': 1.0, 'ids': [1, 2], 'enabled': True}))
        for changed in (
            {'value': 1.00000001, 'ids': [1, 2], 'enabled': True},
            {'value': 1.0, 'ids': [2, 1], 'enabled': True},
            {'value': 1.0, 'ids': [1, 2], 'enabled': 1},
            {'value': 1.0, 'ids': [1, 2]},
        ):
            with self.subTest(changed=changed):
                self.assertFalse(matches(path, json.dumps(changed).encode()))

    def test_missing_corrupt_and_other_files(self):
        self.assertFalse(matches(self.root / 'missing.png', b'png'))
        path = self.root / 'broken.png'
        path.write_bytes(b'broken')
        self.assertFalse(matches(path, png(Image.new('RGBA', (1, 1)))))
        path = self.root / 'exact.txt'
        path.write_bytes(b'a')
        self.assertTrue(matches(path, b'a'))
        self.assertFalse(matches(path, b'b'))


if __name__ == '__main__':
    unittest.main()
