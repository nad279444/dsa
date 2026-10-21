"""Shift every lowercase letter in `text` forward by `key` positions (Caesar cipher).

Approach: for each character, find its index in the alphabet, add the key, and
take `% 26` so the shift wraps around (z + 1 -> a). Characters that are not
lowercase letters (spaces, digits, capitals) are left unchanged — they simply
fall through the lookup without matching.
Time: O(n * 26) = O(n) for the per-character alphabet scan; Space: O(n) output.
"""


def caesor_cipher(text: str, key: int):
    new_str = ""
    for char in text:
        new_char = generate_new_char(char, key)
        new_str += new_char
    return new_str


def generate_new_char(char: str, key: int) -> str:
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    for index, letter in enumerate(alphabet):
        if char == letter:
            new_index = (index + key) % 26
            return alphabet[new_index]
    return char


if __name__ == "__main__":
    # x -> z, y -> a, z -> b (wraps past the end of the alphabet)
    assert caesor_cipher("xyz", 2) == "zab"

    assert caesor_cipher("abc", 1) == "bcd"

    # h -> k, e -> h, l -> o, l -> o, r -> u
    assert caesor_cipher("hello", 3) == "khoor"

    # A full rotation of 26 lands back on the original text
    assert caesor_cipher("abc", 26) == "abc"

    # Non-letters pass through untouched
    assert caesor_cipher("ab c", 1) == "bc d"

    print("All tests passed")
