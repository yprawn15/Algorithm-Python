# unit 18. break, continue로 반복문 제어하기
# break 제어흐름 중단 / continue 제어흐름 유지, 코드 실행만 건너뜀

# 18.1.1 while에서 break로 반복문 끝내기
i = 0
while True:
    print(i)
    i += 1
    if i == 100:
        break

# 18.1.2 for에서 break로 반복문 끝내기
for i in range(10000):
    print(i)
    if i == 100:
        break

# 18.2.1 for에서 continue로 코드 실행 건너뛰기
for i in range(100): # 0 ~ 99까지 증가하면서 100번 반복
    if i % 2 == 0:  # i를 2로 나누었을 때 나머지가 0
        continue  # 아래 코드를 실행하지 않고 건너뜀
    print(i)

# 18.2.2 while 반복문에서 continue로 코드 실행 건너뛰기
i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# 참고. 반복문과 pass
# for, while의 반복 코드가 없지만 반복문의 형태를 유지하고 싶다면 pass를 이용
for i  in range(10):
    pass
#while True: 씹함정 누르면 맛감 강종 하는법 crtl + c
    #pass

# 18.3.1 입력한 횟수대로 반복하기

count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break
 
 # 18.3.1 입력한 숫자까지 홀수 출력하기

count = int(input('반복할 횟수 입력요망: '))
for i in range(count + 1):
    if i % 2 == 0:
        continue
    print(i)
              
# practice
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)



i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i += 1

start, stop = map(int, input().split())

i = start

while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > stop:
        break