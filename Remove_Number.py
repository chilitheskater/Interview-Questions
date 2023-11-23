#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#Return k.

def remove_element(nums, val): #This defines a function named remove_element that takes two parameters: nums, which is the list of integers, and val, which is the value to be removed from the list.
    # Initialize two pointers
    i, k = 0, 0

    # Iterate through the array
    while i < len(nums): #This starts a while loop that continues until the end of the array is reached.
        # If the current element is not equal to val, move it to the front
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        i += 1 #Inside the loop, it checks if the current element (nums[i]) is not equal to val. If true, it means the element is not equal to the value to be removed. 

    # The first k elements in nums are now the elements not equal to val
    return k

# Example usage:
nums1 = [3, 2, 2, 3]
val1 = 3
output1 = remove_element(nums1, val1)
print(f"Example 1: {output1}, Modified nums: {nums1[:output1]}")

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
output2 = remove_element(nums2, val2)
print(f"Example 2: {output2}, Modified nums: {nums2[:output2]}")
