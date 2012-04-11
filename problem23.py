def sumDivisors(n):
    sum = 1
    for x in range(2,int(n**0.5)):
        if n%x == 0:
            sum+= x + n/x
        if int(n**.5)==n**.5:
            sum -= n**.5
    return sum

def abundantTo(n):
    abundant = [12]
    for num in range(13,n+1):
        if sumDivisors(num) > num:
            abundant.append(num)
    return abundant

abNums = abundantTo(28123)
c=len(abNums)

sumAbundant = range(0,28124)

for x in range(0,c):
    for y in range(x,-1,-1):
        check = abNums[x]+abNums[y]
        if check < 28124:
            sumAbundant[check] = 0
        else:
            continue

print sum(sumAbundant)
