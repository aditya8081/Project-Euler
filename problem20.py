def Factorial(q):  # a function that finds the factorial of a number
    z=1
    for c in range(2,q+1):
        z= z*c
    return z

digits = []

def Digitize(x): # see problem 4 for comments
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

print sum(Digitize(Factorial(100))) # self explanatory really
