from random import *

def main():
    greet("multiverse")
    n = int(random() * 100)
    print("Hello, world number ",n,"!",sep="")
    return

def greet(who):
    print("Greetings to the ",who,"...",sep="")
    return 

main()

