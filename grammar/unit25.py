# unit25 dictionary 응용하기

# 25.1.1 딕셔너리에 키-값 쌍 추가하기
# setdefault : 키-값 쌍 추가
# update : 키의 값 수정, 키가 없으면 키-값 쌍 추가

# 25.1.2 딕셔너리에 키와 기본값 저장하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)
# setdefault에 키만 지정하면 값에 None 저장
x.setdefault('f', 100)
print(x)

# 25.1.3 딕셔너리에서 키의 값 수정하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)
# 만약 딕셔너리에 키가 없으면 키-쌍 값 추가함
x.update(e=50)
# update는 여러 개 수정 가능
x.update(a=900, f=60)
print(x)

# update(키=값)은 키가 문자열일 경우만 사용할 수 있다 
#키가 문자열이 아닐경우 
# 1. update(딕셔너리)
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
print(y)

# 2. update(리스트), update(튜플)
y.update([[2, 'TWO'], [4, 'FOUR']]) #[[키1, 값1], [키2, 값2]] 형식 / 튜플도 같은 형식
print(y)

# 3. update.(반복가능한객체) 키-값 쌍으로 된 반복 가능한 객체로 값을 수정
y.update(zip([1, 2], ['one', 'two']))
print(y)


# 25.1.4 딕셔너리에 키-값 쌍 삭제하기 (pop)
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.pop('a'))
print(x)
print(x.pop('z', 1)) # pop(키, 기본값) 해당 키가 없는데 삭제할 때 기본 값을 반환하게 된다.

# del로도 삭제 가능
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
print(x)

# 25.1.5 딕셔너리에서 임의의 키-값 쌍 삭제하기 popitem()
# popitem()은 딕셔너리에서 임의의 키-값 쌍을 삭제한 뒤 삭제한 키-값 쌍을 튜플로 반환한다.
# 참고로 Python 3.6에서는 맨 뒤 키-값 쌍을 삭제하고 3.5이하에서는 임의로 삭제함
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.popitem())
print(x)

# 25.1.6 딕셔너리의 모든 키-값 쌍을 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)

# 25.1.7 딕셔너리에서 키의 값 가져오기 
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('a'))
print(x.get('z', 0)) # get도 pop과 마찬가지로 없는 것을 가져올 때 설정한 기본 값을 반환한다.

# 25.1.8 딕셔너리에서 키-값 쌍을 모두 가져오기
# items : 키-값 쌍을 모두 가져옴
# keys : 모든 키를 가져옴
# values: 모든 값을 가져옴
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())
print(x.keys())
print(x.values())


# 25.1.9 리스트와 튜플로 딕셔너리 만들기 dict.fromkeys(키 리스트)
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)

y = dict.fromkeys(keys, 100) # 값 추가하기
print(y)

# ref defaultdict 사용하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x['z'] 딕셔너리에 없는 키를 사용하게 되면 에러가 뜸
from collections import defaultdict # collections 모듈에서 defaultdict를 가져옴
y = defaultdict(int) # int로 기본값 0 생성
print(y['z'])
# int넣는데 기본값이 0인 이유 : int() = 0이라서

# 기본값 변경법
z = defaultdict(lambda: 'Python') # lambda 이용해서
print(z['a'])
print(z[0])


# 25.2 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end=' ')
# 이렇게 하면 키만 출력됨

# for 키, 값 in 딕셔너리.items():
# 반복할 코드

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items(): # x.items() 대신 직접 딕셔너리를 넣어도 무관함
    print(key, value)

# 25.2.1 딕셔너리의 키만 출력하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key in x.keys():
    print(key, end=' ')

# 25.2.2 딕셔너리의 값만 출력하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for value in x.values():
    print(value )

# 25.3 딕셔너리 표현식 사용하기
# 1. {key: value for key, value in dictionary}
# 2. dict({key: value for key, value in dictionary})

keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)


{key: 0 for key in dict.fromkeys({'a', 'b', 'c', 'd'}).keys()}
# 값은 모두 0, dict.fromkeys(dic).keys > 키리스트 / 따라서 키: 값0 딕셔너리 만들기
x = {value: 0 for value in ({'a': 10, 'b': 20, 'c': 30, 'd': 40}).values()}
# 값을 키로 사용
print(x)
x = {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}
# 키- 값 바꿈
print(x)

# 25.3.1 딕셔너리 표현식에서 if 조건문 사용하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# 딕셔너리는 for 반복문으로 반복하면서 키-값 쌍을 삭제하면 안 됩니다.
x = {key: value for key, value in x.items() if value != 20}
print(x)
# {키: 값 for 키, 값 in 딕셔너리 if 조건식}, dict({키: 값 for 키, 값 in 딕셔너리 if 조건식})

# 25.4 딕셔너리 안에서 딕셔너리 사용하기(중첩 딕셔너리)
# 딕셔너리 = {키1 : {키A : 값A}, 키2 : {키B : 값B}}
# 값 접근하는 법 : 딕셔너리[키1][키2]
# 계층형 데이터를 저장할 때 유용

# 25.5 딕셔너리의 할당과 복사
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x # list와 마찬가지로 딕셔너리는 한 개이다.
z = x.copy() 
print(z is x) # copy로 복사해서 z는 x와 이제 같은 객체가 아니다.
z['a'] = 99
print(x)
print(z) # 별개의 객체이므로 x에 영향을 주지 않는다.

# 중첩 딕셔너리의 할당과 복사는 list 때랑 마찬가지다 그냥 copy를 하면 안되고 copy module을 가져와서 deepcopy를 해야한다.
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy # copy 모듈을 가져옴
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
print(x)
print(y)
