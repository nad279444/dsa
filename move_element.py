"""Move every occurrence of `target` to the end of the array, keeping order.

Approach: two-pointer in-place stable partition. `pointer` marks the boundary
of the block of non-target values already placed at the front. Scanning with i,
whenever arr[i] is not the target it is swapped into the pointer's slot and the
pointer advances; targets are left behind and end up gathered at the end.
Because a swap only happens for non-target values, the relative order of the
non-target elements is preserved.
Time: O(n); Space: O(1), in place.
"""


def move_element_toEnd(arr: list[int], target: int):
    pointer = 0
    for i in range(len(arr)):
        if arr[i] != target:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            # move the pointer only after arr[i] != target and the swap takes place
            pointer += 1
    return arr


if __name__ == "__main__":
    # All 2's gather at the end, 1/3/4 keep their relative order
    assert move_element_toEnd([2, 1, 2, 2, 2, 3, 4, 2], 2) == [1, 3, 4, 2, 2, 2, 2, 2]

    # Target never appears -> unchanged
    assert move_element_toEnd([1, 2, 3], 9) == [1, 2, 3]

    # Everything is the target -> unchanged
    assert move_element_toEnd([2, 2, 2], 2) == [2, 2, 2]

    # No targets at the front to begin with -> immediate swap-free pass
    assert move_element_toEnd([5, 6, 1, 1], 1) == [5, 6, 1, 1]

    assert move_element_toEnd([], 1) == []

    print("All tests passed")
