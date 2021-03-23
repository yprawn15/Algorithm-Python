# input > split
#a, b = input('숫자 두 개를 입력해주세요:').split()
#a = int(a)
#b = int(b)
#print(a + b)
#print(int(a) + int(b))

# map 사용하기
# a, b = map(int, input('숫자 두 개를 입력하세요:').split())
# print(a + b) 

# 입력받은 값을 콤마를 기준으로 분리하기
#a, b = map(int, input('숫자 두 개를 입력하세요: ').split(','))

#print(a + b)

#a, b, c, d = map(int, input().split())
#print((a+ b + c +d)//4)

# 값 여러 개 출력하기
#print(1, 2, 3)
#print('hello', 'python')

# sep으로 값 사이에 문자 넣기
#print(1, 2, 3, sep=', ') # 공백 넣기
#print(1, 2, 3, sep='ㅗ') # ㅗ 넣기
#print('hello', 'python', sep='')
#print(1920, 1080, sep='x')

#print('1\n2\n3')
#print(1, 2, 3, sep='\n')

# end 사용하기
#print(1, end='')
#print(2, end='d')
#print(3)

# boolean 불과 비교, 논리 연산자
#print(3 > 1)
#print(10 == 10)
#print(10 != 5)

# ==, !=은 값을 비교하는데 사용하며, is, is not은 객체를 비교한다.
# 1.0 is 1 >> false
# 1.0 == 1 >> true 따라서 값 비교에 is를 쓰지 않는다.

#논리 연산자
# and >> 두 값이 모두 True여야 True다. 하나라도 False면 False
# or >> 두 값 중 하나라도 True면 True
# not >> not은 논리값을 뒤집는다. not true = false
# 위 3개 판단 순서 not, and, or 순

# 여러 줄로 된 문자열 사용 ''' ''' / """   """
#hello = '''hello, world!
#안녕하세요,
#python입니다.'''
#print(hello)

single_quote = '''"안녕하세요."
'파이썬'입니다.'''

double_quote = """"hello"
'python'"""

double_quote2 = """hello, 'python'"""

print(single_quote)
print(double_quote)
print(double_quote2)