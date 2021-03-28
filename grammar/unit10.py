# unit 10 list & tuple

a = [25, 40, 23, 51, 11]
print(a)

# list에 저장된 값을 요소(element)라 한다.

person = ['james', 17, 175.3, True]
print(person)

# 빈 리스트 만들기
a = []
print(a)
b = list()
print(b)

# range를 사용하여 리스트 만들기 * range는 마지막 수를 포함하지 않는다.
a = list(range(10))
print(a)

b =  list(range(5, 12))
print(b)

c = list(range(-4, 10, 2))
print(c)

d = list(range(10, 0, -1))
print(d)

# 튜플 만들기
a = (38, 21, 53, 62, 19)
print(a)

# 튜플은 요소를 변경, 추가, 삭제 할 수 없게 만드는 리스트(읽기 전용 리스트)

# 요소(element)가 한 개인 튜플 만들기
(38, )
38, 

# range를 사용한 튜플 만들기
a = tuple(range(10))
print(a)

b = tuple(range(5, 12))
print(b)

c = tuple(range(-4, 10, 2))
print(c)

# 튜플을 리스트로 만들고 리스트를 튜플로 만들기
a = [1, 2, 3]
print(tuple(a))

b = (4, 5, 6)
print(list(b))

# list, tuple 안에 문자열을 넣으면?
print(list('hello'))
print(tuple('hello'))

# list, tuple로 변수 만들기
a, b, c = [1, 2, 3]
print(a, b, c)

d, e, f = (4, 5, 6)
print(d, e, f)

x = [1, 2, 3]
a, b, c = x
print(a, b, c)

y = (4, 5, 6)
d, e, f = y
print(d, e, f)

# input.split은 리스트를 반환함
print(input().split())

x = input().split()
a, b = x
print(a, b)

