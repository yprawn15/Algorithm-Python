# n, m  = map(int, input().split())
# arr = list(map(int, input().split()))

# b = []
# c = []

# from itertools import combinations # combinations는 조합을 구하는 모듈

# for i in combinations(arr, 3): # arr 중 3개를 순서에 상관없이 뽑는 경우의 수
#     b.append(sum(i))

# for j in b:
#     if j <= m:
#         c.append(j)

# print(max(c))

n, m = map(int, input().split())
arr = list(map(int, input().split()))

b = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i] + arr[j] + arr[k] <= m:
                b.append(arr[i] + arr[j] + arr[k])

print(max(b))
