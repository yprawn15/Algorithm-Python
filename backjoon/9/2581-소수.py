m = int(input())
n = int(input())

cnt = []
for i in range(m, n+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break # 포인트
        if error == 0:
            cnt.append(i)

if len(cnt) == 0:
    print(-1)
else:
    print(sum(cnt))
    print(min(cnt))

# 소수찾기와 같은 문제지만 line 8 ~ 10까지 돌아갈 때 error가 떠도 계속 돌기 때문에 시간초과가 나오게 된다
# 그래서 error가 카운트되면 바로 멈추게 break를 쓰는 것이 핵심!