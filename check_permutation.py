def check_permutation(s1, s2):
    """
    Given two strings, write a method to decide if one is a permutation of the other
    """
    d = dict()
    for c in s1:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in s2:
        if c not in d:
            return False
        else:
            if d[c] == 0:
                return False
            d[c] -= 1
    return True

print(check_permutation("banana", "nanaba"))
