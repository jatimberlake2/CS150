#Recursive version
def gcd(dividend, divisor):
	remainder = dividend%divisor
	#Base case
	if (remainder == 0):
		return divisor
	else:
	#Recursive case
		return gcd(divisor, remainder) #Recursive call

def loopGCD(dividend, divisor):
	while (divisor != 0):
		remainder = dividend%divisor
		dividend = divisor
		divisor = remainder
	return dividend

