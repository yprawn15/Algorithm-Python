n = int(input()) 

i = 2
while n != 1: # n이 1이 되기전까지
    if n % i == 0: 
        n //= i 
        print(i)
    else:
        i += 1


