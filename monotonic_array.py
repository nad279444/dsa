"""Check whether a list is monotonic: entirely non-decreasing or non-increasing.

Approach: track two flags over every adjacent pair. Any drop (arr[i] >
arr[i + 1]) disproves non-decreasing; any rise (arr[i] < arr[i + 1]) disproves
non-increasing. Equal neighbours violate neither. The list is monotonic if at
least one flag survives the single pass (a constant list is both).
Time: O(n) with one pass; Space: O(1).
"""


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
    # Strictly decreasing -> non-increasing
    assert monotonic_array([-1, -4, -10, -1100, -1100, -1101, -1102, -9001]) is True

    # Non-decreasing (repeats allowed)
    assert monotonic_array([1, 2, 2, 3]) is True

    # Rise then fall -> neither direction holds
    assert monotonic_array([1, 3, 2]) is False

    # Constant list is both non-decreasing and non-increasing
    assert monotonic_array([2, 2, 2]) is True

    # Strictly increasing
    assert monotonic_array([1, 2, 3]) is True

    print("All tests passed")
