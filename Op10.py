import re


def AverageNewR():
    # Average New Revision values
    f = open("mbox.txt")

    counter = 0
    num = 0.0

    for line in f:
        line = line.rstrip()
        extractor = re.findall('^New Revision: (\d+)', line)  # Regular expression
        if len(extractor) != 1: continue
        num += float(extractor[0])
        counter += 1

    return num / counter


AverageNewR()
