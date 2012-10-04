def factorial(num):
    answer = 1
    if num == 0 or num==1:
        return 1
    for y in range(num,1,-1):
        answer *= y
    return answer

def Combination(n,r):
    return factorial(n)/factorial(r)/factorial(n-r)

primeSquares = [4,9,25,49]
tested = []

final = 0

rows = 51
for n in range(0,rows):  # generates pascal's triangle
    for r in range(0,rows/2+1):
        check = Combination(n,r)
        for y in primeSquares: # checks if each value is divisible by square numbers
            if check%y == 0:
                div = False
                break
            div = True
        if div and check not in tested: # appends to a list of tested values
            tested.append(check)
            final +=check

print final
        
    
