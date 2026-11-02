"""Discount codes for checkout."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Discount:
    code: str
    percent: int

    def apply(self, amount):
        if not 0 < self.percent <= 100:
            raise ValueError("percent must be 1-100")
        return round(amount * (100 - self.percent) / 100, 2)


CODES = {
    "WELCOME10": Discount("WELCOME10", 10),
    "STUDENT20": Discount("STUDENT20", 20),
}


def lookup(code):
    try:
        return CODES[code.upper()]
    except KeyError:
        raise ValueError(f"unknown discount code: {code}") from None
