def string_rotation(s1, s2):
    """
    given two strings, s1 and s2, write code to check
    if s2 is a rotation of s1 using only one call to
    isSubstring() (assume method isSubstring which checks if one word is a substring of another)
    e.g., "waterbottle" is a rotation of "erbottlewat"
    """

    for x in range(len(s2)):
        if s2[x:] + s2[:x] == s1:
            return True

    return False

print(string_rotation("waterbottle", "erbottlewat"))
