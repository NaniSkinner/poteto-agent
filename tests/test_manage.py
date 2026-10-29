import importlib.util
import pathlib
import tempfile
import tomllib
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / 'scripts/manage.py'

class ProfileTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.exists(), 'profile helper not implemented')
        spec = importlib.util.spec_from_file_location('manage', SCRIPT)
        self.m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.m)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = pathlib.Path(self.tmp.name) / 'café "tea"'
        (self.root / 'poteto-advisor/references').mkdir(parents=True)
        (self.root / 'poteto-advisor/references/contract.md').write_text('# Contract 1.0.0\nUnicode 🍵\n', encoding='utf-8')
    def test_render_valid_unicode_toml(self):
        data = tomllib.loads(self.m.profile_text(self.root))
        self.assertEqual(data['name'], 'workflow-advisor')
        self.assertIn('🍵', data['developer_instructions'])
        self.assertIn(str(self.root), data['developer_instructions'])
    def test_matching_profile_and_idempotent_render(self):
        self.m.render(self.root)
        self.m.check(self.root)
        before = self.m.target(self.root).stat().st_mtime_ns
        self.m.render(self.root)
        self.assertEqual(before, self.m.target(self.root).stat().st_mtime_ns)
    def test_contract_drift_detected_read_only(self):
        self.m.render(self.root)
        p = self.m.target(self.root)
        before = p.read_bytes(), p.stat().st_mtime_ns
        (self.root / 'poteto-advisor/references/contract.md').write_text('changed', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'drift'):
            self.m.check(self.root)
        self.assertEqual(before, (p.read_bytes(), p.stat().st_mtime_ns))
    def test_unrelated_existing_file_preserved(self):
        p = self.m.target(self.root)
        p.parent.mkdir()
        p.write_text('unrelated', encoding='utf-8')
        with self.assertRaises(ValueError): self.m.render(self.root)
        self.assertEqual(p.read_text(), 'unrelated')
    def test_missing_check_creates_nothing(self):
        with self.assertRaises(ValueError): self.m.check(self.root)
        self.assertFalse(self.m.target(self.root).parent.exists())
    def test_symlink_destination_refused(self):
        elsewhere = pathlib.Path(self.tmp.name) / 'elsewhere'
        elsewhere.mkdir()
        (self.root / 'codex').symlink_to(elsewhere, target_is_directory=True)
        with self.assertRaises(ValueError): self.m.render(self.root)
        self.assertEqual(list(elsewhere.iterdir()), [])

if __name__ == '__main__': unittest.main()
