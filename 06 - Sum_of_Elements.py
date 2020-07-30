''' For a given list, get the sum of each number in the list '''

def sum_of_elements(nums_list):
    total = 0

    for n in nums_list:
        total += n

    return total

userList = [12, 14, 30, 4 , 6, 80]
print("The Sum of the elemnets is: ", sum_of_elements(userList))

# Shortcut

total = sum(userList)

print(total)
