t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    d = y - x
    cnt = 0
    move = 1
    move_plus = 0
    while move_plus < d:
        cnt += 1
        move_plus += move:
        if cnt % 2 == 0:
            move += 1
    print(cnt)

# d 1일 때 cnt 1 move 1
# d = 2, cnt 2 move 1
# d = 3, cnt 3 move 
# d = 4, cnt 3 move 2
# d = 5, cnt 4 move 
# d = 6, cnt 4 mvoe 2 
# d = 7, cnt 5 move 
# d = 9, cnt 5 move 3
# d = 10 ~ 12, cnt 6 move 3

# move의 합이 d인 것을 이용한 풀이법