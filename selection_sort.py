"""Sort a list with selection sort.

Approach: maintain a sorted prefix at the front of the array. For each position
i, scan the unsorted suffix (i + 1..end) to find the index of the smallest
value, then swap it into position i. After n passes the whole list is sorted.
Time: O(n^2) comparisons even on sorted input; Space: O(1), sorts in place.
"""


def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap(arr, i, min_idx)
    return arr


def swap(arr: list[int], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    # Unsorted input -> sorted ascending
    assert selection_sort([5, 0, 9, 2, 7, 3]) == [0, 2, 3, 5, 7, 9]

    # Already sorted -> unchanged
    assert selection_sort([1, 2, 3]) == [1, 2, 3]

    # Descending input -> reversed
    assert selection_sort([3, 1]) == [1, 3]

    # Empty list -> empty list
    assert selection_sort([]) == []

    print("All tests passed")
