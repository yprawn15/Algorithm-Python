a = int(input())
b = input()

for i in reversed(range(3)):
  print(a*int(b[i]))

print(a*int(b))

# 시간은 처음 풀었을 때보다 더 걸렸다. 이유는?
