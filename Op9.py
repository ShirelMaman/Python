import re


def AverageXDC():
    # Average confidence values X-DSPAM.
    f = open("mbox.txt")

    counter = 0
    num = 0.0

    for line in f:

        line = line.rstrip()
        extractor = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)  # Regular expression
        if len(extractor) != 1: continue
        num += float(extractor[0])
        counter += 1

    return num / counter


AverageXDC()
