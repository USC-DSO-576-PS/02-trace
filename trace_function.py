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


print("gate_fee(30, False) ->", gate_fee(30, False))
print("gate_fee(61, False) ->", gate_fee(61, False))
print("gate_fee(61, True) ->", gate_fee(61, True))
