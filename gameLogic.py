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
def choose_word_from_file(file_path, index):
    try:
        with open(file_path, "rt") as fileRead:
            fileContent = fileRead.read()
            wordList = fileContent.split(" ")
            return wordList[index % len(wordList)]
    except OSError as e:
        print("an error has occurred: {}".format(e))
