n = int(input())

k = 0

while True:
    if n in range(3*k*(k+1)+2):
        print(k+1)
        break
    k += 1

# 한 칸 (2 ~ 7), (8 ~ 19), (20 ~ 37), (38 ~ 61), ....
# 한 칸 가장 왼쪽 2 + 6*Σ(k) / 2 + 6*sum(range(1, k)) / Σ(k) == k*(k+1) / 2
# n이 다음 왼쪽보다 작을 때 k값에 1일때 1칸을 더해서 칸 수를 구했다.

# 2 실패했음

N = int(input())

i = 0

while True:
    if 2 + 6 * sum(range(1, i)) <= n <= 7 + 6 * sum(range(2, i+1)):
        print(i + 1)
        break
    i += 0

# 작은 값들은 제대로 나왔다.
# 큰 수를 반복할 경우 시간이 오래걸렸고 실패로 떴다. 
# 계산 자체에는 오류가 없다고 판단됨

# 3 
if n < 2 + 6 * sum(range(1, i)): 

#  2를 더 간단하게 but 결과는 실패



# 4
arr = range(1000000000)

if n < arr[:2 + 6*sum(range(1, i))]:

# 결과는 2, 3과 다른게 없었다.
# 1은 결과 출력하는 속도도 그렇고 성공했고, 나머지랑 차이점을 모르겠음
# 2 + 6*sum(range)를 k(k+1) /2로 바꾼건데  