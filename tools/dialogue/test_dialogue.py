"""Authoring regression checks for names and fail-closed story sources."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import dialogue as D


class AuthoringTest(unittest.TestCase):
    def source(self, heading):
        with tempfile.TemporaryDirectory(dir=D.PROJECT / 'build') as folder:
            path = Path(folder) / 'source.txt'
            path.write_text(heading + '\nThe kettle is warm beside the desk.\n', encoding='utf-8', newline='\n')
            with patch.object(D, 'sources', side_effect=lambda gated: ({path: 'lines'} if gated else {}, {}, {})):
                return D.load_all()

    def test_story_index_alone_never_opens_a_story_line(self):
        with self.assertRaisesRegex(D.Error, 'explicit when'):
            self.source('## chat.village story=story.ch1.done fn=react')

    def test_story_sources_also_need_their_index(self):
        with self.assertRaisesRegex(D.Error, 'story='):
            self.source('## chat.village fn=react | when: {"flag":"story.ch1.done"}')

    def test_a_real_story_gate_is_kept_on_the_compiled_item(self):
        lines, _, _ = self.source('## chat.village story=story.ch1.done fn=react | when: {"flag":"story.ch1.done"}')
        self.assertEqual({'flag': 'story.ch1.done'}, lines[0]['when'])
        self.assertTrue(lines[0]['gated'])

    def test_given_names_cannot_leak_into_written_dialogue(self):
        with self.assertRaisesRegex(D.Error, 'literal name'):
            D.check_text('fixture', 'Ask Atsuko about it.', [], {}, False)
        D.check_text('fixture', 'Ask {given:role:sensei} about it.', [], {}, False)


if __name__ == '__main__':
    unittest.main()
