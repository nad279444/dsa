def semordnilap(words: list[str]):
    pairs = []
    word_set = set(words)
    for word in words:
        reversed_word = "".join(reversed(word))  # [::-1] does the same thing
        if reversed_word in word_set:
            pairs.append([word, reversed_word])
    return pairs


if __name__ == "__main__":
    print(semordnilap(["diaper", "abc", "test", "cba", "repaid"]))
