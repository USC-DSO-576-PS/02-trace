"""The per-scan handling fee the box office charges at the gate.

Prints the fee for a few representative scans.
"""


def gate_fee(amount, comp):
    fee = 2
    if amount > 30:
        fee = 4
    if amount > 60:
        fee = 7
    if comp:
        fee = 0
    return fee


for amount, comp in [(30, False), (61, False), (61, True)]:
    print(f"gate_fee({amount}, {comp}) -> {gate_fee(amount, comp)}")
