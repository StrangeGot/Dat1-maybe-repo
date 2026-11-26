#I make a list for prime numbers
Primenum = []
#I make loop that checks each number, then another loop inside that checks whether it can be divided into a whole number by any number before it. if it can, we break loop. if it can't, we append the number to the Primenum list and break. If i don't break after that, it appends too many of same numbers
for num in range(2,100):
    for n in range(2,num):
        if num % n == 0:
            break
        else:
            Primenum.append(num)
            break

print(Primenum)