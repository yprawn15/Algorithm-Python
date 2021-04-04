# unit24 문자열 응용하기
# 24.1.1 문자열 바꾸기 replace
s = 'Hello, world!'
s = s.replace('world', 'Python')
print(s)

# 24.1.2 문자 바꾸기
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))
# 먼저 str.maketrans('바꿀 문자', '새문자')로 변환 테이블은 만들고 translate(테이블)을 사용하면 문자를 바꾼 뒤 결과를 반환

# 24.1.3 문자열 분리하기
# split()은 공백을 기준으로 문자열을 분리하여 리스트로 만든다. input().split()에서 문자열을 입력받은 뒤 리스트로 만든게 이 녀석이다.
print('apple pear grape pineapple orange'.split())
# split('기준문자열')과 같이 기준 문자열을 지정하면 기존 문자열로 문자열을 분리한다. 
print('apple, pear, grape, pineapple, orange'.split(', '))
# 즉 기존 문자열을 ', '로 했을 때 단어만 나옴

# 24.1.4 구분자 문자열과 문자열 리스트 연결하기
print(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
# join(리스트)는 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만든다.

# 24.1.5 소문자를 대문자로 바꾸기
print('python'.upper())

# 24.1.6 대문자를 소문자로 바꾸기
print('PYTHON'.lower())

# 24.1.7 왼(오른, 양)쪽 공백 삭제하기
# lstrip, rstrip, strip
print('   Python   '.lstrip())
print('   Python   '.rstrip())
print('   Python   '.strip())

# 24.1.10 왼쪽의 특정 문자 삭제하기
# lstrip('삭제할 문자들')
print(', python.'.lstrip(',.'))

# 24.1.11 오른쪽 특정 문자 삭제하기
print(', python.'.rstrip(',.'))

# 24.1.12 양쪽 특정 문자 삭제하기
print(', python.'.strip(',.'))

# ref 구두점을 간단하게 삭제하기
import string
print(', python.'.strip(string.punctuation))
# 공백까지 삭제하고 싶다면 ' '을 연결
print(', python.'.strip(string.punctuation + ' '))
print(', python.'.strip(string.punctuation).strip())

# 24.1.13 문자열을 왼(오른)쪽 정렬하기
# ljust(길이)는 문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬하며 남은 공간을 공백으로 채운다.
print('python'.ljust(10))
print('python'.rjust(10))

# 24.1.15 문자열 가운데 정렬
print('python'.center(10))
# 가운데 정렬했는데 전체 길이와 남는 공간이 모두 홀수가 된다면 왼쪽에 공백이 한칸 더 들어간다.

# 24.1.16 method chaining
print('python'.rjust(10).upper())
# method를 줄줄이 연결해서 호출하는 방법

# 24.1.17 문자열 왼쪽에 0 채우기
# zfill(zero fill) Python을 사용하다보면 왼쪽에 0을 채워야 하는 순간이 온다.
print('34'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))

# 24.1.18 문자열 위치 찾기
# find('찾을 문자열')은 문자열에서 특정 문자열을 찾아서 인덱스를 반환, 문자열이 없으면 -1을 반환
# find는 왼쪽부터 문자열을 찾는데 같은 문자열이 여러 개일 경우, 처음 찾은 문자열의 인덱스를 반환
print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))

# 24.1.19 오른쪽부터 문자열 위치 찾기
print('apple pineapple'.rfind('pl'))

# 24.1.20 문자열 위치 찾기
# find 외에도 index, rindex로 문자열의 위치를 찾을 수 있따.
# index('찾을 문자열') 단, 문자열이 없으면 에러를 발생
print('apple pineapple'.index('pl'))
print('apple pineapple'.rindex('pl'))

# 24.1.22 문자열 개수 세기
# 특정 문자열이 몇번 나오는지 알아봄
print('apple pineapple'.count('pl'))

# 24.2 문자열 서식지정자와 포매팅

# 24.2.1 서식 지정자(format specifier)로 문자열 중간에 다른 문자열 넣기
# '%s' % '문자열'
print('I am %s' % 'james')
# format specifier는 %로 시작하고 자료형을 뜻하는 문자가 붙는다. s(string), d(decimal integer), f(fixed point)
name = 'maria'
print('I am %s' % name)

# 24.2.2 format specifier로 숫자 넣기
print('I am %d years old' % 20)

# 24.2.3 format specifier로 소수점 표현하기
print('%f' % 2.3) # 기본적으로 소수점 이하 6자리까지 표시함
# 소수점 이하 자리수를 지정하고 싶다면 .(자리수)f
print('%.2f' % 2.3)

# 24.2.4 서식 지정자로 문자열 정렬하기
# %길이s 하면 문자열을 지정된 길이로 만든 뒤 오른쪽 정렬하고 남는 공간을 공백으로 채움
print('%10s' % 'python')

# ref 자리수가 다른 숫자 출력하기
print('%10d' % 150)
print('%10d' % 15000)

print('%10.2f' % 2.3)
print('%10.2f' % 2000.3)

# 왼쪽 정렬하는법
print('%-10s' % 'python')

# 24.2.5 서식 지정자로 문자열 안에 값 여러 개 넣기
# '%d %s' % (숫자, '문자열')
print('Today is %d %s' % (3, 'April'))

# 24.2.6 format method 사용하기
print('Hello, {0}'.format('world!'))
print('Hello, {0}'.format('100'))
# {}안에 인덱스를 지정하고 format에 넣을 값을 지정

# 24.2.7 format method로 값을 여러 개 넣기
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))

# 24.2.8 format method로 같은 값을 여러 개 넣기
print('{0} {0} {1} {1}'.format('Python', 'Script'))

# 24.2.9 format method에서 인덱스 생략하기
print('Hello, {} {} {}'.format('Python', 'Script', 3.6))
# {}에서 인덱스를 생략하면 format의 값이 순서대로 들어간다.

# 24.2.10 format method에서 인덱스 대신 이름 지정하기
print('Hello, {language} {version}'.format(language='Python', version=3.6))
# index 대신 이름 지정 가능

# 24.2.11 문자열 포매팅에 변수를 그대로 사용하기
language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')

# ref 중괄호 출력하기
print('{{ {0} }}'.format('Python'))

# 24.2.12 format method로 문자열 정렬하기
# '{index:<length}'.format(value) 부등호가 방향
print('{0:<10}'.format('Python')) # 길이 10으로하고 왼쪽 정렬

print('{0:>10}'.format('Python')) # 오른쪽 정렬

print('{:>10}'.format('Python'))

# 24.2.13 숫자 개수 맞추기
# '%0개수d' % 숫자
# '{인덱스:0개수d}'.format(숫자)
print('%03d' % 1)
print('{0:03d}'.format(35))

print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37)) # 실수 주의 할점 : .(점)도 숫자에 포함임

# 24.2.14 채우기와 정렬을 조합해서 사용하기
# '{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}'

print('{0:0<10}'.format(15)) # 길이 10으로 하고 왼쪽 정렬 남는 공간은 0으로 채움
print('{0:1>10}'.format(15)) # 길이 10으로 하고 오른쪽 정렬 남는 공간 1로 채움

print('{0:0>10.2f}'.format(15))

# ref 금액에서 천단위로 콤마 넣기
print(format(153495200, ',')) # format(숫자, ',')
print('%20s' % format(1493500, ',')) # 길이 20, 오른쪽으로 정렬
print('{0:,}'.format(1493500))

# raw 문자열 사용하기
# 문자열 앞에 r 또는 R을 붙이면 raw 문자열이 된다.
print(r'1\n2\n3\n') # \n 제어문자가 작동 안되는 것을 확인 가능

# practice
