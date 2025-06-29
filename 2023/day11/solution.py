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
        print(f"diff: {expected_result-actual_result}")


def parse_input(content, galaxy_indexes):
    galaxy_map = []
    galaxy_names = []
    starting_indexes = []
    gi1 = 0
    gi2 = 0

    for i in range(len(content)):
        row = []
        for y in range(len(content[i])):
            chart_value = content[i][y]
            if chart_value == "#":
                chart_value = f"{galaxy_indexes[gi2]}{galaxy_indexes[gi1]}"
                galaxy_names.append(chart_value)
                starting_indexes.append((i, y, (len(galaxy_names)-1)))
                if gi1 == 25:
                    gi1 = 0
                    gi2 += 1
                else:
                    gi1 += 1

            row.append(chart_value)
        galaxy_map.append(row)

    return galaxy_map, galaxy_names, starting_indexes

def print_map(galaxy_map):
    for i in range(len(galaxy_map)):
        row = ""
        for y in range(len(galaxy_map[i])):
            row = row+("["+(f"{galaxy_map[i][y]}".ljust(2))+"]")
        print(row)

def expand_universe(galaxy_map, size):
    for row_i in range(len(galaxy_map)):
        if len(list(filter(is_dot, galaxy_map[row_i]))) == 0:
            update_row_vals(galaxy_map, row_i, size)
        else:
            update_row_vals(galaxy_map, row_i, 1)

    for col_i in range(len(galaxy_map[0])):
        col = get_column(galaxy_map, col_i)
        if len(list(filter(is_dot, col))) == 0:
            update_col_vals(galaxy_map, col_i, size)


def get_galaxy_names():
    galaxy_indexes = []

    for galaxy_index in "ABCDEFGHIJKLMNOPQRSTUWVXYZ":
        galaxy_indexes.append(galaxy_index)

    return galaxy_indexes

def is_dot(column_entry):
    return column_entry != '.' and type(column_entry) != int

def get_column(galaxy_map, column_i):
    return [row[column_i] for row in galaxy_map]

def update_row_vals(galaxy_map, row_i, value):
    for i in range(len(galaxy_map[row_i])):
        if galaxy_map[row_i][i] == '.':
            galaxy_map[row_i][i] = value

def update_col_vals(galaxy_map, col_i, value):
    col = get_column(galaxy_map, col_i)
    for i in range(len(col)):
        if col[i] == '.' or type(col[i]) == int:
            galaxy_map[i][col_i] = value

def in_bounds(galaxymap, xn, yn):
    maxx = len(galaxymap)
    maxy = len(galaxymap[0])
    return xn > -1 and xn < maxx and yn > -1 and yn < maxy

def get_key_val(galaxy_name):
    start_key = 0
    for char in galaxy_name:
        start_key+=ord(char)
    return start_key

def get_diff(x1, x2):
    if x1 < x2:
        xdiff = x2 - x1
    else:
        xdiff = x1 - x2

    return xdiff

def get_coord_diff(x1, x2):
    if x1 == x2:
        return 0
    elif x1 > x2:
        return -1
    elif x1 < x2:
        return 1  


def walk_dir(start, dest):
    x_dir = get_coord_diff(start[0], dest[0])
    y_dir = get_coord_diff(start[1], dest[1])
        
    return x_dir, y_dir

def comp_walk_dir(x_dir):
    if x_dir == -1:
        def func(a, b):
            return a+b
        return func
    elif x_dir == 1:
        def func(a, b):
            return a+b
        return func
    elif x_dir == 0:
        def func(a, b):
            return a
        return func

def walk_distance(galaxy_map, start, dest, galaxy_names):

    walkx = True
    cur_pos = start
    start_galaxy = galaxy_names[start[2]]
    dest_galaxy = galaxy_names[dest[2]]
    key = f"{start_galaxy}->{dest_galaxy}"
    key_rev = f"{dest_galaxy}->{start_galaxy}"
    
    x_dir, y_dir = walk_dir(start, dest)
    x_func = comp_walk_dir(x_dir)
    y_func = comp_walk_dir(y_dir)
    steps = []
    y_went = True
    next_up = "x"
    if start_galaxy != dest_galaxy and key not in discovered_routes and key_rev not in discovered_routes:
        while cur_pos != dest:
            x, y, z = cur_pos
                       
            if x == dest[0]:
                nx = x
                walkx = False

            if y == dest[1]:
                ny = y
            
            if y != dest[1] and not walkx:
                if x != dest[0]:
                    walkx = True
                ny = y_func(y, y_dir)
                nx = x

            if y_dir == 0:
                walkx = True

            if x != dest[0] and walkx:
                walkx = False
                nx = x_func(x, x_dir)
                ny = y

            cur_pos = (nx, ny, dest[2])
            step_val = galaxy_map[nx][ny]
            if type(step_val) == int:
                steps.append(step_val)
            else:
                steps.append(1)
            
        sum_steps = sum(steps)
        discovered_routes[f"{key}"] = {
            "steps": sum_steps,
            "start_galaxy": start_galaxy,
            "dest_galaxy": dest_galaxy
        }
        sums.append(sum_steps)

discovered_routes = dict()
sums = []

def main1(inputfile, expected_result_1=0, expected_result_2=0):
    
    galaxy_indexes = get_galaxy_names()

    galaxy_map, galaxy_names, starting_indexes = parse_input(read_file(inputfile).splitlines(), galaxy_indexes)

    expand_universe(galaxy_map, 2)

    for start in starting_indexes:
        for dest in starting_indexes:
            walk_distance(galaxy_map, start, dest, galaxy_names)
    
    actual_result = sum(sums)
    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    actual_result = 0

    galaxy_indexes = get_galaxy_names()

    galaxy_map, galaxy_names, starting_indexes = parse_input(read_file(inputfile).splitlines(), galaxy_indexes)

    expand_universe(galaxy_map, 1000000)
    print_map(galaxy_map)

    for start in starting_indexes:
        for dest in starting_indexes:
            walk_distance(galaxy_map, start, dest, galaxy_names)
    
    actual_result = sum(sums)

    parse_result(actual_result, expected_result_2, inputfile)


if __name__ == "__main__":
    for inputfile in (
        ("example", 374, 8410),
        ("input", 9403026, 543018317006),
    ):
        main1(*inputfile)
        main2(*inputfile)
