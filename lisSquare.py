def lis(A):
    result = [1 for _ in range(len(A))]
    for n in range(1, len(A)):
        for s in range(n):
            if A[n] > A[s]:
                result[n] = max(result[n], result[s]+1)
    return result
