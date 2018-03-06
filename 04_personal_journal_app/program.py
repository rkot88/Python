import journal


# from journal /import load, save less explicit you can use only function names and it works
# from journal * /even less explicit better dont use it you can run into the possibility if name clashes


def main():
    print_header()
    run_event_loop()


def print_header():
    print("--------------------")
    print("-----JOURNAL--------")
    print("--------------------")


def run_event_loop():
    print("what do you want do do with your journal? ")
    cmd = "EMPTY"
    journal_name = "default"
    journal_data = journal.load(journal_name)  # []  # or list()

    while cmd != "x" and cmd:
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: ")
        cmd = cmd.lower().strip()  # to prevent errors when using uppercase or lowercase input or with space eg. _l

        if cmd == "l":
            list_entries(journal_data)
        elif cmd == "a":
            add_entry(journal_data)
        elif cmd != "x" and cmd:
            print("sorry, we don't understand '{}'.".format(cmd))

    print("Done goodbye.")
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Your journal entries:")
    entries = reversed(data)  # created to reverse the collection to see newest entries first in console
    for idx, entry in enumerate(entries):
        # for in loop to work with COLLECTIONs and loops
        # USE enumerate not for loops to pair entry items with indexes :D /
        # tuples - (PL krotki) (n - elements) python will take those two items from the tuple and assign them to idx and entry variable
        # after pairing entry with index by enumerate python now that id is first and its assigning it to idx variable etc
        print("* [{}], {}".format(idx + 1, entry))


def add_entry(data):
    text = input("Type your entry <enter> to exit ")
    journal.add_entry(text, data)
    # data.append(text)


#print("__file__ " + __file__)
#print("__name__ " + __name__)

#if __name__ == " __main__": # if the program is executed right now kick off the main()
if __name__ == "__main__":
    main()


# main()  # main call must be at the bottom after declaration of all functions to run properly
