def kmpPre(P):
    i, j = 0, -1
    f = [-1 for n in range(len(P)+1)]
    while i < len(P):
        while j >= 0 and P[i]!=P[j]: j=f[j]
        i += 1; j += 1
        f[i] = j
    return f

def kmp(T, P):
    points = []
    i, j = 0, 0
    f = kmpPre(P)
    while i < len(T):
        while j >= 0 and T[i]!=P[j]: j = f[j]
        i += 1; j += 1
        if j == len(P):
            points.append(i-j)
            j = f[j]
    return points
