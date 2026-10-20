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
    print(runlength("aaaaaaaaaaaaabbbcccddd"))
