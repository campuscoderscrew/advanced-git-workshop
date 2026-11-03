"""Core inventory model for the pantry app."""


class OutOfStockError(Exception):
    """Raised when removing more of an item than is in stock."""


class Inventory:
    def __init__(self):
        self._items = {}  # name -> {"qty": int, "price": float}

    def add(self, name, qty, price):
        if qty <= 0:
            raise ValueError("qty must be positive")
        item = self._items.setdefault(name, {"qty": 0, "price": price})
        item["qty"] += qty
        item["price"] = price

    def remove(self, name, qty):
        current = self.quantity(name)
        if qty > current:
            raise OutOfStockError(f"only {current} {name} left")
        self._items[name]["qty"] = current - qty

    def quantity(self, name):
        return self._items.get(name, {"qty": 0})["qty"]

    def total_value(self):
        """Total value of everything in stock, in dollars."""
        total = sum(d["qty"] * d["price"] for d in self._items.values())
        return round(total, 2)

    def items(self):
        return {name: dict(data) for name, data in self._items.items()}
