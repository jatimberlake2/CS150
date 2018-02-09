def ahead(items):
	return items[0]

def atail(items):
	return items[1:]

#python arrays
def count(items):
	if (items == []):
		return 0
	else:
		1 + count(atail(items))

def listcount(items):
	if items == None:
		return 0
	else:
		1 + count(atail(items))

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

def div2(n):
	if n == 0:
		return 0
	if n == 1:
		return 0
	else:
		return 1 + div2(n - 2)

def sum(items):
	if items == None:
		return 0
	else:
		return head(items) + sum(atail(items))
