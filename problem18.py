triangle = [
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,27,65],
[19,1,23,75,3,34],
[88,2,77,73,07,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,04,68,89,53,67,30,73,16,69,87,40,31],
[04,62,98,27,23,9,70,98,73,93,38,53,60,04,23]]

def rowCheck(array, rowNum): # this is a function to sum up tow values
    for x in range(0,len(array[rowNum])):  # while x is still in the row
        
        if array[rowNum+1][x] > array [rowNum+1][x+1]: # we choose which path to add
            array[rowNum][x] += array[rowNum+1][x]
        else:
            array[rowNum][x] += array[rowNum+1][x+1]  # and add the appropriat path           
    return array[rowNum] # and return the reduced row

for y in range(13,-1,-1): # this part iterates through all the rows from bottom to top until the answer is reached
    triangle[y]=rowCheck(triangle,y)

print triangle[0][0] # which is printed here
