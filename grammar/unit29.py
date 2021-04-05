# unit29 함수 사용하기
# 함수 - 특정 용도의 코드를 한 곳에 모아 놓은 것 / 한번 작성하면 나중에 필요할 때 계속 불러 쓸 수 있다. print, input 등도 다 미리 만들어 둔 함수

# 29.1.1 함수 만들기
def hello():
    print('Hello, world!')

# 29.1.2 함수 호출하기
print(hello())

# 29.1.4 함수의 실행 순서
# 1. 파이썬 스크립트 최초 실행
# 2. hello 함수 호출
# 3. hello 함수 실행
# 4. print 함수 실행 및 'Hello, world!' 출력
# 5. hello 함수 종료
# 6. 파이썬 스크립트 종료

# 29.1.5 함수 작성과 함수 호출 순서
# 함수 만들기 전에 함수 호출부터 하면 안됨 순서에 어긋남

# ref 빈 함수 만들기
# def hello():
#     pass

# 29.2 덧셈 함수 만들기
# def 함수이름(매겨변수1, 매개변수2):

def add(a, b):
    print(a + b)

print(add(10, 20))
# 순서 add 함수 호출, 10 20 전달 print(a+b) 30 출력

# ref 함수 독스트링 사용하기
# def 함수이름(매개변수):
#     """독스트링""" >> 함수에 대한 설명을 넣을 수 있음 
# 여러 줄의 독스트링일 경우 
#     """
#   여러 줄로 된
#   독스트링 
#     """   
#     코드

def add(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    return a + b

x = add(10, 20)
print(x)

print(add.__doc__) # 함수의 __doc__로 독스트링 출력

# help에 함수를 넣으면 함수의 이름, 매개변수, 독스트링을 도움말 형태로 출력해준다.
print(help(add))

# 29.3 함수의 결과 반환하기
# 함수에서 값을 꺼내 오는 return (return에 값을 지정하지 않으면 None을 반환)
# def 함수이름(매개변수):
#     return 반환값

def add(a, b):
    return a + b

x = add(10, 20)
print(x)  # return을 사용하면 값을 함수 바깥으로 반환 가능, 함수에서 나온 값을 변수에 저장 가능

# ref 매개변수는 없고 반환값만 있는 함수 
def one():
    return 1

x = one()
print(x)

# ref return으로 함수 중간에서 빠져나오기
def not_ten(a):
    if a == 10:
        return
    print(a, '입니다.', sep='')

print(not_ten(5))
print(not_ten(10)) # 이런식으로 아무 것도 출력되지 않게 if와 조합해서 특정 조건일때 함수 중간에 빠져나올때 보통 쓴다.

# 29.4 함수에서 값을 여러 개 반환하기
# def 함수이름(매개변수):
#     return 반환값1, 반환값2 이렇게 ,로 구분 가능

def add_sub(a, b):
    return a + b, a - b

x, y = add_sub(10, 20)
print(x)
print(y)

# return으로 값을 여러 개 반환하면 실제로는 튜플이 반환된다.
x = add_sub(10, 20)
print(x)

# ref 값 여러 개를 직접 반환하기
def one_two():
 #   return (1, 2) # 직접 반환할때 튜플을 지정 return 1, 2와 의미가 같다.
    return [1, 2] # 리스트로 반환 가능

x = one_two() # 기본은 튜플이지만 return에 리스트로 직접하면 리스트로 반환됨
print(x)

# 29.5 함수의 호출 과정 알아보기
# 함수 여러 개를 만든 뒤, 각 함수의 호출 과정을 stack diagram이라 한다.
# stack은 접시 쌓기와 같은데 접시 쌓기는 차곡차곡 쌓고 꺼낼 때 위에 부터지만 파이썬에서는 방향이 반대
# 아래부터 위로
def mul(a, b):
    c = a * b
    return c

def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)

x = 10
y = 20
print(add(x, y))
