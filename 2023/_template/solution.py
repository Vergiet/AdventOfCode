import os

def read_file(file):
    filepath = os.path.join(os.path.split(__file__)[0], file)
    with open(filepath) as filepath:
        content = filepath.read()
        return content


def main1(inputfile):
    print(read_file(inputfile))



def main2(inputfile):
    pass









if __name__=="__main__":
    for inputfile in ("example", "input"):
        main1(inputfile)
        main2(inputfile)
    