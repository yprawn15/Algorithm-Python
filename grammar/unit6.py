# 변수 사용 

# Python에서는 = 같다는 등호가 아니라 변수를 할당하는 연산자이다.

y = "Hello, World!"

print(y)

# 변수의 자료형 알아내기 (문자의 자료형은 str)
print(type(y))

# 변수 삭제하기
x = 10
del x
#print(x)

# 빈 변수만들기
x = None
print(x)

a = 10
# print(a + 20)
# print(a) a에 20을 더하지만 결과를 유지하지 않기에 값은 10
a += 20
print(a)
# += , -=, *=, /= 모두 사용 가능

# input  사용자가 입력한 값을 가져오는 함수
x = input('문자열을 입력하세요: ')
print(x)

a = input('첫번째 숫자를 입력하세요: ')
b = input("두번째 숫자를 입력하세요: ")

print(a + b) # a,b에 입력한 숫자가 문자열이라 결과가 12가 되었다

a = int(input('첫번째 숫자: '))
b = int(input('두번째 숫자: '))

print(a + b) # 정수로 변환해야함 변수에 int 안쓰고 print(int(a)+int(b)) 가능

# 여러 개의 변수에 input 받는법 (split)
a, b = input("문자열 두 개 요망: ").split()
print(a)
print(b) #공백을 기준으로 분리함 따라서 hellop ython > hellop yhon

# 위 방식으로 int를 계속 넣어서 하면 불편 map을 사용하자
a, b = map(int, input('숫자 두개 요망: ').split())
print(a + b)

