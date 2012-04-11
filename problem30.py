def Digitize(x):
    digits= []
    digitVal=0
    while 10** digitVal <= x:
        digitVal +=1
    xTemp = x
    while digitVal >= 0:
        placeVal = xTemp/(10**digitVal)
        digits.append(int(placeVal))
        xTemp= xTemp - (10**digitVal)*digits[len(digits)-1]
        digitVal -=1
    return digits

def fifthSum(matrix):
    sum=0
    for y in range(0,len(matrix)):
        sum += matrix[y]**5
    return sum

check = 0

for x in range(100,354294):  # the hightest value fot 9^5
    if fifthSum(Digitize(x))==x:
        check = check+x

print check
