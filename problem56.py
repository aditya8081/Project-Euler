def sumDigits(number):
    answer = 0
    for y in str(number):
        answer += int(y)
    return answer

final = 20
for a in range(0,100):  # goes through every base/power pair
    for b in range(0,100):
        check = (sumDigits(a**b)) # and finds the highest value
        if final < check:
            final = check
            
print final
