from TUI import invalid_input_showcase

SEPARATOR = " "
EMPTY_LETTER = "_"


def check_win(secret_word, old_letter_guessed):
    """
    This function checks if the user has won or not
    :param secret_word: the secret word chosen
    :param old_letter_guessed: all the letters the user already guessed
    :type secret_word: str
    :type old_letter_guessed: list
    :return: whether the user won = True, or not = False
    :rtype: bool
    """
    # Builds a list of all letters in secret word that the user didn't guess yet, returns true if the
    # len of this list is 0 (meaning he guessed every letter)
    return len([x for x in secret_word if x not in old_letter_guessed]) == 0


def show_hidden_word(secret_word, old_letters_guessed):
    """
    this function shows the user his progress,meaning it shows the letters in the secret word that the user has guessed
     correctly and underscores for the other letters, all of it separated
    :param secret_word: the secret word chosen
    :param old_letters_guessed: all the letters the user already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: the word progress - secret word with underscores when needed
    :rtype: str
    """
    # replace the letters the user didn't guess with replaced with an underscore
    user_word_progress_list = [x if x in old_letters_guessed else EMPTY_LETTER for x in secret_word]
    # this just joins the list to make it a word separated with spaces
    return SEPARATOR.join(user_word_progress_list)


def valid_character(letter_guessed):
    """
    This checks the validation of the string - if it's one letter and if it's an alphabetical character
    :param letter_guessed: the input of the user which is supposed to be an alphabetical character
    :type letter_guessed: str
    :return: valid = True invalid = False
    :rtype: bool
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha()


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks if the guess is valid - and if it's not been guesses before, uses function valid_character
    :param letter_guessed: current letter guess
    :param old_letters_guessed: old guesses
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: true if it's valid and false if not
    :rtype: bool
    """
    return valid_character(letter_guessed) and letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Add to guesses the current guess if it's valid and not in old guesses and return true else return false
    use the check_valid_input function, if it's not valid also show the use the screen suitable

    :param letter_guessed: current letter guess
    :param old_letters_guessed: old guesses
     :type letter_guessed: str
    :type old_letters_guessed: list
    :return:  true if it's valid and false if not
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    invalid_input_showcase(old_letters_guessed)
    return False


def choose_word_from_file(file_path, index):
    """
    chooses a word in a certain index from the file, if index is bigger than the file size pick the index modulo file
    size
    :param file_path: the path of the file
    :param index: the index of the word to take
    :type file_path: str
    :type index: int
    :return: word picked or None if error
    :rtype: str
    """
    try:
        with open(file_path, "rt") as file_read:
            file_content = file_read.read()
            word_list = file_content.split()
            # in case of an empty file error
            if len(word_list) == 0:
                print("error! entered an empty file!")
                return None
            return word_list[index % len(word_list)]
    except OSError as e:
        print("an error has occurred: {}".format(e))
        return None
