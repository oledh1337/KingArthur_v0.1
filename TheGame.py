#klein begin
from sys import exit
from random import randint
from textwrap import dedent
people_amount = 10000 # number of people playing the game, this will be equal to the change there is of winning.

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
        self.username = self
        self.membship = membship

    def setup(self):
        if self.membship == "gold":
            self.user_chance = 20
        else:
            self.user_chance = 1


class Play(object):

    def __init__(self, membship):
#        super(Play, self).__init__()
        self.user = User(membship)

    def setup(self):
        pass

#testing some things
ole = Play("gold") # var ole will be the username of a person
ole.user.setup()
x = 1
for i in range(0, x):
    # make it run x times
    lottery(ole.user.user_chance, people_amount)
