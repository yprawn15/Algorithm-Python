# n = int(input())

# a = []
# for i in range(n):
#     a.append(int(input()))

a = [5, 2, 3, 4, 1]



for i in range(5):
    print(min(a))
    a.remove(min(a))
    print(a)