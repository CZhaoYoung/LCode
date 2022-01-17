# https://leetcode.com/discuss/interview-question/858129/roblox-oa-new-grad-2021

# Dp solution

# Returns the maximum value
# with knapsack of W capacity

def unboundedKnapsack(W, n, val, wt):

    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    dp = [0 for i in range(W + 1)]

    ans = 0

    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

    return dp[W]
