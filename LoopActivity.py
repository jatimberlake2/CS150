def main():
    word = "poker"
    word0 = word
    print("The word is", len(word), "letters long.")
    while word != "":
        guess = input("Guess a letter.")
        if guess in word:
            word = word.replace(guess,"")
            print("You guessed a correct letter!")
        else:
            print("Try harder.")
    print("You got the whole word! The word was", word0)

main()
