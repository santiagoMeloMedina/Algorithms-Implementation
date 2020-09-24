
def erathostenes(n):
    saved = [m for m in range(n+1)]
    primes = []
    for m in range(2, n+1):
        if saved[m]:
            s = m * m
            while s < n+1:
                saved[s] = 0
                s += m
            primes.append(m)
    print(primes)

# erathostenes(1000000)
