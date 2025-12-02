""" 
01/12/25
"""

# FILE = "./sample.txt"
FILE = "./input.txt"


def part2():
    """Part 2"""
    position = 50
    zeros = 0

    with open(FILE, encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    for line in lines:
        rotation = line[0:1]
        number = int(line[1:])

        # increase number
        if rotation == "R":
            zeros += (position + number) // 100
            position = (position + number) % 100

        # decrement number
        # there must be a more elegant way to do this
        else:
            temp_position = position - number

            while temp_position < 0:
                zeros += 1
                temp_position += 100

            position = temp_position

    print("Part 2: ", zeros)


part2()
