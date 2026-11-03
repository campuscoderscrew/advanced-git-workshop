"""Tiny demo CLI.  Run with:  python -m pantry.cli"""
from pantry.inventory import Inventory
from pantry.reports import low_stock, stock_report


def demo_inventory():
    inv = Inventory()
    inv.add("apples", 6, 0.5)
    inv.add("bread", 2, 2.25)
    inv.add("milk", 1, 1.15)
    return inv


def main():
    inv = demo_inventory()
    print("DEBUG raw items:", inv.items())  # TODO remove before merging
    print(stock_report(inv))
    print(f"Total value: ${inv.total_value():.2f}")
    low = low_stock(inv)
    if low:
        print("Low stock: " + ", ".join(low))


if __name__ == "__main__":
    main()
