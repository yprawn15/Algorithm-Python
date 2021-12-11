t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    f0 = list(range(1, n+1)) # [1, 2, 3, 4, ....., n] n개
    
    for i in range(k):
        for j in range(1, n): # 1, 2, 3, 4, .... n-1
            f0[j] += f0[j-1]  
    print(f0[-1])

# f0[j] += f0[j-1] <<< 이 생각이 상당히 히트