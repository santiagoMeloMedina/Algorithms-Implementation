
def rodCutting(k, A):
    dpt = [[0 for _ in range(k+2)] for _ in range(len(A))]
    for a in range(len(A)):
        for c in range(k+2):
            best = dpt[a-1][c] if a else float("-inf")
            prob = 0
            for n in range(A[a], c, A[a]):
                rest_best = dpt[a-1][c-n] if a and c >= A[a] else 0
                prob = max(n + rest_best if c >= A[a] else 0, prob)
            dpt[a][c] = max(prob, best)
    return dpt
