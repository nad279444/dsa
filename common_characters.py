def common_characters(characters: list[str]):
    common = set(characters[0])
    # loop through the remaing strings
    for char in characters[1:]:
        # find the intersection with main and the remaining strings
        common = common & set(char)
    return common


if __name__ == "__main__":
    print(common_characters(["abc", "bcd", "cbaccd"]))
