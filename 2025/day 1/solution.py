import os


def read_file(file):
    filepath = os.path.join(os.path.split(__file__)[0], file)
    with open(filepath) as filepath:
        content = filepath.read()
        return content


def parse_file(text):
    lines = text.splitlines()
    arr = []
    for line in lines:
        side = line[0]
        steps = int(line[1::])
        arr.append((side, steps))
    return arr


def run_dial(dial, steps, curr):
    count_of_zero = 0
    for step in steps:
        if step[0] == "L":
            stepsize = step[1]
            if stepsize > 99:
                stepsize = stepsize % 100
            curr = dial[curr - stepsize]
        elif step[0] == "R":
            stepsize = curr + step[1]
            if stepsize > 99:
                stepsize = stepsize % 100
            curr = dial[stepsize]
        else:
            raise ValueError(f"Invalid step: {step}")
        if curr == 0:
            count_of_zero += 1
    return count_of_zero


def apply_operator(operator, a, b):
    switch = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
    }
    return switch[operator](a, b)

def run_dial_2(steps, curr):
    count_of_zero = 0
    operator = ""
    for step in steps:
        old_count_of_zero = count_of_zero
        if step[0] == "L":
            operator = "-"
        elif step[0] == "R":
            operator = "+"
        newpos = apply_operator(operator, curr, step[1])
        add_count_of_zero = 0
        if newpos <= 0:
            if curr == 0:
                add_diff = 0
            else:
                add_diff = 1
            add_count_of_zero = abs(int(newpos / 100)) + add_diff
            count_of_zero += add_count_of_zero
        if newpos > 99:
            add_count_of_zero = int(newpos / 100)
            count_of_zero += add_count_of_zero
        newpos = (newpos % 100 + 100) % 100
        curr = newpos
    return count_of_zero


def create_dial():
    dial = []
    for x in range(0, 100):
        dial.append(x)

    return dial


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
    dial = create_dial()
    actual_result = run_dial(dial, parse_file(read_file(inputfile)), 50)

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):

    actual_result = run_dial_2(parse_file(read_file(inputfile)), 50)

    parse_result(actual_result, expected_result_2, inputfile)

if __name__ == "__main__":
    for inputfile in (
        ("example", 3, 6),
        ("input", 1007, 5820),
    ):
        main1(*inputfile)
        main2(*inputfile)
