def replaceCharacter(string, char, key):
    if len(string) == 0:
        return string
    smallerList = string[1:]
    smallerOutput = replaceCharacter(smallerList, char, key)
    if string[0] == char:
        return key + smallerOutput
    else:
        return string[0] + smallerOutput

print(replaceCharacter('abcdddfcdfkgdd', 'd', 'x'))