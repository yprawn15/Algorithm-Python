n, m = map(int, input().split())

bw = []
wb = []

for _ in range(n):
    a = input()
    bw.append(a.count('BW'))
    wb.append(a.count('WB'))

print(bw)
print(wb)

print(sum(bw))
print(sum(wb))