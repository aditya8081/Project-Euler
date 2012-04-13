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

for x in range(2,int(1000**0.5)):         # i've used this algorith so much
    if primeCheck[x]:   # do you really need me to comment it again?
        seiveAlg(x)
        
for y in range(2,1000):
    if primeCheck[y]:
        primes.append(y)

for y in primes:
    if y<0:
        break
    primes.append(-y)
##### We also need to check for negative prime values for negative coefficients as well

for a in primes:
    for b in primes:  # this runs through every combination of a and b
        n=0  # we start with a count of primes at 0
        check = n**2  + a*n + b  # this is the check value for number 1
        if check < 0:  # if this comes out negative, skip and move onto the next prime
            continue        
        while primes.count(abs(n**2  + a*n + b)) >0:   # so while this value is prime
            n+=1  # check the next one
        if n> consecPrimes: # once we are done with that, if that was a new record
            consecPrimes = n  # make that the consecutive prime mark
            finalA=a # and save the numbers as the final a and b
            finalB=b

print finalA*finalB # finally, print the answer right here
