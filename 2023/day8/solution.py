import os
import re
import sys
from math import lcm

regex = r'(^[0-9A-Z]{3})(?>\s=\s\()([0-9A-Z]{3})(?>,\s)([0-9A-Z]{3})(?>\))'
counter = 0
sys.setrecursionlimit(214748364)  # 2147483647


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
        print(f"diff: {expected_result-actual_result}")


def parse_header(header):
    steps = []
    for step in header:
        steps.append(step)

    return steps


def parse_line(line):
    id, l, r = re.findall(regex, line)[0]

    return id, {
        "L": l,
        "R": r,
    }


def parse_body(body):
    structure = {}
    for line in body:
        id, struct = parse_line(line)
        structure[id] = struct

    return structure


def parse_input(file_content):
    header, body = file_content.split('\n', maxsplit=1)
    steps = parse_header(header)
    structure = parse_body(body.strip('\n').splitlines())
    return steps, structure


def step_counter(func):

    def wrapper(*args):
        global counter
        counter += 1
        return func(*args)
    return wrapper


@step_counter
def walk_structure(id, structure, steps, step_index=0):

    if step_index >= len(steps):
        step_index = 0

    newid = structure[id][steps[step_index]]

    if newid != 'ZZZ':
        walk_structure(newid, structure, steps, step_index+1)


def walk_structure_2(id):

    counter = 0

    while True:

        for i in range(len(steps)):

            counter += 1
            id = structure[id][steps[i]]

            if id[2] == "Z":
                return counter


def get_starting_positions(structure):
    starting_positions = []
    for key in structure.keys():
        if key[2:] == 'A':
            starting_positions.append(key)

    return starting_positions


def main1(inputfile, expected_result_1=0, expected_result_2=0):
    global counter
    counter = 0
    steps, structure = parse_input(read_file(inputfile))

    print(f"counter: {counter}")
    walk_structure(StartPoint, structure, steps)
    print(f"counter: {counter}")

    actual_result = counter

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    global steps
    global structure
    steps, structure = parse_input(read_file(inputfile))
    starting_positions = get_starting_positions(structure)

    stepcounters = list(map(walk_structure_2, starting_positions))
    print(f"stepcounters: {stepcounters}")
    actual_result = lcm(*stepcounters)

    parse_result(actual_result, expected_result_2, inputfile)


if __name__ == "__main__":
    for inputfile in (
        ("example", 6, -1),
        ("example2", -1, 6),
        ("input", 12643, 13133452426987),
    ):
        main1(*inputfile)
        main2(*inputfile)
