a = []
b = []

a = []
b = []
for i in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

def dest(c):
    if c.count(max(c)) < c.count(min(c)):
        return max(c)
    else:
        return min(c)

print(dest(a), dest(b))


