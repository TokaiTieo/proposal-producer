"""Local installation tests; no network access or user-global writes."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent


class Installation(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.work = Path(self.temporary.name)
        self.dest = self.work / 'skills'

    def tearDown(self):
        self.temporary.cleanup()

    def run_install(self, *arguments, root=ROOT, code=0):
        result = subprocess.run([sys.executable, str(root / 'install.py'), '--dest', str(self.dest), *arguments], capture_output=True, text=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return json.loads(result.stdout or result.stderr)

    def test_fresh_install_and_repeat(self):
        self.assertEqual(self.run_install()['action'], 'install')
        self.assertTrue((self.dest / 'proposal-producer/SKILL.md').is_file())
        self.assertEqual(self.run_install()['action'], 'unchanged')

    def test_dry_run_does_not_write(self):
        self.assertTrue(self.run_install('--dry-run')['dry_run'])
        self.assertFalse(self.dest.exists())

    def test_existing_changes_require_update(self):
        self.run_install()
        file = self.dest / 'proposal-producer/SKILL.md'
        file.write_text('LOCAL USER CHANGE')
        self.run_install(code=2)
        self.assertEqual(file.read_text(), 'LOCAL USER CHANGE')

    def test_update_preserves_backup(self):
        self.run_install()
        file = self.dest / 'proposal-producer/SKILL.md'
        file.write_text('LOCAL USER CHANGE')
        result = self.run_install('--update')
        self.assertEqual((Path(result['backup']) / 'SKILL.md').read_text(), 'LOCAL USER CHANGE')
        self.assertIn('name: proposal-producer', file.read_text())
        self.assertNotIn(str(self.dest) + '/', result['backup'])

    def test_tampered_payload_is_rejected(self):
        copy = self.work / 'repo'
        copy.mkdir()
        for name in ['install.py']:
            shutil.copy2(ROOT / name, copy / name)
        file = copy / 'install.py'
        file.write_text(file.read_text().replace('ffc55ef6463635a152dd576f76e725a40ffff6eadf59d441b0dc0dc270189664', '0000000000000000000000000000000000000000000000000000000000000000', 1))
        self.run_install(root=copy, code=2)
        self.assertFalse(self.dest.exists())

    def test_project_location(self):
        result = subprocess.run([sys.executable, str(ROOT / 'install.py'), '--project', str(self.work / 'project')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.work / 'project/.agents/skills/proposal-producer/SKILL.md').is_file())


if __name__ == '__main__':
    unittest.main(verbosity=2)
