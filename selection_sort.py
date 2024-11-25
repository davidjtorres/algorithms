def findSmallestElement(arr: list):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


arr = [2, 5, 42, 23, 1, 4]
sortedArr = []
copiedArr = list(arr)

for i in range(len(copiedArr)):
    smallest_index = findSmallestElement(copiedArr)
    sortedArr.append(copiedArr.pop(smallest_index))

print(sortedArr)
