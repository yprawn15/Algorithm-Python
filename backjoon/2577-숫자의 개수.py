A = int(input())
B = int(input())
C = int(input())

arr = list(str(A * B * C))


for i in range(10):
  print(arr.count(f'{i}'))

# count는 리스트 내 특정 요소의 개수를 구하는 매서드다.
# 여기서 주의점 1. a,b,c의 곱을 그냥 리스트에 넣으면 int는 반복 가능한 객체가 아니므로 str을 써서 반복가능한 객체인 문자열로 만들어주고
# 2. count()안에 그냥 i를 넣으면 리스트안의 숫자들은 문자열이라서 오류를 범하게 된다. 그래서 f 포매팅으로 해결해서 i를 넣어야 한다.
