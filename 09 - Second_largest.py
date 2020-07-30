''' For a list, find the second largest number in the list '''

def second_largest(nums):
    largest = 0
    second_largest = 0

    for n in nums:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest:
            second_largest = n
    return second_largest

listA = [40, 70, 20, 100, 60, 120]
print("This is the second largest number: ", second_largest(listA))

# Simple way
def second_largest2(nums):

    nums.remove(max(nums))
    second_largest = max(nums)

    return second_largest

print("This is the second largest number: ", second_largest2(listA))

# Using sort method
def second_largest3(nums):

    nums.sort()
    second_largest = nums[-2]

    return second_largest

print("This is the second largest number: ", second_largest2(listA))
