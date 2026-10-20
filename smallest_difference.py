def smallest_difference(arr1: list[int], arr2: list[int]):
    arr1.sort()
    arr2.sort()

    idx1 = 0
    idx2 = 0
    current = float("inf")
    smallest = float("inf")

    smallestPairs = []

    while idx1 < len(arr1) and idx2 < len(arr2):
        first_num, second_num = arr1[idx1], arr2[idx2]
        if first_num < second_num:
            current = second_num - first_num
            idx1 = idx1 + 1

        elif second_num < first_num:
            current = first_num - second_num
            idx2 = idx2 + 1
        else:
            return [first_num, second_num]
        if current < smallest:
            # condition always overides the other because smallest is initially infinity
            smallest = current
            smallestPairs = [first_num, second_num]
    return smallestPairs


if __name__ == "__main__":
    print(smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
