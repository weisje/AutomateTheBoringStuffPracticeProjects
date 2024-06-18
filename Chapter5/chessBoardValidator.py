"""
CODE ASSIGNMENT:
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.
A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and
all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.
"""


def isValidChessBoard(currentBoardState) -> bool:
    """
    Function to check if the current state of a board is valid or if there is something that would make it not a valid chess board
    :param currentBoardState: dict
    :return: bool
    """

    pieceInventory = {'wpawn': 0, 'bpawn': 0, 'wknight': 0, 'bknight': 0, 'wbishop': 0, 'bbishop': 0, 'wrook': 0, 'brook': 0, 'wqueen': 0, 'bqueen': 0, 'wking': 0, 'bking': 0}
    squareInventory = {'1a': 0, '1b': 0, '1c': 0, '1d': 0, '1e': 0, '1f': 0, '1g': 0, '1h': 0, '2a': 0, '2b': 0, '2c': 0, '2d': 0, '2e': 0, '2f': 0, '2g': 0, '2h': 0, '3a': 0, '3b': 0, '3c': 0, '3d': 0, '3e': 0, '3f': 0, '3g': 0, '3h': 0, '4a': 0, '4b': 0, '4c': 0, '4d': 0, '4e': 0, '4f': 0, '4g': 0, '4h': 0, '5a': 0, '5b': 0, '5c': 0, '5d': 0, '5e': 0, '5f': 0, '5g': 0, '5h': 0, '6a': 0, '6b': 0, '6c': 0, '6d': 0, '6e': 0, '6f': 0, '6g': 0, '6h': 0, '7a': 0, '7b': 0, '7c': 0, '7d': 0, '7e': 0, '7f': 0, '7g': 0, '7h': 0, '8a': 0, '8b': 0, '8c': 0, '8d': 0, '8e': 0, '8f': 0, '8g': 0, '8h': 0}
    whitePieceCount = 0
    blackPieceCount = 0
    for key, value in currentBoardState.items(): # Sort out each key & value to provide proper counting of each piece
        if currentBoardState[key][0] == 'w':
            whitePieceCount += 1
        elif currentBoardState[key][0] == 'b':
            blackPieceCount += 1
        else:
            print("Count Error")
            return False
        try:
            squareInventory[key] += 1
            pieceInventory[value] += 1
        except KeyError: # If an invalid piece or square is found, return False
            print("KeyError")
            return False

    if whitePieceCount > 16 or blackPieceCount > 16: # Check to make sure players don't have too many pieces
        return False
    if pieceInventory['wking'] != 1 or pieceInventory['bking'] != 1: # Check to make sure there is only one king of each color
        return False
    if pieceInventory['wpawn'] > 8 or pieceInventory ['bpawn'] > 8: # Check to make sure there are less than 8 pawns on the board
        return False

    return True


def main():
    currentBoardState = {'1a': "wking", "8h": "bking", '2a': 'wpawn', '3b': 'wpawn', '4c': 'wpawn', '5d': 'wpawn', '6e': 'wpawn', '7f': 'wpawn', '2h': 'wpawn', '3a': 'wpawn'}
    print(isValidChessBoard(currentBoardState))


if __name__ == "__main__":
    main()