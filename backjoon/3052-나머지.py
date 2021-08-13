a = []

for i in range(10):
  num = int(input())
  a.append(num % 42)
  
b = set(a)
print(len(b))

  
# append는 리스트 맨마지막 인덱스에 요소를 추가하는 매서드
# set로 중복되던 요소들을 제거