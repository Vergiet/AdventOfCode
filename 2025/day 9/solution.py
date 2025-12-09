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


def create_coords(input):
    coords = []
    for line in input.splitlines():
        x, y = line.split(",")
        coords.append((int(x), int(y)))
    return coords


def calculate_area(coords):
    biggest = 0
    for coord_a in coords:
        a_x, a_y = coord_a
        for coord_b in coords:
            b_x, b_y = coord_b
            if coord_a != coord_b:
                coord_diff_y = 0
                coord_diff_x = 0
                if a_x == b_x or a_y == b_y:
                    break
                if a_x > b_x:
                    coord_diff_x = (a_x - b_x) + 1
                if a_x < b_x:
                    coord_diff_x = (b_x - a_x) + 1
                if a_y < b_y:
                    coord_diff_y = (b_y - a_y) + 1
                if a_y > b_y:
                    coord_diff_y = (a_y - b_y) + 1

                area = coord_diff_x * coord_diff_y
                if area > biggest:
                    biggest = area
    return biggest

def calculate_area_2(coords):
    

def main1(inputfile, expected_result_1=0, expected_result_2=0):
    actual_result = calculate_area(create_coords(read_file(inputfile)))

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    actual_result = 0

    parse_result(actual_result, expected_result_2, inputfile)


if __name__ == "__main__":
    for inputfile in (
        ("example", 50, 24),
        ("input", 4754955192, -1),
    ):
        main1(*inputfile)
        main2(*inputfile)
