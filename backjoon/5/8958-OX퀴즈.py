n = int(input())


for i in range(n):
  arr = list(input())
  point = 0
  score = 0  
  for j in range(len(arr)):
    if arr[j] == 'O':
      point += 1
      score += point
    elif arr[j] == 'X':
      score += 0
      point = 0
  print(score)


# 점수 표현하는데 상당히 애먹음;
# 다음에 더 잘 생각해봐야 할듯