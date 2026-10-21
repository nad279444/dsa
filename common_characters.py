"""Return the unique characters that appear in EVERY string of the list.

Approach: treat each string as a character set and intersect them all. Start
with the set of the first string, then intersect (`&`) it with each remaining
string — characters that are missing from any string are dropped as soon as
their string is reached. The result is a set, so duplicates within a string
never matter and ordering is not defined.
Time: O(total characters across all strings); Space: O(k) for k distinct chars.
"""


def common_characters(characters: list[str]):
    common = set(characters[0])
    # loop through the remaing strings
    for char in characters[1:]:
        # find the intersection with main and the remaining strings
        common = common & set(char)
    return common


if __name__ == "__main__":
    # 'b' and 'c' are the only letters in all three strings
    assert common_characters(["abc", "bcd", "cbaccd"]) == {"b", "c"}

    # No overlap between the strings
    assert common_characters(["abc", "def"]) == set()

    # A single string yields its own characters
    assert common_characters(["abc"]) == {"a", "b", "c"}

    # Duplicates inside a string do not change the result
    assert common_characters(["aab", "abb", "abbb"]) == {"a", "b"}

    print("All tests passed")
