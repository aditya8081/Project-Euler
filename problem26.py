def cycleLength(n):
    i = 1
    if n%2 == 0:
        return cycleLength(n/2)
    if n%5 == 0:
        return cycleLength(n/5)  ## both of these divide 10, so any of these are just a shift
    while True:# to determine a fraction from a repeating pattern, we take the pattern and multiply it by 10 until we have a divisor
        if ((10**i)-1)%n == 0:    # then subtract 1 like this algorithm
            return i
        else:
            i+=1

answer = 7
maxCycleLength = 3
check = 0
for x in range(1,1000):
    check = cycleLength(x)
    if check > maxCycleLength:
        maxCycleLength = check
        answer = x

print answer
