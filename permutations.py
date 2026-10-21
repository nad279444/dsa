"""Apply a permutation P to array A in place.

Approach: perm[i] says where the element currently at index i must go. Starting
from every index we walk its cycle: repeatedly swap A[i] with A[perm[next]] so
the element at i lands in its final slot, and mark perm[next] negative (by
subtracting n) so we can tell that slot has already been placed and stop the
cycle. When the while loop ends for one index, the outer loop moves on — any
index whose cycle was already followed by an earlier i is skipped because its
perm entry is still negative. Finally n is added back to every entry, restoring
perm in a single pass.
Time: O(n) — each index is swapped a constant number of times; Space: O(1).
"""


def apply_permutation(perm, A):
    n = len(perm)
    for i in range(n):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= n
            next = temp
    # Restore perm — runs ONCE, after every index has been processed
    perm[:] = [a + n for a in perm]


if __name__ == "__main__":
    # Cycle 0 -> 2 -> 1 -> 0: each element moves to its perm index
    perm, A = [2, 0, 1], ["a", "b", "c"]
    apply_permutation(perm, A)
    assert A == ["b", "c", "a"]
    assert perm == [2, 0, 1]  # permutation is restored

    # Full reversal: element i moves to index perm[i]
    perm, A = [3, 2, 1, 0], [10, 20, 30, 40]
    apply_permutation(perm, A)
    assert A == [40, 30, 20, 10]
    assert perm == [3, 2, 1, 0]

    # Identity permutation leaves the array untouched
    perm, A = [0, 1, 2], [10, 20, 30]
    apply_permutation(perm, A)
    assert A == [10, 20, 30]
    assert perm == [0, 1, 2]

    print("All tests passed")
