numPrimes = 2000000
isPrime = [True]*numPrimes
primes = []

def primeCheck(x):
    for y in range(2*x,numPrimes,x):
        isPrime[y] = False
    return 0

primeCheck(2)
for y in range(3,int(numPrimes**.5),2):
    if isPrime[y]:
        primeCheck(y)

for y in range(2,len(isPrime)):
    if isPrime[y]:
        primes.append(y)


diagonals = [1]
sideLength = 1

new = 1
ratio = 1
check = 900
while ratio > .1:
    new +=1
    sideLength +=2
    new+=sideLength-2
    diagonals.append(new)
    for y in range(0,3):
        new+=sideLength-1
        diagonals.append(new)
    numDiag = 0
    for y in diagonals:
        if y in primes:
            numDiag +=1
    check = numDiag
    ratio = float(numDiag)/float(len(diagonals))

print(sideLength)
