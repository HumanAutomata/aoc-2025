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

            # take the largest digit possible while leaving room for the rest
            number = ""

            for tail_len in range(11, -1, -1): # 11..0

                # we have to take the rest of the digits
                if len(number) + len(line) == 12:
                    number += line
                    break

                largest_digit = 0
                digit_pool = [int(char) for char in line[: len(line) - tail_len]]

                for digit in digit_pool:
                    largest_digit = digit if digit > largest_digit else largest_digit

                number += str(largest_digit)
                index = line.index(str(largest_digit)) + 1
                line = line[index:]

            answer += int(number)

        print(f"Part 2: {answer}")


solution()
