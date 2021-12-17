M, N = map(int, input().split())

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)

# 에라토스테네스 체의 원리 
# (1, 121)까지라고 했을 때 
# 2부터 121의 제곱근까지의 배수들을 모두 지워나가면 나머지가 소수가 되는 원리이다.
