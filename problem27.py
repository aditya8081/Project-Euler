import math


finalA= 1
finalB= 41
consecPrimes = 40

primeCheck = [True] * 1000
primes = []

# I needa function to mark multiples as composite
def seiveAlg(prime):
    for d in range(2*prime,len(primeCheck),prime):
        primeCheck[d] = False

for x in range(2,int(1000**0.5)):
    if primeCheck[x]:
        seiveAlg(x)
        
for y in range(2,1000):
    if primeCheck[y]:
        primes.append(y)

for y in primes:
    if y<0:
        break
    primes.append(-y)

for a in primes:
    for b in primes:
        n=0
        check = n**2  + a*n + b
        if check < 0:
            continue        
        while primes.count(abs(n**2  + a*n + b)) >0:
            n+=1
        if n> consecPrimes:
            consecPrimes = n
            finalA=a
            finalB=b

print finalA*finalB
