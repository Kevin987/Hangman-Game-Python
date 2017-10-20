#Hangman Program
#Key Functions
# Open file and read into a list
# Select a random word from the list
# Create an equal length word with dashes
# Print dashes and prompt for input
# Get input
# Check if letter exists in word (and position)
# If letter exists, insert it in the dashes
# Loop to find and substitute further occurances
# Draw hanging man
# .....

#Imports
import random

TRUE = 1
FALSE = 0

#Open file and read into a list
def getlistfromfile():
    try:
        hangfile = open('HangmanList.txt')
        hanglist = hangfile.read().splitlines()
        hangfile.close
        return(hanglist)
    except FileError:
        print("Cannot open HangmanList.txt")
        exit()

# Create an equal length word with dashes
def createdashes():
    wordlen = len(hang_word)
    dashes = ''
    for x in range(0,wordlen):
        dashes = dashes +'-'
    return (dashes)



hang_list = getlistfromfile()
print('\n\n')
print('HANGMAN GAME\n************\n')
print('Use lower case letters only\n')
newgame = 'y'
while newgame == 'y':
    #Select a random word from the list
    hang_word = random.choice(hang_list)
    dash_word = createdashes()
    tries_left = 12

    #"Search for letters" Loop
    incomplete = TRUE
    print ('\nReady to go:')
    while incomplete == TRUE:
    
        print
        print (dash_word) #Looks like "--a-e--"
        print
    
        # Get input
        guess = raw_input('Guess a letter and hit enter>')
        if (guess < 'a'):
            #Next line to prevent control characters going further
            guess = 'X'
        # Check if letter exists in word (and position)
        findpos = hang_word.find(guess)
        if ((findpos < 0) or (len(guess) != 1)): # only one letter and not found
            tries_left = tries_left - 1
            print
            print("Letter not found. Tries left: %d" % tries_left)
            
        else:
            #Loop to find and substitute further occurances
            while (findpos >= 0):    
                dashtemp = dash_word[0:findpos]
                dashtemp = dashtemp + guess
                dashtemp = dashtemp + dash_word[findpos+1:]
                dash_word = dashtemp
                findpos = hang_word.find(guess,findpos+1)
    
        if tries_left == 0:
            print
            print("Failed\n")
            print('Word is: %s \n' % hang_word)
            incomplete = FALSE

        if dash_word.find('-') < 0:
            print
            print(dash_word)
            print
            print('Congratulations\n')
            incomplete = FALSE

    newgame = raw_input('To play again type "y" and hit enter>')
     






    




