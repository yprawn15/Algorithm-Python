n = int(input()) # 4

arr = list(map(int, input().split())) # [1, 3, 5, 7]

cnt = 0
for i in arr: # [1, 3, 5, 7]
    error = 0
    if i > 1: # 1은 소수가 아님
        for j in range(2, i): # 2부터 i-1까지  
            if i % j == 0: # 나누었을 때 0이면 
                error += 1 # 소수가 아님
        if error == 0: # 나누어 떨어지지 않으면 
            cnt += 1 # 소수의 개수 +1
print(cnt)

# 소수는 1과 자기 자신을 제외하고는 나눠지지 않음
