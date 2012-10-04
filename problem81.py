mat = open('problem81.txt','r')
raw_path = mat.read().split('\n')
path = []
for y in raw_path:
    path.append(y.split(','))
for y in range(0,len(path)):
    for x in range(0,len(path[0])):
        path[y][x] = int(path[y][x])
mat.close()

## Gets the matrix into a readable form of integers
## First value represents vertical, second value represents horizontal
##path =[[131,673,234,103,18],  # my approach: start at the bottom right
##       [201,96,342,965,150],  # add the smallest value possible from either the right
##       [630,803,746,422,111], # or the bottom until you get to the top
##       [537,699,497,121,956],
##       [805,732,524,37,331]]
side = len(path)
for diagonal in range(1,side*2-1):
    y = side-1
    x = side-1-diagonal
    if x < 0:
        y+=x
        x-=x        # starting point for the diagonals
    while x <= side-1 and y >= 0:
         # runs along the diagonal
        if y==side-1:
            path[y][x] += path[y][x+1]
        elif x ==side-1:
            path[y][x] +=path[y+1][x]
        else:
            if path[y+1][x] < path[y][x+1]:
                path[y][x]+=path[y+1][x]
            else:
                path[y][x] += path[y][x+1]
        x+=1
        y-=1

print path[0][0]
