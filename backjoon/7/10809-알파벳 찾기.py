s = list(input()) # ['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']

k = [] 

a = list(range(97, 123)) # ASCII 코드 (a ~ z) 26개

for i in range(len(s)): # len(s) = 8
    k.append(ord(s[i])) # k = [98, 97, 101, 107, 106, 111, 111, 110]


t = k + ['0']*(26-len(k)) # [98, 97, 101, 107, 106, 111, 111, 110, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for j in range(len(a)): # 0 ~ 25
    if t[j] in a:  
        a[a.index(t[j])] = t.index(t[j])
    
for al in range(len(a)):
    if a[al] > 26:
        a[al] = -1

print(a)






# baekjoon
# 0 1 2 3 4 5 7
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# a b e j k n o
# 0 1 2 3 4 7 5 
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1- 1- 

 
# 2 
S = input() # baekjoon
a = list(range(97, 123)) # 아스키 코드(a~z)의 번호 

for i in a:
    print(S.find(chr(i)))

# find() 문자열 내에 해당 문자열이 있는지 파악하고 있으면 해당 인덱스를 반환
# chr() 문자열의 아스키 코드 숫자를 받으면 해당 문자열을 반환
    
