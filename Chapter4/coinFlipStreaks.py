"""
Write a program to find out how often a streak of six heads or a streak
of six tails comes up in a randomly generated list of heads and tails in batches of 100. Your
program breaks up the experiment into two parts: the first part generates
a list of randomly selected 'heads' and 'tails' values, and the second part
checks if there is a streak in it. Put all of this code in a loop that repeats the
experiment 10,000 times so we can find out what percentage of the coin
flips contains a streak of six heads or tails in a row. As a hint, the function
call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value
the other 50% of the time
"""
import random


def coinFlipper(flipCount=100) -> list:
    """
    Function to randomly generate a list of values "Heads" or "Tails" & return them as a list
    :param flipCount: How many times the function should flip a coin
    :type flipCount: int
    :return: list
    """
    returnList = []
    for flip in range(flipCount):
        randomSide = random.randint(0, 1)
        if randomSide == 0:
            returnList.append("Tails")
        else:
            returnList.append("Heads")
    return returnList


def experimentBatch(batchCount=10000, batchSize=100) -> list:
    """
    Function for performing a number of a secondary function and returning each result in a list
    :param batchCount: Number of times the second function should be called
    :type batchCount: int
    :param batchSize: How many items should be in each batch
    :type batchSize: int
    :return: list
    """
    returnList = []
    for count in range(batchCount):
        returnList.append(coinFlipper(batchSize))

    return returnList


def flipComparer(flipBatch, streakSize=6) -> bool:
    """
    Function that compares the values within a given list and determines if said values happen in a streak of streakSize
    :param flipBatch: List of items to be compared
    :type flipBatch: list
    :param streakSize: How many repeats in a row to look for
    :type streakSize: int
    :return: bool
    """
    counter = 0
    for item in flipBatch:
        currentBatch = flipBatch[counter:counter+streakSize]
        if currentBatch.count(item) >= streakSize:
            return True
        counter += 1
    return False


def main():
    batchSize = 100
    totalBatches = 100000
    streakSize = 6
    streakCounter = 0
    totalExperiment = experimentBatch(totalBatches, batchSize)
    for batch in totalExperiment:
        if flipComparer(batch, streakSize):
            streakCounter += 1

    streakChance = (streakCounter / totalBatches) * 100
    roundedStreakChance = round(streakChance, 4)

    print(f"Chance of a streak of {streakSize} in {batchSize} flips: {roundedStreakChance}%")


if __name__ == '__main__':
    main()
