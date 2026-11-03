"""Search the inventory by name."""


def search(inventory, term):
    """Return the names of items containing term."""
    matches = [n for n in inventory.items() if term.lower() in n.lower()]
    return sorted(matches, key=str.lower)
