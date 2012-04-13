x=0 
y=1 #Starts with the two first fibonacci numbers
sum=0 # initializes a sum variable
while y < 4000000:            # while the fibonacci term is less than 4 million
    z=x+y                     # find the next term
    if z%2 == 0:              
        sum += z            # add it to the sum if it is even
    x=y                     #refresh the variables for the next iteration
    y=z
print sum
    
