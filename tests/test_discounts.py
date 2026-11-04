import unittest

from pantry.discounts import Discount, lookup
from pantry.inventory import Inventory


class DiscountTests(unittest.TestCase):
    def test_lookup_is_case_insensitive(self):
        self.assertEqual(lookup("welcome10").percent, 10)

    def test_unknown_code(self):
        with self.assertRaises(ValueError):
            lookup("FREESTUFF")

    def test_apply(self):
        self.assertEqual(Discount("X", 20).apply(10.0), 8.0)

    def test_discounted_total(self):
        inv = Inventory()
        inv.add("bread", 4, 2.5)
        self.assertEqual(inv.discounted_total("STUDENT20"), 8.0)


if __name__ == "__main__":
    unittest.main()
