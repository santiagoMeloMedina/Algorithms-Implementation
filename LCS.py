def lcs(a, b):
    global memo, A, B
    key = "{}:{}".format(a, b)
    if key in memo:
        return memo[key]
    if a < 0 or b < 0:
        result = 0
    else:
        if A[a] == B[b]:
            result = 1 + lcs(a-1, b-1)
        else:
            result = max(lcs(a, b-1), lcs(a-1, b))
    memo[key] = result
    return result
