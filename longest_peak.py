"""Return the length of the longest "peak" in `arr`.

A peak is a run of strictly increasing values that then strictly decreases;
the single tip must be a strict local maximum (arr[i-1] < arr[i] > arr[i+1]).
The peak length includes the tip and every increasing/decreasing element on
both flanks.

Approach: scan left to right looking for a tip. Only tips are inspected, so the
flanks never need re-checking from scratch:
  - find tip i where arr[i-1] < arr[i] > arr[i+1]
  - walk left while values are still increasing toward the tip
  - walk right while values are still decreasing away from the tip
  - peak length = rightIdx - leftIdx - 1 (indices just outside the flanks)
  - jump i to rightIdx, since everything inside this peak cannot start a
    longer peak
Time: O(n) — each element is visited O(1) times overall because i leaps forward
by the size of each peak; Space: O(1).
"""


def longest_peak(arr: list[int]):
    longestPeakLength = 0
    i = 1
    while i < len(arr) - 1:
        isPeak = arr[i - 1] < arr[i] and arr[i] > arr[i + 1]
        if not isPeak:
            i = i + 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and arr[leftIdx] < arr[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(arr) and arr[rightIdx] < arr[rightIdx - 1]:
            rightIdx += 1
        currentPeaklength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeaklength)
        i = rightIdx
    return longestPeakLength


if __name__ == "__main__":
    # Best peak is 0,1,2,1,0 -> length 5
    assert longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]) == 6

    # Classic example -> 0,1,2,1,0 length 5
    assert longest_peak([1, 2, 3, 4, 5, 1]) == 6

    # No peak at all -> strictly increasing
    assert longest_peak([1, 2, 3, 4]) == 0

    # No peak at all -> strictly decreasing
    assert longest_peak([4, 3, 2, 1]) == 0

    # Plateau at the tip is not a strict peak -> 0
    assert longest_peak([1, 2, 2, 1]) == 0

    # Two peaks, the second is longer: [0,1,2,0] vs [0,1,2,3,4,2]
    assert longest_peak([0, 1, 2, 0, 1, 2, 3, 4, 2]) == 6

    # Minimum peaks
    assert longest_peak([1, 2, 1]) == 3
    assert longest_peak([]) == 0
    assert longest_peak([1, 2]) == 0

    print("All tests passed")
