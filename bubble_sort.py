# Repeat passes through the list until no swaps occur
# For each pass, compare adjacent elements (i and i+1)
# If left > right, swap them and mark list as unsorted
# Stop when a full pass completes with no swaps


def bubble_sort(arr: list[int]) -> list[int]:
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                isSorted = False
    return arr


def swap(arr: list[int], i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    print(bubble_sort([5, 7, 8, 9, 2, 1]))
