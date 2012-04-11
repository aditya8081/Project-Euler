list1 = []
list2 = []  # initializes 2 blank lists

for e in range(1,101):
    list1.append(e)    # in the first, we add every number from 1 to 100

for e in range(1,101):
    list2.append(e*e)  # in the second, we add the square of every number from 1 to 100

print sum(list1)**2 - sum(list2) #finally, we take the difference of the square
# of the sums and the sum of squares
