# There are too many iterations to test by brute force
# instead, we will create a set of iterations to hit 1 for every number
# we start like this
cache = {2:1} # because the sequence for 2 will converge after 1 step

def Collatz(number):  # this defines the Collatz operation
    if number not in cache: # if the number cache does not exist yet
        if number%2:# if the number is odd,
            cache[number] = 1 + Collatz(3*number + 1) # then the sequences it will take equals one plus the next number
        else:  # if it is even
            cache[number] = 1 + Collatz(number/2)  # then the sequance equals 1 + half of the number
    return cache[number] # once we have defined it, this is the number of steps it will take


lChain = 0   # we start with the longest chain as 0
num = 0    # the number that is the answer is 0 as well
for x in range(3,1000000): # for 3 to one million
    check = Collatz(x)   # we make a check value for the Collatz length of x
    if check > lChain:   # if the length is greater
        lChain = check   # we create a new length
        num = x   # and x becomes the new answer
print num
