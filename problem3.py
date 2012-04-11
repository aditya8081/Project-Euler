check = int(600851475143**.5)
primeCheck = [True] * check
primes = []

def seiveAlg(prime):
    d= 2*prime
    while d< len(primeCheck):
        primeCheck[d] = False
        d+=prime

x=2
while x < check**.5:
    if primeCheck[x]:
        seiveAlg(x)
    x+=1

y=2
while y<600851475143**.5 - 1:
    if primeCheck[y]:
        primes.append(y)
    y+=1

answer = 0
check = 600851475143
while check !=1:
    for y in primes:
        if check%y == 0:
            check /=y
            if y > answer:
                answer = y

print answer
