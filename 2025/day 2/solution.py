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


def parse_file(text):
    ranges = []
    for range_as_str in text.split(","):
        begin, end = range_as_str.split("-")
        ranges.append((int(begin), int(end) + 1))
    return ranges


def is_even(val):
    if len(f"{val}") % 2 == 0:
        return True
    else:
        return False


def devide_vals(val):
    val_devisions = []
    val_as_str = f"{val}"
    if len(val_as_str) > 3:
        start_range = 2
    else:
        start_range = 1
    for x in range(start_range, len(val_as_str)):
        # print(val % x)
        if len(val_as_str) % x == 0:
            if x == 1:
                devide_by = 2
            else:
                devide_by = x
            part = val_as_str[0 : len(val_as_str) // devide_by]
            max_count = len(val_as_str) // len(part)
            if val != int(part):
                val_devisions.append((val, part, x, max_count))
    return val_devisions


def devide_ranges(ranges):
    val_devisions = []
    for range_entry in ranges:
        begin, end = range_entry
        for x in range(begin, end):
            val_devisions.append(devide_vals(x))
    return val_devisions


def print_ranges(ranges):
    silly_patterns = []
    for range_entry in ranges:
        begin, end = range_entry
        for x in range(begin, end):
            if is_even(x):
                x_as_str = f"{x}"
                first_half, second_half = [
                    x_as_str[start:end]
                    for start, end in [
                        (0, len(x_as_str) // 2),
                        (len(x_as_str) // 2, len(x_as_str)),
                    ]
                ]
                if int(first_half) == int(second_half):
                    silly_patterns.append(x)
    return silly_patterns


def match_ranges(devided_ranges):
    silly_patterns = []
    for devided_range in devided_ranges:
        match_devisions(devided_range, silly_patterns)
    return silly_patterns


def match_devisions(devided_range, silly_patterns):
    for devision in devided_range:
        val, part, x, max_count = devision
        result = f"{val}".count(part) == max_count
        if result:
            silly_patterns.append(val)
            return


def main1(inputfile, expected_result_1=0, expected_result_2=0):
    ranges = parse_file(read_file(inputfile))
    silly_patterns = print_ranges(ranges)
    actual_result = sum(silly_patterns)
    # actual_result = 0

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    ranges = parse_file(read_file(inputfile))
    devided_ranges = devide_ranges(ranges)
    actual_result = sum(match_ranges(devided_ranges))
    # actual_result = 0

    parse_result(actual_result, expected_result_2, inputfile)


# 33807867275 to low

if __name__ == "__main__":
    for inputfile in (
        ("example", 1227775554, 4174379265),
        ("input", 24157613387, -1),
    ):
        # main1(*inputfile)
        main2(*inputfile)
