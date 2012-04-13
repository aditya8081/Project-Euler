convergesTo = {1:1, 89:89 , 44:1,32:2,13:1,10:1,85:89,145:89,42:89,20:89,4:89,16:89
,37:89,58:89}

def digitize(n):
    number = str(n)
    a=[]
    for x in number:
        a.append(int(x))
    return a

def squareSum(matrix):
    y = 0
    for n in matrix:
        y+=n**2
    return y

def Chain(number):
    if number not in convergesTo:
        convergesTo[number] = Chain(squareSum(digitize(number)))
    return convergesTo[number]

count = 0
for x in range(2,10000000):
    if Chain(x) > 2:
        count+=1

print count
