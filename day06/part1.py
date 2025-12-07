"""06/12/25"""

import numpy

# FILE = "./sample.txt"
FILE = "./input.txt"


def solution():
    """solution"""
    with open(FILE, encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]
        numbers = [line.split() for line in lines[:-1]]
        ops = [line.split() for line in lines[-1:]]
        ops = ops[0]

        numbers = numpy.transpose(numbers)

        answer = 0

        for index, op in enumerate(ops):
            operands = [int(num) for num in numbers[index]]

            match op:
                case "+":
                    answer += sum(operands)

                case "*":
                    answer += numpy.prod(operands)

                case "_":
                    print("We should never print this")

        print(f"Part 1: {answer}")


solution()
