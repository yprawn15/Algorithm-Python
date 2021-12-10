year = int(input())


if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  print(1)
else:
  print(0)

# %가 나머지 구하는 연산자라는 것만 알아두자