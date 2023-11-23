#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

#Example 1:

#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
#Example 2:

#Input: n = 1
#Output: ["()"]
 

#Constraints:

#1 <= n <= 8

def generate_parentheses(n): #defines a function named generate_parentheses that takes an integer n as input, representing the number of pairs of parentheses.
    def generate(partial, left, right): #This defines a helper function named generate
        if left == 0 and right == 0: 
            result.append(partial)
            return # This is the base case for the recursion. If both left and right are zero, it means a valid combination of parentheses has been formed. The current partial combination is added to the result list, and the function returns.
        if left > 0:
            generate(partial + '(', left - 1, right)
        if right > left:
            generate(partial + ')', left, right - 1) #These are the recursive calls. If there are remaining open parentheses (left > 0), the function is called with an added open parenthesis, and left is decremented by 1. If there are more open parentheses than close parentheses (right > left),
           
    result = []
    generate('', n, n)
    return result

# Example usage:
n1 = 3
output1 = generate_parentheses(n1)
print(f"Example 1: {output1}")

n2 = 1
output2 = generate_parentheses(n2)
print(f"Example 2: {output2}")
