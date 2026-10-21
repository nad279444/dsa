"""Sort a list with insertion sort.

Approach: grow a sorted prefix from left to right. For each element at index i
(1 onward), repeatedly swap it one position left while it is smaller than its
left neighbour — like placing a playing card into a hand of sorted cards. Once
it can move no further, everything up to i is sorted.
Time: O(n^2) worst/average (O(n) when already sorted); Space: O(1), in place.
"""


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
    # Out-of-order tail bubbles into place
    assert insertion_sort([5, 7, 8, 9, 2, 1]) == [1, 2, 5, 7, 8, 9]

    # Fully reversed input
    assert insertion_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]

    # Already sorted -> unchanged
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]

    # Duplicates keep their relative order
    assert insertion_sort([3, 1, 3, 2]) == [1, 2, 3, 3]

    assert insertion_sort([]) == []

    print("All tests passed")
