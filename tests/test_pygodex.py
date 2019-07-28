import contextlib
import os
import unittest
from unittest.mock import patch

from pygodex import Pygodex


class TestPygodex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with contextlib.suppress(FileNotFoundError):
            os.remove("tests/created_dex.json")
            os.remove("tests/created_dex2.json")

    @classmethod
    def tearDownClass(cls):
        with contextlib.suppress(FileNotFoundError):
            os.remove("tests/created_dex.json")
            os.remove("tests/created_dex2.json")

    def test_01_init(self):
        p = Pygodex()
        self.assertIsNone(p.user_dex)
        self.assertIsNone(p.pokedex_file)
        self.assertIsNotNone(p.base_dex)

    def test_02_load_fail(self):
        p = Pygodex()
        p.load("../../tests/some-nonexisting-pokedex-file.json")
        self.assertIsNone(p.user_dex)
        self.assertIsNone(p.pokedex_file)

    def test_03_load(self):
        p = Pygodex()
        p.load("../../tests/test_dex.json")
        self.assertIsNotNone(p.user_dex)
        self.assertIsNotNone(p.pokedex_file)

    def test_04_unload(self):
        p = Pygodex()
        p.unload()  # shouldn't fail

        p.load("../../tests/test_dex.json")
        p.unload()
        self.assertIsNone(p.user_dex)
        self.assertIsNone(p.pokedex_file)

        p.unload()  # shouldn't fail if called again

    def test_05_create(self):
        p = Pygodex()
        p.create("../../tests/created_dex.json")
        self.assertIsNotNone(p.user_dex)
        self.assertIsNotNone(p.pokedex_file)

    def test_06_auto_unload(self):
        p = Pygodex()
        p.load("../../tests/test_dex.json")

        with patch.object(p, "unload") as mock:
            p.load("../../tests/test_dex.json")
            mock.assert_called()

        with patch.object(p, "unload") as mock:
            p.create("../../tests/created_dex2.json")
            mock.assert_called()
