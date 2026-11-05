"""Export the inventory to CSV."""
import csv
import io


def to_csv(inventory):
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(["name", "qty", "price"])
    for name, d in sorted(inventory.items().items()):
        writer.writerow([name, d["qty"], f"{d['price']:.2f}"])
    return buf.getvalue()
