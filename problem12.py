def triangle(n):       #a function that calculates the nth triangle number
    return n*(n+1)/2

def numFactors(y):     # a function that calculates the number of divisors a number has
    value=2    # we start with 2 that means 1 and the number
    for x in range(2,int(y**0.5)):  # up to the sqrt of said number
        if y%x ==0:   # if any number divides the triangle number
            value +=2  # increase the number of divisors by 2 (for x and y/x)
    return value

###########################################################

num = 1
numDiv= 1
while numDiv < 500:  # while the number of divisors is less than 100
    numDiv = numFactors(triangle(num)) # the number of divisors equals the nth triangle number
    num+=1 # increase n by 1 each time
print triangle(num-1) # when the final value is reached, print the triangle number

