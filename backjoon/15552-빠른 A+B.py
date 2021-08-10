import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
  A, B = map(int, input().split())
  print(A + B)

# sys.stdin.readline을 사용하는 이유는 입출력 속도를 빠르게 하기 위함
# 입출력하는 수가 매우 클 경우 사용
