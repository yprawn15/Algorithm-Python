a = [5, 50, 50, 70, 80, 100]
avg = 70
num = 0
for i in range(len(a)):
  if avg < a[i]:
    num += 1

print(num)