x = int(input()) # 10

i = 0 # x가 몇번째 그룹인지 찾기
while x > sum(range(i)):
    i += 1

group = i-1 # 4

y = x - sum(range(group)) # 10 - 6 

  
arr = list(range(group+1)) # [0, 1, 2, 3, 4]

if group % 2 == 0:
    print(arr[y],'/',arr[-y],sep='')
else:
    print(arr[-y],'/',arr[y],sep='')
    



 