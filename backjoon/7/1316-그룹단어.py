n = int(input()) #3

group = n

for i in range(n):
    w = input()
    for j in range(len(w)-1):
        if w[j] == w[j+1]:
            pass
        elif w[j] in w[j+1:]:
            group -=1
            break

print(group)


# 아이디어도 안떠올랐음
# 슬라이스, pass, break 생각하자