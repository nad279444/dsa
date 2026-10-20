def move_element_toEnd(arr: list[int], target: int):
    pointer = 0
    for i in range(len(arr)):
        if arr[i] != target:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            # move the pointer only after arr[i] != target and the swap takes place
            pointer += 1
    return arr


if __name__ == "__main__":
    print(move_element_toEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
