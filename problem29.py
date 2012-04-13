combo = [] # we start with an empty list of combinations
c = 0 # where c = o
for a in range(2,101):
    for b in range(2,101):  # for every a and b in the range
        c = a**b  # c = a to the power of b
        if c not in combo:  # if c was not in combo
            combo.append(c) # add it to combo

print len(combo)  # finally, print the length of the list as the answer
