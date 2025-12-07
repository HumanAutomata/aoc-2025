"""06/12/25"""

# FILE = "./sample.txt"
FILE = "./input.txt"


def overlap(l1, h1, l2, h2):
    """true if ranges intercept"""
    return not ((h1 < l2) or (l1 > h2))


def eat_ranges(valid_ids, low, high):
    """merge overlapping ranges"""

    # first range
    if len(valid_ids) == 0:
        valid_ids.append((low, high))
        return valid_ids

    # find largest range
    for low_range, high_range in valid_ids:
        if overlap(low, high, low_range, high_range):
            low = low if low < low_range else low_range
            high = high if high > high_range else high_range

    # remove any overlapping ranges
    index = 0
    while index < len(valid_ids):
        low_range = valid_ids[index][0]
        high_range = valid_ids[index][1]

        if overlap(low, high, low_range, high_range):
            del valid_ids[index]
            index -= 1

        index += 1

    # add the new range
    valid_ids.append((low, high))
    return valid_ids


# We could also merge continuous ranges is needed
# ie, (3, 6) + (7, 10) = (3,10)


def solution():
    """solution"""
    with open(FILE, encoding="UTF-8") as file:
        lines = [line.rstrip() for line in file]
        ranges = lines[: lines.index("")]

        valid_ids = []
        for id_range in ranges:
            low, high = id_range.split("-")
            valid_ids = eat_ranges(valid_ids, int(low), int(high))

        answer = 0
        for low, high in valid_ids:
            answer += high - low + 1

        print(f"Part 2: {answer}")


solution()
