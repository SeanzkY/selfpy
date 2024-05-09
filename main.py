import random
from gui import *
LETTER_ASK = "please enter your guess: "
WORD_ASK = "Please enter a word: "
MAX_TRIES = 6
CURR_FILE_PATH = r"C:\Users\seanr\PycharmProjects\pythonProject4\wordList.txt"


# this function checks if the user has won or not
def check_win(secret_word, old_letter_guessed):
    for x in secret_word:
        if x not in old_letter_guessed:
            return False
    return True


# this function shows the user his progress, it builds the word to reveal from past guesses and the secret word
def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    for i in range(len(secret_word)):
        letter_to_add = "_ "
        for letter in old_letters_guessed:
            if secret_word[i] == letter:
                letter_to_add = letter
        result += letter_to_add
    return result


# this checks the validation of the string - if it's one letter and if it's an alphabetical character
def valid_character(letter_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha()


# This function checks if the guess is valid - and if it's not been guesses before
def check_valid_input(letter_guessed, old_letters_guessed):
    if valid_character(letter_guessed) and letter_guessed not in old_letters_guessed:
        return True
    return False


# add to guesses the current guess if it's valid and not in old guesses and return true else return false
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print(letter_guessed.upper())
    print(old_letters_guessed)
    return False


# chooses a random word from a file
def choose_word(file_path, index):
    with open(file_path, "rt") as fileRead:
        fileContent = fileRead.read()
        wordList = fileContent.split(" ")
        return wordList[index % len(wordList)]


def play():
    secret_word = input(WORD_ASK)
    guess = ""
    while True:
        guess = input(LETTER_ASK).lower()
        if check_valid_input(guess):
            pass


def main():

    index = random.randint(0, 100)
    secret_word = choose_word(CURR_FILE_PATH, index)
    old_guesses = list()
    num_of_tries = 0
    opening_screen()
    old_user_progress = show_hidden_word(secret_word, old_guesses)
    while num_of_tries < MAX_TRIES:
        curr_letter = user_input()
        if try_update_letter_guessed(curr_letter, old_guesses):
            num_of_tries += 1
            new_user_progress = show_hidden_word(secret_word, old_guesses)
            # this means that he guessed correctly
            if new_user_progress != old_user_progress:
                pass







if __name__ == '__main__':
    main()
