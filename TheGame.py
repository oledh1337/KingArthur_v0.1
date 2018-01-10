# klein begin
from sys import exit
from random import randint
from textwrap import dedent
people_amount = 10000 # number of people playing the game

def win():
    return print("You pulled the fucking sword out!")

def lose():
    return print("The sword is still in the fucking rock")

def lottery(user_chance, people_amount):
    winner = randint(0, people_amount)
    user_numbs = []
    for i in range(0, user_chance):
        user_numbs.append(randint(0, people_amount))
    if winner in user_numbs:
        win()
    else:
        lose()

class User(object):

    def __init__(self, membship):
        username = self
        self.membship = membship

    def setup(self):
        pass # to be finished

class Play(object):

    def __init__(self):
        pass

    def setup(self):
        pass
