import unittest

from pantry.inventory import Inventory, OutOfStockError


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()

    def test_add_and_quantity(self):
        self.inv.add("apples", 3, 0.5)
        self.inv.add("apples", 2, 0.5)
        self.assertEqual(self.inv.quantity("apples"), 5)

    def test_remove_some(self):
        self.inv.add("apples", 5, 0.5)
        self.inv.remove("apples", 2)
        self.assertEqual(self.inv.quantity("apples"), 3)

    def test_remove_all_stock(self):
        self.inv.add("apples", 5, 0.5)
        self.inv.remove("apples", 5)
        self.assertEqual(self.inv.quantity("apples"), 0)

    def test_remove_too_many(self):
        self.inv.add("apples", 1, 0.5)
        with self.assertRaises(OutOfStockError):
            self.inv.remove("apples", 2)

    def test_total_value(self):
        self.inv.add("apples", 3, 0.5)
        self.inv.add("bread", 1, 2.25)
        self.assertEqual(self.inv.total_value(), 3.75)

    def test_total_value_does_not_truncate_cents(self):
        # 1.15 * 100 == 114.99999999999999 in floating point; int() dropped a cent
        self.inv.add("milk", 1, 1.15)
        self.assertEqual(self.inv.total_value(), 1.15)


if __name__ == "__main__":
    unittest.main()
