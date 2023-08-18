def lastIndex(list, key):
    length = len(list)
    if length == 0:
        return -1
    smaller_list = list[1:]
    smaller_list_searching = lastIndex(smaller_list, key)

    if smaller_list_searching != -1:
        return smaller_list_searching + 1
    else:
        if list[0] == key:
            return 0
        else:
            return -1

# Alternatively not copying the whole list
def lastIndexBetter(list, key, start_index):
    length = len(list)
    if start_index == length:
        return -1
    smaller_list = lastIndexBetter(list, key, start_index + 1)
    if smaller_list != -1:
        return smaller_list
    else:
        if list[start_index] == key:
            return start_index
        else:
            return -1

list = [2, 24, 42, 12, 12, 412,3, 2,3, 12,32,13, 12, 3, 123, 23, 213, 2]
key = 2
print (lastIndex(list, key))
print (lastIndexBetter(list, key, 0))