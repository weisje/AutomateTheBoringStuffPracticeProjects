"""
CODE ASSIGNMENT:
Say you have a list of lists where each value in the inner lists is a one-character
string, like this:
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
Think of grid[x][y] as being the character at the x- and y-coordinates
of a “picture” drawn with text characters. The (0, 0) origin is in the upperleft corner, the x-coordinates increase going right, and the y-coordinates
increase going down. Copy the previous grid value, and write code that uses it to print
the image.
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
"""


def main():
    originalGrid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    newGrid = []

    for xCoord in range(len(originalGrid[0])):
        newGridRow = []
        for yCoord in range(len(originalGrid)):
            newGridRow.append(originalGrid[yCoord][xCoord])
        newGrid.append(newGridRow)

    for row in newGrid:
        rowString = ""
        for item in row:
            rowString += item
        print(rowString)


if __name__ == '__main__':
    main()
