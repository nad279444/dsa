"""Return an array where output[i] is the product of all other elements in the input.

Two approaches are provided below.

Approach 1 (Naive): for each index, multiply all other elements via nested loops.
Time: O(n^2) — two nested loops; Space: O(1) extra (excluding output array).

Approach 2 (Prefix/Suffix): build products of all elements to the left and right,
then multiply prefix_i * suffix_i for each index.
Time: O(n) — three passes; Space: O(1) extra (excluding output array).
"""


def array_products_naive(array: list[int]):
    new_array = []
    for i in range(len(array)):
        result = 1
        for j in range(len(array)):
            if i != j:
                result = result * array[j]
        new_array.append(result)
    return new_array


def array_products(array: list[int]):
    result = len(array) * [1]
    prefix = 1
    for i in range(len(array)):
        result[i] = prefix
        prefix = prefix * array[i]
    suffix = 1
    for j in range(len(array) - 1, -1, -1):
        result[j] = result[j] * suffix
        suffix = suffix * array[j]
    return result


if __name__ == "__main__":
    # Classic example: [1,2,3,4] -> [24,12,8,6]
    assert array_products_naive([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert array_products([1, 2, 3, 4]) == [24, 12, 8, 6]

    # With zeros: [0,1,2,3] -> [6,0,0,0]
    assert array_products_naive([0, 1, 2, 3]) == [6, 0, 0, 0]
    assert array_products([0, 1, 2, 3]) == [6, 0, 0, 0]

    # All zeros: [0,0,0] -> [0,0,0]
    assert array_products_naive([0, 0, 0]) == [0, 0, 0]
    assert array_products([0, 0, 0]) == [0, 0, 0]

    # Two elements: [a,b] -> [b,a]
    assert array_products_naive([5, 2]) == [2, 5]
    assert array_products([5, 2]) == [2, 5]

    print("All tests passed")
