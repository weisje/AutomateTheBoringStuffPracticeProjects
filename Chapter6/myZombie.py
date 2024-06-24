"""
CODE ASSIGNMENT:
Try writing some of your own bots to play Zombie Dice and see how they
compare against the other bots. Specifically, try to create the following bots:
•  A bot that, after the first roll, randomly decides if it will continue or stop
•  A bot that stops rolling after it has rolled two brains
•  A bot that stops rolling after it has rolled two shotguns
•  A bot that initially decides it’ll roll the dice one to four times, but will
stop early if it rolls two shotguns
•  A bot that stops rolling after it has rolled more shotguns than brains
Run these bots through the simulator and see how they compare
to each other.
"""

import random
import zombiedice


class MyZombie:
    def __init__(self, name):

        self.name = name # All zombies must have a name
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        # 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        # ('green', 'shotgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        """
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
        """


class RandomAfterOneRoll:
    def __init__(self, name):

        self.name = name # All zombies must have a name
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        # 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        # ('green', 'shotgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        randomChoice = random.randint(0,1)
        diceRollResults =zombiedice.roll()
        while diceRollResults is not None:
            if randomChoice == 0:
                diceRollResults = zombiedice.roll()
            else:
                break


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1Shotgun', minShotguns=1),
    RandomAfterOneRoll(name='Random after one')
    # Add any other zombie players here.
    )
# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)