## start with 1 at the top right
## the two intersections to the left and the right are 1
## each intersection is then the sum of the two numbers above and to the left of it
## this makes the grid essentially pascal's triangle diagonally
## so the number of routes will be the midway point on the 40th row of Pascal's triangle
## which is a combination table. So the answer will be 40 combination 20

def factorial(x):
    product = 1
    for num in range(1,x+1):
        product = product * num
    return product

def Combination(x,y):
    return factorial(x)/factorial(y)/factorial(x-y)

print Combination(40,20)
