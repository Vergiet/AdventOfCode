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



def main1(inputfile, expected_result_1=0, expected_result_2=0):
    print(read_file(inputfile))
    actual_result = 0


    parse_result(actual_result, expected_result_1, inputfile)



def main2(inputfile, expected_result_1=0, expected_result_2=0):
    actual_result = 0
    

    parse_result(actual_result, expected_result_2, inputfile)









if __name__=="__main__":
    for inputfile in (
        ("example", 0, 0), 
        ("input", 0, 0),
    ):
        main1(inputfile)
        main2(inputfile)
    