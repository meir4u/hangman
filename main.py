import string
import os
import copy
import random
import textwrap

def set_word(w="meir for you"):
    """
    :param w: (str) have default value
    :return: its striped value converted to list
    """
    return list(w.strip())


def count_total_lines_in_file(file_name):
    line_count = 0
    file = open(file_name, "r");
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    return line_count


def get_sentence_from_file(file_name="sentences.txt"):
    """
    :param file_name: a filename where we have sentences
    :return: return a random sentence from file
    """
    f = open(file_name, "r");
    total_lines = count_total_lines_in_file(file_name)
    line_to_output = []
    line_to_output.append(random.randint(0, total_lines-1))
    print(line_to_output, total_lines)
    for position, line in enumerate(f):
        if position in line_to_output:
            return line


def change_word_to_under_line(s):
    """
    :param s: sentence converted to list
    :return: return the sentence where A-z words underlined
    """
    alphabet_string = string.ascii_letters
    str_underline = copy.copy(s)
    for i, v in enumerate(s):
        if v in alphabet_string:
            str_underline[i] = "_"
    return str_underline


def is_guessed(underline, letter):
    """
    :param underline: list where all letter that not guessed yet are underline
    :param letter: char of guessed letter by user
    :return: true or false, true if the letter found in the list
    """
    return letter in underline


def is_one_letter(letter):
    """
    :param letter: user input
    :return: return true if letter contain only 1 char
    """
    return len(letter) > 1


def is_alpha(letter):
    return letter not in list(string.ascii_letters)


def test_error(underline, guess):
    if is_one_letter(guess):
        print("You can enter just 1 letter in i guess")
        return True
    elif is_guessed(underline, guess):
        print("This letter already guessed choose another ")
        return True
    elif is_alpha(guess):
        text = "You must enter ascii English letters! for example: " + string.ascii_letters
        print(textwrap.fill(text, 50))
        return True
    else:
        return False


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def is_letter_in_sentence(word, underline, letter):
    wrong = True
    for i, v in enumerate(word):
        if v.lower() == letter.lower() and underline[i] == "_":
            wrong = False
            underline[i] = v

    return wrong, underline


total_wrong_attempts = 5

wrong_letters = []
print("game started")
word = set_word(get_sentence_from_file())
word_underline = change_word_to_under_line(word)
print("word to find: ", "".join(word_underline))

while total_wrong_attempts >= 0 and ("_" in word_underline):
    attempt = input("enter your guess letter: ")

    if test_error(word, word_underline, attempt):
        continue

    test, word_underline = is_letter_in_sentence(word_underline, attempt)
    clear_console()
    if test:
        total_wrong_attempts -= 1
        wrong_letters.append(attempt)
        print("You guess wrong :", attempt, "not in word, you have ", total_wrong_attempts, "more attempts")
    else:
        print("Correct guess: ", attempt)
        print("[{0}]".format(" ".join(str(i) for i in word_underline)))
        # print('[%s]' % ', '.join(map(str, word_underline)))
    print("Total wrong guesses:", len(wrong_letters))
    print("Wrong guesses letters: ", wrong_letters)
if total_wrong_attempts < 0:
    print("\n"*5, "Sorry you don't have more attempts, the statement is: ", word)
else:
    print("\n"*5, "You Won! the statement is ", "".join(word))

