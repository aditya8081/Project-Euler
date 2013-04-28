# how many n-digit integers exist that are an nth power of something
def numDigits(number):
    return len(str(number))

answer = 1
for y in range(2,10):
    n=1
    while n==numDigits(y**n):
        answer+=1
        n+=1

print(answer)
