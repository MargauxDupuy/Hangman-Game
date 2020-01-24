#! /usr/bin/env python3
# coding: utf-8


from random import choice
import json
import re
import os


class Hangman:
    """Hangman consists of guessing a word by revealing its letters."""

    def __init__(self):
        self._list_words = [
            "avenue",
            "buffalo",
            "banana",
            "banjo",
            "cycle",
            "faraway",
            "faraway",
            "garage",
            "icebox",
            "jackpot",
            "kiwi",
            "list",
            "mountain",
            "radio",
            "sockets",
            "taxi",
            "vampire",
            "vodka",
        ]
        self.file_name = "scores.json"



    def get_score(self, player_name):
        """This function gets the scores and return an object {} with the score associated to the player."""

        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self._scores = json.load(file)
                if not player_name in self._scores:
                    self._scores[player_name] = 0
        else:
            self._scores = {}
            self._scores[player_name] = 0

        return self._scores



    def save_scores(self, players_scores):
        """This function save the player's score in a file."""

        with open(self.file_name, "w") as file:
            json.dump(players_scores, file)



    def get_username(self):
        """This function gets the player's username and checks if it is composed at least 4 characters."""

        self._player_name = input("What is your username ? ").capitalize()

        if len(self._player_name) < 4:
            print("This name is invalid, please enter at least 4 characters")
            self.get_username()
        else:
            return self._player_name



    def pick_word(self):
        """The computer choose one word to guess"""

        return choice(self._list_words)



    def get_letter(self):
        """This function asks to the player to choose a letter and checks if that he chooses one letter."""

        self._letter_picked = input("What letter do you choose ? ").lower()

        if len(self._letter_picked) != 1:
            print("Please, enter only one letter.")
            self.get_letter()
        if re.search('[a-zA-Z]', self._letter_picked) == None :
            print("Please, enter a letter.")
            self.get_letter()

        return self._letter_picked



    def get_word_state(self, word_to_found, letters_found):
        """This function return the word's state with * for the not found letter.
         The letters discovered are visible."""

        self._word_state = ""

        for letter in word_to_found:
            if letter in letters_found:
                self._word_state += letter
            else:
                self._word_state += "*"

        return self._word_state



