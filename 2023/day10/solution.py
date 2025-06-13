import os
from enum import Enum
import sys

sys.setrecursionlimit(2147483647)

walked_paths = set()


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


def input_to_map(input_lines):
    pipe_map = []
    start_point = None
    for i in range(len(input_lines)):
        pipe_row = []
        for j in range(len(input_lines[i])):
            char = input_lines[i][j]
            pipe = string_to_pipe(i, j, char)
            if char == "S":
                start_point = (i, j)
            pipe_row.append(pipe)
        pipe_map.append(pipe_row)
    return pipe_map, start_point


class Pipe():
    def __init__(self, x, y, val, north=False, east=False, south=False, west=False):
        self.x = x
        self.y = y
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.val = val

    def __repr__(self):
        return f"{self.val}"

    def __str__(self):
        return f"{self.val}"


class North_South(Pipe):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, north=True, south=True, val="|")
        pass


class East_West(Pipe):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, east=True, west=True, val="-")
        pass


class North_East(Pipe):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, north=True, east=True, val="L")
        pass


class North_West(Pipe):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, north=True, west=True, val="J")
        pass


class South_West(Pipe):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, south=True, west=True, val="7")
        pass


class South_East(Pipe):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, south=True, east=True, val="F")

        pass


class Ground(Pipe):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, val=".")
        pass


class Start(Pipe):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, val="S")
        pass


def string_to_pipe(x, y, string):
    match string:
        case "|":
            return North_South(x, y)
        case "-":
            return East_West(x, y)
        case "L":
            return North_East(x, y)
        case "J":
            return North_West(x, y)
        case "7":
            return South_West(x, y)
        case "F":
            return South_East(x, y)
        case ".":
            return Ground(x, y)
        case _:
            return Start(x, y)


def direction_to_pipe(first, second, x, y):
    match first:
        case "north":
            match second:
                case "east":
                    return North_East(x, y)
                case "west":
                    return North_West(x, y)
                case "South":
                    return North_South(x, y)
        case "south":
            match second:
                case "east":
                    return South_East(x, y)
                case "west":
                    return South_West(x, y)
        case "east":
            match second:
                case "west":
                    return East_West(x, y)


def convert_startpoint(pipe_map, start_point, moves):
    x, y = start_point

    next_pipes = []
    allowed_moves = []
    for move in moves:
        nx = x + move["d"][0]
        ny = y + move["d"][1]
        if nx > -1 and ny > -1 and nx < len(pipe_map) and ny < len(pipe_map):
            next_pipe = pipe_map[nx][ny]
            if next_pipe.val in move["allowed_pipes"]:
                next_pipes.append(next_pipe)
                allowed_moves.append(move)
    start_replacement_pipe = direction_to_pipe(
        allowed_moves[0]["name"], allowed_moves[1]["name"], x, y)
    pipe_map[x][y] = start_replacement_pipe


def get_allowed_moves(pos, moves):
    north = 0
    south = 1
    east = 2
    west = 3
    allowed_moves = []
    if pos.north:
        allowed_moves.append(moves[north])
    if pos.south:
        allowed_moves.append(moves[south])
    if pos.east:
        allowed_moves.append(moves[east])
    if pos.west:
        allowed_moves.append(moves[west])

    if len(allowed_moves) != 2:
        raise ValueError("There should always be exactly 2 moves")

    return allowed_moves


def print_map(pipe_map, x, y):

    for i in range(len(pipe_map)):
        row = ""
        for j in range(len(pipe_map[i])):
            if i == x and y == j:
                char = "S"
            else:
                char = pipe_map[i][j]
            row = f"{row}{char}"
        print(row)
    print("x"*len(pipe_map))


def walk_map(pipe_map, start_point, moves, depth=0):
    if start_point in walked_paths:
        return [depth]
    else:
        walked_paths.add(start_point)

    x, y = start_point

    cur_pos = pipe_map[x][y]
    allowed_moves = []
    for allowed_move in get_allowed_moves(cur_pos, moves):
        allowed_moves.append(allowed_move)

    if len(allowed_moves) == 0:
        return [depth]

    results = []
    for allowed_move in allowed_moves:
        direction = allowed_move["d"]
        nx = x + direction[0]
        ny = y + direction[1]
        results.extend(walk_map(pipe_map, (nx, ny), moves, depth+1))

    return results


def create_moves():
    up = {
        "d": (-1, 0),
        "allowed_pipes": ["|", "F", "7"],
        "name": "north",
    }
    down = {
        "d": (1, 0),
        "allowed_pipes": ["|", "J", "L"],
        "name": "south",
    }
    right = {
        "d": (0, 1),
        "allowed_pipes": ["-", "J", "7"],
        "name": "east",
    }
    left = {
        "d": (0, -1),
        "allowed_pipes": ["-", "L", "F"],
        "name": "west",
    }

    return [up, down, right, left]


def main1(inputfile, expected_result_1=0, expected_result_2=0):
    actual_result = 0
    moves = create_moves()
    pipe_map, start_point = input_to_map(read_file(inputfile).splitlines())

    convert_startpoint(pipe_map, start_point, moves)

    actual_result = max(walk_map(pipe_map, start_point, moves))//2

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    actual_result = 0

    parse_result(actual_result, expected_result_2, inputfile)


if __name__ == "__main__":
    for inputfile in (
        ("example", 8, -1),
        # ("input", 6867, -1),
    ):
        # main1(*inputfile)
        main2(*inputfile)
