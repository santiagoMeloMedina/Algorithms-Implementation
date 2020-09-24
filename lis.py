def binarySearch(A, lw, hi, key):
    while lw < hi-1:
        middle = lw + ((hi-lw)//2)
        if (A[middle] >= key):
            hi = middle
        else:
            lw = middle
    return lw

def lis(A):
    dp = [A[0]]
    for n in range(1, len(A)):
        if (A[n] < dp[0]):
            dp[0] = A[n]
        elif (A[n] > dp[-1]):
            dp.append(A[n])
        else:
            index = binarySearch(dp, -1, len(dp), A[n])
            dp[index] = A[n]
    print(dp)
    return len(dp)

lis([1,1,2,2,4,5,3,4,5,6])
