def createArray(size):
	return ["-"] * size

def createBoard(rows, cols):
	matrix = createArray(rows)
	for i in range(rows):
		matrix[i] = createArray(cols)
	return matrix

def displayBoard(b):
	rows = len(b)
	cols = len(b[0])
	for i in range(rows):
		for j in range(cols):
			print(b[i][j], end = "")
		print()

def main():
	
	db = createBoard(4,4)
	nameCounter = 0
	cwidCounter = 0
	cityCounter = 0
	yearCounter = 0
 
	while True:

		action = input("Enter addName, addCWID, addCity, or addYear")
		actionList = action.split(" ")
		if actionList[0] == "addName":
			db[nameCounter][0] = actionList[1]
			nameCounter += 1
		elif actionList[0] == "addCWID":
			db[0][1] = actionList[1]
		elif actionList[0] == "addCity":
			db[0][2] = actionList[1]
		else:
			db[0][3] = actionList[1]
#	for i in range(len(db)):
#		name = input("What name?")
#		CWID = input("CWID?")
#		city = input("City?")
#		year = input("What year?")
#		db[i][0] = name
#		db[i][1] = CWID
#		db[i][2] = city
#		db[i][3] = year
#		print("Data recorded.")
	displayBoard(db)
	
main()
