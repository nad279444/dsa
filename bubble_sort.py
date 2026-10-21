# Repeat passes through the list until no swaps occur
# For each pass, compare adjacent elements (i and i+1)
# If left > right, swap them and mark list as unsorted
# Stop when a full pass completes with no swaps
#
# Time: O(n^2) worst / average case (O(n) when already sorted, because the
# first pass makes no swaps); Space: O(1), sorts in place.


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
    # Out-of-order values bubble up across several passes
    assert bubble_sort([5, 7, 8, 9, 2, 1]) == [1, 2, 5, 7, 8, 9]

    # Fully reversed input
    assert bubble_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]

    # Already sorted -> one pass with no swaps
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

    # Duplicates
    assert bubble_sort([3, 1, 3, 2]) == [1, 2, 3, 3]

    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]

    print("All tests passed")
