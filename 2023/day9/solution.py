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


def parse_input(line):
    new_line = []
    for val in line.split():
        new_line.append(int(val))

    return new_line


def check_all_values_0(diff_history):
    counter_0 = 0
    if len(diff_history) == 0:
        raise Exception("history should atleast have 1 entry")
    for val in diff_history.copy():
        if val == 0:
            counter_0 += 1

    return len(diff_history) == counter_0


def calc_next_val(history):
    diffs = []
    for history_index in range(1, len(history)):
        diffs.append(history[history_index] - history[history_index - 1])

    print(diffs)
    if check_all_values_0(diffs):
        return history[-1]
    else:
        next_diff = calc_next_val(diffs)

        return history[-1] + next_diff


def calc_next_val_2(history):
    diffs = []
    for history_index in range(1, len(history)):
        diffs.append(history[history_index] - history[history_index - 1])

    print(diffs)
    if check_all_values_0(diffs):
        return history[0]
    else:
        next_diff = calc_next_val_2(diffs)

        return history[0] - next_diff


def main1(inputfile, expected_result_1=0, expected_result_2=0):

    print(read_file(inputfile))

    parsed_input = list(map(parse_input, read_file(inputfile).splitlines()))

    diffs = list(map(calc_next_val, parsed_input))
    print(diffs)

    print(len(diffs))
    print(len(parsed_input))

    actual_result = sum(diffs)

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):

    print(read_file(inputfile))

    parsed_input = list(map(parse_input, read_file(inputfile).splitlines()))

    diffs = list(map(calc_next_val_2, parsed_input))
    print(diffs)

    print(len(diffs))
    print(len(parsed_input))

    actual_result = sum(diffs)

    parse_result(actual_result, expected_result_2, inputfile)


if __name__ == "__main__":
    for inputfile in (
        ("example", 114, 2),
        ("input", 1834108701, 993),
    ):
        # main1(*inputfile)
        main2(*inputfile)
