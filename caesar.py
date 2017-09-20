""" Runs the Caesar Cipher """


def alphabet_position(character):
    """ Determines the numeric position of the character """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)


def rotate_string_13(text):
    """ Rotates the string by 13 """

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]

    return rotated


def rotate_character(char, rot):
    """ Rotates the character by a specified number """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_idx].upper()
    return alphabet[rotated_idx]


def rotate_string(text, rot):
    """ Rotates the string by a specified number """

    rotated = ''

    for char in text:
        if char.isalpha():
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated
