a, b = input().split()

A = ''.join(list(reversed(a)))
B = ''.join(list(reversed(b)))

if int(A) > int(B):
    print(int(A))
else: 
    print(int(B))

