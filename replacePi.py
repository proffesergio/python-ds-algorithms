def replacePi(string):
    list_length = len(string)
    if list_length == 0 or list_length == 1:
        return string
    if string[0] == 'p' and string[1] == 'i':
        smaller_list = string[2:]               # splitting the list from index 2 to the end
        return '3.14' + replacePi(smaller_list)
    else:
        smallOutput = replacePi(string[1:])
        return string[0] + smallOutput

string = "abpicdpi"
print (replacePi(string))