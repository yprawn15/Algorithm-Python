def gold(n):
    a = [False, False] + [True]*(n-1) # n+1개 index 0, 1은 False
    m = int(n**0.5)
    for i in range(2, m+1):
        if a[i] == True:
            for j in range(2*i, n+1, i):
                a[j] = False
    b = [i for i in range(2, n+1) if a[i] == True]
    
    A = n // 2
    B = n // 2

    while A + B == n:
        if A in b and B in b:
            print(A, B)
            break
        A -= 1
        B += 1
    

T = int(input())
for i in range(T):
    n = int(input())
    gold(n)
