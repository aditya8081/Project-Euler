def Digitize(x):   # used this a lot as well. Nothing really more to say
    digits= []
    temp = str(x)
    for y in temp:
        digits.append(int(y))
    return digits

def fifthSum(matrix):  # this is a function that prints the sum of all digits to the 5th
    sum=0 #start with sum = 0
    for y in matrix: # and for every number in the list 
        sum += y**5 # add it to the fifth to the running total
    return sum

answer = 0

for x in range(100,354294):  # the hightest value fot 9^5 is the upper bound
    if fifthSum(Digitize(x))==x: # if the fifth sum of the digits equals x
        answer += x  # add x to the running total

print answer # print the answer at the end
