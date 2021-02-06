# time complexity: O(n+m)
# memory complexity: T(n+m)
import doctest


def list_diff(lst1: list, lst2: list) -> list:
    """
    >>> list_diff([8, 1], [1, 23, 3])
    [8]
    >>> list_diff([3], [3])
    []
    >>> list_diff([], [])
    []
    >>> list_diff([], [123, 234])
    []
    >>> list_diff([1, 2, 3], [2])
    [1, 3]
    """
    lst_set1 = set(lst1)
    lst_set2 = set(lst2)

    return list(lst_set1 - lst_set2)


if __name__ == "__main__":
    doctest.testmod()
