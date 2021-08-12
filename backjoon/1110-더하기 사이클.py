# 주의 
# n이 한자리 숫자일 때, 0 + n으로 계산된다. n + 0이 아님

N = int(input())

num = N # 26
count = 0

while True:
  share = num // 10 # 몫 2
  remain = num % 10 # 나머지 6
  sum = share + remain # 2 + 6 = 8
  num = (remain * 10) + (sum % 10)
  count += 1
  if num == N:
    break

print(count)