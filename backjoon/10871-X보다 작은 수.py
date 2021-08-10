import sys
input = sys.stdin.readline


N, X = map(int, input().split())

A = list(map(int, input().split()))

for i in range(N):
  if X > A[i]:
    print(A[i], end=' ')

# list안에 input으로 요소를 받이서 리스트를 만드는 발상
# 리스트 요소 접근은 리스트[인덱스]
# end=' '으로 한 줄로 출력하기