def is_unique(s):
    """
    Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures?
    """
    d = dict()
    for c in s:
        if c in d:
            return False
        else:
            d[c] = 1
    return True

print(is_unique("hiiiiiii"))
