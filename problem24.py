def swap(matrix,i,j):
    a = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = a
    return matrix

def nextPermutation(digits):
    i = len(digits)-1
    while digits[i-1] >= digits[i]:
        i-=1
    j = len(digits)
    while digits[j-1] <= digits[i-1]:
        j-=1
    digits = swap(digits,i-1,j-1)
    i+=1
    j= len(digits)
    while i<j:
        digits = swap(digits,i-1,j-1)
        i+=1
        j-=1
    return digits

def facUnder(number):
    product = 1
    check = 0
    step = 2
    while product < number:
        product *= step
        step +=1
        check = step
    return check


print facUnder(25)
digits = [0,1,2,3,4,5,6,7,8,9]
##for y in range(0,10):
##    digits = nextPermutation(digits)
##    print digits
