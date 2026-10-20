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
    print(caesor_cipher("xyz", 2))
