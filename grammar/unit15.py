# elif 사용하기
x = 20
if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')

# if, elif, else 모두 사용하기
x = 30
if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')

# practice 15.3
x = int(input())
if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

age = int(input())
balance = 9000
if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
elif age >= 19:
    balance -= 1250