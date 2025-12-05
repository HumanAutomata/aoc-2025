"""
04/12/25
"""

# FILE = "./sample.txt"
FILE = "./input.txt"


def solution():
    """solution"""

    with open(FILE, encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

        answer = 0

        for line in lines:

            first_digit = 0
            second_digit = 0

            # don't check last digit
            for char in line[: len(line) - 1]:
                digit = int(char)
                first_digit = digit if digit > first_digit else first_digit

            # check all digit after the index of the first
            for char in line[line.index(str(first_digit)) + 1 :]:
                digit = int(char)
                second_digit = digit if digit > second_digit else second_digit

            answer += int(str(first_digit) + str(second_digit))

        print(f"Part 1: {answer}")


solution()
