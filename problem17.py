sum = 0
def Digitize(x):   # see problem 4 for comments
    digits=[]
    digitVal=0
    while 10** digitVal <= x:
        digitVal +=1
    xTemp = x
    while digitVal >= 0:
        placeVal = xTemp/(10**digitVal)
        digits.append(int(placeVal))
        xTemp= xTemp - (10**digitVal)*digits[len(digits)-1]
        digitVal -=1
    if digits[0] ==0:
        digits.remove(0)
    return digits

def digitCheck(n):  # this represents the number of letters for each number
    if n == 1 or n == 2 or n == 6:
        return 3
    elif n == 4 or n == 5 or n == 9:
        return 4
    elif n == 3 or n == 7 or n == 8:
        return 5
    else:
        return 0

def digitCheck2(n):  # this represents each letter number for tens
    if n == 2 or n == 3 or n == 8 or n == 9:
        return 6
    elif n == 4 or n == 5 or n == 6:
        return 5
    elif n==7:
        return 7
    else:
        return 0

def digitCheckTeen(n): # this represents the letter number for the teens
    if n == 5 or n==6:
        return 7
    elif n == 3 or n == 8 or n == 9 or n==4:
        return 8
    elif n==1 or n==2:
        return 6
    elif n ==7:
        return 9
    else:
        return 3

dCheck = []

for x in range(1,1000):
    dCheck = Digitize(x)
    if len(dCheck) == 1:# if the number is 1 digit
        sum = sum + digitCheck(dCheck[0])   # then use the values for the first
    elif len(dCheck) == 2:  # if it is 2 digit
        if dCheck[0] == 1:
            sum = sum + digitCheckTeen(dCheck[1])  # this is the value for teen
        else:
            sum = sum + digitCheck2(dCheck[0]) # while these are the values for the ones
            sum = sum + digitCheck(dCheck[1])  # and tens places
    else:
        sum = sum + 10 # for "hundred and"
        sum = sum + digitCheck(dCheck[0]) # this is the value for the hundreds place
        if dCheck[1] == 1:  # and the same code from before applies here
            sum = sum + digitCheckTeen(dCheck[2])
        else:
            sum = sum + digitCheck2(dCheck[1])
            sum = sum + digitCheck(dCheck[2])
        if dCheck [1] == 0 and dCheck[2] == 0:
            sum = sum-3 #because the and must be taken out
sum = sum + 11  # the 11 is added for 1 thousand
print sum
