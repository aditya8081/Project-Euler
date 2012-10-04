d = ''
y = 1
while len(d) < 1000000:
    d+= str(y)
    y+=1   # creates the string in question

answer = 1   # finds the product of the specific digits that we want
for x in range(0,7):
    answer *= int(d[10**x-1])

print answer
