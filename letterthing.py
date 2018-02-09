def main():
    myName = inputName()
    print(myName)
    j = 0
   #  while (j < len(myName)):
   #      print(myName[j])
   #      j = j + 1
def inputName():
    Name = [None, None, None, None, None, None]
    Name[0] = input("What is the first letter of your name?")
    i = 1 
    while (i <= 5 ):
        Name[i] = input("What is the next letter of your name?")
        i = i + 1
    temp = Name[0]
    Name[0] = Name[5]
    Name[5] = temp
    return Name
main()
