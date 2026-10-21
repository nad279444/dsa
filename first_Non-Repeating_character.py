"""Return the first character of the string that appears exactly once.

Approach: two passes over the string with a hash map. The first pass counts
occurrences of every character; the second pass walks the string in its
original order and returns the first character whose count is 1. Scanning the
string again (rather than the map) preserves input order. Returns -1 when
every character repeats.
Time: O(n); Space: O(k) for k distinct characters.
"""


def non_repeating_character(characters: str):
    count = {}

    for char in characters:
        count[char] = count.get(char, 0) + 1

    for char in characters:
        if count[char] == 1:
            return char

    return -1


if __name__ == "__main__":
    # 'b' is the first character that appears only once
    assert non_repeating_character("abcdcaf") == "b"

    # Every character repeats -> -1
    assert non_repeating_character("aabb") == -1

    # Counting happens in one pass, ordering is preserved by the second
    assert non_repeating_character("abcabcxyz") == "x"

    # Single character
    assert non_repeating_character("z") == "z"

    print("All tests passed")
