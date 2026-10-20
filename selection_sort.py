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
    print(selection_sort([5, 0, 9, 2, 7, 3]))
