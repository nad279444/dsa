"""Find "semordnilap" pairs: words that read backwards as each other.

Approach: put every word in a set for O(1) lookups, then reverse each word and
check whether the reverse is also in the set. When a pair is found, both words
are removed from the set so each pair is reported exactly once — otherwise the
reverse direction would be listed a second time when its own turn comes.
Words already consumed as a partner are skipped. A word that is its own
reverse (a palindrome) never forms a pair.
Time: O(n * k) for n words of average length k; Space: O(n).
"""


def semordnilap(words: list[str]):
    pairs = []
    word_set = set(words)
    for word in words:
        if word not in word_set:
            continue  # already consumed as the partner of an earlier word
        reversed_word = "".join(reversed(word))  # [::-1] does the same thing
        if reversed_word in word_set and reversed_word != word:
            pairs.append([word, reversed_word])
            word_set.discard(word)
            word_set.discard(reversed_word)
    return pairs


if __name__ == "__main__":
    # diaper <-> repaid and abc <-> cba; "test" has no reverse in the list
    assert semordnilap(["diaper", "abc", "test", "cba", "repaid"]) == [
        ["diaper", "repaid"],
        ["abc", "cba"],
    ]

    # No reverse partners -> empty
    assert semordnilap(["abc", "def"]) == []

    # A palindrome is not its own pair
    assert semordnilap(["racecar"]) == []

    assert semordnilap([]) == []

    print("All tests passed")
