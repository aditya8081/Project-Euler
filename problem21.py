amiPairs = {}
toBeTested = range(2,10001)

def sumDivisors(number):
    divisors = [1]
    for x in range(2,int(number**.5)+1):
        if number%x == 0:
            divisors.append(x)
            divisors.append(number/x)
    return sum(set(divisors))

for y in range(2,10001):
    amiPairs[y] =  sumDivisors(y)

answer = 0
for x in toBeTested:
    if amiPairs[x] == 1 or amiPairs[x]>10000:
        continue
    elif amiPairs[x] == x:
        continue
    elif x== amiPairs[sumDivisors(x)]:
        answer += x+ amiPairs[x]
        toBeTested.remove(amiPairs[x])

print answer
