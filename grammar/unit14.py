# 14.1 else 사용하기

x = 5
if x == 10:
    print('10입니다.')

else:
    print('10이 아닙니다.') # else는 단독으로 쓰이지 않는다.

# 변수에 값 할당을 if, else로 축약하기
x = 5
y = x if x == 10 else 0
print(y)

# if조건문의 동작 방식 알아보기

if True:
    print('참') 
else:
    print('거짓')

if False:
    print('참')
else: 
    print('거짓')

if None:
    print('참')
else:
    print('거짓')


# if조건문에 숫자 지정하기 0을 제외한 정수, 실수는 모두 참이다.
if 0:
    print('참')
else:
    print('거짓')

# if조건문에 문자열 넣기
if 'Hello':   # 문자열
    print('참') # 문자열은 참
else:
    print('거짓')

if '':            # 빈 문자열
    print('참')   
else:
    print('거짓')  # 빈 문자열은 거짓

# 조건식 여러개 지정하기
x = 10
y = 20

if x == 10 and y == 20:
    print('참')
else:
    print('거짓')

# 중첩 if 조건문과 논리 연산자
if x > 0:
    if x < 20:
        print('20보다 작은 양수입니다.')

if x > 0 and x < 20:
    print('20보다 작은 양수입니다.')

if 0 < x < 20:
    print('20보다 작은 양수입니다.')

a, b, c, d = map(int, input().split())
x = (a + b + c + d) / 4

if 0 <= a <= 100 and 0 <= b <= 100 and 0 <= c <= 100 and 0 <= d <= 100:
    if x >= 80:
        print('합격')
    if x < 80:
        print('불합격')
else:
    print('잘못된 점수')










    





