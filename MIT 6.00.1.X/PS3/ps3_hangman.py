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
    # FILL IN YOUR CODE HERE...
    secretWordFreq = {}
    lettersGuessedFreq = {}

    for letter in secretWord:
        if letter not in secretWordFreq:
            secretWordFreq[letter] = 0
        secretWordFreq[letter] += 1

    for letter in lettersGuessed:
        if letter not in lettersGuessedFreq:
            lettersGuessedFreq[letter] = 0
        lettersGuessedFreq[letter] += 1

    for letter, freq in secretWordFreq.items():
        if letter not in lettersGuessedFreq:
            return False
        if freq > lettersGuessedFreq[letter]:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessedFreq = {}
    guessedWordArr = []

    for letter in lettersGuessed:
        if letter not in lettersGuessedFreq:
            lettersGuessedFreq[letter] = 0
        lettersGuessedFreq[letter] += 1

    for letter in secretWord:
        if letter in lettersGuessedFreq and lettersGuessedFreq[letter] > 0:
            guessedWordArr.append(letter)
        else:
            guessedWordArr.append('_ ')

    return ''.join(guessedWordArr)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    all_letters = string.ascii_lowercase
    available_letters_arr = []

    for letter in all_letters:
        if letter not in lettersGuessed:
            available_letters_arr.append(letter)

    return ''.join(available_letters_arr)


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
    secretWord = secretWord
    lettersGuessed = []
    guessesLeft = 8

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ',
          len(secretWord), ' letters long.')

    while True:
        if guessesLeft == 0:
            print('-------------')
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break

        if isWordGuessed(secretWord, lettersGuessed):
            print('-------------')
            print('Congratulations, you won!')
            break

        availableLetters = getAvailableLetters(lettersGuessed)

        print('-------------')
        print('You have', guessesLeft, 'guesses left.')
        print('Available letters:', availableLetters)
        guessedLetter = input('Please guess a letter: ')
        guessedLetter = guessedLetter.lower()
        guessedWord = getGuessedWord(secretWord, lettersGuessed)

        if guessedLetter in availableLetters and guessedLetter in secretWord:
            for letter in secretWord:
                if letter == guessedLetter:
                    lettersGuessed.append(letter)

            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print('Good guess:', guessedWord)
        elif guessedLetter in lettersGuessed:
            print("Oops! You've already guessed that letter:", guessedWord)
        else:
            print("Oops! That letter is not in my word:", guessedWord)
            lettersGuessed.append(guessedLetter)
            guessesLeft -= 1


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
