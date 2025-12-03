"""02/12/2025"""

# FILE = "./sample.txt"
FILE = "./input.txt"


def validate(number):
    """Determine if a number is invalid"""

    # check different length sequences
    for length in range(1, len(number)):

        # skip non-divisor length
        if len(number) % length != 0:
            continue

        start = 0
        end = length
        substr = number[:length]
        is_invalid = True

        while end <= len(number) and is_invalid:
            if number[start:end] != substr:
                is_invalid = False
            start = end
            end += length

        if is_invalid:
            return int(number)

    return 0


def part2():
    """Part 2"""
    result = 0

    with open(FILE, encoding="utf-8") as file:
        bounds = file.read().strip().split(",")

        for bound in bounds:
            lower, upper = bound.split("-")

            for number in range(int(lower), int(upper) + 1):
                result += validate(str(number))

    print("Part 2: ", result)


part2()
# validate("446445")

# 55647141923 is too low
