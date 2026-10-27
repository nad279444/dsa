"""Merge overlapping intervals.

Approach:
1. Sort the intervals by their start times.
2. Start with the first interval in the result list.
3. For each subsequent interval, if it overlaps with the last interval in result
   (current.start <= last.end), merge them by updating last.end = max(last.end, current.end).
4. Otherwise, add the current interval as a new entry.
5. Return the merged list.

Two intervals [s1,e1] and [s2,e2] overlap if s2 <= e1 (assuming sorted by start).
Time: O(n log n) due to sorting; Space: O(n) for the result array.
"""


def merge_overlapping_intervals(intervals: list[list[int]]):
    if not intervals:
        return []
    
    # Sort intervals based on start times
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
    merged = [list(sorted_intervals[0])]
    
    for current in sorted_intervals[1:]:
        last_merged = merged[-1]
        # Check if current interval overlaps with the last merged interval
        # They overlap if current start <= last merged end
        if current[0] <= last_merged[1]:
            # Merge: update the end of last merged interval
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add current interval as a new merged interval
            merged.append(list(current))
    
    return merged


# Alias for compatibility with common naming
overlapping_intervals = merge_overlapping_intervals


if __name__ == "__main__":
    # Classic example
    assert merge_overlapping_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]) == [[1, 2], [3, 8], [9, 10]]
    
    # All overlapping
    assert merge_overlapping_intervals([[1, 4], [2, 5], [3, 6]]) == [[1, 6]]
    
    # No overlapping
    assert merge_overlapping_intervals([[1, 1], [2, 3], [4, 5]]) == [[1, 1], [2, 3], [4, 5]]
    
    # Already merged
    assert merge_overlapping_intervals([[1, 5]]) == [[1, 5]]
    
    # Empty array
    assert merge_overlapping_intervals([]) == []
    
    # Overlapping at exact point
    assert merge_overlapping_intervals([[1, 2], [2, 3]]) == [[1, 3]]
    
    print("All tests passed")
