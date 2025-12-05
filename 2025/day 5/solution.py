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


# def filter_ranges(fresh_ranges):
#     filtered_ranges = []
#     for start, end in fresh_ranges:
#         for filtered_start, filtered_end in filtered_ranges:
#             if start <= filtered_start and end > filtered_start and end <= filtered_end:
#                 pass
#             else:
#                 filtered_ranges.append((start, end))
#     return fresh_ranges


def filter_ranges(fresh_ranges):
    filtered_ranges = []
    for start, end in fresh_ranges:
        add_to_list = True
        print("Checking Filtered")
        print(f"{start} - start")
        print(f"{end} - end")
        print("")
        if len(filtered_ranges) == 0:
            filtered_ranges.append((start, end))
        else:
            for filtered_start, filtered_end in filtered_ranges:
                print("Checking Filtered")
                print(f"{filtered_start} - start")
                print(f"{filtered_end} - end")
                print("")
                # print()
                if start == filtered_start and end == filtered_end:
                    # print(f"{start} - start")
                    # print(f"{filtered_start} - filtered_start")
                    # print(f"{end} - end")
                    # print(f"{filtered_end} - filtered_end")
                    add_to_list = False
                    # break
                elif (
                    start < filtered_start
                    and end > filtered_start
                    and end <= filtered_end
                ):
                    print("1")
                    print(f"{start} - start")
                    print(f"{filtered_start} - filtered_start")
                    print(f"{end} - end")
                    print(f"{filtered_end} - filtered_end")
                    new_start = start
                    new_end = filtered_end
                    print(f"{new_start} - new_start")
                    print(f"{new_end} - new_end")
                    filtered_ranges.remove((filtered_start, filtered_end))
                    print(f"adding to list {new_start} {new_end}")
                    filtered_ranges.append((new_start, new_end))
                    new_start = 0
                    new_end = 0
                    add_to_list = False
                    # break
                elif start >= filtered_start and end <= filtered_end:
                    # print(f"{start} - start")
                    # print(f"{filtered_start} - filtered_start")
                    # print(f"{end} - end")
                    # print(f"{filtered_end} - filtered_end")
                    add_to_list = False
                elif (
                    start == filtered_start
                    and start < filtered_end
                    and end > filtered_end
                ):
                    print("2")
                    print(f"{start} - start")
                    print(f"{filtered_start} - filtered_start")
                    print(f"{end} - end")
                    print(f"{filtered_end} - filtered_end")
                    new_start = start
                    new_end = end
                    print(f"{new_start} - new_start")
                    print(f"{new_end} - new_end")
                    filtered_ranges.remove((filtered_start, filtered_end))
                    print(f"adding to list {new_start} {new_end}")
                    filtered_ranges.append((new_start, new_end))
                    new_start = 0
                    new_end = 0
                    add_to_list = False
                    # break

        print(f"add_to_list: {add_to_list}")
        if add_to_list:
            print(f"adding to list {start} {end}")
            filtered_ranges.append((start, end))

        print("Status:")
        print(f"{len(fresh_ranges)} - fresh_ranges")
        print(f"{len(filtered_ranges)} - filtered_ranges")
        print("")
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
    print(f"Number of fresh ranges: {len(fresh_ranges)}")
    print(f"Number of filtered ranges: {len(filtered_ranges)}")
    actual_result = calculate_fresh_ids(filtered_ranges)
    # actual_result = calculate_fresh_ids(fresh_ranges)
    # actual_result = 0

    parse_result(actual_result, expected_result_2, inputfile)


# 49577959599068 to low
# 49807208925952 to low
# 61419725698598 to low
# 58240463842684 to low
# 355672034204528 not correct
# 376909854969867 not correct
# 427981489340584 not correct
# 445171204094492 to high
# 445171204094492 to high

if __name__ == "__main__":
    for inputfile in (
        # ("example", 3, 14),
        ("input", 782, -1),
    ):
        # main1(*inputfile)
        main2(*inputfile)
