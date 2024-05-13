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


def input_file():
    """
    This function gets the file name from user
    :return: file name
    :rtype: str
    """
    file_path = input(FILE_INPUT_REQUEST)
    return file_path


def input_number():
    """
    This function gets the index of the word in the file
    :return: the index in the file
    :rtype: str
    """
    index_input = input(INDEX_INPUT_REQUEST)
    return index_input


def opening_screen():
    """
    This print the opening screen just when entering (before starting) the game - the welcoming to the game
    :return: Nothing
    """
    print(HANGMAN_ASCII_ART)


def start_screen():
    """
    This prints the screen just after input file and starting the game itself
    :return: Nothing
    """
    print(START_MESSAGE)
    print(HANGMAN_PHOTOS[FIRST_STAGE_INDEX])


def user_input():
    """
    This asks the user to guess a letter and takes a letter input from the user
    :return: The string the user entered
    :rtype: str
    """
    result = input(ASK_FOR_INPUT)
    return result.lower()


def showcase_failure(num_fails):
    """
    This prints the screen according to number of guessing failures
    :param num_fails: number of times failed in guessing
    :type num_fails: int
    :return: Nothing
    """
    print(FAILURE_SIGN)
    print(HANGMAN_PHOTOS[num_fails])


def showcase_progress(user_progress):
    """
    This showcase the progress of the user (the letters he guessed correctly in the word) - prints it
    :param user_progress: the secret word made out of it's letter which the user has guessed correctly and underscores
    :type user_progress: str
    :return: None
    """
    print(user_progress)


def invalid_input_showcase(old_letters_guessed):
    """
    This prints that the guessing was an invalid character or already guessed, it prints the letter guessed
in alphabetical order separated and a sign before that
    :param old_letters_guessed: list of all the letters guessed
    :type old_letters_guessed: list
    :return: Nothing
    """
    print(INVALID_INPUT_SIGN)
    result_str = LETTER_GUESSED_SEPARATOR.join(sorted(old_letters_guessed))
    print(result_str)


def game_end_status(is_win):
    """
    This prints a message according to the status of the game when finished
    :param is_win: a flag that symbol whether the user won or not - is_win = 1 = win, else = lost
    :type is_win: int
    :return: Nothing
    """
    if is_win:
        print(VICTORY_MESSAGE)
    else:
        print(DEFEAT_MESSAGE)
