def DomainMessage():
    # Frequency of messages for each domain from which messages were sent
    f = open("mbox.txt")

    list_of_domain = dict()

    for line in f:

        words = line.split()
        if len(words) == 0: continue
        if words[0] != 'From': continue

        for i in range(len(words[1])):  # Eliminates "@" from the line
            if words[1][i] == "@":
                words1 = words[1][i + 1:]

        list_of_domain[words1] = list_of_domain.get(words1, 0) + 1

    return "Distribution of each Domain", list_of_domain


DomainMessage()
