import os
import platform
import subprocess
import cat_service


def main():
    # print the header
    print_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    print("Found or crated folder: " + folder)
    # download cats
    download_cats(folder)
    # display cats
    display_cats(folder)


def print_header():
    print("---------------------------")
    print("------cat factory----------")
    print("---------------------------")


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = "cat_pictures"
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creating new directory at {}".format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print("contacting server to download cats")
    cat_count = 8
    for i in range(1, cat_count + 1):
        # print(i, end = ", ")
        name = "lolcat_{}".format(i)
        print("Downloading cat " + name)
        cat_service.get_cat(folder, name)


def display_cats(folder):
    # open folder for different platforms
    print("Displaying cats i OS window")
    if platform.system() == "Darwin":
        subprocess.call(["open", folder])
    elif platform.system() == "Windows":
        subprocess.call(["explorer", folder])
    elif platform.system() == "Linux":
        subprocess.call(["xdg-open", folder])
    else:
        print("We don't support your os: " + platform.system())


if __name__ == "__main__":
    main()
