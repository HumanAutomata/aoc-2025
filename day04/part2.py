"""05/12/25"""

from enum import Enum

# FILE = "./sample.txt"
# DIMENSION = 12

FILE = "./input.txt"
DIMENSION = 138


class Directions(Enum):
    """define 8 directions"""

    NORTH = (-1, 0)
    NORTH_EAST = (-1, 1)
    EAST = (0, 1)
    SOUTH_EAST = (1, 1)
    SOUTH = (1, 0)
    SOUTH_WEST = (1, -1)
    WEST = (0, -1)
    NORTH_WEST = (-1, -1)


BOARD = [["." for _ in range(DIMENSION)] for _ in range(DIMENSION)]


def print_board():
    """print the board"""
    for row in BOARD:
        for col in row:
            print(col, end=" ")
        print()


def populate_board():
    """populate board with the input"""
    with open(FILE, encoding="UTF-8") as file:
        lines = [list(line.rstrip()) for line in file]

        for row, _ in enumerate(lines):
            for col in range(len(lines)):
                BOARD[row + 1][col + 1] = lines[row][col]


def is_accessable(row, col):
    """check if a roll of paper is accessible"""
    neighbours = 0
    for direction in Directions:
        x, y = direction.value

        if BOARD[row + x][col + y] == "@":
            neighbours += 1

    return neighbours < 4


def solution():
    """solution"""
    populate_board()

    accessible = 0
    reset = True

    while reset:
        removed = False
        for row in range(1, DIMENSION - 1):
            for col in range(1, DIMENSION - 1):
                # you could cache the positions of @
                # to make the next loops a lot faster
                if BOARD[row][col] == "@":
                    if is_accessable(row, col):
                        accessible += 1
                        BOARD[row][col] = "X"
                        removed = True
        if not removed:
            reset = False

    print(f"Part 2: {accessible}")


solution()
