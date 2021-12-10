n = int(input())

cnt = 0

if len(str(n)) < 3:
    cnt = n
else:
    cnt = 99
    for i in range(100, n+1):
        if (int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2])):
            cnt += 1

print(cnt)