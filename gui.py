HANGMAN_ASCII_ART = """ 
Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
6"""

STAGE_0 = """ x-------x """

STAGE_1 = """ 
    x-------x
    |
    |
    |
    |
    |"""

STAGE_2 = """   
x-------x
|       |
|       0
|
|
|"""

STAGE_3 = """
x-------x
|       |
|       0
|       |
|
|"""

STAGE_4 = """
x-------x
|       |
|       0
|      /|\\
|
|"""

STAGE_5 = """
x-------x
|       |
|       0
|      /|\
|      /
|"""

STAGE_6 = """
x-------x
|       |
|       0
|      /|\
|      / \
|"""

HANGMAN_PHOTOS = {0: STAGE_0, 1: STAGE_1, 2: STAGE_2, 3: STAGE_3, 4: STAGE_4, 5: STAGE_5, 6: STAGE_6}

ASK_FOR_INPUT = "Please guess a letter:"

FAILURE_SIGN = ":("

FILE_INPUT_REQUEST = "Enter file path: "

INDEX_INPUT_REQUEST = "Enter index: "

VICTORY_MESSAGE = "You Won!"

DEFEAT_MESSAGE = "You Lost!"


def input_file():
    file_path = input(FILE_INPUT_REQUEST)
    return file_path


def input_number():
    index_input = input(INDEX_INPUT_REQUEST)
    return index_input


def opening_screen():
    print(HANGMAN_ASCII_ART)


def user_input():
    result = input(ASK_FOR_INPUT)
    return result.lower()


def showcase_failure(numTries):
    print(FAILURE_SIGN)
    print(HANGMAN_PHOTOS[numTries])


def showcase_progress(user_progress):
    print(user_progress)


def game_end_status(is_win):
    if is_win:
        print(VICTORY_MESSAGE)
    else:
        print(DEFEAT_MESSAGE)
