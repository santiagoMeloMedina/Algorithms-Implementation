def maxSum(A):
    dp = [0 for _ in range(len(A))]
    dp[0] = A[0]
    for n in range(1, len(A)):
        dp[n] = A[n]
        if dp[n-1] > 0:
            dp[n] += dp[n-1]
    return max(dp)
