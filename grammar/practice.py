count = int(input())
i = count
for i in range(count):
    for j in reversed(range(count)):
        if j > i:
            print(' ', end='')
        else:print('*', end='')
    for j in range(count):
        if j < i:
            print('*', end='')
    print()


