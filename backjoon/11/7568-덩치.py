n = int(input())

w = []
h = []
for _ in range(n):
    x, y = map(int, input().split())
    w.append(x)
    h.append(y)

# [55, 58, 88, 60, 46] [185, 183, 186, 175, 155]

grade = []

for i in range(n):
    cnt =0
    for j in range(n):
        if w[i] < w[j] and h[i] < h[j]:
            cnt += 1  
    grade.append(cnt + 1)

print(*grade)