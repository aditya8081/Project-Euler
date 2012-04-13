pentagonals = []

for n in range(1,700):
    pentagonals.append(n*(3*n-1)/2)

print 'Done with pentagonal list'


for x in pentagonals:
    print x
    for y in pentagonals:
        if pentagonals.count(x+y) !=0 and pentagonals.count(x-y) !=0:
            print 'Yay'
            break

print 'Done'
