w = list(input().upper()) # Mississipi

acnt = []

for i in range(len(w)):
    acnt.append(w.count(w[i]))



cnt = 0
for j in range(len(acnt)):
    if max(acnt) == acnt[j]:
        cnt += 1

print(cnt)

# for k in range(len(w)):
#     if w.count(w[k]) == max(acnt) and cnt == 1:
#         print(w[i])
#     else:
#         print('?')




