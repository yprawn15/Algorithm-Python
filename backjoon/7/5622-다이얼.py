S = list(input()) # 

time = 0

for i in range(len(S)):
    if S[i] == 'A' or S[i] == 'B' or S[i] == 'C':
        time += 2
    elif S[i] == 'D' or S[i] == 'E' or S[i] == 'F':
        time += 3
    elif S[i] == 'G' or S[i] == 'H' or S[i] == 'I':
        time += 4
    elif S[i] == 'J' or S[i] == 'K' or S[i] == 'L':
        time += 5
    elif S[i] == 'M' or S[i] == 'N' or S[i] == 'O':
        time += 6
    elif S[i] == 'P' or S[i] == 'Q' or S[i] == 'R' or S[i] == 'S':
        time += 7
    elif S[i] == 'T' or S[i] == 'U' or S[i] == 'V':
        time += 8
    else:
        time += 9

print(time + len(S))

#2
s = list(input())

arr = list(range(65, 91)) # A ~ Z

sc = 0

for j in range(len(s)):
    if 65 <= ord(s[j]) <= 67:
        sc += 2
    elif 68 <= ord(s[j]) <= 70:
        sc += 3
    elif 71 <= ord(s[j]) <= 73:
        sc += 4
    elif 74 <= ord(s[j]) <= 76:
        sc += 5
    elif 77 <= ord(s[j]) <= 79:
        sc += 6
    elif 80 <= ord(s[j]) <= 83:
        sc += 7
    elif 84 <= ord(s[j]) <= 86:
        sc += 8
    else:
        sc += 9

print(sc + len(s))

# 3 블로그 풀이
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)

# 이 생각을 못했음..