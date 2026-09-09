import argparse
import tempfile
import unittest
from datetime import date
from pathlib import Path

from tools.new_entry import create_entry, parse_date, slugify


class NewEntryTests(unittest.TestCase):
    def test_slugify_normalizes_topic(self) -> None:
        self.assertEqual(slugify("Python File Safety"), "python-file-safety")

    def test_slugify_rejects_empty_slug(self) -> None:
        with self.assertRaises(ValueError):
            slugify("---")

    def test_parse_date_requires_iso_format(self) -> None:
        self.assertEqual(parse_date("2026-09-09"), date(2026, 9, 9))
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_date("09/09/2026")

    def test_create_entry_writes_template_and_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = create_entry(
                root,
                date(2026, 9, 9),
                "Atomic Files",
                "Learned why exclusive creation protects existing notes.",
            )

            self.assertEqual(path.name, "2026-09-09-atomic-files.md")
            self.assertIn("## Verification", path.read_text(encoding="utf-8"))
            with self.assertRaises(FileExistsError):
                create_entry(root, date(2026, 9, 9), "Atomic Files", "Again")


if __name__ == "__main__":
    unittest.main()
