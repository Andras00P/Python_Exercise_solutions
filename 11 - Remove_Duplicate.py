''' For a given string, remove all duplicate characters from that string '''


def remove_duplicate(char):
    result = ""

    for i in char:
        if i not in result:
            result += i
    return result

listA = "this is a string"
print("Unique characters of the string: ", remove_duplicate(listA))
