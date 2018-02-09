import sys

def main():
    #Reading from user input
    name = input("What is your name?")
    print(name)
    age = eval(input("What is your age?"))
    print(age)
    print(name, age, sep = "5", end = "")
    #sep is default space, end no new line

    #sys.argv[1] out of range???
    print(sys.argv)
    print("The name of my program is", sys.argv[0])
    print("The next argument is", sys.argv[1])
    for arg in sys.argv:
        print(arg)

    readfile = open("grade.py", "r") #must be string and r for read or w for write
    contents = readfile.read()
    print(contents)
    
    readfile.close()
    
    #writefile = open("notes.txt", "w")
    writeContents = input("What do you want to write?")
    writefileP = open(writefile, "w")
    writefile.write(writeContents)
    writefile.close()
    readContents = writefile.read()
    print(readContents)
 
    writefile.close()

    with open("notes.txt", "a") as appendfile:
        appendContents = input("What do you want to append?")
        appendfile.write(appendContents)
main()
