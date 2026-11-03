"""EXPERIMENTAL: move prices to Decimal. Not finished, do not ship."""
from decimal import ROUND_HALF_UP, Decimal


def to_money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# TODO: wire this into Inventory
