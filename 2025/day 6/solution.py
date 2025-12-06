import os


def read_file(file):
    filepath = os.path.join(os.path.split(__file__)[0], file)
    with open(filepath) as filepath:
        content = filepath.read()
        return content


def apply_operator(operator, a, b):
    switch = {
        "+": lambda a, b: a + b,
        "*": lambda a, b: a * b,
    }
    return switch[operator](a, b)


def print_line(input):
    list_of_list_of_vals = []
    for line in input.splitlines():
        # print(line)
        vals_on_line = []
        new_val = []
        for char in line:
            if char != " ":
                new_val.append(char)
            if char == " ":
                if len(new_val) > 0:
                    vals_on_line.append(new_val)
                new_val = []
        if len(new_val) > 0:
            vals_on_line.append(new_val)

        list_of_list_of_vals.append(vals_on_line)

    answer = 0
    math_problems = []
    for index_in_row in range(len(list_of_list_of_vals[0])):
        math_problem = []
        for row in list_of_list_of_vals:
            math_problem.append(row[index_in_row])
        math_problems.append(math_problem)
    for problem in math_problems:
        values = []
        for value_index in range(len(problem)):
            if problem[-1] != problem[value_index]:
                values.append(int("".join(problem[value_index])))
        operator = problem[-1][0]
        if operator == "+":
            temp = 0
        else:
            temp = 1

        for value in values:
            temp = apply_operator(operator, temp, value)
        answer = answer + temp

    return answer


def print_line_2(input):
    operators = []
    for line in input.splitlines():
        if line[0] == "+" or line[0] == "*":
            print(line)

            length = 0
            operator = ""
            for char in line:
                if char == " ":
                    length += 1
                else:
                    if operator != "":
                        operators.append((operator, length))
                        length = 1
                        operator = char
                    else:
                        operator = char
                        length += 1
            operators.append((operator, 0))

    list_of_list_of_vals = []
    for line in input.splitlines():
        new_val = []
        previous_index = 0
        for operator in operators:
            from_index = previous_index
            if operator[1] == 0:
                to_index = len(line)
            else:
                to_index = previous_index + operator[1]
            new_val.append(line[from_index:to_index])
            previous_index += operator[1]
        list_of_list_of_vals.append(new_val)

    answer = 0
    math_problems = []
    for index_in_row in range(len(list_of_list_of_vals[0])):
        math_problem = []
        for row in list_of_list_of_vals:
            math_problem.append(row[index_in_row])
        math_problems.append(math_problem)

    for problem in math_problems:
        horizontal_values = []
        for char_index in range(len(problem[0])):
            horizontal_value_chars = []
            for value_index in range(len(problem)):
                if problem[-1] != problem[value_index]:
                    value = problem[value_index]
                    char = value[char_index]
                    horizontal_value_chars.append(char)

            value = "".join(horizontal_value_chars)
            if len(value.strip()) > 0:
                horizontal_values.append(int(value))
        # print()
        operator = problem[-1][0]
        if operator == "+":
            temp = 0
        else:
            temp = 1

        for value in horizontal_values:
            temp = apply_operator(operator, temp, value)
        answer = answer + temp

    return answer


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
    actual_result = print_line(read_file(inputfile))
    # actual_result = 0

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    actual_result = print_line_2(read_file(inputfile))
    # actual_result = 0

    parse_result(actual_result, expected_result_2, inputfile)


if __name__ == "__main__":
    for inputfile in (
        # ("example", 4277556, 3263827),
        ("input", 5877594983578, 11159825706149),
    ):
        main1(*inputfile)
        main2(*inputfile)
