# time complexity: O(n)
# memory complexity: T(1)
import doctest


def filter_non_zero(lst: list) -> list:
    """
    >>> filter_non_zero([1, 0, 0, 2])
    [1, 2]
    >>> filter_non_zero([0, 0])
    []
    >>> filter_non_zero([])
    []
    >>> filter_non_zero([0, 1, 0])
    [1]
    """
    non_zero_idx = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[non_zero_idx] = lst[i]
            non_zero_idx += 1
    return lst[:non_zero_idx]


if __name__ == "__main__":
    doctest.testmod()




