# 22.1 리스트 조작하기

# method(객체에 속한 함수)

# 22.1.1 리스트에 요소 추가하기
# append : 요소 하나를 추가
# extend : 리스트를 연결하여 확장
# insert : 특정 인덱스에 요소 추가

# 22.1.2 리스트에 요소 하나 추가하기
a = [10, 20, 30]
a.append(500)
print(a)
print(len(a))

a = []
a.append(10)
print(a)

# 22.1.3 리스트 안에 리스트 추가하기
a = [10, 20, 30]
a.append([500, 600])
print(a)
print(len(a)) # 5아닌 4인 이유 : [500, 600]이 리스트로 된 요소라서

# 22.1.4 리스트 확장하기
a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))

# 22.1.5 리스트의 특정 인덱스에 요소 추가하기
a = [10, 20, 30]
a.insert(2, 500)
print(a)

# insert에서 자주 사용하는 패턴 2가지
# insert(0, 요소) : 리스트의 맨 처음에 요소 추가
# insert(len(리스트), 요소) : 리스트 끝에 요소를 추가

a = [10, 20, 30]
a.insert(0, 500)
print(a)

a = [10, 20, 30]  # a.append(500)과 같은 방법
a.insert(len(a), 500)
print(a)

# 리스트 중간에 요소 여러개 추가
a = [10, 20, 30] 
a[1:1] = [500, 600] # 슬라이스 응용
print(a)

# 22.1.6 리스트에서 요소 삭제하기
# pop : 마지막 요소 또는 특정 인덱스의 요소를 삭제
# remove : 특정 값을 찾아서 삭제

# 22.1.7 pop
a = [10, 20, 30]
print(a.pop()) # pop은 리스트의 마지막 요소를 삭제하고 삭제한 요소를 반환함
print(a)

a = [10, 20, 30]
print(a.pop(1)) # 인덱스를 지정해서 특정 요소를 삭제하는 법
print(a)

# pop 대신 del을 사용해도 무관
a = [10, 20, 30]
del a[1]
print(a)

# 22.1.8 리스트에서 특정 값을 찾아서 삭제하기
a = [10, 20, 30]
a.remove(20)
print(a)

a = [10, 20, 30, 20]
a.remove(20)
print(a) # 리스트에 같은 값이 여러개면 처음 찾은 값을 삭제함

# 참고
from collections import deque # collections 모듈에서 deque를 가져옴
a = deque([10, 20, 30])
print(a)
a.append(500) # appendleft 왼쪽에 요소추가
print(a)
a.popleft() # pop() 오른쪽 요소 삭제
print(a)

# 22.1.9 리스트에서 특정 값의 인덱스 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.index(20)) # 가장 먼저 찾은 값을 구함

# 22.1.10 특정 값의 개수 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.count(20))

# 22.1.11 리스트의 순서를 뒤집기
a = [10, 20, 30, 15, 20, 40]
a.reverse()
print(a)

# 22.1.12 리스트의 요소를 정렬하기 (오름차순)
a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a)

# 참고 sort method와 sorted 함수
# 둘 다 정렬을 시키는 함수지만 약간의 차이점이 있다. sort는 method를 사용한 리스트를 변경하지만, sorted함수는 정렬된 새 리스트를 만든다.
b = [10, 20, 30, 15, 20, 40]
sorted(b)

# 22.1.13 리스트의 모든 요소 삭제하기
a = [10, 20, 30]
a.clear()
print(a) # del a[:]

# 22.1.14 리스트를 슬라이스로 조작하기
a = [10, 20, 30]
a[len(a) : ] = [500] # a.append(500)과 동일
print(a)

a = [10, 20, 30]
a[len(a) : ] = [500, 600] # a.extend([500, 600]) 동일
print(a)

# 리스트가 비어있는지 확인하기
# if not len(seq) : # 리스트가 비어 있으면 True
# if len(seq) : # 리스트에 요소가 있으면 True

# if not seq : # 리스트가 비어 있으면 T
# if seq : # 리스트에 내용이 있으면 T

seq = [10, 20, 30] 
print(seq[-1]) # 리스트가 비어 있는데 -1을 쓰면 에러가 난다.

seq = []
if seq : # 리스트에 요소가 있는지 확인 
    print(seq[-1]) # 요소가 있을 시 마지막 요소 가져옴

# 22.2 allocation and copy by list (리스트의 할당, 복사)
a = [0, 0, 0, 0, 0]
b = a # 리스트가 2개로 늘어난 것 처럼 보이지만 1개다

print(a is b) # 객체가 같음 따라서 b의 요소를 변경하면 a도 같이 변함

b[2] = 99
print(a)

# a와 b를 완전히 두 개로 만들려면 copy method 이용
a = [0, 0, 0, 0, 0]
b = a.copy()
b[2] = 99
print(a is b)
print(a)
print(b)

# 22.3 반복문으로 리스트의 요소를 모두 출력하기
# 22.3.1 for 반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
for i in a: # == for i in [38, 21, 53, 62, 19]
    print(i)

# 22.3.2 인덱스와 요소를 함께 출력하기
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)

# 인덱스 크기 늘리기
for index, value in enumerate(a, start=1): # == enumerate(a, 1)
    print(index, value)

# for 반복문에서 인덱스로 요소 출력하기
a = [38, 21, 53, 62, 19]
for i in range(len(a)):
    print(a[i])

# 22.3.3 while 반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
i = 0
while i < len(a):
    print(a[i])
    i += 1

# 22.4.1 가장 작은 수와 가장 큰 수 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i

print(smallest)

a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)

a = [38, 21, 53, 62, 19]
a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])

a =  [38, 21, 53, 62, 19]
print(min(a))
print(max(a))

# 22.4.2 요소의 합계 구하기
a = [10, 10, 10, 10, 10]
x = 0
for i in a:
    x += i
print(x)

a = [10, 10, 10, 10, 10]
print(sum(a))

# 22.5 list comprehension
# [식 for 변수 in 리스트]
# list(식 for 변수 in 리스트)

a = [i for i in range(10)]
print(a)

b = list(i for i in range(10))
print(b)

c = [i + 5 for i in range(10)]
print(c)

d = list(i*2 for i in range(10))
print(d)

# [] 방식과 list 방식 중 [] 방식 쓰는게 더 좋음

# 22.5.1 리스트 표현식에서 if 조건문 사용하기
a = [i for i in range(10) if i % 2 == 0]
print(a)

b = [i + 5 for i in range(10) if i % 2 == 0]
print(b)

# 22.5.2 for 반복문과 if 조건문을 여러번 사용하기
a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)

a = [i * j for j in range(2, 10)
           for i in range(1, 10)] # 들여쓰기 필수는 아니지만 가독성을 위해 해주는게 좋다.
print(a)

# 22.6 리스트에 map 사용하기 (map은 원본 리스트를 변경하지 않고 새 리스트를 생성한다.)
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))

a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

a = list(map(str, range(10)))
print(a)

# 22.6.1 input().split()과 map
a = input().split()
print(a)

a = map(int, input().split())
# print(a)
print(list(a))

# 22.7.1 튜플에서 특정 값의 인덱스 구하기
a = (38, 21, 53, 62, 19, 53)
print(a.index(53))

# 22.7.2 특정 값의 개수 구하기
a = (10, 20, 30, 15, 20, 40)
print(a.count(20))

# 22.7.3 for 반복문으로 요소 출력하기
a = (38, 21, 53, 62, 19, 53)
for i in a:
    print(i, end=' ')

# 22.7.4 튜플 표현식 사용하기
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

# 22.7.5 apply map to tuple
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

# 22.7.6 튜플에서 가장 작은 수, 가장 큰 수, 합계 구하기
a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))


# practice
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

a, b = map(int, input().split())
c = list(range(a, b+1))
c.pop(1)
c.remove(b-1)
d = [2**i for i in c]
print(d)