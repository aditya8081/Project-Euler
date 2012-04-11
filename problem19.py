answer= 0 # we start with 0 months starting on a sunday
modsum = 2  # the first january in the range begins on a tuesday (2 in mod 7 assuming sunday is 0)
monthMod = [3,0,3,2,3,2,3,3,2,3,2,3] # this is an array for all of month lengths mod 7
for year in range(1901,2001):  # for every year
    for x in range(0,12):  # for every month
        modsum = modsum + monthMod[x]  # we add the modulo of the month
        if x==1 and year%4 == 0:      # if the month is february and it is a leap year, we add 1 more
            modsum +=1
        if modsum%7 == 0:   # then if the mod is 0, the month has sunday as the first day
            answer +=1   # so we add one to the sum
print answer
