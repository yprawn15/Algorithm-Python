a, b = map(int, input().split())
c = list(range(a, b+1))
c.pop(1)
c.remove(b-1)
d = [2**i for i in c]
print(d)
