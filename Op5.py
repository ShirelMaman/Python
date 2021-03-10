def AuthorInformation():
    # Message details (month, day, year)
    f = open("mbox.txt")

    date = ""

    for line in f:

        words = line.split()
        if len(words) == 0: continue

        if words[0] == 'From':
            date += str(words[2:])

    return date


AuthorInformation()
