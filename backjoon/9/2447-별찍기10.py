def star(n):
    global sqr

    if n == 3:
        sqr[0][:3] = sqr[2][:3] = [1]*3
        sqr[1][:3] = [1, 0, 1]
        return
    
    a = n // 3
    star(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                sqr[a*i+k][a*j:a*(j+1)] = sqr[k][:a] # 핵심코드
    # for row in sqr:
    #     print(*row) 핵심코드를 직관적으로 볼 수 있는 코드

N = int(input()) # N == 9,

sqr = [[0 for i in range(N)] for i in range(N)]

star(N)

for i in sqr:
    for j in i:
        if j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()

# 이 문제의 아이디어는 크게 보면 3*3의 정사각형에 3인 부부을 3*3으로 쪼개가며 결국 한칸이 1인 3*3으로 채우는 작업이다.
# 그래서 sqr[k][:a]가 중요한 것인데 이것의 역할은 제일 큰 3*3사각형을 한 개씩 나누는 역할을 한다고 보면 된다.
# sqr[row][column] 즉 sqr[a*i+k][a*j:a*(j+1)]
# line 13 ~ 14는 가운데 부분에 빈 공간을 만드는 역할이다.
# line 16의 [a*j:a*(j+1)] 부분은 쪼갠 3*3 정사각형을 column 부분을 3개로 또 쪼개는 역할
# line 16의 [a*i+k]는  row를 3개로 쪼개는 역할이다.

def get_stars(t):
    matrix = []
    for i in range(3 * len(t)): # (0 ~ 27)
        if i // len(t) == 1: # i = 9 ~ 17
            matrix.append(t[i % len(t)] + ' ' * len(t) + t[i % len(t)])
        else:
            matrix.append(t[i % len(t)] * 3)
    return matrix



stars = ['***', '* *', '***']
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
    e += 1

for i in range(e):
    stars = get_stars(stars)
for i in star:
    print(i)

# 풀이2
# 부분이 전체를 이루는 구조를 프렉탈 구조라 한다.
# 이 풀이의 아이디어는 가운데 행일 경우에 line45처럼 따로 처리하는 것이다.
