from scanner import *

def shuffle(array1,array2):
    array3 = []
#    if (len(array1) > len(array2)):
    i = 0
    while(i<len(array1) and i < len(array2)):
        array3.append(array1[i])
        array3.append(array2[i])
    return array3
#    return array3 + array2[i+1:]

def merge(array1,array2):
    array3 = []
    i = 0
    j = 0
    while (i < len(array1) and j < len(array2)):
        if (array1[i] < array2[j]):
            array3.append(array1[i])
            i = i + 1
        else:
            array3.append(array2[j])
            j = j + 1
    return array3 + array1[i:] + array2[j:]



def main():

    deck1 = []
    deck2 = []

    s = Scanner("deck1.txt")
    card = s.readline()
    while card != "":
        deck1.append(card)
        card = s.readline()
   
    s2 = Scanner("deck2.txt")
    card = s2.readline()
    while card != "":
        deck2.append(card)
        card = s.readline()
    
    print(deck1)
    print(deck2)
    
    fulDeck = shuffle(deck1, deck2)
    
    print(fulDeck)

main()
