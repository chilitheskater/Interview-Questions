# Wite a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

 

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:

#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
 

#Constraints:

#1 <= strs.length <= 200
#0 <= strs[i].length <= 200
#strs[i] consists of only lowercase English letters.


def longest_common_prefix(strs): #This defines a function named longest_common_prefix that takes a list of strings (strs) as input.
    if not strs: #This checks if the input list strs is empty
        return ""

    # Sort the strings to make it easier to find the common prefix
    strs.sort()

    # Take the first and last strings in the sorted array
    first_str = strs[0]
    last_str = strs[-1]
    #The first and last strings in the sorted list are extracted

    # Find the common prefix between the first and last strings
    prefix = [] #A loop iterates through the characters of the first string (first_str). It checks if the character at position i in the first string is equal to the character at the same position in the last string (last_str). 
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            prefix.append(first_str[i])
        else:
            break #If they are equal, the character is added to the prefix list. If a mismatch is found or the end of either string is reached, the loop breaks.

    return "".join(prefix)

# Example usage:
input1 = ["flower", "flow", "flight"]
output1 = longest_common_prefix(input1)
print(f"Example 1: {output1}")

input2 = ["dog", "racecar", "car"]
output2 = longest_common_prefix(input2)
print(f"Example 2: {output2}")
