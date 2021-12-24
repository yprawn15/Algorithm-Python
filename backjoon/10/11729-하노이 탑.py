n = int(input())

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)

sum = 0
for i in range(n):
    sum += 2**i
print(sum)
hanoi(n, 1, 2, 3)

# 핵심 아이디어는 n-1까지 2번 발판에 모은뒤, 3번으로 옮기는 것
# 그래서 2번 발판을 3번 발판인 것 마냥 3번 자리에 위치시킨 듯한 효과를 줌