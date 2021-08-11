i = 0
while i > -1:
  A, B = map(int, input().split())
  if A + B == 0:
    break
  print(A + B)


# while은 반복할 횟수가 정해지지 않았을 때 사용이 권장됨
# break는 해당 조건을 만족시키면 반복문을 종료시킨다. continue는 그 조건에 해당하는 코드를 건너뛰고 반복문을 실행한다.
