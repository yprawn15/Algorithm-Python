s = input().upper() # 'MISSISSIPI'

w = sorted(list(set(s))) # ['I', 'M', 'P', 'S']

arr = []

for i in w:
    arr.append(s.count(i)) # [4, 1, 1, 4]

if arr.count(max(arr)) > 1: # arr.count(4) = 2
    print('?') 
else:
    print(w[arr.index(max(arr))]) # arr.index(max(arr)) = 0, 3

# upper로 대문자로 만들어줌


