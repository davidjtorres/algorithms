arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5


def findElementIndex(target, arr, start=None, end=None):

    low_index = start if start is not None else 0
    high_index = end if end is not None else len(arr) - 1
    mid_index = (low_index + high_index) // 2

    if low_index > high_index:
        return -1

    if target == arr[mid_index]:
        return mid_index

    elif target > arr[mid_index]:
        return findElementIndex(target, arr, mid_index + 1, high_index)

    else:
        return findElementIndex(target, arr, low_index, mid_index - 1)


print(findElementIndex(target, arr))
