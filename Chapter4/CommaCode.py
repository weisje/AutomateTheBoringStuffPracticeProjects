"""
CODE REQUIREMENTS:
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
"""

import sys


def listSplitter(listToSplit, seperatorCharacter=",", finalIndicator="and") -> str:
    """
    Function to take a provided list and generate a string from said list with a specified character(comma is default). It also adds a final indicator before the last thing on the list(so long as there is more than one thing on the list)(default "and").
    :param listToSplit: List provided to the program to be split into a string
    :type listToSplit: list
    :param seperatorCharacter: Character provided by the user to define what should be used to indicate the separation of different values from the list
    :type seperatorCharacter: str
    :param finalIndicator: Character to defined what indicates the end of a string with more than one item on the provided list
    :type finalIndicator: str
    :return: str
    """
    if len(listToSplit) == 0:
        return "No items in list provided!" # Inform caller that list does not contain any values
    elif len(listToSplit) == 1:
        return str(listToSplit[0]) # Simply return a string of the only item on the list to caller
    elif len(listToSplit) == 2: # Don't include a separator, just the final indicator
        return f"{listToSplit[0]} {finalIndicator} {listToSplit[1]}"
    else: # Include separator as well as an Oxford Comma
        counter = 0
        returnString = ""
        for item in listToSplit:
            if counter == len(listToSplit) - 1: # Check to see if the item is the last on the list
                returnString += f"{finalIndicator} {item}"
            else: # Add each item from list as well as the separator character
                returnString += f"{item}{seperatorCharacter} "
            counter += 1
        return returnString


def main():
    testList = ["Apple", "Cat", "Ball", "Microphone"]
    print(listSplitter(testList))


if __name__ == '__main__':
    main()
