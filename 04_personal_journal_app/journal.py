"""
This is journal module

"""
import os


def load(name):
    """
    This method creates and load a new journal.

    :param name: this base name of the journal to load
    :return: a new journal data structure populated with the file data
    """
    data = []  # create empty journal
    filename = get_full_path_name(name)  # then we get filename

    if os.path.exists(filename):  # if it exist load it using simple format of one entry per line
        with open(filename) as fin:  # fin - file input
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    # base+dir = "~/myworkingfolder"
    # rel_dir = "data/temp.txt"
    #
    # full_file = base_dir + "/" + rel_dir

    filename = get_full_path_name(name)
    print(".....saving to: {}".format(filename))

    # fout = open(filename, "w")

    with open(filename, "w") as fout:  # fout - file output file stream # we create a writable file

        for entry in journal_data:  # and we just write out the format that we are expecting by for in loop
            fout.write(entry + "\n")

    # fout.close() - dont need with open as is closing automatically


def get_full_path_name(name):
    filename = os.path.abspath(os.path.join(".", "journals/", name + ".jrl"))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
