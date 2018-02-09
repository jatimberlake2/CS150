def countEvens(items):
	if items == None:
		return 0
	elif head(items) % 2 == 0:
		return 1 + countEvens(tail(items))
	else:
		return 0 + countEvens(tail(items))

def extractEvens(items):
	if items == None:
		return None
	elif head(items) % 2 == 0:
		return join(head(items), extractEvens(tail(items)))		else:
		return extractEvens(tail(items))

def map(func, items):
	if items == None:
		return None
	else:
		return join(func(head(items)), map(func, tail(items)))

def find(target, items):
	if items == None:
		return False
	elif head(items) == target:
		return True
	else:
		find(target, tail(items))
