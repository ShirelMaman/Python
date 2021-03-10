def GetMessage():
    # Returns the number of messages

    f = open("mbox.txt")

    counter = 0
    for line in f:

        words = line.split()
        if len(words) == 0: continue
        if words[0] == 'From':
            counter += 1

    return "Number of inbox messages", counter


GetMessage()
