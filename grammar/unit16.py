# for 와 range
# for 변수 in range(횟수):
for i in range(100): 
    print('Hello, world!')

for a in range(100):
    print('Hwang', a)

# 시작하는 숫자와 끝나는 숫자 지정하기
for i in range(5, 12):
    print('Hello', i)

# 증가폭 사용하기
for i in range(0, 12, 2):
    print('Hello', i)

# 숫자를 감소 시키기
for i in range(10, 0, -1):
    print('Hello', i)

# 숫자 순서 반대로
for i in reversed(range(10)):
    print('Hello', i)

for i in reversed(range(5, 12)):
    print('hello', i)

for i in reversed(range(0, 12, 2)):
    print('hello', i)

# 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello', i)

# 시퀀스 객체 반복하기
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter, end=' ')

# practice
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i*10)

b = int(input('df'))
for i in range(1, 10):
    print(b, '*', i, '=', b*i)

    
