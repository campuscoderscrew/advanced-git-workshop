import unittest

from pantry.inventory import Inventory
from pantry.reports import format_line, low_stock, stock_report


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
        self.inv.add("apples", 6, 0.5)
        self.inv.add("milk", 1, 1.15)

    def test_low_stock(self):
        self.assertEqual(low_stock(self.inv), ["milk"])

    def test_format_line(self):
        line = format_line("apples", {"qty": 6, "price": 0.5})
        self.assertEqual(line, "apples: 6")

    def test_stock_report_is_sorted(self):
        self.assertEqual(stock_report(self.inv).splitlines()[0], "apples: 6")


if __name__ == "__main__":
    unittest.main()
