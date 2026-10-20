def reverse(s: str) -> str:
    result = ""
    for char in s:
        result = char + result
    return result


def palindrome_check(palindrome: str):
    reversed_str = reverse(palindrome)
    for item, reverse_item in zip(palindrome, reversed_str):
        if item != reverse_item:
            return False
    return True


if __name__ == "__main__":
    print(palindrome_check("abcdcba"))
    print(palindrome_check("abedcba"))
