c = int(input()) # 5

for i in range(c): 
  n = list(map(int, input().split())) # [5, 50, 50, 70, 80, 100]
  ssum = 0
  num = 0
  for j in range(len(n)-1):  # range(5)
    ssum += n[j+1]     # n[1], n[2], n[3], n[4], n[5]
  avg = ssum / n[0]  # 350 / 5
  for k in range(len(n)-1): 
    if avg < n[k+1]:   
      num += 1
  ratio = (num / n[0]) * 100
  print(f'{ratio:.3f}%')
   
  
  
    
# 초안
# 예외를 조심할 것 n[0]의 범위는 0 < n[0] <= 1000 임
# f포매팅에서 소수점 표시하는법 :.nf 여기서 n은 정수, 그리고 몇자리까지 나타낼것인지

c = int(input())

for i in range(c):
  n = list(map(int, input().split()))
  cnt = 0

  avg = sum(n[1:]/n[0])

  for j in range(1, len(n)):
    if n[i] > avg:
      cnt += 1
  ratio = (cnt / n[0]) * 100
  print(f'{ratio:.3f}%')

# 개선안
# sum함수와 슬라이스를 이용해서 간단히 만들수 있었음