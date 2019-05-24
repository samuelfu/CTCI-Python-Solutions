def one_away(s1, s2):
    """
    There are three types of edits that can be performed on strings.
    Insert a character, remove a character, or replace a character.
    Given two strings, write a function to check if they are one edit (or zero edits) away.
    """
    if s1 == s2:
        return True

    for x in range(len(s1)):
        for y in range(len(s2)):
            if s1[:x] + s1[x+1:] == s2:
                return True
            if s1[:x] + s1[x+1:] == s2[:y] + s2[y+1:]:
                return True
            if s1 == s2[:y] + s2[y+1:]:
                return True
    return False

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
