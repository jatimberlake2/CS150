import sys
from List import *

def findSmallest(items):
	index = 0
	spot = items
	smallest = head(spot)
	ismallest = 0
	while (spot != None):
		if (head(spot) < smallest):
			ismallest = index
			smallest = head(spot)
		index += 1
		spot = tail(spot)
	return smallest

def main():
	strings = ArrayToList(sys.argv[1:])
	numbers = ListMap(int, strings)
	print("The smallest number is", findSmallest(numbers))

main()	
