def digits(number):   # returns a list of digits of a number
    answer = []
    for y in str(number):
        answer.append(int(y))
    return answer

def undigits(matrix):   # converts a list of digits into a base 10 number
    answer = 0
    for y in range(0,len(matrix)):
        answer += matrix[y]*10**(len(matrix)-y-1)
    return answer

def commonGen(number):   # makes a list of numbers with a common digit...
    answer = []          # ...that are less than the number given
    matrix = digits(number)
    for y in matrix:
        for x in range(1,10):
            check1 = undigits([x,y])
            check2 = undigits([y,x])
            if answer.count(check1) < 1 and check1 < number:
                answer.append(check1)
            if answer.count(check2) < 1 and check2 < number:
                answer.append(check2)
    return answer

def elim(list1,list2): # eliminates similarities between 2 lists....
    answer = []        #... without altering the original lists
    temp1=[]
    temp2=[]
    for y in list1:
        temp1.append(y)
    for y in list2:
        temp2.append(y)
    for y in temp1:
        if temp2.count(y) > 0:
            temp1.remove(y)
            temp2.remove(y)
    return [temp1[0],temp2[0]]

def gcd2(c,d): #this formula also gets the gcd, but does not show the steps of the Euclidean Algorithm
    if c%d == 0: # it is used for the lcm calculation later on
        return d
    return gcd2(d,(c%d))

answerNum = 1
answerDen = 1

for den in range(10,100):  # den = denominators
    if 0 in digits(den):
        continue
    nums = commonGen(den)  # nums = list of numerators
    for num in nums:  # num = numerator
        check = elim(digits(num),digits(den))
        eliminated = float(check[0])/float(check[1])
        original = float(num)/float(den)  # checks the eliminated fraction with
        if eliminated == original:   # the original
            answerNum*=check[0]
            answerDen*=check[1]

factor = gcd2(answerNum,answerDen)
print str(answerNum/factor) +'/'+ str(answerDen/factor)
