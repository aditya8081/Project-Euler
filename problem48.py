sum = 0
for x in range(1,1001):
    sum+= x**x
sum = str(sum)
print sum[len(sum)-10:len(sum)]
