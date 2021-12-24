def get_stars(t):
    matrix = []
    for i in range(3 * len(t)): # (0 ~ 8)
        if i // len(t) == 1: # i == 3
            matrix.append(t[i % len(t)] + ' ' * len(t) + t[i % len(t)])
        else:
            matrix.append(t[i % len(t)] * 3)
    return matrix



star = ['***', '* *', '***']
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
    e += 1

for i in range(e):
    star = get_stars(star)
for i in star:
    print(i)

print(star)