"""Release consistency and offline relocation contracts."""
import importlib.util
from pathlib import Path
import shutil
import socket
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("release_builder", ROOT / "scripts/build_release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class PortabilityTests(unittest.TestCase):
    def test_generated_metadata_and_full_reader_match_sources(self):
        for name, expected in release.generated_files().items():
            with self.subTest(path=name):
                self.assertEqual((ROOT / name).read_bytes(), expected.encode("utf-8"))

    def test_relocated_runtime_installs_without_network_and_retains_license(self):
        with tempfile.TemporaryDirectory(prefix="nne portable ") as temp:
            base = Path(temp)
            source = base / "副本" / "no-negative-echo"
            shutil.copytree(ROOT / "no-negative-echo", source,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            with patch.object(socket, "socket", side_effect=AssertionError("network requested")):
                target = release.installer.install_skill(
                    source, base / "host skills",
                    expected_provenance_sha256=release.installer.CURRENT_PROVENANCE_SHA256)
            for relative in release.installer.RUNTIME_FILES:
                self.assertEqual((target / relative).read_bytes(), (source / relative).read_bytes())
            self.assertEqual((target / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())

    def test_previous_release_keeps_its_exact_manifest_shape(self):
        previous = release.installer.PREVIOUS_PROVENANCE_RUNTIME_FILES[
            "41e324f77249235fc34c61388ceba3dd9230938bf19b14eb1af21c4f1eaddf4f"]
        self.assertNotIn(Path("LICENSE"), previous)
        self.assertEqual(previous | {Path("LICENSE")}, release.installer.RUNTIME_FILES)


if __name__ == "__main__":
    unittest.main()
