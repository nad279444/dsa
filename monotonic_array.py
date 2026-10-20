def monotonic_array(arr: list[int]):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            isNonDecreasing = False
        if arr[i] < arr[i + 1]:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing


if __name__ == "__main__":
    print(monotonic_array([-1, -4, -10, -1100, -1100, -1101, -1102, -9001]))
    print(monotonic_array([1, 2, 2, 3]))
    print(monotonic_array([1, 3, 2]))
