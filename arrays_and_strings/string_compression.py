def string_compression(s):
    """
    Implement a method to perform basic string compression using the counts of repeated characters. 
    For example, the string aabcccccaaa would become a2b1c5a3.
    If the compressed string would not become smaller than the original string, your method
    should return the original string. You can assume the string has only uppercase and
    lowercase letters (a-z)
    """
    compressed = ""
    x = 0
    while x < len(s):
        count = 0
        c = s[x]
        while x < len(s) and c == s[x]:
            count += 1
            x += 1
        compressed += c + str(count)

    return compressed if len(compressed) < len(s) else s

print(string_compression("aabccccaaa"))
