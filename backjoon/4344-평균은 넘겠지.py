c = int(input())

for i in range(c):
  n = list(map(int, input().split()))
  ssum = 0
  num = 0
  for j in range(len(n)-1):
    ssum += n[j+1]
  avg = ssum / n[0]
  for k in range(len(n)):
    if avg < n[k]:
      num += 1
  ratio = (num / n[0]) * 100
  print(f'{ratio:.3f}%')
   
  
  
    

# a = [5, 50, 50, 70, 80, 100]
# avg = 70
# num = 0
# for i in range(len(a)):
#   if avg < a[i]:
#     num += 1

# print(num) 2