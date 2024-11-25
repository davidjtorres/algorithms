arr = [2321, 234, 25, 6, 12, 423, 543, 23, 5, 52414, 3213, 534, 3, 2, 1, 6, 7]
target = 5


def findElementIndex(target, arr, start=None, end=None):

    low_index = start if start else 0
    high_index = end if end else len(arr) - 1
    mid_index = low_index + high_index // 2

    if low_index > high_index:
        return -1

    if target == arr[mid_index]:
        return mid_index

    elif target > arr[mid_index]:
        return findElementIndex(target, arr, mid_index + 1, high_index)

    else:
        return findElementIndex(target, arr, low_index, mid_index - 1)


print(findElementIndex(target, arr))
