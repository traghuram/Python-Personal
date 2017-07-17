# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    counter = 0
    for char in secretWord:
        if char in lettersGuessed:
            counter += 1
    
    if counter == len(secretWord):
        return True
    return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    
    for char in secretWord:
        if char in lettersGuessed:
            guessedWord = guessedWord + char
        else:
            guessedWord = guessedWord + "_ "
    
    return guessedWord
        



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            availableLetters = availableLetters + char
    
    return availableLetters
            
            


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print("The secret word has " + str(len(secretWord)) + " letters. Good luck!")
    
    lettersGuessed = []
    numGuesses = 8
    mistakesMade = 0
        
    while numGuesses - mistakesMade > 0:
        print ("You have " + str(numGuesses - mistakesMade) + " guesses left")
        print("Here are the remaining letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Guess a letter: ")
        
        lettersGuessed.append(guess)
        
        if guess in secretWord:
            print (guess + " is in the secret word!")
        
        else:
            print("Nice try, but no dice.")
            mistakesMade += 1
        
        if isWordGuessed(secretWord, lettersGuessed):
            print ("YOU GOT IT - " + secretWord)
            print('NICE BOIIIIII')
            break
        
        else:
            print ("So close yet so far... " + getGuessedWord(secretWord, lettersGuessed))
            print ("-----------------------")
        
        
    if mistakesMade >= numGuesses:
        print("Sorry you suck - the word was " + secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
