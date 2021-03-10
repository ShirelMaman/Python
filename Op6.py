def MaxDay():
    # The day the highest number of messages was received
    f = open("mbox.txt")
    list_of_max = dict()
    for line in f:

        words = line.split()
        if len(words) == 0: continue

        if words[0] == 'From':
            list_of_max[words[2]] = list_of_max.get(words[2], 0) + 1

    return max(zip(list_of_max.values(), list_of_max.keys()))


MaxDay()
