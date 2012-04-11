primeCheck = [True] * 2000000 # starts by initializing a list of true

def seiveAlg(prime): # a function to mark each value as composite
    for d in range(2*prime,len(primeCheck),prime):  # goes through each multiple of the primes
        primeCheck[d] = False    # and marks the multiples as composite

for x in range(2,int(2000000**0.5),1):  # for all numbers up to the sqrt of 2 million
    if primeCheck:    # if it is prime
        seiveAlg(x)    # cross out the multiples

answer = 2  # intializes a sum value as 2 for that prime
        
for y in range(3,1999999,2):   # for every odd number up to 2 million
    if primeCheck[y]:   # if the number is prime
        answer +=y     # add it to the sum

print answer # print the value at the end
