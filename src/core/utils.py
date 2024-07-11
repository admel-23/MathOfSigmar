from src.core.dice import Dice

def bin_search(sorted_array: list[int], l: int, r: int, value: int) -> int:
    '''
        What's always true:
        sorted_array[l] <= value
        sorted_array[r] >= value
    '''
    if l == r:
        return l
    m: int = (l + r) // 2
    if sorted_array[m] >= value:
        return bin_search(sorted_array, l, m, value)
    else:
        return bin_search(sorted_array, m + 1, r, value)


def percentile(sorted_array: list[int], value: int) -> float:
    index = int(len(sorted_array) * value / 100)
    v = sorted_array[index]
    l = bin_search(sorted_array, 0, index, v)
    r = bin_search(sorted_array, index, len(sorted_array) - 1, v+1)
    return v + (index - l) / (r - l)


def get_value(value: int | Dice):
    if isinstance(value, Dice):
        return value.roll()
    else:
        return value