import os


def read_file(file):
    filepath = os.path.join(os.path.split(__file__)[0], file)
    with open(filepath) as filepath:
        content = filepath.read()
        return content


def parse_input_to_map(input):
    map = []
    for line in input.splitlines():
        row = []
        for char in line:
            row.append(char)
        map.append(row)
    return map


def parse_coords_to_check(i, j, leni, lenj):
    coords_to_check = []

    ib = i - 1
    io = i + 1
    jl = j - 1
    jr = j + 1

    if ib >= 0 and jl >= 0:
        coords_to_check.append((ib, jl))

    if ib >= 0 and j >= 0:
        coords_to_check.append((ib, j))

    if ib >= 0 and jr >= 0 and jr < lenj:
        coords_to_check.append((ib, jr))

    if jl >= 0:
        coords_to_check.append((i, jl))

    if jr >= 0 and jr < lenj:
        coords_to_check.append((i, jr))

    if io >= 0 and io < leni and jl >= 0:
        coords_to_check.append((io, jl))

    if io >= 0 and io < leni and j >= 0:
        coords_to_check.append((io, j))

    if io >= 0 and io < leni and jr >= 0 and jr < lenj:
        coords_to_check.append((io, jr))

    return coords_to_check


def parse_map(map):
    rolls_of_paper_can_be_accessed = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "@":
                surrounding = 0
                coords_to_check = parse_coords_to_check(i, j, len(map), len(map[i]))
                for xi, xj in coords_to_check:
                    if map[xi][xj] == "@":
                        surrounding += 1

                if surrounding < 4:
                    rolls_of_paper_can_be_accessed += 1
    return rolls_of_paper_can_be_accessed


def parse_map_2(map):
    rolls_of_paper_can_be_accessed = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "@":
                surrounding = 0
                coords_to_check = parse_coords_to_check(i, j, len(map), len(map[i]))
                for xi, xj in coords_to_check:
                    if map[xi][xj] == "@":
                        surrounding += 1

                if surrounding < 4:
                    map[i][j] = "."
                    rolls_of_paper_can_be_accessed += 1
    return rolls_of_paper_can_be_accessed


def redo_map_2(map):
    rolls_of_paper_can_be_accessed_2 = 0
    rolls_of_paper_can_be_accessed = 1
    while rolls_of_paper_can_be_accessed > 0:
        rolls_of_paper_can_be_accessed = parse_map_2(map)
        if rolls_of_paper_can_be_accessed > 0:
            rolls_of_paper_can_be_accessed_2 += rolls_of_paper_can_be_accessed

    return rolls_of_paper_can_be_accessed_2


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
    actual_result = parse_map(parse_input_to_map(read_file(inputfile)))
    # actual_result = 0

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    actual_result = redo_map_2(parse_input_to_map(read_file(inputfile)))

    parse_result(actual_result, expected_result_2, inputfile)


if __name__ == "__main__":
    for inputfile in (
        ("example", 13, 43),
        ("input", 1351, -1),
    ):
        main1(*inputfile)
        main2(*inputfile)
