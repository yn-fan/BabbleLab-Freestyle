"""Package checks; these do not grade generated writing or humor."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAME = "babblelab-freestyle"
SKILL = ROOT / "skills" / NAME


class DistributionTest(unittest.TestCase):
    def test_retained_licenses_match_recorded_sources(self):
        lock = json.loads((SKILL / "sources.lock.json").read_text(encoding="utf-8"))
        self.assertRegex(lock["base"]["revision"], r"^[0-9a-f]{40}$")
        for entry in lock["retained_files"]:
            path = SKILL / entry["path"]
            self.assertTrue(path.resolve().is_relative_to(SKILL.resolve()))
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), entry["sha256"])
        self.assertEqual((ROOT / "LICENSE").read_bytes(), (SKILL / "LICENSE").read_bytes())

    def test_markdown_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            for target in re.findall(r"\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                self.assertTrue((path.parent / target.split("#")[0]).exists(), f"{path}: {target}")

    def test_standalone_install_keeps_all_skill_files_and_references(self):
        with tempfile.TemporaryDirectory() as temporary:
            parent = Path(temporary) / "个人 技能"
            result = subprocess.run([sys.executable, str(ROOT / "tools/install.py"),
                                     "--to", str(parent)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            installed = parent / NAME
            for source in SKILL.rglob("*"):
                if source.is_file() and "__pycache__" not in source.parts:
                    copy = installed / source.relative_to(SKILL)
                    self.assertEqual(source.read_bytes(), copy.read_bytes())
                    if copy.suffix == ".md":
                        for link in re.findall(r"\]\(([^\s)]+)\)", copy.read_text(encoding="utf-8")):
                            if "://" not in link and not link.startswith("#"):
                                self.assertTrue((copy.parent / link.split("#")[0]).exists())

    def test_existing_install_or_symlink_is_preserved(self):
        with tempfile.TemporaryDirectory() as temporary:
            parent = Path(temporary)
            installed = parent / NAME
            installed.mkdir()
            marker = installed / "my-file.txt"
            marker.write_text("keep", encoding="utf-8")
            command = [sys.executable, str(ROOT / "tools/install.py"), "--to", str(parent)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(), "keep")
        with tempfile.TemporaryDirectory() as temporary:
            parent = Path(temporary)
            (parent / NAME).symlink_to(parent / "missing")
            result = subprocess.run([sys.executable, str(ROOT / "tools/install.py"),
                                     "--to", str(parent)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((parent / "missing").exists())

    def test_recursive_destination_is_rejected_without_writing(self):
        parent = SKILL / "recursive-install-test"
        self.assertFalse(parent.exists())
        result = subprocess.run([sys.executable, str(ROOT / "tools/install.py"),
                                 "--to", str(parent)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(parent.exists())


if __name__ == "__main__":
    unittest.main()
