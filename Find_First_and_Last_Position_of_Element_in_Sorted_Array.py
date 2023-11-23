#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexity.


def searchRange(nums, target): #Calls the binary_search_left and binary_search_right functions to find the leftmost (left_index) and rightmost (right_index) occurrences of the target.
    def binary_search_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

                #If true, it means the target may be to the right of mid, so it updates the left pointer to mid + 1.
#If false, it means the target may be to the left or at mid, so it updates the right pointer to mid - 1.

    def binary_search_right(nums, target): # performs a binary search to find the leftmost occurrence of the target in the sorted array nums
        left, right = 0, len(nums) - 1
        while left <= right: 
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1 # If true
            else:
                right = mid - 1 #If false
        return right

#If true, it means the target may be to the right of mid, so it updates the left pointer to mid + 1.
#If false, it means the target may be to the left or at mid, so it updates the right pointer to mid - 1.
#The loop continues until the pointers meet (left > right), and the function returns the right pointer.
 

    left_index = binary_search_left(nums, target) #finds the rightmost occurrence of the target in the sorted array.
    right_index = binary_search_right(nums, target)

    if left_index <= right_index:
        return [left_index, right_index]
    else:
        return [-1, -1]

#If the leftmost index is less than or equal to the rightmost index, it means the target is found in the array. In this case, it returns [left_index, right_index].
#If the target is not found, it returns [-1, -1].
# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = searchRange(nums, target)
print(result)
