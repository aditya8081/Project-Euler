primeCheck = [True] * 2000000 # starts with an array of True for 2 million numbers

def seiveAlg(prime): # this is a function that crosses out any multiple of a prime
    for d in range(2*prime,len(primeCheck),prime): # it starts at twice the prime and adds the prime each time
        primeCheck[d] = False  # marking every multiple as false

count = 0  # we start at 0. The count will increase after the first prime
num = 2    # this is the first number we check for primeness
while count <10001:   # while we have not hit the 10001st prime
    if primeCheck[num]:   # if the number is prime
        seiveAlg(num)    # cross out the multiples
        count +=1     # and add one to the count of prime numbers
    num+=1   # move onto the next number to check

print num-1   # the num counter goes 1 too high, so we print the last value as the answer
