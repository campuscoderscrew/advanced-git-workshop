import unittest

from pantry.inventory import Inventory
from pantry.search import search


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
        for name in ["Oat Milk", "bread", "milk"]:
            self.inv.add(name, 1, 1.0)

    def test_case_insensitve(self):
        self.assertEqual(search(self.inv, "MILK"), ["milk", "Oat Milk"])

    def test_no_match(self):
        self.assertEqual(search(self.inv, "cheese"), [])


if __name__ == "__main__":
    unittest.main()
