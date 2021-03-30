start, stop = map(int, input('입력 요망: ').split())

i = start

while True:
    if i % 10 == 3:
        i += 1
        continue
    if i == stop + 1:
        break
    print(i, end=' ')
    i += 1