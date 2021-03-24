# input은 입력 받기 print는 출력

print(1, 2, 9)
print('hello', 'python')
#print에 콤마로 구분해서 출력하면 여러 개의 변수나 자료형 출력 가능 ,를 기준으로 한 칸 띄워져서 출력됨

# 7.1.1 sep으로 값 사이에 문자 넣기
print(2021, 3, 24, sep='-')
print('Hello', 'Python', sep='') 
print(1920, 1080, sep='x')

# 7.1.2 줄바꿈 활용하기
print(1, 2, 3, sep='\n') 
print('1\n2\n3')

# 7.1.3 end 사용하기
print(1)
print(2)
print(3)
# 한줄로 출력하기 위해서는 end에 빈 문자열을 넣어주면 된다. 기본적으로 print는 \n이 되어있어서 한줄로 표현이 안되었지만 end의 빈 문자열을 사용하면 강제적으로 \n을 지워준다.
print(1, end='')
print(2, end='')
print(3)

print(1, end=' ')
print(2, end=' ')
print(3)

