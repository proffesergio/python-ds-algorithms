# Find the first index of a given number from a list

def firstIndex(list, key, start_index):
    list_length = len(list)
    if start_index == list_length:
        return "Not Found in the list!"
    if list[start_index] == key:
        return start_index
    sm_list = firstIndex(list, key, start_index + 1)
    return sm_list

list = [3, 5, 623, 23, 32, 12, 523, 232 , 123, 2, 12, 12, 1,2,4]
key = 12
start_index = 0
print("First index of the given number {} is: {}".format(key, firstIndex(list, key, start_index)))