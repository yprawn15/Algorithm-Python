# while 반복문
i = 0
while i < 100:
    print('Hello', i)
    i += 1

# 초기값 1부터 시작하기
i = 1
while i <= 100:
    print('Hello', i)
    i += 1

# 초기값 감소시키기
i = 100
while i > 0:
    print('Hello', i)
    i -= 1

# 입력한 횟수만큼 반복
count = int(input())

i = 0
while i < count:
    print('Hello', i)
    i += 1

# 초기값을 받아서 진행
count = int(input("반복할 횟수를 입력해주세요: "))

while count > 0:
    print('hello', count)
    count -= 1

# 사실 while 반복문은 반복횟수가 정해지지 않았을 때 가장 많이 사용함
import random # 난수를 생성하기 위해 random 모듈을 가져옴

# 일반적인 난수 random.random()
print(random.randint(1, 6)) # 정수를 가져오는 난수

i = 0
while i != 3:
    i = random.randint(1, 6)
    print(i)

# random choice(시퀀스객체) 리스트, 튜플, range, 문자열 다 됨
dice = [1,2,3,4,5,6]
print(random.choice(dice))

# while 반복문 무한루프
#while True:
    #print('Hello, world!')

# practice
i = 2
j = 5
while i <= 32 or 0 < j <= 5:
    print(i, j)
    i *= 2
    j -= 1



x = int(input())
while x >= 1350:
    print(x-1350)
    x -= 1350