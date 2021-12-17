x, y, w, h = map(int, input().split())

def confirm(a, b):
    if a <= abs(b-a):
        return a
    else:
        return abs(b-a)

if confirm(x, w) <= confirm(y, h):
    print(confirm(x, w))
else:
    print(confirm(y, h))
