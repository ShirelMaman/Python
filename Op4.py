def MaxDomain():
    # Returns a domain from which the largest number of messages were sent
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

    max_domain = max(list_of_domain.values())

    for i, j in list_of_domain.items():  # Find tje maximum value
        if max_domain == j:
            max_domain_value = i

    return "The domain from which the most messages were sent", max_domain_value


MaxDomain()
