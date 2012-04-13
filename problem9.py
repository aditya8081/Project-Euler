a=300
b=400
c=400 # we have a starting point


while a**2 + b**2 != c**2: # while the numbers are not a pythagorean triple
    if a**2 + b**2 > c**2: # if a and b are too high
        a -=1  # subtract 1 from a
        b -=1  # and 1 from b
        c +=2  # but add 2 to c to keep the numbers' sum at 1000
    if a**2 + b**2 < c**2: # but if c is too high
        b+=1  # add 1 to b
        c-=1  # and subtract 1 from x

print a*b*c #once we hit the pythagorean triple, print the product of the numbers
    
