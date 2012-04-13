x=0
y=0
z=1 # these are the 3 variables that we have for the fibbonaci number
count = 1
while z/10**999 <1: # this is the way to determine if z is more than 1000 digits
    x=y
    y=z # this is where we set each variable to the previous one
    
    z=x+y  # this calculates the fibbonacci number next
    count +=1 # and increases the fibbonaci count by 1

print count

