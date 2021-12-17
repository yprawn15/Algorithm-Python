while True:
    a = list(map(int, input().split()))
    max_a = max(a)
    if sum(a) == 0:
        break
    a.remove(max(a))
    if max_a**2 == (a[0]**2) + (a[1]**2):
        print('right')
    else:
        print('wrong')

# 함정은 변 길이의 순서 바꿔도 문제없이 판단하게 코드 짜야함