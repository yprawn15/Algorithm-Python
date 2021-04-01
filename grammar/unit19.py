# unit19.
for i in range(5): # 5번 반복. 바깥쪽 루프는 세로 방향
    for j in range(5): # 5번 반복. 안쪽 루프는 가로 방향
        print('j:', j, sep='', end=' ') # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
    print('i:', i, '\\m', sep='') # i값 출력, 개행 문자 모양도 출력
                              # 가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감
                              # print는 기본적으로 출력 후 다음 줄로 넘어감

# 19.1.1 * 사각형 만들기
for i in range(5):
    for j in range(5):
        print('*', end='')
    print() # print는 기본적으로 \n 상태이므로 end=''로 줄바꿈을 없애주지 않는한 줄바꿈을 함

# 19.2.1 사각형 모양 바꾸기
for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

# 19.3 계단식으로 별 만들기
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

# 19.3.1 대각선으로 별 출력하기
for i in range(5): # 5번 반복                  *  i=0 j=0 나머지 빈칸 4칸하고 줄바꿈
    for j in range(5): # 5번 반복 가로 방향      * i=1 j=0일때 한칸 띄고 1일때 * 찍고 3칸 띄고
        if j == i:                           #   * 나머지 역시 같은 원리
            print('*', end='')               #    *
        else:   # 세로 방향 변수와 다를 때           * 
            print(' ', end='')
    print()

# practice
for i in range(5):
    for j in range(5):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
