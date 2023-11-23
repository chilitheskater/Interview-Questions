def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1, nums2, and the merged array
    p1 = m - 1  # Pointer for nums1
    p2 = n - 1  # Pointer for nums2
    p_merged = m + n - 1  # Pointer for the merged array

    # Merge elements from nums1 and nums2
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p_merged] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
        p_merged -= 1

    # Copy any remaining elements from nums2 to nums1
    nums1[:p2 + 1] = nums2[:p2 + 1]

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
