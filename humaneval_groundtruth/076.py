
def is_simple_power(x: int, n: int):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    assert type(x) == int and type(n) == int, "invalid inputs" # $_CONTRACT_$
    if x == 1: return True
    if n == 0: return x == 0
    if n == 1: return x == 1
    if n == -1: return abs(x) == 1
    p = n
    while abs(p) <= abs(x):
        if p == x: return True
        p = p * n
    return False

def check(candidate):

    # Check some simple cases
    assert candidate(16, 2)== True
    assert candidate(143214, 16)== False
    assert candidate(4, 2)==True
    assert candidate(9, 3)==True
    assert candidate(16, 4)==True
    assert candidate(24, 2)==False
    assert candidate(128, 4)==False
    assert candidate(12, 6)==False
    assert candidate(1, 4)==True
    assert candidate(2, 2)==True
    assert candidate(8, 2)==True
    assert candidate(3, 2)==False
    assert candidate(3, 1)==False
    assert candidate(5, 3)==False

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1)==True
    assert candidate(1, 12)==True


check(is_simple_power)