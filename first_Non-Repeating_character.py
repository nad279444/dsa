def non_repeating_character(characters: str):
    count = {}

    for char in characters:
        count[char] = count.get(char, 0) + 1

    for char in characters:
        if count[char] == 1:
            return char

    return -1


if __name__ == "__main__":
    print(non_repeating_character("abcdcaf"))
