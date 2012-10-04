def undigits(matrix):   # converts a list of digits into a base 10 number
    answer = 0
    for y in range(0,len(matrix)):
        answer += matrix[y]*10**(len(matrix)-y-1)
    return answer

def palGen(digits):   # makes a list of palindromes that are a certain number
    answer = []      # of digits long by adding one to the outsides of the number
    number = []      # and carrying over digits to the inside as necessary
    for y in range(0,digits):
        number.append(0)
    lim = digits/2
    if digits%2 ==0:
        lim-=1    # could be made easier by taking the numbers 1 to whatever
    while True:   # and appending the reverse of themself to the end
        number[0]+=1
        number[len(number)-1] =number[0]
        for y in range(0,lim):
            if number[y] > 9:
                number[y]-=10
                number[digits-1-y] = number[y]
                number[y+1] +=1
                number[digits-y-2] = number[y+1]
                if number[0] == 0:
                    number[0]+=1
                    number[digits-1] = number[0]
        if number[lim]==10:
            break
        answer.append(undigits(number))
    return answer

def palList(upTo):   # generates all palindromes from 1 digit to how many ever
    answer=[]      # digits you want
    limit = len(str(upTo))-1
    for y in range(1,limit+1):
        for x in palGen(y):
            answer.append(x)
    return answer

def binarize(number):   # converts a number into binary by subtracting
    check= number    # the highest power of two possible each time
    answer = []    # there is probably a function for this in python,
    n = 0           # I just don't know it
    while 2**n <= number:
        n+=1
    for y in range(n,-1,-1):
        if 2**y <= check:
            answer.append(1)
            check -=2**y
        else:
            answer.append(0)
    return undigits(answer)

def isPal(number):   # checks to see if a number is binary
    check = str(number)
    for y in range(0,len(check)/2):
        if check[y] != check[len(check)-1-y]:
            return False
    return True

palindromes = palList(1000000)  # generates the list of palindromes up to 1 million
final = 0
for y in palindromes:
    if isPal(binarize(y)):  # for each number that has a binary palindrome
        final+=y  # add it to the running sum
print final
