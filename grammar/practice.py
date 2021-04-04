# unit23
# list = [[v, v], [v, v], [v, v]] v = value
a = [[10, 20], [30, 40], [50, 60]]
print(a) 

a = [[10, 20],
     [30, 40],
     [50, 60] ]

# 23.1.1 2차원 리스트의 요소에 접근하기
a = [[10, 20], [30, 40], [50, 60]]
print(a[0][0]) # fitst[] = row(세로) second[] = column(가로)
print(a[1][1])
a[0][1] = 1000 # value allocation
print(a[0][1])

# ref 톱니형 list
a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]

a = []
a.append([])
a[0].append(10)
a[0].append(20)
a.append([])
a[1].append(500)
a[1].append(600)
a[1].append(700)
print(a)


a = [[10, 20], [30, 40], [50, 60]]
from pprint import pprint
pprint(a, indent=4, width= 20)
# indent 들여쓰기 칸 수, width 가로 폭

# 23.2.1 for 반복문을 한 번만 사용하기
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a: # take off in list of row element
    print(x, y)

# 23.2.2 for 반복문 두 번 사용
a = [[10, 20], [30, 40], [50, 60]]
for i in a: # a안의 안쪽 리스트를 꺼냄
    for j in i: # 안쪽 리스트의 요소를 하나 씩 꺼냄
        print(j, end=' ')
    print()

# 23.2.3 for와 range 사용하기
a = [[10, 20], [30, 40], [50, 60]]

for i in range(len(a)): # range(3) (0, 1, 2) 반복 즉 # row size
    for j in range(len(a[i])): # a[0,1,2] # 세로 크기
        print(a[i][j], end=' ')
    print()
