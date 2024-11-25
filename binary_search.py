from time import sleep


item_to_find = 6
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
low = 0
high = len(arr) - 1
result = None


while low <= high:
    mid = (low + high) // 2
    mid_element = arr[mid]

    if mid_element == item_to_find:
        result = mid
        break
    elif mid_element > item_to_find:
        high = mid - 1
    else:
        low = mid + 1
    sleep(1)

print(result)