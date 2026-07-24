"""trace_function.py — a small function with SUCCESSIVE `if` statements.

FROZEN specimen. Do not edit it. Predict each printed result on paper first,
then run to confirm.

`gate_fee` is the per-scan handling fee the box office charges. Note these are
successive `if`s, NOT `elif`: every `if` runs in order, so a later check can
overwrite an earlier result. The ORDER of the checks is part of the behavior.

  * amount == 30 -> `30 > 30` is False, so `fee` stays 2 (the boundary excludes 30)
  * amount == 61 -> `> 30` sets 4, then `> 60` overwrites it to 7 (both run)
  * comp == True -> the last `if` resets `fee` to 0, whatever it was before
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
