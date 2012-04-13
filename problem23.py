def sumDivisors(n):  # this is a function for the sum of divisors of x (similar to problem 21)
    number = 1  # instead of initializing an array, it just creates a sum
    for x in range(2,int(n**0.5)+1):  # for the same range
        if n%x == 0:   # it adds the corresponding values
            number+= x + n/x
        if x*x == n:  # if the number is a square number, we have to remove the repeat from the value
            number -=x
    return number  # we then return the final result

def abundantTo(n):   # this calculates the abundant numbers to a value
    abundant = [12]   # we start with the first number, 12
    for num in range(13,n+1):  # from 13 to where we need
        if sumDivisors(num) > num:   # it checks if the sum of divisors is greater than the number
            abundant.append(num) # and appends that to the abundant number array
    return abundant # it then returns said array


abNums = abundantTo(28111) # first we need the number of abundants to our value
c=len(abNums)

sumAbundant = [True]* 28124 # this is an array for if a number cannot be written as the sum of 2 primes

for x in abNums:
    for y in abNums:          # this iteratres through every pair of x and y
        check = x + y
        if check < 28124:       # and crosses out every number than can be written as the sum
            sumAbundant[check] = False
        else:   # if the number is larger than our range
            break  # break off the loop and move on to the next x


answer = 0 # this initializes the answer as 0
for x in range(0,28124): # for all of the numbers we wish to check
    if sumAbundant[x]:  # if the number cannot be written as the sum of abundants
        answer+=x  # add it to the answer
        
print answer # prints the answer at the end
