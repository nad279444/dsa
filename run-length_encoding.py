"""Compress a string into runs of "<character><count>", with counts capped at 9.

Approach: walk the string once, tracking the length of the current run. When
the character changes OR the run reaches MAX_LENGTH (9), flush the run as
"<char><count>" and restart the counter at the current character. The final
run is flushed after the loop. Runs longer than 9 are therefore split into
multiple groups (20 a's -> a9a9a2).
Time: O(n); Space: O(n) for the output.
"""


def runlength(characters: str):
    length = 1
    MAX_LENGTH = 9
    chars = []

    for index in range(1, len(characters)):
        if characters[index] != characters[index - 1] or length == MAX_LENGTH:
            chars.append(characters[index - 1])
            chars.append(str(length))
            length = 0
        length = length + 1

    chars.append(characters[len(characters) - 1])
    chars.append(str(length))

    return "".join(chars)


if __name__ == "__main__":
    # 13 a's split at the cap, then 3 of each trailing character
    assert runlength("aaaaaaaaaaaaabbbcccddd") == "a9a4b3c3d3"

    # Short runs keep the count of 1
    assert runlength("ZBBBBBB") == "Z1B6"

    # Runs longer than 9 split into chunks of 9
    assert runlength("a" * 20) == "a9a9a2"

    # Single character / single run
    assert runlength("a") == "a1"
    assert runlength("aa") == "a2"

    print("All tests passed")
