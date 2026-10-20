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
    print(generateDocument("GORAMPRM", "PROGRAM"))
