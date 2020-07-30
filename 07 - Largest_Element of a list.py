''' Find the largest element of a list '''

def get_largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

nums = [12, 14, 30, 4 , 6, 80]
largest = get_largest(nums)

print("The largest is: ", largest)

# Simple way
total = max(nums)
print("The largest is: ", total)
