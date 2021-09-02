n = int(input())


a, b = divmod(n, 5)
c = b // 3

if b % 3 == 0:
    print(-1)
else:
    print(a + c)