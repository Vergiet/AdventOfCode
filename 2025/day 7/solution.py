import os


def read_file(file):
    filepath = os.path.join(os.path.split(__file__)[0], file)
    with open(filepath) as filepath:
        content = filepath.read()
        return content


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


def parse_input(input):
    map = []
    for line in input.splitlines():
        row = []
        for char in line:
            row.append(char)
        map.append(row)

    return map


def print_map(map):
    for x in range(len(map)):
        print(map[x])


def go_until_next_splitter(x, y, map, split_coords):
    if map[x][y] == ".":
        map[x][y] = "|"

    while x + 1 < len(map):
        if map[x][y] == "^":
            if f"{x},{y}" not in split_coords.keys():
                add_coords(split_coords, x, y)
                yl = y - 1
                yr = y + 1
                go_until_next_splitter(x, yl, map, split_coords)
                go_until_next_splitter(x, yr, map, split_coords)
            break
        x = x + 1
        if map[x][y] == ".":
            map[x][y] = "|"
        # print()
        # print()
        # print("Start new")
        # print_map(map)
        asd = ""


def find_s(map):
    return 0, map[0].index("S")


def add_coords(split_coords, x, y):
    split_coords[f"{x},{y}"] = True


def main1(inputfile, expected_result_1=0, expected_result_2=0):
    map = parse_input(read_file(inputfile))
    x, y = find_s(map)

    split_coords = dict()
    go_until_next_splitter(x, y, map, split_coords)
    actual_result = len(split_coords)

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    actual_result = 0

    parse_result(actual_result, expected_result_2, inputfile)


if __name__ == "__main__":
    for inputfile in (
        ("example", 21, -1),
        ("input", -1, -1),
    ):
        main1(*inputfile)
        # main2(*inputfile)
