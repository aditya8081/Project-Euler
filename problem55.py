def digits(number):
    ans = []
    for y in str(number):
        ans.append(int(y))
    return ans

def undigits(list1):
    ans = ''
    for y in list1:
        ans += str(y)
    return int(ans)

def flipNum(number):  # makes the palindrome of the number
    temp = digits(number)
    temp.reverse()
    return undigits(temp)

def isLych(number,iterations):  # after 50 iterations, checks if the number flipped
    if iterations == 0:  # is actually a palindtrome
        return isLych(number + flipNum(number),iterations+1)
    if iterations >= 50:
        return 1
    elif flipNum(number) == number:
        return 0
    else:
        return isLych(number + flipNum(number),iterations+1)

answer = 0


for y in range(1,10000):
    answer += isLych(y,0)

print answer
