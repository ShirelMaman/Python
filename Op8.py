def MaxHour():
    # The time which appeared the most times
    f = open("mbox.txt")
    list_of_max = dict()

    for line in f:

        words = line.split()
        if len(words) == 0: continue

        if words[0] == 'From':
            list_of_max[words[5]] = list_of_max.get(words[5], 0) + 1

    return max(zip(list_of_max.values(), list_of_max.keys()))


MaxHour()
