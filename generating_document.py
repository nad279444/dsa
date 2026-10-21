"""Decide whether `documents` can be written using only characters from `characters`.

Approach: count every character available in `characters` with a hash map, then
scan `documents` and consume one count per character used. If a needed
character is missing from the map, or its count has dropped to zero, there are
not enough copies and False is returned early. Finishing the scan means every
required character was available.
Time: O(len(characters) + len(documents)); Space: O(k) for k distinct characters.
"""


def generateDocument(characters: str, documents: str):
    characterCounts = {}

    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0
        characterCounts[character] += 1
    for character in documents:
        if character not in characterCounts or characterCounts[character] == 0:
            return False
        characterCounts[character] -= 1
    return True


if __name__ == "__main__":
    # "PROGRAM" can be spelled from the letters of "GORAMPRM"
    assert generateDocument("GORAMPRM", "PROGRAM") is True

    # Extra characters are allowed; only the document's letters must be available
    assert generateDocument("aabc", "abc") is True

    # Document needs a second 'd' that characters does not have
    assert generateDocument("abc", "abcd") is False

    # A character the source never contains
    assert generateDocument("abc", " ") is False

    # Empty document is trivially possible
    assert generateDocument("abc", "") is True

    print("All tests passed")
