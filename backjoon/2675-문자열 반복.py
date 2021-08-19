t = int(input())

for i in range(t):
    q, r = input().split()
    print(*sorted(r*int(q)), sep='')

# alphanumeric 문자  0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:
# 에러 1. 0DE$ 일때, $먼저 나옴;


# 2
t = int(input())

for i in range(t):
    r, s = input().split()
    text = ''
    for j in s:
        text += int(r)*j
    print(text)