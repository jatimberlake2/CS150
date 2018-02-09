import math

def distanceTo(s,p):
	return math.sqrt((p[0]-s[0])**2+(p[1]-s[1])**2)


def main():

	endPts = []*3
	endPts = eval(input("Gimme three points:"))
	A = endPts[0]
	B = endPts[1]
	C = endPts[2]	
	#A = eval(input("What is your first point?"))
	#B = eval(input("What is your second point?"))
	#C = eval(input("What is your last point?"))
	
	area = abs((A[0]*(B[1]-C[1])+B[0]*(C[1]-A[1])+C[0]*(A[1]-B[1]))/2)
	side1 = distanceTo(A,B)
	side2 = distanceTo(B,C)
	side3 = distanceTo(C,A)
	print("Side1:", side1)
	print("Side2:", side2)
	print("Side3:", side3)
	print("Perimeter:", side1+side2+side3)
	print("Area:", area)

main()
