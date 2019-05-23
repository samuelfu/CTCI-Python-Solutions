def palindrome_permutation(s):
    """
    Given a string, write a function to check if it is a permutation
    of a palindrome.
    """
    s = ''.join(s.split())
    d = dict()
    count = 0
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in s:
        if d[c]%2 == 1:
            count += 1
    for key, value in d.items():
        print(key, value)
    return True if count%2 == 1 else False

print(palindrome_permutation("Tact Coa"))
