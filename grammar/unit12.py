# 딕셔너리 사용하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
# 키 값이 중복될 경우 가장 뒤에 있는 값만 사용함
print(lux)

# 딕셔너리의 키에는 문자열뿐만 아니라 정수, 실수, 불, 자료형 모두 사용 가능
# 값에는 리스트 딕셔너리 등 모든 자료형을 사용할 수 있음
# 단, 키에는 리스트와 딕셔너리를 사용할 수 없음

# 빈 딕셔너리 만들기
x = {}
print(x)
y = dict()
print(y)

# dict로 딕셔너리 만들기
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
# 키와 값을 리스트가 아닌 튜플도 가능
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
# 리스트안에 튜플 나열하는 방법
lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(lux1)
print(lux2)
print(lux3)
print(lux4)

# 딕셔너리 [키]
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health'])
print(lux['armor'])

# 딕셔너리 키에 값 할당하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037
lux['mana'] = 1000
print(lux)

lux['mana_regen'] = 3.27
print(lux)
# 딕셔너리에 없는 키에 값을 할당하면 해당 키와 값이 추가된다.

# 딕셔너리에 키가 있는지 확인하기 (키 in 딕셔너리)
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print('mana' in lux)
print('mana_portion' in lux)
print('mana_portion' not in lux)

# 딕셔너리의 키 개수 구하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(len(lux))
print(len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}))


a = input().split()
b = map(float, input().split())
c = dict(zip(a, b))
print(c)


