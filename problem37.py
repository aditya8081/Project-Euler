primeNum = 1000000
primeCheck = [True] * primeNum
primes = []

def sieveAlg(x):
    for y in range(2*x,primeNum,x):
        primeCheck[y] = False

for y in range(2,int(primeNum**0.5)+1):
    if primeCheck[y]:
        sieveAlg(y)

for x in range(2,primeNum):
    if primeCheck[x]:
        primes.append(x)
########################################################
# generates list of primes#

def digits(number):   # converts a number to a list of numbers
    answer = []
    for y in str(number):
        answer.append(int(y))
    return answer

def undigits(list1):  # converts a list of numbers to one number
    answer = ''
    for y in list1:
        answer += str(y)
    return int(answer)

def truncate(number,places):  # splits a number based on is places
    part1 = []
    part2 = []
    dig = digits(number)
    for y in range(0,places):
        part1.append(dig[y])
    for y in range(places,len(dig)):
        part2.append(dig[y])
    return [undigits(part1),undigits(part2)]

def digCheck(number):  # certain digits cannot be in certain places
    dig = digits(number)  # this function makes sure of that
    checklist1 = [0,2,4,5,6,8]  # any even numbers, 5 or 0 cannot be in the middle
    for y in range(1,len(dig)-1): # since when the truncation occurs, these numbers
        if dig[y] in checklist1:  # indicate a composite number
            return False
    checklist2 = [1,4,6,8,9] # these numbers cannot be at the ends since
    if dig[0] in checklist2: # eventually, these numbers will stand alone, and 
        return False  # therefore must be prime
    if dig[len(dig)-1] in checklist2:
        return False
    return True

newPrimes = []  
for y in primes: # takes out some of the primes that require no truncation to check
    if y<10:
        continue
    if y < 100:
        newPrimes.append(y)
    elif digCheck(y):
        newPrimes.append(y)


truncatable = []
for num in newPrimes:  # checks the truncation of each prime number
    truncatable.append(num)    
    for y in truncate(num,1):
        if y not in primes and truncatable.count(num) ==1:
            truncatable.remove(num)
    if num > 100:
        for y in truncate(num,2):
            if y not in primes and truncatable.count(num) ==1:
                truncatable.remove(num)
    if num > 1000:
        for y in truncate(num,3):
            if y not in primes and truncatable.count(num) ==1:
                truncatable.remove(num)
    if num > 10000:
        for y in truncate(num,4):
            if y not in primes and truncatable.count(num) ==1:
                truncatable.remove(num)
    if num > 100000:
        for y in truncate(num,5):
            if y not in primes and truncatable.count(num) ==1:
                truncatable.remove(num)

print(sum(truncatable))
## anything with a 0,2,4,5,6,8 within it will not be prime 


