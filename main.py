import os
from TUI import *
from gameLogic import *

MAX_TRIES = 6

# path = C:\Users\seanr\PycharmProjects\pythonProject4\wordList.txt


# choose the secret word, first input and validate the input for the file path and index then return the word chosen
# from file
def choose_secret_word():
    file_path = input_file()
    while not os.path.isfile(file_path):
        file_path = input_file()
    index = input_number()
    while not index.isnumeric():
        index = input_number()
    return choose_word_from_file(file_path, int(index))


# calls the necessary functions to choose the word, and show the user the opening screen, returns the secret word chosen
def start_game():
    opening_screen()
    secret_word = choose_secret_word()
    if secret_word is not None:
        start_screen()
        return secret_word.lower()
    return secret_word


# This function is the main controller, handles the game from start to finish
def handleGame():
    secret_word = start_game()
    if secret_word is None:
        return
    old_letters_guessed = list()
    num_of_tries = 0
    old_user_progress = show_hidden_word(secret_word, old_letters_guessed)
    showcase_progress(old_user_progress)
    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        curr_letter = user_input()
        if try_update_letter_guessed(curr_letter, old_letters_guessed):
            new_user_progress = show_hidden_word(secret_word, old_letters_guessed)
            # this means that he guessed incorrectly
            if new_user_progress == old_user_progress:
                num_of_tries += 1
                showcase_failure(num_of_tries)
            showcase_progress(new_user_progress)
            old_user_progress = new_user_progress
    # this sends a boolean that tell the function if the game is won or not - true = won -false = lost hence the use
    # of "NOT"
    game_end_status(not num_of_tries == MAX_TRIES)


def main():
    handleGame()


if __name__ == '__main__':
    main()
