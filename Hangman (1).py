# I imported random because the program is going to have to choose a word randomly for the mystery word
import random
# These are mystery words that the program will choose from
words = [
        "world",
        "globe",
        "states",
        "cabinet",
        "door",
        "computer"

        ]
def main():
    word_list = []
    guessed_list = []

    guessed_characters = []
    tries = 0
    lives = 5
# This line takes one of the mystery words at random and picks one from 0 to the amount of words there are minus one
    word = words[random.randint(0, len(words) - 1)]
# The first line take the word and put it in the wordlist, the second line is a really easy way to make the outlines of the word
    for char in word:
        word_list.append(char)
        guessed_list.append("_")
# I am using a while loop because I want the guessed letters to be updated all the time
#This takes the guessed list and prints the letters you've already guessed correctly
    while word_list != guessed_list and lives > 0:
        for char in guessed_list:
            #"end=" "" means instead of going to the next line, it makes a space on the same line
            print(char, end=" ")
        print("Lives:", lives)
        # "\n" means to go to a new line
        guess = input("Guess a letter:\n")[0].lower()
# This takes your letter and because it was already guessed, it says that you already guessed the letter
        if guess in guessed_characters:
            print("You already guessed that letter!")
# This takes your guessed letter, and because it is in the wordlist, the program fills in the letter you guessed into the word
        elif guess in word_list:
            for i in range(len(word_list)):
                if word_list[i] == guess:
                    guessed_list[i] = guess
# Every time you guess a letter wrong your lives go down
        else:
            lives -= 1
            print("Letter not in word!")
#and your tries go up
        tries += 1
        print()
# Once the lives reach zero, or once they figure out the word, the game will end
    if lives <= 0:
        print("Nice try!")
        print ("The word was", word)
        again = input("Try again?:\n").lower()
        if again == "yes":
            main()
    else:
        print ("Good job!")
        again = input("Try again?:\n").lower()
        if again == "yes":
            main()
        if again == "no":
            print ("Ok then see ya!")

main()
