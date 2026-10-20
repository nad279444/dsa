def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1)
            j = j - 1
    return arr


def swap(arr: list[int], i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    print(insertion_sort([5, 7, 8, 9, 2, 1]))
