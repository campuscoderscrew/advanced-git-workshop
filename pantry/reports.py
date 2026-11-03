"""Human-readable reports."""

LOW_STOCK_THRESHOLD = 3


def low_stock(inventory, threshold=LOW_STOCK_THRESHOLD):
    """Names of items at or below the threshold, alphabetically."""
    return sorted(
        name for name, d in inventory.items().items() if d["qty"] <= threshold
    )


def format_line(name, data):
    return f"{name}: {data['qty']} @ ${data['price']:.2f}"


def stock_report(inventory):
    lines = [format_line(n, d) for n, d in sorted(inventory.items().items())]
    return "\n".join(lines)
