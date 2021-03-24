# 8 불(bool)과 비교, 논리 연산자

# bool은 True, False로 표현하며, 1, 3, 5, 'python' 처럼 값의 일종이다.

print(3 > 1)

print(10 == 10)

print(10 != 5) # != 같지 않다는 부호

# 8.1 is와 is not
print(1 == 1.0)

print(1 is 1.0)

print(1 is not 1.0)

# == is의 차이 ==은 값 자체만을 is는 1, 1.0의 자료형까지 비교했기 때문
# 값 비교에 is를 사용하지 말자

# 8.2 논리 연산자(and, or, not)
print(True and True)
print(True and False) # 무조건 둘 다 True여야 결과가 True

print(True or False) # 하나만 True를 충족시켜도 True

print(not True)
print(not False) # not은 논릿값을 뒤집는다.