import os
from tkinter.constants import TRUE


def read_file(file):
    filepath = os.path.join(os.path.split(__file__)[0], file)
    with open(filepath) as filepath:
        content = filepath.read()
        return content


def parse_input(input):
    fresh_ranges = []
    available_ingredients = []
    for line in input.splitlines():
        if line.count("-") == 1:
            start, end = line.split("-")
            fresh_ranges.append((int(start), int(end)))
        elif len(line) > 0:
            available_ingredients.append(int(line))

    return fresh_ranges, available_ingredients


# def create_fresh_ingredients(fresh_ranges):
#     a = "."
#     fresh_ingredients = {}
#     for start, end in fresh_ranges:
#         for position in range(start, end + 1):
#             fresh_ingredients[position] = a
#     return fresh_ingredients


# def available_fresh_ingredients(fresh_ingredients, available_ingredients):
#     available_fresh_ingredients = 0
#     for available_ingredient in available_ingredients:
#         if int(available_ingredient) in fresh_ingredients:
#             available_fresh_ingredients += 1
#     return available_fresh_ingredients


def evaluate_freshness(fresh_ranges, available_ingredients):
    available_fresh_ingredients = 0
    for ingrediant in available_ingredients:
        for start, end in fresh_ranges:
            if ingrediant >= start and ingrediant <= end:
                available_fresh_ingredients += 1
                break

    return available_fresh_ingredients


def filter_ranges(fresh_ranges):
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    filtered_ranges = []
    for start, end in sorted_ranges:
        if not filtered_ranges or start > filtered_ranges[-1][1] + 1:
            filtered_ranges.append((start, end))
        else:
            filtered_ranges[-1] = (
                filtered_ranges[-1][0],
                max(filtered_ranges[-1][1], end),
            )
    return filtered_ranges


def calculate_fresh_ids(fresh_ranges):
    total_ids = 0
    for start, end in fresh_ranges:
        total_ids += end - start + 1
    return total_ids


def parse_result(actual_result, expected_result, inputfile):
    if expected_result == actual_result:
        print("Success!")
        print(f"inputfile: {inputfile}")
        print(f"expected_result: {expected_result}")
        print(f"actual_result: {actual_result}")
    else:
        print("Catastrophic Failure!")
        print(f"inputfile: {inputfile}")
        print(f"expected_result: {expected_result}")
        print(f"actual_result: {actual_result}")
        print(f"diff: {expected_result - actual_result}")


def main1(inputfile, expected_result_1=0, expected_result_2=0):
    fresh_ranges, available_ingredients = parse_input(read_file(inputfile))
    actual_result = evaluate_freshness(fresh_ranges, available_ingredients)

    # actual_result = 0

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    fresh_ranges, available_ingredients = parse_input(read_file(inputfile))
    filtered_ranges = filter_ranges(fresh_ranges)
    actual_result = calculate_fresh_ids(filtered_ranges)
    # actual_result = calculate_fresh_ids(fresh_ranges)
    # actual_result = 0

    parse_result(actual_result, expected_result_2, inputfile)


if __name__ == "__main__":
    for inputfile in (
        # ("example", 3, 14),
        ("input", 782, -1),
    ):
        # main1(*inputfile)
        main2(*inputfile)
