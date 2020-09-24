
def mergeSort(a):
    if len(a)-1:
        mid = len(a)>>1
        l = a[:mid]
        r = a[mid:]
        mergeSort(l)
        mergeSort(r)
        n, m, c = 0, 0, 0
        while n < len(l) and m < len(r):
            if l[n] < r[m]:
                a[c] = l[n]
                n += 1; c += 1
            else:
                a[c] = r[m]
                m += 1; c += 1
        while n < len(l) or m < len(r):
            if n < len(l):
                a[c] = l[n]
                n += 1; c += 1
            else:
                a[c] = r[m]
                m += 1; c += 1

# a = [1,4,2,6,4,7,2,7,1]
# mergeSort(a)
# print(a)
