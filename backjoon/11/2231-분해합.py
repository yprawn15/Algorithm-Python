n = int(input())

# b = []
for i in range(1, n+1):
    a = list(map(int, str(i)))
    if i + sum(a) == n:
        print(i)
        break

    if i == n:
        print(0)


# if b:
#     print(min(b))
# else:
#     print(0)
# 마지막 처리를 이렇게 하면 최소 i가 아닌 모든 i까지 찾으므로 시간이 더 걸리게 됨


