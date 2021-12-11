n = int(input())

cnt = 0

while n >= 0:
    if n % 5 == 0:
        print(cnt + (n//5))
        break
    n -= 3
    cnt += 1
else: 
    print(-1)
        
# 의문 else를 저렇게 써도 되는가