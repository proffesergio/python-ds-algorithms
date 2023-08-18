def merge_sort(list):
    # base case
    if len(list) == 0 or len(list) == 1:
        return
    # split the list into half
    mid = len(list) // 2

    # seperate into two different list
    list1 = list[0: mid]
    list2 = list[mid: ]

    # sort these two list
    merge_sort(list1)
    merge_sort(list2)

    # merge two sorted list into one list
    merge(list1, list2, list)

def merge(list1, list2, list):
    i = 0
    j = 0
    k = 0
    # sorting the two smaller list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list[k] = list1[i]
            i = i + 1
            k = k + 1
        else:
            list[k] = list2[j]
            j = j + 1
            k = k + 1

    # now copy the remaining elements to the main list
    while i < len(list1):
        list[k] = list1[i]
        i = i + 1
        k = k + 1
    while j < len(list2):
        list[k] = list2[j]
        j = j + 1
        k = k + 1

list = [1, 24, 3, 33, 53, 52, 12, 122, 54, 55, 555, 152, 121]
merge_sort(list)
print("Sorted List: {}".format(list))