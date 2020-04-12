import random


class Roll:
    def __init__(self, roll_name=''):
        if roll_name == '':
            self.roll_name = random.choice(['rock', 'scissors', 'paper'])
        else:
            self.roll_name = roll_name.lower()

    def win(self):
        """
        :return: string of the roll defeated by a given key. i.e rock defeats scissors, so we return scissors for key = rock
        """
        d = dict(rock='scissors', scissors='paper', paper='rock')
        return d[self.roll_name]

    def name(self):
        return str(self.roll_name)


class Player:
    def __init__(self, name):
        self.name = name

    def name(self):
        return str(self.name())

    def play(self):
        return Roll()
