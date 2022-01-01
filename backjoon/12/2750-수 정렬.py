# 풀이1
n = int(input())

# a = []

# for _ in range(n):
#     a.append(int(input()))

# b = sorted(a)
# print(b)

# for i in b:
#     print(i)
# set가 숫자로만 이루어져 있을 때 순서대로 출력된 것을 이용
# 세트로 풀던 sorted로 풀던 답이 틀렸다고 나오는데 원하는 풀이가 아니라서 그런것인가?


# # 풀이2
a = []
for _ in range(n):
    a.append(int(input()))

for i in range(n):
    print(min(a))
    a.remove(min(a)) 

# # 최솟값 출력 후 제거하면서 오름차순으로 출력