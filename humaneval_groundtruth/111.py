
def histogram(test: str):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    assert isinstance(test, str), "invalid inputs" # $_CONTRACT_$
    words = test.split(" ") # $_CONTRACT_$
    for word in words: # $_CONTRACT_$
        if word != "": # $_CONTRACT_$
            assert len(word) == 1 and word.islower(), "invalid inputs" # $_CONTRACT_$

    if test == "": return {}    
    count, ans = dict(), dict()
    for word in test.split(" "):
        if word != "":
            if word not in count: count[word] = 0
            count[word] += 1
    mx = max(list(count.values()))
    for ch, c in count.items():
        if c == mx:
            ans[ch] = c
    return ans

def check(candidate):

    # Check some simple cases
    assert candidate('a b b a') == {'a':2,'b': 2}
    assert candidate('a b c a b') == {'a': 2, 'b': 2}
    assert candidate('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}
    assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}
    assert candidate('b b b b a') == {'b': 4}
    assert candidate('r t g') == {'r': 1,'t': 1,'g': 1}
    
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('') == {}
    assert candidate('a') == {'a': 1}


check(histogram)