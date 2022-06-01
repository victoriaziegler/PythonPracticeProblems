# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.


def remove_duplicate_letters(s):
    result = ""
    string = list(s)
    new_list = []
    if len(s) == 0:
        return None
    for letter in string:
        if letter not in result:
            new_list.append(letter)
        result = "".join(new_list)
    return result


s = ("abccbaccc")
print(remove_duplicate_letters(s))

s2 = ()
print(remove_duplicate_letters(s2))
