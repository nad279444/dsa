"""Check whether a string reads the same forwards and backwards.

Approach: build the reversed string by prepending every character to an
accumulating result, then compare the two strings position by position with
zip — the first mismatch means it is not a palindrome; finishing the loop means
every mirrored pair matched. Equal-length strings are guaranteed by the
reversal, so zip never truncates a real mismatch.
Time: O(n^2) because each prepend rebuilds the string; Space: O(n).
"""


def reverse(s: str) -> str:
    result = ""
    for char in s:
        result = char + result
    return result


def palindrome_check(palindrome: str):
    reversed_str = reverse(palindrome)
    for item, reverse_item in zip(palindrome, reversed_str):
        if item != reverse_item:
            return False
    return True


if __name__ == "__main__":
    # Mirrored around the centre -> palindrome
    assert palindrome_check("abcdcba") is True

    # 'e' breaks the mirror -> not a palindrome
    assert palindrome_check("abedcba") is False

    # Symmetrical even-length palindrome
    assert palindrome_check("abba") is True

    # Single character / empty string are trivially palindromes
    assert palindrome_check("a") is True
    assert palindrome_check("") is True

    print("All tests passed")
