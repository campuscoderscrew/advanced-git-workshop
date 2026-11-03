"""Search the inventory by name."""


def search(inventory, term):
    """Return the names of items containing term."""
    return [name for name in inventory.items() if term.lower() in name.lower()]
