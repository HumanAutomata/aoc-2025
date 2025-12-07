"""06/12/25"""

# FILE = "./sample.txt"
FILE = "./input.txt"


def solution():
    """solution"""
    with open(FILE, encoding="UTF-8") as file:
        lines = [line.rstrip() for line in file]

        ranges = lines[: lines.index("")]
        ids = [int(id) for id in lines[lines.index("") + 1 :]]

        valid_ids = []
        for id_range in ranges:
            low, high = id_range.split("-")
            valid_ids.append((int(low), int(high)))

        fresh = 0
        for food_id in ids:
            for low, high in valid_ids:
                if low <= food_id <= high:
                    fresh += 1
                    break

        print(f"Part 1: {fresh}")


solution()
