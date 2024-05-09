import os
from gui import *
from gameLogic import *

MAX_TRIES = 6


def choose_secret_word():
    file_path = input_file()
    while not os.path.isfile(file_path):
        file_path = input_file()
    index = input_number()
    while not index.isalnum():
        index = input_number()
    return choose_word_from_file(file_path, index)


def start_game():
    opening_screen()
    return choose_secret_word()


def handleGame():
    secret_word = choose_secret_word()
    old_letters_guessed = list()
    num_of_tries = 0
    opening_screen()
    old_user_progress = show_hidden_word(secret_word, old_letters_guessed)
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
