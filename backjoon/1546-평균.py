N = int(input())

arr = list(map(int, input().split()))

M = max(arr)

plus = 0

for i in range(N):
  plus += (arr[i] / M) * 100

print(plus / N)
