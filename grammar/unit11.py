# 시퀀스 자료형 (list, tuple, range, str)
a = [0, 10, 20, 30, 40, 50]
print(30 in a)
print(100 in a) 
print(100 not in a)
print(30 not in a)

print(43 in (38, 76, 43, 62, 19))
print(1 in range(10))
print('P' in 'Hello, Python')

# 시퀀스 객체 연결하기
a = [0, 10, 20, 30]
b = [9, 8, 7, 6]
print(a + b)

print([0, 10, 20, 30] + [9, 8, 7, 6])

# range는  +로 연결 불가능 (list, tuple 사용해서 하면 가능)

print(list(range(0, 10)) + list(range(10, 20)))
print(tuple(range(0, 10))+ tuple(range(10, 20)))

print('Hello, ' + 'World!')

# 정수와 문자열을 연결할 경우 정수를 문자열로 변환해줘야 함
# print('Hello, ' + 10) 이렇게 하면 안됨 str로 정수를 문자열로 변환
print('Hello, ' + str(10))
print('Hello, ' + str(1.5)) # 실수 변환 역시 str

# 시퀀스 객체 반복하기 (0 or 음수를 곱하면 빈 객체가 나오며 실수는 곱하기 안됨)
print([0, 10, 20]*3)

# 앞에서 range를 +로 연결 못한 것 처럼 * 역시 안됨 list나 tuple 사용해서는 가능
print(list(range(0, 4))*3)
print(tuple(range(0, 4))*2)
print('Hello, '*3)

# 시퀀스 객체 요소 구하기
a = [0, 10, 20, 30, 40]
print(len(a))

b = (25, 45, 30, 24)
print(len(b))

# range 생성 개수 구하기
print(len(range(0, 10, 2)))

# 문자열 길이 구하기
hello = 'Hello, World!'
print(len(hello))

# 시퀀스 객체에 들어있는 요소에 접근하는 방법 [index]4
a = [38, 21, 52, 62, 19]
print(a[0])
print(a[2]) # >>> 52

b = (28, 39,50, 88)
print(b[0])

r = range(0, 10, 2)
print(r[2])

hello = 'Hello, World!'
print(hello[7])

# _getitem_ 메서드 (객체가 []일때 이 메서드를 사용해서 직접 호출)
a = [38, 21, 53, 62, 19]
print(a.__getitem__(1))

# 음수 인덱스 지정하기 (뒤에서 부터 요소를 순서대로 가져옴)
a = [38, 21, 53, 62, 19]
print(a[-1])

b = (38, 21, 53, 62, 19)
print(b[-5])

r = range(0, 10 ,2)
print(r[-3])

hello = 'Hello, World!'
print(hello[-4])

# 마지막 요소 접근하기
a = [38, 21, 53, 62, 19]
print(len(a)) #>> 5
print(a[4]) # 5로 넣으면 error

print(a[len(a)-1])


# 요소에 값 할당하기
a = [0, 0, 0, 0, 0]
a[0] = 38
a[1] = 21
a[2] = 45
a[3] = 62
a[4] = 19
print(a)
print(a[0])
print(a[4])
# 튜플은 안에 저장된 요소를 변경할 수 없기 때문에 인덱스를 지정한뒤 값을 할당하면 에러가 발생한다.
# range 역시 요소 변경 불가 / 시퀀스 자료형 중 tuple, range, 문자열은 읽기 전용

# del로 요소 삭제하기 (튜플, range, 문자열 요소 변경할 수 없기에 del 사용 불가능)
a = [38, 21, 53, 62, 19]
del a[2]
print(a)

# 슬라이스 사용하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[0:4] # 인덱스 0부터 3까지 잘라서 새 리스트를 만듬
print(a[0:4]) # 주의 : 끝 인덱스는 가져오려는 범위에 포함되지 않음
print(a[4:7])
print(a[4:-1])
print(a[2:8:3]) # 증가폭 이용 / 단, 요소의 증가폭이 아니라 인덱스의 증가폭임을 명심
print(a[:7]) # 리스트 처음부터 인덱스 6까지 가져옴
print(a[7:]) # 리스트 인덱스7부터 마지막 요소까지 가져옴
print(a[:]) # 리스트 전체를 가져오는 법
print(a[:7:2]) # 리스트 첨부터 인덱스 2 증가시키면서 인덱스 6까지 가져옴
print(a[7::2]) # 인덱스7부터 마지막까지
print(a[::2]) # 리스트 전체
print(a[::]) # 리스트 전체를 가져옴

# 슬라이스의 인덱스 증가폭을 음수로 지정하면?
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[5:1:-1])
print(a[::-1])

# len 응용하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0:len(a)])
print(a[:len(a)])

# range, 문자열, tuple 모두 슬라이스 응용 가능

# 슬라이스 객체 사용하기
# range(10)[slice(4, 7, 2)] = range(4, 7, 2)
# range(10).__getitem__(slice(4,7,2)) = range(4, 7, 2)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
s = slice(4, 7)
print(a[s])

r = range(10)
print(r[s])

hello = 'Hello, world!'
print(hello[s])

# 슬라이스에 요소 할당하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c']
print(a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c', 'd', 'e'] # 할당한 요소 개수가 지정한 인덱스 이상이면 원래 요소의 개수가 늘어남
print(a) 

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:8:2] = ['a', 'b', 'c']
print(a) # 인덱스 증가폭을 지정했을 때는 슬라이스 범위 요소 개수와 할당할 요수 개수가 정확히 일치 해야 함
# tuple, range, 문자열은 슬라이스 범위를 지정하더라도 요소를 할당할 수 없다.

# del로 슬라이스 삭제하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:5]
print(a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a{2:8:2}
print(a)
# 마찬가지로 tuple, range, 문자열은 del로 삭제 불가능


