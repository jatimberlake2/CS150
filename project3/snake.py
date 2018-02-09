import random
import math

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

def placeObj(b, snake, player):
	b[player[0]][player[1]] = "i "
	b[snake[0][0]][snake[0][1]] = "@ "
	for i in range(1, len(snake)):
		b[snake[i][0]][snake[i][1]] = "X "

def appendSnake(b, s):
	end = s[-1]
	possAdd = []
	#up
	if (end[0] - 1 >= 0 and b[end[0]-1][end[1]] == "_ "):
		possAdd.append((end[0]-1,end[1]))
	#left
	if (end[1] - 1 >= 0 and  b[end[0]][end[1]-1] == "_ "):
		possAdd.append((end[0],end[1]-1))
	#right
	if (end[1] + 1 < len(b[0]) and b[end[0]][end[1]+1] == "_ "):
		possAdd.append((end[0],end[1]+1))
	#down
	if (end[0] + 1 < len(b) and b[end[0]+1][end[1]] == "_ "):
		possAdd.append((end[0]+1, end[1]))
	#print(possAdd)
	if (len(possAdd) != 0):
		nxt = random.randint(0,len(possAdd)-1)
		added = (possAdd[nxt][0],possAdd[nxt][1])
		s.append(added)
	return s

def movePlayer(b, p):
	dr = str(input())
	b[p[0]][p[1]] = "_ "
	if (dr == "i" or dr == "I"):
		if (p[0]-1 >= 0 and b[p[0]-1][p[1]] == "_ "):
			p = (p[0]-1, p[1])
		else:
			print("You can't move there. Try again.")	
			movePlayer(b,p)
	elif (dr == "k" or dr == "K"):
		if (p[1]+1 < len(b[0]) and b[p[0]][p[1]+1] == "_ "):
			p = (p[0], p[1]+1)
		else:
			print("You can't move there. Try again.")	
			movePlayer(b,p)
	elif (dr == "j" or dr == "J"):
		if (p[1]-1 >=  0 and b[p[0]][p[1]-1] == "_ " ):
			p = (p[0], p[1]-1)
		else:
			print("You can't move there. Try again.")	
			movePlayer(b,p)
	elif (dr == "m" or dr == "M"):
		if (p[0]+1 < len(b) and b[p[0]+1][p[1]] == "_ "):
			p = (p[0]+1, p[1])	
		else:
			print("You can't move there. Try again.")	
			movePlayer(b,p)
	else:
		print("Invalid input.")
		movePlayer(b,p)
	return p

def distanceTo(s,p):
	return math.sqrt((p[0]-s[0])**2+(p[1]-s[1])**2)

def snakeMove(b,s,p):
	frnt = s[0]
	possMov = []
	#up
	if (frnt[0] - 1 >= 0 and s.count((frnt[0]-1,frnt[1])) == 0):
		possMov.append((frnt[0]-1,frnt[1]))
	#left
	if (frnt[1] - 1 >= 0 and  s.count((frnt[0],frnt[1]-1)) == 0):
		possMov.append((frnt[0],frnt[1]-1))
	#right
	if (frnt[1] + 1 < len(b[0]) and s.count((frnt[0],frnt[1]+1)) == 0):
		possMov.append((frnt[0],frnt[1]+1))
	#down
	if (frnt[0] + 1 < len(b) and s.count((frnt[0]+1,frnt[1])) == 0):
		possMov.append((frnt[0]+1, frnt[1]))
	#top left
	if (frnt[0] - 1 >= 0 and frnt[1] - 1 >= 0 and s.count((frnt[0]-1,frnt[1]-1)) == 0):
		possMov.append((frnt[0]-1,frnt[1]-1))	
	#top right
	if (frnt[0] - 1 >= 0 and frnt[1] + 1 < len(b[0]) and s.count((frnt[0]-1,frnt[1]+1)) == 0):
		possMov.append((frnt[0]-1,frnt[1]+1))
	#bottom left
	if (frnt[0] + 1 < len(b) and frnt[1] - 1 >= 0 and s.count((frnt[0]+1,frnt[1]-1)) == 0):
		possMov.append((frnt[0]+1,frnt[1]-1))
	#bottom right
	if (frnt[0] + 1 < len(b) and frnt[1] + 1 < len(b[0]) and s.count((frnt[0]+1,frnt[1]+1)) ==0):
		possMov.append((frnt[0]+1,frnt[1]+1))
	if (len(possMov) != 0):
		smallest = possMov[0]
		for i in range(0, len(possMov)-1):
			if (distanceTo(possMov[i],p) < distanceTo(smallest,p)):
				smallest = possMov[i]
		s2 = s[:]
		for i in range(1,len(s)):
			s[i] = s2[i-1]
		s[0] = (smallest[0],smallest[1])
	return s

def checkGame(b,s,p,pos):
	if (s[0] == pos):
		print("The snake is trapped! You win!")
		return True
	for i in range(len(s)):
		if (p == (s[i][0],s[i][1])):
			print("Oh no! The snake got you! Game over.")
			return True
	return False

def main():
	board = createBoard(20,30)
	snake = [(0,3),(0,2),(0,1)]
	player = (15,25)
	endGame = False
	scoreCount = 0

	placeObj(board, snake, player)
	displayBoard(board)
	while (not endGame):
		print("Enter j to move left, k to move right, i to move up, and m to move down.")
		if (scoreCount %5 == 0 and scoreCount != 0):
			snake = appendSnake(board, snake)
		scoreCount += 1
		pos = snake[0]
		for i in range(len(snake)):
			board[snake[i][0]][snake[i][1]] = "_ "
		player = movePlayer(board, player)
		snake = snakeMove(board,snake,player)
		endGame = checkGame(board,snake,player, pos)
		placeObj(board, snake, player)
		displayBoard(board)
	print("Score:",scoreCount)

main()
