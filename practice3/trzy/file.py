from scanner import *

def findSmallest(list):
	smallest = list[0]
	for i in range(len(list)):
		if (list[i] < smallest):
			smallest = list[i]
	return smallest

def main():
	s = Scanner("data.txt")
	i = s.readint()
	array = []
	while (i != ""):
		array.append(i)
		i = s.readint()
	print(array)
	print("The smallest number is", findSmallest(array))
	s.close()
main()	
