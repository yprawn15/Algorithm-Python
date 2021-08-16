# 1
def self():
  arr = list(range(1, 10001)) # [1, 2, 3, .... ,10000]

  for i in range(1, 10000): 
    gen = i + (i // 1000) + ((i % 1000) // 100) + (((i % 1000) % 100) // 10) + (((i % 1000) % 100) % 10)
    # gen = 생성자가 있는 숫자 
    if gen in arr: 
      arr.remove(gen) # 생성자가 있는 숫자만 남기기
    
  for j in range(len(arr)): 
    print(arr[j])

self()

# d(75) = 75 + 7 + 5 = 87
# 75는 d(75)의 생성자라 한다.
# 생성자는 한 개 이상일 수 있다. ex) 101의 생성자는 91, 100이다.
# 생성자가 없는 숫자를 셀프 넘버라고 한다. 

# 2
num_set = list(range(1, 10001)) # [1, 2, 3, ...., ,10000]
gen_set = []

def gen(i): # gen 함수 > 생성자 있는 숫자
  geng = i # 9786

  while i > 0:  
    geng += i % 10
    i //= 10
  
  return geng

for i in range(1, 10001):
  gen_set.append(gen(i))

new_set = sorted(list(set(num_set) - set(gen_set)))

for j in new_set:
  print(j)

# print(*new_set, sep='\n') *list하면 list 내의 요소들을 모두 뽑아 낼 수 있다.
# 전부 함수안에 집어 넣는 것은 안 좋음
# 쓸 부분만 판단해서 함수로 이용
# 1방식과 마찬가지만 while 반복문을 이용해서 간편히 만들었고 1과 다른점은 1은 앞에서부터 9786을 뽑아내려했다면 
# 2는 뒤에서부터 뽑아냈다.
# list()안에 set를 넣을 수 있었다를 알게됨 




# 3
n_set = list(range(1, 10001)) 
g_set = []

def gen(i):
  geng = sum(list(map(int, i))) + int(i)
  return geng

for k in list(map(str, range(1, 10001))):
  g_set.append(gen(k))

now_set = sorted(list(set(n_set) - set(g_set)))

for j in now_set:
  print(j)

# 2의 비슷한 방식으로 3을 풀어봤음