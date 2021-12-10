t = int(input())

for i in range(t):
    h, w, n = map(int, input().split()) # h는 층 수, w는 방 수, n은 손님수
    full = list(range(101, h*100 + w + 1)) # 101부터 마지막 방까지 리스트 
    room = []
    for j in range(w):
        room += full[j::100] # [101, 201, ... h01] + [102, 202, ..] + ... + [10w, 20w, ... h0w]
    print(room[n-1])

# 슬라이스의 증가폭을 이용해서 n번째 손님 방을 구했음








