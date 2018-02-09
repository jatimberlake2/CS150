def main():
    arrayThing = [0, 0, 0]
    print(arrayThing)
    arrayThing[0] = float(input("First input?"))
    arrayThing[1] = float(input("Second input?"))
    arrayThing[2] = float(input("Third input?"))
    print("Current State: ", arrayThing)
    temp = arrayThing[0]
    arrayThing[0] = arrayThing[2]
    arrayThing[2] = temp
    print("Swapped: ", arrayThing)
main()
