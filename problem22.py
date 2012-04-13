f=open('C:\Python27\Euler\problem22.txt','rU') # this bit of code opens up the file in question
names = []   # names represents the names...
names = sorted(f.read().replace("",'').split(','),key=str)  # we then add a sorted list from the file as names

## just some code that reads the text file and outputs the sorted list of names

letterValues = {   # this represents a dictionary of all of the values for each letter
    'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
    'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def letterConverter(letter):  #this is a function that read the letter
    lc = 0
    lc = letterValues[letter]
    return lc # and outputs the corresponding number


numNames = len(names)
answer = 0
for x in range(0,numNames):   # this iterates through every name
    nameSum = 0              # and resets the sum of the name as 0
    for i in range(1,len(names[x])-1):  # this iterates through every letter
        nameSum += letterConverter(names[x][i])  # and adds the value of the letter to the nameSum
    answer += (x+1)*nameSum  # the answer will be the sum of the name times the place value, so we add that to the answer
     
print answer # tadaa, we have our answers
