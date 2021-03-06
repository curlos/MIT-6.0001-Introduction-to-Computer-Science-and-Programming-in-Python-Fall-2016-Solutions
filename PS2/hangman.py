# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from colorama import Fore
from colorama import Style

WORDLIST_FILENAME = "words.txt"


def load_words():
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_letters_hash = {}
    letters_guessed_hash = {}

    for letter in secret_word:
        if letter not in secret_word_letters_hash:
            secret_word_letters_hash[letter] = 0

        secret_word_letters_hash[letter] += 1

    for letter in letters_guessed:
        if letter not in letters_guessed_hash:
            letters_guessed_hash[letter] = 0

        letters_guessed_hash[letter] += 1

    for letter, count in secret_word_letters_hash.items():
        if letter not in letters_guessed_hash:
            return False

        if count != letters_guessed_hash[letter]:
            return False

    return True


# print(is_word_guessed('apple', ['e', 'i', 'k', 'p', 'r', 's', 'p', 'a', 'l']))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed_hash = {}
    guessed_word_arr = []

    for letter in letters_guessed:
        if letter not in letters_guessed_hash:
            letters_guessed_hash[letter] = 0

        letters_guessed_hash[letter] += 1

    for letter in secret_word:
        if letter in letters_guessed_hash:
            count = letters_guessed_hash[letter]

            if count > 0:
                guessed_word_arr.append(letter)
        else:
            guessed_word_arr.append('_ ')

    guessed_word = ''.join(guessed_word_arr)
    return guessed_word


# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters_arr = []
    letters_guessed_hash = {letter: 1 for letter in letters_guessed}

    for letter in string.ascii_lowercase:
        if letter not in letters_guessed_hash:
            available_letters_arr.append(letter)

    available_letters = ''.join(available_letters_arr)
    return available_letters


# print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))


def hangman(secret_word='tact'):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    word_guessed = False
    letters_guessed = []

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warnings} left.')

    while guesses > 0 and not word_guessed:
        print(secret_word, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses * len(set(secret_word))
            print('Congratulations, you won!')
            print(f'Your total score for this game is: {total_score}')
            return

        print(f'{Fore.GREEN}-------------{Style.RESET_ALL}')
        print(f'You have {guesses} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        guessed_letter = input('Please guess a letter: ')

        if guessed_letter not in string.ascii_lowercase:
            warnings -= 1
            if warnings == 1:
                print(
                    f"Oops! That is not a valid letter. You have {warnings} warning left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                print(
                    f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")

        elif guessed_letter in letters_guessed:
            if warnings > 0:
                warnings -= 1
                if warnings == 1:
                    print(
                        f"Oops you've already guessed that letter. You have {warnings} warning left: {get_guessed_word(secret_word, letters_guessed)}")
                else:
                    print(
                        f"Oops you've already guessed that letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                print(
                    f"Oops you've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                guesses -= 1

        elif guessed_letter not in letters_guessed:

            if guessed_letter not in secret_word:
                letters_guessed.append(guessed_letter)
                guesses -= 1
                print(
                    f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                for letter in secret_word:
                    if letter == guessed_letter:
                        letters_guessed.append(guessed_letter)
                print(
                    f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_no_spaces = my_word.strip().replace(' ', '')

    if len(my_word_no_spaces) == len(other_word):
        for i in range(len(my_word_no_spaces)):
            letter1 = my_word_no_spaces[i]
            letter2 = other_word[i]

            if letter1 != letter2:
                if letter1 == '_' and letter2 in my_word_no_spaces:
                    return False
                elif letter1 != '_':
                    return False
    else:
        return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    words = load_words()
    possible_matches = []

    for word in words:
        if match_with_gaps(my_word, word):
            print(word)
            possible_matches.append(word)

    return ' '.join(possible_matches)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    word_guessed = False
    letters_guessed = []

    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warnings} left.')

    while guesses > 0 and not word_guessed:
        print(secret_word, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses * len(set(secret_word))
            print('Congratulations, you won!')
            print(f'Your total score for this game is: {total_score}')
            return

        print(f'{Fore.GREEN}-------------{Style.RESET_ALL}')
        print(f'You have {guesses} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')
        guessed_letter = input('Please guess a letter: ')

        if guessed_letter == '*':
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print(
                f"Possible word matches are: {show_possible_matches(guessed_word)}")
        elif guessed_letter not in string.ascii_lowercase:
            warnings -= 1
            if warnings == 1:
                print(
                    f"Oops! That is not a valid letter. You have {warnings} warning left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                print(
                    f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")

        elif guessed_letter in letters_guessed:
            if warnings > 0:
                warnings -= 1
                if warnings == 1:
                    print(
                        f"Oops you've already guessed that letter. You have {warnings} warning left: {get_guessed_word(secret_word, letters_guessed)}")
                else:
                    print(
                        f"Oops you've already guessed that letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                print(
                    f"Oops you've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")
                guesses -= 1

        elif guessed_letter not in letters_guessed:

            if guessed_letter not in secret_word:
                letters_guessed.append(guessed_letter)
                guesses -= 1
                print(
                    f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            else:
                for letter in secret_word:
                    if letter == guessed_letter:
                        letters_guessed.append(guessed_letter)
                print(
                    f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
