def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(100))

def gcd(a,b):
    if a%b == 0:
        return 1  
    else:
        return n*factorial(n-1)

def loopFactorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        m = 1
        for i in range(1, n+1):
            #m = m*i
            m *= i
    return m

def main():
    print(loopFactorial(4))

main()
