def main():
    boo = eval(input("Give me a boolean."))
    please = input("Give me a string.")
    num = int(input("Give me an integer."))
    if boo:
        print("\"",please,"\"", please)
    else:
        print(2*num)
main()
