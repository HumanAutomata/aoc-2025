""" 
01/12/25
"""

# FILE = "./sample.txt"
FILE = "./input.txt"


def part1():
    """Part 1"""
    position = 50
    zeros = 0

    with open(FILE, encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    for line in lines:
        rotation = line[0:1]
        number = int(line[1:])

        # increase number
        if rotation == "R":
            position = (position + number) % 100

        else:
            position = (position - number) % 100

        if position == 0:
            zeros += 1

    print("Part 1: ", zeros)


part1()
