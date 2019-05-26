def one_away(s1, s2):
    """
    There are three types of edits that can be performed on strings.
    Insert a character, remove a character, or replace a character.
    Given two strings, write a function to check if they are one edit (or zero edits) away.
    """
    if s1 == s2:
        return True

    if len(s1) == len(s2):
        count = 0
        for x in range(len(s1)):
            if s1[x] != s2[x]:
                if count == 1:
                    return False
                count += 1
        return True
    elif len(s1) > len(s2):
        for x in range(len(s1)):
            if s1[:x] + s1[x+1:] == s2:
                return True
    else:
        for x in range(len(s2)):
            if s2[:x] + s2[x+1:] == s1:
                return True

    return False

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
