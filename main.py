# SCRABBLE
import random
import string
import pandas as pd
from pandas import read_html
import html5lib


letters = 'EAIONRTLSUDGBCMPFHVWYKJXQZ'

# Variable showing point value of letters
point_for_tiles = {'E':1, 'A':1, 'I':1, 'O':1, 'N':1, 'R':1, 'T':1, 'L':1, 'S':1, 'U':1,
                   'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,
                   'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10}

# Variable showing how many tiles available
tiles_avail = {'E':12, 'A':9, 'I':9, 'O':8, 'N':6, 'R':6, 'T':6,
               'L':4, 'S':4, 'U':4, 'D':4, 'G':3, 'B':2, 'C':2, 'M':2, 'P':2, 'F':2, 'H':2, 'V':2, 'W':2, 'Y':2,
               'K':1, 'J':1, 'X':1, 'Q':1, 'Z':1}

rack_size = 7

file_with_words = "dictionary.txt"

def words():
    infile = open(file_with_words, 'r')
    word_list = []
    for line in infile:
        word_list.append(line.strip().upper())
    print(word_list)
    print(" ", len(word_list), "words have been imported.")
    return word_list


def get_frequency_Dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) +1
        return freq


def find_word_score(word):
    """This returns the score for a word as well as the total score the player has.
    The score for the word is multiplied by the length of the word"""
    score = 0

    for letter in word:
        score += point_for_tiles[letter]
    score *= len(word)

    return score


def display_rack(rack):
    """This displays letters available on the rack that can be used"""
    for letter in rack.keys():
        for j in range(rack[letter]):
            print(letter, end=" ")
    print()


def remove_from_bag(n):
    """This returns a random rack containing letter tiles in uppercase"""

    rack = {}
    for i in range(7):
        x = letters[random.randrange(0, len(letters))]
        rack[x] = rack.get(x,0) + 1
    return rack


def calculate_rack_length(rack):
    """This returns the number of tiles currently present on the rack"""
    return sum(rack.values())


def is_word_valid(word, rack, word_list):
    """This checks if word entered by player is found in list of imported words"""
    if word not in word_list:
        return False

    word_dict = get_frequency_Dict(word)
    for i in word_dict:
        if i not in rack:
            return False
        # This checks how many times a letter is repeated in the word and compares to how many times is present on the rack and if the times is greater it will return False
        if word_dict[i] > rack[i]:
            return False
    return True



def update_rack(rack, word):
    """This provides the letter tiles remaining once some have been used to create words"""
    new_rack = dict(rack)
    for i in word:
        new_rack[i] = new_rack[i] - 1
    return new_rack


def play_rack(rack, word_list, n):
    """This allows the user to player letter tiles from the rack"""
    total_score = 0

    while(calculate_rack_length(rack)):
        display_rack(rack)
        user_input = input()

        if user_input == ".":
            break
        else:
            if not is_word_valid(user_input, rack, word_list):
                print("Invalid word")
                print()
            else:
                word_score = find_word_score(user_input)
                print("Points for the word is", word_score)
                print()
                total_score += word_score
                # This updates the rack
                rack = update_rack(rack, user_input)

    print("The game has finished")
    print("Total score at the end of the game is:")
    print(total_score)


def play_game(word_list):
    """Allows the player to enter various inputs that determine whether the game will generate a new rack, use the previous rack or exit the game"""
    while True:
        user_input = input("Enter N (play with new rack) | R (play with previous rack) | E (exit the game): ")
        if user_input == 'N':
            rack = remove_from_bag(rack_size)
            play_rack(rack, word_list, rack_size)

        elif user_input == 'R':
            play_rack(rack, word_list, rack_size)

        elif user_input == 'E':
            print("Thank you for playing Scrabble")
            return
        else:
            print("Invalid input")


if __name__ == '__main__':
    word_list = words()
    play_game(word_list)