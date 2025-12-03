"""02/12/2025"""

# FILE = "./sample.txt"
FILE = "./input.txt"


def validate(number):
    """Determine if a number is invalid"""
    middle = len(number) // 2
    left = number[:middle]
    right = number[middle:]

    return int(number) if left == right else 0


def part1():
    """Part 1"""
    result = 0

    with open(FILE, encoding="utf-8") as file:
        bounds = file.read().strip().split(",")

        for bound in bounds:
            lower, upper = bound.split("-")

            for number in range(int(lower), int(upper) + 1):
                result += validate(str(number))

    print("Part 1: ", result)


part1()
