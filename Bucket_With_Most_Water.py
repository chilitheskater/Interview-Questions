#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

#Find two lines that together with the x-axis form a container, such that the container contains the most water.


def max_area(height):
    max_water = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # Calculate the width between the two pointers
        width = right - left

        # Calculate the height of the container (minimum height between the two lines)
        h = min(height[left], height[right])

        # Calculate the water that can be held by the container
        water = width * h

        # Update the maximum water if the current container holds more water
        max_water = max(max_water, water)

        # Move the pointers towards each other
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
