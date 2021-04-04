# unit23 2차원 list 

# 23.1 2차원 list 만들고 element에 접근하기
a = [[10, 20], [30, 40], [50, 60]]
print(a)

a = [ [10, 20],
      [30, 40],
      [50, 60] ]
# row 3, column 2

# 23.1.1 2차원 리스트의 요소에 접근하기
# list[row index][column index]
# list[row index][column index] = value

a = [ [10, 20], [30, 40], [50, 60] ]
print(a[0][0]) 
print(a[1][1])
a[0][1] = 1000
print(a[0][1]) 

# 참고
# 톱니형(jagged) list
a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]
# 행의 요소 개수 제각각 append method로 생성 가능
a = []
a.append([])
a[0].append(10)
a[0].append(20)
a.append([])
a[1].append(500)
a[1].append(600)
a[1].append(700)
print(a)

# 2차원 tuple
# a 튜플 = ((값, 값), (값, 값), (값, 값)) 튜플 안에 튜플을 넣은 2차원 튜플
# b 튜플 = ([값, 값], [값, 값], [값, 값]) 튜플 안에 리스트를 넣음
# c 리스트 = [(값, 값), (값, 값), (값, 값)] 리스트 안에 튜플을 넣음

# 튜플은 내용을 변경 할 수 없음 따라서 a는 변경 불가능 b는 안쪽 리스트만 c는 바깥쪽 리스트만

# 사람이 알아보기 쉽게 출력하기
a = [[10, 20], [30, 40], [50, 60]]
from pprint import pprint
pprint(a, indent=4, width=20) # indent = 들여쓰기 칸 수, width = 가로 폭

# 23.2 반복문으로 2차원 리스트 요소 모두 출력하기

# 23.2.1 for 반복문을 한 번만 반복하기
a = [[10,20], [30,40], [50, 60]]
for x, y in a:
    print(x, y)

# 23.2.2 for 반복문을 두 번 사용하기
a = [[10,20], [30,40], [50, 60]]
for i in a: # a에서 안쪽 리스트를 꺼냄
    for j in i: # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j, end=' ')
    print()

# 23.2.3 for와 range 사용하기
a = [[10,20], [30,40], [50, 60]]

for i in range(len(a)): # 세로 크기
    for j in range(len(a[i])): # 가로 크기
        print(a[i][j], end=' ')
    print()

# 23.2.4 while 반복문을 한 번 사용하기
a = [[10,20], [30,40], [50, 60]]

i = 0
while i < len(a): # (세로 크기)
    x, y = a[i]  # 요소 두 개를 한꺼번에 가져오기
    print(x, y)
    i += 1

# 23.2.5 Use 'while' twice
a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a): # row size / len(a) 3보다 작을 때까지 반복
    j = 0
    while j < len(a[i]): # column size / len(a[i]) = 2 
        print(a[i][j], end=' ') # element extraction
        j += 1
    print()
    i += 1

# 23.3 반복문으로 리스트 만들기
# 23.3.1 for 반복문으로 1차원 리스트 만들기
a = [] # 빈 리스트 생성
for i in range(10): 
    a.append(0) # append로 요소 추가 / 값은 0

print(a) # 요소가 9개, 값은 0인 리스트 생성

# 23.3.2 for 반복문으로 2차원 리스트 만들기
a = [] # 빈 list 생성

for i in range(3): # row size
    line = [] # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2): # column size
        line.append(0) # 안쪽 리스트에 0 추가
    a.append(line) # a 리스트에 line 리스트 추가

print(a)

# 23.3.3 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)

a = [[0] * 2 for i in range(3)]
print(a)

# 23.3.4 톱니형 list 만들기
a = [3, 1, 3, 2, 5] # 가로 크기를 저정한 리스트
b = [] # 결과물 list

for i in a: # a list에서 오소를 반복
    line = [] # 안쪽 빈 list 생성
    for j in range(i): # a 요소 크기 만큼의 가로 크기 반복
        line.append(0) 
    b.append(line)

print(b)

a = [[0] * i for i in [3, 1, 3, 2, 5]]
print(a)

# ref sorted(반복 가능한 객체, key=정렬함수, reverse=True or False) 
students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]

print(sorted(students, key=lambda student: student[1])) # 안쪽 리스트의 인덱스 1을 기준으로 정렬

# 23.4 2차원 리스트의 할당과 복사 알아보기 
# 리스트를 변수에 할당해도 그 변수 이름만 달라질 뿐 같은 리스트 / 2차원 리스트도 마찬가지
a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500
print(a)
print(b)  
print(a is b)

a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
print(a)
print(b)

# 2차원 이상의 다차원 리스트는 리스트를 완전히 복사하려면 copy method 대신 copy module의 deepcopy 함수를 사용해야 한다
a = [[10, 20], [30, 40]]
import copy # copy module을 가져옴
b = copy.deepcopy(a) # copy.deepcopy 함수를 사용하여 복사
b[0][0] = 500
print(a)
print(b)

# 23.6 3차원 list
a = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
print(a)