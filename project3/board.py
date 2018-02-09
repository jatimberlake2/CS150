def createArray(size):
	return ["_ "] * size

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

def move(b, s, player):
	if (s == 1):
		if b[0][0] != "_ ":
			print("Taken.")
			return
		b[0][0] = player
	elif (s == 2):
		if b[0][1] != "_ ":
			print("Taken.")
		b[0][1] = player
	elif (s == 3):
		
		b[0][2] = player
	elif (s == 4):
		b[1][0] = player
	elif (s == 5):
		b[1][1] = player
	elif (s == 6):
		b[1][2] = player
	elif (s == 7):
		b[2][0] = player
	elif (s == 8):
		b[2][1] = player
	elif (s == 9):
		b[2][2] = player
	else:
		print("Invalid input.")
		return	


def main():
	board = createBoard(3, 3)
	displayBoard(board)
	winFlag = False
	whoseMove = True
	while not winFlag:
		# input from user for one space
		space = int(input("Which space?"))
		if whoseMove == True:
			move(board, space, "X")
		else:
			move(board, space, "O")
		displayBoard(board)
		
		whoseMove = not whoseMove


main()
