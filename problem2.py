x=0
y=1
sum=0
while y < 4000000:
    z=x+y
    if z%2 == 0:
        sum = sum+z
    x=y
    y=z
print sum
    
