
def knapsack(A, k):
    dp = [[0 for n in range(k+2)] for _ in A]
    dp[0][0] = 0
    for a in range(len(A)):
        for n in range(1, k+2):
            last = dp[a-1][n] if a-1 >= 0 else 0
            if A[a][0] <= n:
                sub = dp[a-1][n-A[a][0]] if a-1 >= 0 else 0
                dp[a][n] = max(last, A[a][1]+sub)
    return dp[-1][-1]

# A = [(6,3), (4,6), (5,2), (2,5)]
# print(knapsack(A, 6))
