from sys import exit
from random import randint
from textwrap import dedent

people_amount = 10000 # number of people playing the game
membships = {'default': 1, 'gold': 20, 'diamond': 40, 'platina': 100}

def winner():
    return print("You pulled the fucking sword out!")

def loser():
    return print("The sword is still in the fucking rock")

def lottery(user_chance, people_amount):
    winner = randint(0, people_amount)
    user_numbs = []
    for i in range(0, user_chance):
        user_numbs.append(randint(0, people_amount))
    if winner in user_numbs:
        return "win"
    else:
        return "lose"

class User(object):

    def __init__(self, membship):
        self.username = self
        self.membship = membship

    def setup(self):
        if self.membship == "gold":
            self.chance = 20
        else:
            self.chance = 1


class Play(object):

    def __init__(self, membship):
#        super(Play, self).__init__()
        self.user = User(membship)

    def setup(self):
        pass

#testing some things
