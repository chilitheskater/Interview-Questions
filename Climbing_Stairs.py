#The function `climbStairs(n)` takes one argument, `n`, which represents the number of steps in the staircase.


def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
 #If `n` is 1, it immediately returns 1 because there is only one way to climb a single step (by taking one step). If `n` is 2, it returns 2 because there are two ways to climb two steps (either two steps at once or two separate steps of 1 each).


    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

        #This loop calculates the number of ways to reach each step from step 3 to step `n` using dynamic programming.

    
    return dp[n]
    #This contains the number of distinct ways to reach the top of the staircase with `n` steps.



# Example 1
n1 = 2
print(climbStairs(n1))  # Output: 2

# Example 2
n2 = 3
print(climbStairs(n2))  # Output: 3


#Inside the loop, the number of ways to reach the current step `i` is calculated as the sum of the number of ways to reach the previous step `i - 1` and the step before that `i - 2`. This is based on the fact that you can only take 1 or 2 steps at a time.
