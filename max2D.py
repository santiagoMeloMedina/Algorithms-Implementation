
def max2d(grid):
    sum = float("-inf")
    top, bottom, left, right = 0, 0, 0, 0
    for c1 in range(len(grid[0])):
        dp = [0 for _ in range(len(grid))]
        for c2 in range(c1, len(grid[0])):
            for r in range(len(grid)):
                dp[r] += grid[r][c2]
                tmp = sumA(dp)
                if sum < tmp[0]:
                    sum = tmp[0]
                    top, bottom, left, right = tmp[1], tmp[2], c1, c2
    return sum, top, bottom, left, right


def sumA(A):
    best = 0
    s, e = float("-inf"), float("-inf")
    best_current = 0
    s_current = 0
    for n in range(len(A)):
        best_current += A[n]
        if best_current < 0:
            best_current = 0
            s_current += 1
        if best_current > best:
            s = s_current
            e = n
            best = best_current
    return best, s, e
