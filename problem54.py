file = open('problem54.txt','r')

handVals = {'high':1,'pair':2,'two pair':3,'triple':4,'straight':5,'flush':6
            ,'full house':7,'four of a kind':8, 'straight flush':9} # poker hand values in order

def pokerSplit(list1):
    numbers = []
    suits = []
    for y in list1:
        if y[0] == 'A':
            numbers.append(14)
        elif y[0] == 'K':
            numbers.append(13)
        elif y[0] == 'Q':
            numbers.append(12)
        elif y[0] == 'J':
            numbers.append(11)  # converts the letters to numbers
        elif y[0] == 'T':
            numbers.append(10)
        else:
            numbers.append(int(y[0]))  # makes the hands into a number component
        suits.append(y[1]) # and a suit component
    return [numbers,suits]

def pokerHand(list1):  # returns poker hands from the split list
    temp = pokerSplit(list1)
    n_list = temp[0]
    n_list.sort()
    s_list = temp[1]
    final = []
    if s_list.count(s_list[0]) == 5:
        final.append([6,0])
    if (n_list[0]+4==n_list[1]+3==n_list[2]+2==n_list[3]+1==n_list[4]):
        final.append([5,n_list[0]])
    elif (n_list[4]-9==n_list[0]+3==n_list[1]+2==n_list[2]+1==n_list[3]):
        final.append([5,0])
    else:
        for y in n_list:
            if n_list.count(y) == 2:
                if [2,y] not in final:
                    final.append([2,y])
            elif n_list.count(y) == 3:
                if [4,y] not in final:
                    final.append([4,y])
            elif n_list.count(y) == 4:
                if [8,y] not in final:
                    final.append([8,y])
            else:
                final.append([1,y])
    final.sort()
    final.reverse()
    if final[0][0] == 4 and final [1][0] == 2:  # a trip and pair = full house
        final = [[7,[final[0][1],final[1][1]]]]
    elif final[0][0] == 2 and final [1][0] == 2: # pair and pair = two pair
        last = final[2]
        final = [[3,[final[0][1],final[1][1]]]]
        final.append(last)
    elif final[0][0] == 6 and final [1][0] == 5: #straight and flush = straight flush
        final = [[9,final[1][1]]]
    return final

def pokerCompare(hand1,hand2,place): # compares one hand with the other
    if hand1[place][0] > hand2[place][0]:
        return 1
    elif hand1[place][0] < hand2[place][0]:
        return 0
    else:
        if hand1[place][1] > hand2[place][1]:
            return 1
        elif hand1[place][1] < hand2[place][1]:
            return 0
        else:
            return pokerCompare(hand1,hand2,place+1)

raw_hand = file.read().split('\n') # list of the cards from the file
file.close()
hands = []
for y in raw_hand:
    hands.append(y.split(' '))

answer = 0

for hand_num in range(0,len(hands)-1): # goes through each hand
    player1 = []
    player2 = []
    for y in range(0,5):
        player1.append(hands[hand_num][y]) # splits them into the 2 players
    for y in range(5,10):
        player2.append(hands[hand_num][y])
    answer+= pokerCompare(pokerHand(player1),pokerHand(player2),0) # checks each hand

print answer
