def AuthorMessage():
    # Sorted list of numbers messages that sent by the writer, from largest to smallest
    f = open("mbox.txt")
    new_f = open("Shirel&Matan.txt", "w")

    list_of_author = dict()

    for line in f:

        words = line.split()
        if len(words) == 0: continue
        if words[0] == 'Author:':
            list_of_author[words[1]] = list_of_author.get(words[1], 0) + 1

    sort_author = str(sorted(list_of_author.items(), reverse=True))  # Reverse sort
    new_f.write(sort_author)
    new_f.close()

    return "Authors information", sort_author


AuthorMessage()
