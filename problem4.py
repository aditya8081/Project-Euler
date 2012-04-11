def Digitize(x):   # a function to convert any number into a list of its digits
    digits = []     # initializes an empty list for the numbers
    digitVal=0      # starts with the digitvalue as 0
    while 10** digitVal <= x:   # this loop checks to see how many digits
        digitVal +=1             # there are int the number
    xTemp = x
    while digitVal >= 0:     # until we get down to the digit
        placeVal = xTemp/(10**digitVal)   # we find the place value of the highest digit yet...
        digits.append(int(placeVal))   # ...then add it to the list
        xTemp= xTemp - (10**digitVal)*digits[len(digits)-1]   # we then subtract that value from the number
        digitVal -=1  # and reduce the digitvalue
    if digits[0] == 0:    # if the first digit is 0, then we remove that digit
        digits.remove(0)   
    return digits

def palindrome(y):# This is a function to check for whether a number is a palindrome
    for x in range(0,int(len(y)/2)):    # this loop runs through the first half of each number
       if y[x] != y[len(y)-1-x]:        # if any number does not match the mirrored number
           return False                 # return false
    return True                         # however, if nothing returns false, then return true


answer = 0  # this is the first answer value, 0                     
a= 999      # we start with a value of 999 for a (must be a 3 digit number) and reduce by one (see below)
while a > 100:    # while it remains a 3 digit number (100 can be excluded because it will trailing zeroes so no palindrome can be formed)
    if a*a < answer:     # if the square of a is less than what we have for the answer, then no multiplication will work, ...
        break            # so just break out of the loop
    else:             # However, if we can get a value higher than what we had before
        for i in range(a,99,-1):   # we will run through each 3 digit number below a (if we did anything above, it would be redundant)
            if palindrome(Digitize(a*i)): # if it is a palindrome...
                if a*i > answer:          # ..and larger than our current top value...
                    answer = a*i          # make that the answer
                    break                 # and break out to the next value in while loop because each value of i will just make the number smaller
    a -=1 # where I reduce by one (see above)

    
print answer
