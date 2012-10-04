files = open('problem46.txt','r')
words = files.read().split(',')

for y in range(0,len(words)):
    words[y] = words[y].replace('"','')

triangles = []

for n in range(1,20):
    triangles.append(n*(n+1)/2)
 # ord - 64 gives right value

final = 0

for w in words: # w is the word
    check = 0  # word value sum
    for c in w: #c is the character
        check +=ord(c) - 64
    if check in triangles: # checks if the words are triangle numbers
        final +=1

print final
