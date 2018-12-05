#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock', 'paper', 'scissors']


class Player:

    import random

    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, their_move):
        pass



def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def move(self):
        human_move = input("What's your move? xx ")
        while human_move not in moves:
            human_move = input("What's your move? ")
        return human_move


class RandomPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.index = 0

    def learn(self, their_move):
        self.their_move = their_move

    def move(self):
        if self.index == 0:
            self.index + 1
            return random.choice(moves)
        else:
            return self.their_move


class CyclerPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.index = -1

    def move(self):
        self.index += 1
        if self.index % 3 == 0 :
            return "rock"

        elif self.index % 3 == 1:
            return "paper"

        else:
            return "scissors"


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p2.learn(move1)
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            return "No winner.\n"
        if beats(move1, move2):
            print("Player 1 WINS")
            self.p1.score += 1
        else:
            print("Player 2 WIN")
            self.p2.score += 1
        print(f"plyer 1 score =  {self.p1.score}")
        print(f"plyer 2 score =  {self.p2.score}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

if __name__ == '__main__':
    while True:
        choice = input("************** "
                       "Welcome to AHDAB Rock-Paper-Scissors based Games "
                       "******************"
                       "\n************************"
                       "***************************"
                       "****************************"
                       "\n*                               "
                       "OPTIONS "
                       "                                     *"
                       "\n*************************"
                       "*****************************"
                       "*************************"
                       "\n* [1] - Random               "
                       "                      "
                       "                           *"
                       "\n* [2] - Reflect              "
                       "                       "
                       "                          *"
                       "\n* [3] - Cycler            "
                       "                         "
                       "                           *"
                       "\n* [4] - Exit                   "
                       "                        "
                       "                       *"
                       "\n**************************"
                       "******************************"
                       "***********************"
                       "\n Please select an option (1, 2, 3 or 4): ")
        if choice == "4":
            print("Goodbye .")
            quit()
        elif choice == "1":
            game = Game(HumanPlayer(), RandomPlayer())
            game.play_game()
            break
        elif choice == "2":
            game = Game(HumanPlayer(), ReflectPlayer())
            game.play_game()
            break
        elif choice == "3":
            game = Game(HumanPlayer(), CyclerPlayer())
            game.play_game()
            break
        else:
            print("WRONG INPUT!!!! PLEASE WRITE AGAIN")
            choice = input(" ask user ..")
