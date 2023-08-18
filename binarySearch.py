def binarySearch(list, key, start_index, end_index):
    if start_index > end_index:
        return -1               # element not found
    # split the list into two part
    mid = (start_index + end_index) // 2
    if list[mid] == key:                    # found the element in the mid
        return mid
    elif list[mid] > key:                   # element is in the right part of the list
        return binarySearch(list, key, start_index, mid - 1)
    else:
        return binarySearch(list, key, mid + 1, end_index)

list = [1, 3, 5, 12, 20, 30, 50, 55, 60, 88, 90]
key = 90
start_index = 0
end_index = len(list) - 1

print("Key Element Found at index: {}".format(binarySearch(list, key, start_index, end_index)))