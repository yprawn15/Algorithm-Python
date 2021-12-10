import sys
input = sys.stdin.readline

T = int(input())

for i in range(1, T+1):
  A, B = map(int, input().split())
  print(f'Case #{i}:', A, '+', B, '=', A+B)

# f 문자열 포매팅
# f'문자열 {변수}' 이렇게 씀