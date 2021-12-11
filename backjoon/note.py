f0 = list(range(1, 11)) #[1, 2, 3, 4,... 10]

f1 = [0]*10

for i in range(10):
    f1[i] += sum(f0[0:i+1])

print(f1)