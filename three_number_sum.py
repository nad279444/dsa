def three_number_sum(arr: list[int], target: int):
    arr.sort()
    three_sums = []

    for i in range(len(arr) - 2):
        # can't loop to the end to reserve numbers for left and right
        left = i + 1
        right = len(arr) - 1

        while left < right:
            # left must always be less than right for the pointers not to point at the same value to prevent duplicates
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                three_sums.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

            elif current_sum < target:
                left += 1

            elif current_sum > target:
                right -= 1
    return three_sums


if __name__ == "__main__":
    print(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0))
