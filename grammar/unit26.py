# unit26 세트 사용하기
# set - 집합을 표현하는 자료형

# 26.1 세트 만들기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)
# 세트의 element 순서가 정해지지가 않음 / 세트를 매번 출력해보면 순서의 결과가 매번 다르게 됨
fruits = {'orange', 'orange', 'cherry'}
print(fruits)
# 세트에 들어가는 요소는 중복이 안됨 

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
# print(fruit[0]) 세트는 인덱스로 특정 요소만 출력하는 것을 지원하지 않음
# print(fruits['strawberry'])

# 26.1.1 세트에 특정 값이 있는지 확인하기
# value in set
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print('orange' in fruits)
print('peach' in fruits)
print('peach' not in fruits)

# 26.1.2 set를 사용하여 세트 만들기
# set(반복 가능한 객체)

a = set('apple') # 세트는 중복을 허용하지 않기에 p는 한번 나옴
print(a)

b = set(range(5))
print(b)

c = set() # 빈 세트 만들기
print(c)
print(type(c))

# ref 한글 문자열 세트로 만들기
print(set('안녕하세요'))

# ref 세트는 list, dictionary와 달리 세트 안에 세트를 넣을 수 없다
# a = {{1, 2}, {3, 4}} print(a) >> error

# ref 프로즌 세트(frozenset) : 튜플처럼 내용을 변경할 수 없는 세트
a = frozenset(range(10)) # 집합 연산, 메서드에서 요소 추가(삭제)하는 연산, 메서드 사용 불가
print(a) # frozenset는 세트 안에 세트를 넣고 싶을 때 사용한다. 단, 일반 세트는 넣을 수 없다.
print(frozenset({frozenset({1, 2}), frozenset({3, 4})})) # 프로즌 세트는 프로즌 세트 안에 중첩해서 넣기 가능

# 26.2 집합 연산
# | 연산자는 합집합(union)을 구하며 OR 연산자 |를 사용한다.
# set.union 메서드와 동작이 같다. / set1 | set2  / set.union(set1, set2)

# set의 합집합 연산
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(set.union(a, b))
# set의 합집합 연산

# & 연산자는 교집합(intersection)을 구하며 AND 연산자 &를 사용한다.
# set.intersection과 동작은 같음
print(a & b)
print(set.intersection(a, b))

# - 연산자는 차집합(difference)을 구하며 뺄셈 연산자 -를 사용한다.
# set1 - set2 / set.difference(set1, set2)
print(a - b)
print(set.difference(a, b))

# ^ 연산자는 대칭차집합(symmetric difference)을 구하며 XOR 연산자 ^를 사용
# set.symmetric_difference와 같음
# set1 ^ set2 / set.symmetric_difference(set1, set2)
print(a ^ b)
print(set.symmetric_difference(a, b)) # 대칭차집합 = 합집합 - 교집합


# 26.2.1 집합 연산 후 할당 연산자 사용하기
# set의 자료형에 연산자와 할당 연산자 =을 함께 사용하면 집합 연산의 결과를 변수에 다시 저장(할당)한다.
# |= 현재 세트에 다른 세트를 더하며 update 메서드와 같다.
a = {1, 2, 3, 4}
a |= {5}
print(a)

a = {1, 2, 3, 4}
a.update({5})
print(a)

# &= 현세트와 다른 세트중 겹치는 요소만 현재 세트에 저장하며 intersection_update 메서드와 같다.
a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
print(a)
a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4})
print(a)

# -= 현 세트와 다른 세트의 차집합 계산 후 변수에 저장 difference_update method 와 같음
a = {1, 2, 3, 4}
a -= {3, 4}
print(a)

a = {1, 2, 3, 4}
a.difference_update({3, 4})
print(a)

# ^= 연산자는 현세트와 타세트 중 겹치지 않는 부분을 현세트에 저장 symmetric_difference_update와 같음
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)

a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})
print(a)



# 26.2.2 부분 집합과 상위 집합 확인하기
# 집합 사이 관계를 확인하는데 부등호를 이용한다.
# <= 부분 집합(subset)을 확인 가능 / set.issubset(other set)
a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4}) # =이 있어서 같아도 됨
print(a.issubset({1, 2, 3, 4}))

# <은 진부분집합인지 확인하며 메서드는 없다.
a = {1, 2, 3, 4}
print(a < {1, 2, 3, 4, 5})

# >= 현세트가 다른 세트의 상위집합(superset)인지 확인하며 issuperset인 메서드가 있다.
a = {1, 2, 3, 4}
print(a >= {1, 2, 3, 4})
print(a.issuperset({1, 2, 3, 4}))

# > 진상위집합 확인 / 메서드는 없다.
a = {1, 2, 3, 4}
print(a > {1, 2, 3})

# 26.2.3 세트가 같은지 확인
a = {1, 2, 3, 4}
print(a == {4, 2, 3, 1})
print(a != {1, 2, 3})

# 26.2.4 세트가 겹치지 않는지 확인하기 isdisjoint
# 겹치는 요소가 없으면 True, 있으면 False
a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))
print(a.isdisjoint({3, 4, 5, 6}))

# 26.3 세트 조작하기

# 26.3.1 set 요소 추가하기
a = {1, 2, 3, 4}
a.add(5)
print(a)

# 26.3.2 set에서 특정 요소 삭제하기
a. remove(3) # 요소가 없으면 error 발생
print(a)
a.discard(2) # 없애는 요소가 없어도 error 발생 안하고 그냥 넘어감
print(a)

# 26.3.3 세트에서 임의의 요소 삭제하기 pop
a = {1, 2, 3, 4}
a.pop()
print(a)

# 26.3.4 세트의 모든 요소 삭제
a = {1, 2, 3, 4}
a.clear()
print(a)

# 26.3.5 세트의 요소 개수 구하기
a = {1, 2, 3, 4, 5}
print(len(a))


# 26.4 세트의 할당과 복사
a = {1, 2, 3, 4}
b = a # 세트는 한 개다 서로 영향을 받음 이 상태는
c = a.copy() # 이제 a, c는 별개의 세트가 됨

# 26.5 반복문으로 세트의 요소를 모두 출력하기
# for 변수 in 세트: 

a = {1, 2, 3, 4}
for i in a:
    print(i) # 숫자로만 이뤄진 세트는 순서대로 출력됨
# in 다음에 세트를 직접 지정해도 상관 없음

# 26.6 세트 표현식 사용하기
# {식 for 변수 in 반복가능객체}
# set(식 for 변수 in 반복가능객체)

a = {i for i in 'apple'}
print(a)

# 26.6.1 세트 표현식에 if 조건문 사용하기
#{식 for 변수 in 세트 if 조건식}
# set(식 for 변수 in 세트 if 조건식)

a = {i for i in 'pineapple' if i not in 'apl'}
print(a)