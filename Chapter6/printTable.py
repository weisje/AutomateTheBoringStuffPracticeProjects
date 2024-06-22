"""
CODE ASSIGNMENT:
Table Printer
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings.
"""

import sys

def printTable(listOfItems, justifyDirection = 'center') -> None:
    """
    Function to take in a list of lists & display the contents of lists justified in a specified direction by the longest item in each set of lists
    :param listOfItems: Items to displayed stored as lists of lists
    :type listOfItems: list
    :param justifyDirection: direction that the text should be justified
    :type: str
    :return: None
    """
    possibleJustifyDirections = ['left',  'right', 'center']
    if justifyDirection not in possibleJustifyDirections:
        sys.exit(f'\'{justifyDirection}\' is not a valid entry for justifyDirection')

    colWidths = [0] * len(listOfItems) # Create a list to hold the longest string in each provided list to justify off of
    colCounter = 0
    for listOfObjects in listOfItems:
        for item in listOfObjects:
            if colWidths[colCounter] <= len(item):
                colWidths[colCounter] = len(item)
        colCounter += 1

    print(colWidths)

    for itemCount in range(len(listOfItems[0])):
        for listCount in range(len(listOfItems)):
            match justifyDirection:
                case 'right':
                    print(listOfItems[listCount][itemCount].rjust(colWidths[listCount]), end=' ')
                case 'left':
                    print(listOfItems[listCount][itemCount].ljust(colWidths[listCount]), end=' ')
                case 'center':
                    print(listOfItems[listCount][itemCount].center(colWidths[listCount]), end=' ')
        print()


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'giraffes']]

    printTable(tableData)


if __name__ == '__main__':
    main()