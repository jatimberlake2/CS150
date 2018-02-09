def findSmallest(list):
	smallest = list[0]
	for i in range(len(list)):
		if (list[i] < smallest):
			smallest = list[i]
	return smallest

def main():
	array = eval(input("Give me an array of numbers:"))
	print("The smallest number is", findSmallest(array))
main()	
