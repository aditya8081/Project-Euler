diagonals = [1] # If you look, these are the sets of numbers that are the mod 1
                # upon division by 1 less than the number of sides
side = 3
while side <=1001:
    for x in range((side-2)**2+1,side**2+1):  # so this part does said value
        if x%(side-1)==1:
            diagonals.append(x)
    side +=2

print sum(diagonals)
