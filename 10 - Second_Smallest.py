''' For a list, find the second smallest number in the list '''


def second_smallest(nums):
    smallest = nums[0]
    second_smallest = nums[0]

    for n in nums:
        if n < smallest:
            second_smallest = smallest
            smallest = n
        elif n < second_smallest:
            second_smallest = n

    return second_smallest

listA = [40, 70, 20, 100, 60, 120]
print("This is the second largest number: ", second_smallest(listA))

# Simple Way
def second_smallest2(nums):

    nums.remove(min(nums))
    second_smallest = min(nums)

    return second_smallest

print("This is the second largest number: ", second_smallest2(listA))

# Using sort method
def second_smallest3(nums):

    nums.sort()
    second_smallest = nums[1]

    return second_smallest

print("This is the second largest number: ", second_smallest3(listA))
