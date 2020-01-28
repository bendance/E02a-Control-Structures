#!/usr/bin/env python3
import sys, random
#This imports the Python modules of system and random.

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
#This function makes the program impossible to run unless the user has Python 3.7

print('Greetings!')
#This function prints out 'Greetings!'

colors = ['red','orange','yellow','green','blue','violet','purple']
#These are all the possible colors the game can choose from

play_again = ''
#This allows the play_again variable to remain valueless

best_count = sys.maxsize            # the biggest number
#This makes it so that the system knows the lowest amount of guesses you've made

while (play_again != 'n' and play_again != 'no'):
#This makes it so that when the player doesn't want to play again, the program stops

    match_color = random.choice(colors)
    #This chooses a random color to be the correct answer
    count = 0
    #This sets the players guess count as zero
    color = ''
    #This sets colors initial variable as nothing
    while (color != match_color):
    #This initializes prompts asked toward the user
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        #This asks for the players input on the system's favorite color
        color = color.lower().strip()
        #This makes the players input standardized in a way the program can register
        count += 1
        #This adds one the count for every guess the player makes
        if (color == match_color):
            #If the color of the input matches the pregenerated color
            print('Correct!')
            #The program prints "Correct!"
        else:
            #If the player doesn't guess correctly
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
            #The system prints out how many guesses the player has made and tells them to try again
    
    print('\nYou guessed it in {} tries!'.format(count))
    #When the player succeeds, the program states how many tries the player made

    if (count < best_count):
        #The the player's count is lower than previous counts
        print('This was your best guess so far!')
        #The system prints out a statement celebrating their success
        best_count = count
        #This sets the new number of guesses that the player strives to score lower than

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()
    #This asks the player whether or not they would like to play again

print('Thanks for playing!')
#The game thanks the player for playing