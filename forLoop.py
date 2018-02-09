def find(target, items):
    for i in range(len(items)):
        if items[i] == target:
            return True
    return False

def findIndex(target, items):
    for i in range(len(items)):
        if items[i] == target:
            return i

def main():
  # word = "poker"
    word = ["p","o","k","e","r"]
    word0 = word
    guessedWord = [None]*len(word)
    correct = 0
    print("The word is", len(word), "letters long.")
    for i in range(7):
        guess = input("Guess a letter.")
    #   if guess in word:
        if find(guess, word):
        #display how many correct letters
            correct += 1     
        #   word = word.replace(guess,"")
            index = findIndex(guess, word)
            guessedWord[index] = guess 
            word[index] = None
            print("You guessed a correct letter! You have guessed", correct,"correct letter(s).")
    
     #  if word == "":
        if word == ([None]*len(word)):
            print("You got the whole word! The word was", word0)
            return
    print("Try harder.")


main()
