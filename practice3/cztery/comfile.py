import sys
from scanner import *

def findSmallest(list):
	smallest = list[0]
	for i in range(len(list)):
		if (list[i] < smallest):
			smallest = list[i]
	return smallest

def main():
	needfile = str(sys.argv[1])
#	print(needfile)
	s = Scanner(needfile)
	i = s.readint()
	array = []
	while (i != ""):
		array.append(i)
		i = s.readint()
#	print(array)
	print("The smallest number is", findSmallest(array))
	s.close()
main()	
