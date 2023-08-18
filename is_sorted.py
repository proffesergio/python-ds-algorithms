# Check a given list is sorted or not

# print("Provide a list of numbers, n = ")
# list = list(map(int, input().rstrip().split()))

def isSorted(list):
    length = len(list)
    if length == 0 or length == 1:
        return True
    if list[0] > list[1]:
        return False

    split_list = list[1:]
    isNewListSorted = isSorted(split_list)

    return isNewListSorted

list = [23, 33, 55, 58, 82, 280, 2000]
print("Sorted: {}".format(isSorted(list)))