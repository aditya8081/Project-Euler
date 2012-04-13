amiPairs = {}      # This initializes a dictionary for each amicable pair
toBeTested = range(2,10001)  # this represents the range of numbers whose amicable pairs we
                             #are trying to test for

def sumDivisors(number):           # This is a function for the sum of divisors
    divisors = [1]   # this initializes a list for the divisors of a number
    for x in range(2,int(number**.5)+1):   # for all of the numbers from 2 to the sqrt of the number 
        if number%x == 0:  # if x is a divisor of the number we are checking
            divisors.append(x)  # we add the divisor
            divisors.append(number/x) # and the corresponding divisor to the list
    return sum(set(divisors))  # at the end, we add them all up 

for y in range(2,10001):     # for all numbers between 2 and 10000
    amiPairs[y] =  sumDivisors(y) # the sum of the divisors is stored as a dictionary called amiPairs

answer = 0  # this initializes the variable for the answer
for x in toBeTested:  # for x in the range we want to test
    if amiPairs[x] == 1 or amiPairs[x]>10000: # if the pair is 1 or greater than 10000 we have exitted our range
        continue  # so go to the next number
    elif amiPairs[x] == x:  # if the sum of the numbers equals the number
        continue # skip it as well
    elif x== amiPairs[sumDivisors(x)]: # but if the sum of the divisors of the sum of divisors of the number equals the number
        answer += x+ amiPairs[x] # the number is an amicable pair so we add it to the answer as well as the corresponding pair
        toBeTested.remove(amiPairs[x]) # and we remove the first number so that the amicable pair sum won't be doubled 

print answer  # after that, we print the answer
