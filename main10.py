#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #prints when the game first starts
colors = ['red','orange','yellow','green','blue','violet','purple'] #a list of options
play_again = '' #will start up the game if the user simply presses enter
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #loops the game unless player enters "no"
    match_color = random.choice(colors) #will randomize the correct answer
    count = 0  #will keep track of how many tries it takes
    color = '' #will allow input of any word, even words not in the "colors" dictionary
    while (color != match_color): #will loop until the correct color is inputted
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #will let any spellings of the colors be registered as possible answers
        count += 1 #will add one point for each incorrect guess
        if (color == match_color):
            print('Correct!')       #will print if the color typed in matches the correct color choice
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #will print otherwise
    print('\nYou guessed it in {0} tries!'.format(count))       #lets the player know how many guesses they have done.
    if (count < best_count):
        print('This was your best guess so far!')
        best_count = count          #this section will print if this attempt was better than the last attempt.
    play_again = input("\nWould you like to play again? ").lower().strip() #will print once the player reaches the correct guess
print('Thanks for playing!') #will print if the player types "no" to end the game.