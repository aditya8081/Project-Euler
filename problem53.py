def factorial(num):  # factorial function
    answer = 1
    if num == 0 or num==1:
        return 1
    for y in range(num,1,-1):
        answer *= y
    return answer

def Combination(n,r):  # combination function
    return factorial(n)/factorial(r)/factorial(n-r)

answer = 0

starting = 23  # starts at 23 since that is the first
ending = 100
for n in range(starting,ending+1): # checks every factorial if it is greater than
    for r in range(2,(n+1)):  # one million
        if Combination(n,r) > 1000000:
            answer += 1
            

print answer
