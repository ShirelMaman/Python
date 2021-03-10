import re


def Modified():
    # List all modified and their quantity
    f = open("mbox.txt")

    list_of_modified = dict()

    num = 0

    for line in f:

        line = line.rstrip()
        words = line.split()

        if len(words) == 0: continue

        if words[0] == 'Log:':  # To ignore the line that start with Log
            num = 0

        if num == 1:
            pattern = r"/"
            y = re.split(pattern, line)  # Eliminates all "/" from the line
            list_of_modified[y[-1]] = list_of_modified.get(y[-1], 0) + 1  # get in to dictionary

        if words[0] == 'Modified:':  # Work only with this lines
            num = 1

    return list_of_modified


Modified()
