import unittest

from pantry.export import to_csv
from pantry.inventory import Inventory


class ExportTests(unittest.TestCase):
    def test_to_csv(self):
        inv = Inventory()
        inv.add("milk", 1, 1.15)
        self.assertEqual(to_csv(inv), "name,qty,price\nmilk,1,1.15\n")


if __name__ == "__main__":
    unittest.main()
