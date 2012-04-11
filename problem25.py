x=0
y=0
z=1
count = 1
while z/10**999 <1:
    x=y
    y=z
    z=x+y
    count +=1

print count

