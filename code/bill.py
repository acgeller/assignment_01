"""
bill.py — the Bill Splitter module.

This is a *module*: a collection of small, reusable functions. None of them read
input or print anything — they just take values in and return a value out. That's
what makes them easy to test (see tests/test_unit.py) and easy to reuse from the
console, notebook, and Streamlit interfaces (console.py, explore.ipynb, dashboard.py).

Your job: implement the four functions below so the Unit Tests in
tests/test_unit.py all pass. Each docstring says exactly what the function should
return — replace the `# TODO` line (and the `pass`) with your code.
"""


def tip_amount(subtotal, pct):
    """Return the tip: `pct` percent of `subtotal`, rounded to the nearest cent.

    >>> tip_amount(50, 20)
    10.0
    """
    
    return round (subtotal * pct / 100, 2)


def grand_total(subtotal, pct):
    """Return the subtotal plus the tip, rounded to the nearest cent.

    Hint: you can call tip_amount() from here.

    >>> grand_total(50, 20)
    60.0
    """
   
    return round (subtotal + tip_amount(subtotal, pct), 2)



def split_evenly(total, people):
    """Return each person's share of `total`, rounded to the nearest cent.

    Must raise ValueError if `people` is not greater than 0.

    >>> split_evenly(60, 4)
    15.0
    """
    if people <= 0:
        raise ValueError("Number of people must be greater than 0")
    return round(total / people, 2)


def is_generous(pct):
    """Return True when a tip percent is considered generous (20% or more).

    >>> is_generous(20)
    True
    """
    if pct >= 20:
        return True
    return False

