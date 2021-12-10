arr = []
for i in range(9):
  arr += list(map(int, input().split())))

print(max(arr))
print(arr.index(max(arr)) + 1)

  
# 궁금점 
# map(int, input().split())은 되고, int(input())은 안됨

# iterable 에러 int(input())은 숫자이므로 반복 가능한 객체가 아니라서 뜸
# split()은 결과를 리스트로 형태로 줌


