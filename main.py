#! /usr/bin/env python3
# coding: utf-8

from hangman import *



game = Hangman()
continue_game = "Yes"

player_name = game.get_username()
players_scores = game.get_score(player_name)


while continue_game != "X":

    number_try = 8

    print("Let's go {0}! Your actual score is {1}".format(player_name, players_scores[player_name]))
    print("The computer picks a word... \n")

    word_to_found = game.pick_word()
    letters_found = []
    word_found = game.get_word_state(word_to_found, letters_found)


    while word_to_found != word_found and number_try >0:

        print("Word to found : {0} (still {1} chances)".format(word_found, number_try))

        letter = game.get_letter()

        if letter in letters_found:
            print("You have already picked this letter")
        elif letter in word_to_found:
            letters_found.append(letter)
            print("Well done, your letter is included in the word to guess. \n")
        else:
            number_try -= 1
            print("What a shame! Your letter is not included in the word to found. \n")

        word_found = game.get_word_state(word_to_found, letters_found)


    if word_to_found == word_found:
        print("Well done, you have won ! You have found the word {} \n".format(word_to_found))
    else:
        print("You have lost, you don't have any try! \n")

    players_scores[player_name] += number_try

    continue_game = input("Press X to stop the game or any character to continue: ").upper()


game.save_scores(players_scores)

print("Your final score is {} points. See you !".format(players_scores[player_name]))
