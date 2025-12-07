"""06/12/25"""

import numpy

# FILE = "./sample.txt"
FILE = "./input.txt"


def solution():
    """solution"""
    with open(FILE, encoding="utf-8") as file:
        lines = [list(line.strip("\n")) for line in file]

        num_lines = len(lines) - 1
        len_lines = len(lines[0])

        ops = lines[-1]
        ops = [op for op in ops if op != " "]

        operand_list = []
        numbers = []
        answer = 0

        for i in range(len_lines):
            number = ""
            for j in range(num_lines):
                number += lines[j][i]

            if number.strip() == "":
                operand_list.append(numbers)
                numbers = []

            else:
                numbers.append(int(number))

        # append the last list
        operand_list.append(numbers)

        for index, operands in enumerate(operand_list):
            op = ops[index]

            match op:
                case "+":
                    answer += sum(operands)
                case "*":
                    answer += numpy.prod(operands)
                case "_":
                    print("We should never print this")

        print(f"Part 2: {answer}")


solution()
