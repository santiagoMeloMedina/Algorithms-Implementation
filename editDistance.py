
def edit(A, B):
    dp = [[None for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    dp[0][0] = 0
    for b in range(len(B)+1): dp[0][b] = b
    for a in range(len(A)+1): dp[a][0] = a
    for a in range(1, len(A)+1):
        for b in range(1, len(B)+1):
            if A[a-1] != B[b-1]:
                dp[a][b] = min(dp[a-1][b], dp[a][b-1], dp[a-1][b-1])+1
            else:
                dp[a][b] = dp[a-1][b-1]
    return dp[-1][-1]

# print(edit("hello", "hola"))
