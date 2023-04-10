"""Reto #13 - python.

/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

"""

import random

# Global game configuration
playable_words = ["computer", "internet", "laptop"]
LIVES = 6
HIDDEN_PERCENTAGE = 60
HIDDING_CHARACTER = "_"


def hide_letters(word, max_percentage):
    """Hide (replace by "_") a random number of letters from a word.

    Args:
        word (str): word to be guessed
        max_percentage (int): maximun percentage of characters that can be hidden

    Returns:
        list[str]: new word with hidden characters, as a list of characters (strings)
    """
    hidden_word = list(word)
    word_length = len(word)
    max_hidden = int(word_length * max_percentage / 100)
    hidden_positions = random.sample(range(word_length - 1), max_hidden)

    for index in range(word_length - 1):
        if index in hidden_positions:
            hidden_word[index] = HIDDING_CHARACTER

    return hidden_word


def get_text_input(length):
    """Get user input from standard input.

    Valid inputs are:
     - one single character / letter
     - a word with length equal the 'length' parameter


    Args:
        length (int): length of the word in play

    Returns:
        str: valid string input written by the user
    """
    while True:
        text_input = input("Enter your guess (1 letter or full word): ")
        if len(text_input) in [1, length]:
            return text_input
        print("Invalid input length. Try again.")


def hangman(word, lives=LIVES, hidden_percentage=HIDDEN_PERCENTAGE):
    """Execute the main workflow of the Hangman game.

    Args:
        word (str): word to be guessed
        lives (int, optional): maximun number of attempts to guess the word. Defaults to LIVES.
        hidden_percentage (int, optional): maximun percentage of characters that can be hidden. Defaults to HIDDEN_PERCENTAGE.
    """
    word_length = len(word)
    hidden_word = hide_letters(word, hidden_percentage)
    letter_found = False

    while lives > 0:
        print(f"The missing word is {hidden_word}.")
        print(f"You have {lives} lives remaining.")
        text_input = get_text_input(word_length)

        if len(text_input) == 1:
            if text_input in word:
                for index, letter in enumerate(word):
                    if (
                        word[index] == text_input
                        and hidden_word[index] == HIDDING_CHARACTER
                    ):  # unhide all letter instances
                        hidden_word[index] = word[index]
                        letter_found = True
            if letter_found:  # check if we have uncovered all the hidden letters
                if HIDDING_CHARACTER in hidden_word:  # we still have hidden letters
                    print("Great. You have discovered a new letter.")
                else:  # Word fully discovered
                    print(
                        "C O N G R A T U L A T I O N S !  You have found the missing word."
                    )
                    return
            else:
                print("Oh no! Letter not found in word or already discovered.")
                lives -= 1
        elif text_input == word:
            print("C O N G R A T U L A T I O N S !  You have found the missing word.")
            return
        else:
            print("Oh no! Wrong guess .That's not the missin word.")
            lives -= 1

    print("O H  N O ! You have run out of lives.")
    print(f"The missing word was {word}")


if __name__ == "__main__":
    hangman(random.choice(playable_words))
