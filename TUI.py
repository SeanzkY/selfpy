HANGMAN_ASCII_ART = r""" 
Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
6"""

STAGE_0 = r""" x-------x """

STAGE_1 = r""" 
    x-------x
    |
    |
    |
    |
    |
    """

STAGE_2 = r"""   
x-------x
|       |
|       0
|
|
|
"""

STAGE_3 = r"""
x-------x
|       |
|       0
|       |
|
|
"""

STAGE_4 = r"""
x-------x
|       |
|       0
|      /|\
|
|
"""

STAGE_5 = r"""
x-------x
|       |
|       0
|      /|\
|      /
|
"""

STAGE_6 = r"""
x-------x
|       |
|       0
|      /|\
|      / \
|
"""

HANGMAN_PHOTOS = {0: STAGE_0, 1: STAGE_1, 2: STAGE_2, 3: STAGE_3, 4: STAGE_4, 5: STAGE_5, 6: STAGE_6}

ASK_FOR_INPUT = "Guess a letter: "

FAILURE_SIGN = ":("

FILE_INPUT_REQUEST = "Enter file path: "

INDEX_INPUT_REQUEST = "Enter index: "

VICTORY_MESSAGE = "WIN"

DEFEAT_MESSAGE = "LOSE"

INVALID_INPUT_SIGN = "X"

START_MESSAGE = "let's start!"

FIRST_STAGE_INDEX = 0

LETTER_GUESSED_SEPARATOR = " -> "


# this gets the file name
def input_file():
    file_path = input(FILE_INPUT_REQUEST)
    return file_path


# this gets the index of the word in the file
def input_number():
    index_input = input(INDEX_INPUT_REQUEST)
    return index_input


# this print the opening screen just when entering the game
def opening_screen():
    print(HANGMAN_ASCII_ART)


# this prints the screen just after input file and starting the game itself
def start_screen():
    print(START_MESSAGE)
    print(HANGMAN_PHOTOS[FIRST_STAGE_INDEX])


# this asks to guess a letter and takes a letter input from the user
def user_input():
    result = input(ASK_FOR_INPUT)
    return result.lower()


# this prints the screen if the user has failed in guessing a letter
def showcase_failure(numTries):
    print(FAILURE_SIGN)
    print(HANGMAN_PHOTOS[numTries])


# this showcase the progress of the user (the letters he guessed correctly in the word)
def showcase_progress(user_progress):
    print(user_progress)


# this prints that the guessing was an invalid character or already guessed
def invalid_input_showcase(old_letters_guessed):
    print(INVALID_INPUT_SIGN)
    result_str = LETTER_GUESSED_SEPARATOR.join(sorted(old_letters_guessed))
    print(result_str)


# this prints the status of the game when finished
def game_end_status(is_win):
    if is_win:
        print(VICTORY_MESSAGE)
    else:
        print(DEFEAT_MESSAGE)
