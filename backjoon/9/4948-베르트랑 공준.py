def sosu(N):
    sieve = [True]*(N+1)
    n = int(N ** 0.5)
    for i in range(2, n+1):
        if sieve[i] == True:
            for j in range(i+i, N+1, i):
                sieve[j] = False
    a = [i for i in range(2, N+1) if sieve[i] == True]
    return len(a)


while True:
    N = int(input())    
    if N == 0:
        break
    print(sosu(2*N)-sosu(N))
