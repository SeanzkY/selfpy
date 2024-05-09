from TUI import invalid_input_showcase

SEPARATOR = " "
EMPTY_LETTER = "_"


# this function checks if the user has won or not
def check_win(secret_word, old_letter_guessed):
    # this builds a list made of all letters in secret word that the user didn't guess yet and returns true if the
    # len of this list is 0 (guessed every letter)
    return len([x for x in secret_word if x not in old_letter_guessed]) == 0


# this function shows the user his progress, it builds the word to reveal from past guesses and the secret word
def show_hidden_word(secret_word, old_letters_guessed):
    # this list consists of all the letter in secret_words that the user guessed correctly in the correct order
    # and if he didn't guess one letter it's replaced with an underscore
    user_word_progress_list = [x if x in old_letters_guessed else EMPTY_LETTER for x in secret_word]
    # this just joins the list to make it a word separated with spaces
    return SEPARATOR.join(user_word_progress_list)


# this checks the validation of the string - if it's one letter and if it's an alphabetical character
def valid_character(letter_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha()


# This function checks if the guess is valid - and if it's not been guesses before
def check_valid_input(letter_guessed, old_letters_guessed):
    return valid_character(letter_guessed) and letter_guessed not in old_letters_guessed


# add to guesses the current guess if it's valid and not in old guesses and return true else return false
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    invalid_input_showcase(old_letters_guessed)
    return False


# chooses a random word from a file
def choose_word_from_file(file_path, index):
    try:
        with open(file_path, "rt") as fileRead:
            fileContent = fileRead.read()
            wordList = fileContent.split()
            # in case of an empty file error
            if len(wordList) == 0:
                print("error! entered an empty file!")
                return None
            return wordList[index % len(wordList)]
    except OSError as e:
        print("an error has occurred: {}".format(e))
        return None
