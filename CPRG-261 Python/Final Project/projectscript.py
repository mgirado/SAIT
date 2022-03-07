# Final Project - CPRG 261
# April 19, 2021
# Matthew Girado

# Import modules
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from collections import Counter
import tkinter as tk
import os
import platform
import re
import sys
import configparser
import time

# Note: Anything with a format of print("...", file=somefile)
# just outputs that data to whatever desired file, multiple occurances throughout the script.
config = configparser.ConfigParser()  # Shortened version of call
try:  # Try to read project.ini
    config.read("project.ini")
    print("Opened project.ini file")
except FileNotFoundError:  # Except if the file wasn't found, halt script and print to console and inform user.
    print('Could not find "project.ini" file, stopping script')
    sys.exit(0)
c = config["GENERAL"]  # Shortened version of another call for ease of use.
home_dir = str(Path.home())  # Get current user's home directory.
if (
    c["directory"] == "default"
):  # Checks to see if config has default directory set or not.
    dir = home_dir
else:  # Otherwise use whatever directory is assigned.
    dir = c["directory"]


def get_time():  # Function for getting and formatting date/time.
    get_time = (
        datetime.now()
    )  # Get's current time local to the machine using datetime module.
    current_time = get_time.strftime(
        "%m-%d-%Y"
    )  # Formats output of current time to MM-DD-YYYY
    return current_time  # Return the value.


def create_folder(dir):  # Function for creating a directory.
    folder = (
        dir + "/pyscript_" + get_time()
    )  # Append foldername/date to desired directory location.
    # Try to make the directory, except if the folder already exists the script will be stopped.
    try:
        os.mkdir(folder)
    except FileExistsError:
        print(folder + " already exists, stopping script.")
        sys.exit(0)
    return folder  # Return folder path.


def create_file(fname):  # Function for creating file(s).
    # Try to create the file, except if the file already exists the script will be stopped.
    try:
        file = open(fname, "w")
    except FileExistsError:
        print("File already exists, stopping script.")
        sys.exit(0)
    return file  # Return file object.


def get_cpu_inforaw():  # Function for outputting raw /proc/cpuinfo data to data file.
    os.system("cat /proc/cpuinfo >> " + datafile_path)


def get_cpu_info():  # Function that tries to read /proc/cpuinfo and outputs it to a file if successful.
    cpu_info = [
        "processor",
        "vendor_id",
        "model",
        "model name",
        "cache size",
    ]  # List of desired items to be pulled from data.
    # Try to open and read file, except if the file isn't found, stop the script.
    try:
        print("Opening /proc/cpuinfo file", file=data_file)
        info_file = open(datafile_path, "r")
        print(
            "Successfully opened /proc/cpuinfo file, printing to output_file.txt.",
            file=data_file,
        )
    except FileNotFoundError:
        print('Could not find "/proc/cpuinfo" file, script stopped.', file=data_file)
        sys.exit(0)
    print("\nPrinting details about machine's CPU info below.\n", file=output_file)
    info_lines = info_file.readlines()
    for (
        info
    ) in (
        cpu_info
    ):  # Parses through all the data and uses regex to compare then take desired data and output it to output file.
        for line in info_lines:
            if re.search(info, line):
                print(line, file=output_file)
                break
    print(
        "Printed data from data_file.txt to output_file.txt.",
        file=data_file,
    )


def delete_files():  # Function for deleting files in desired directory.
    root = tk.Tk()  # Shortened version of call.
    root.withdraw()  # Hides root window.
    messagebox.showwarning(  # Warn the user about usage of this script.
        "projectscript.py",
        "Please becareful with where you decide to delete files from, by continuing you acknowledge the risks and assume all responsibility.",
    )
    answer = messagebox.askyesno(  # Asks user if they are sure they want to continue.
        "projectscript.py", "Are you sure you want to continue?"
    )
    # If they said yes, answer is true and script continues. if they said no, returns to while loop.
    if answer is True:
        print("Select a directory to delete files from: ")
        dir_path = filedialog.askdirectory()  # Gets directory that the user selected.
        answer2 = messagebox.askyesno(  # Confirms with user if directory location is what they desired.
            "projectscript.py", "Is this directory location correct? " + dir_path
        )
        if answer2 is True:  # If they answered yes the script continues.
            current_time = time.time()  # Assigns variable to current time
            print("\nAttempting to delete files.\n")
            # For loop parses through all the files in the directory,
            # then checks if they are older than the min_age in the config and is a file,
            # if conditions are met, deletes the files. If no files are found or are not older than the min_age then,
            # the for loop prints appropriate information and breaks the loop and returns to menu.
            for del_file in os.listdir(dir_path):
                full_path = os.path.join(dir_path, del_file)
                days = int(c["min_age"])
                if os.stat(full_path).st_mtime < (
                    (current_time) - (days * 86400)
                ) and os.path.isfile(full_path):
                    print("Removed: " + full_path)
                    print("Deleted: " + full_path, file=output_file)
                    print("Deleted: " + full_path, file=data_file)
                    os.remove(full_path)
                else:
                    nofile_string = (
                        "Could not find any files older than "
                        + str(days)
                        + " day(s).\n"
                    )
                    print(nofile_string)
                    print(nofile_string, file=data_file)
                    print(
                        "\nNo files were found that exceeded the minimum age("
                        + str(days)
                        + ") in days required for deletion.\n",
                        file=output_file,
                    )
                    break
        else:
            print("Incorrect path chosen, returning to menu.")
    else:  # If they said no whenever they got prompted, they return to menu.
        print("User selected no, returning to menu.")


# Function that counts all instances of the alphabet and then prints that information to output file.
def countdata(sort, max_output):
    count_dict = {}  # Create dictionary
    # Create lists
    char_list = []
    sorted_dict = []
    with open(
        datafile_path
    ) as x:  # Open file as x var and then loop through and take each character as lowercase.
        for line in x:
            for char in line:
                char_list.append(char.lower())
    count = Counter(
        char_list
    )  # Use the counter module to count all instances and assign it to a variable.
    # For loop adds all alphabets and their counts to the count_dict dictionary.
    for alphabet in "abcdefghijklmnopqrstuvwxyz":
        count_dict.update({alphabet: count[alphabet]})
    # If/else statements check for what "sort" was in config and sorts the arrays accordingly.
    if sort == "alphabetical":
        for (
            key,
            value,
        ) in (
            count_dict.items()
        ):  # Sorts everything alphabetically and assigns it to a list.
            temp_list = [key, value]
            sorted_dict.append(temp_list)
    elif sort == "descending":
        # Sorts everything in descending order and assigns it to a list.
        sorted_dict = sorted(count_dict.items(), reverse=True, key=lambda i: i[1])
    elif sort == "ascending":
        # Sorts everything in ascending order and assigns it to a list.
        sorted_dict = sorted(count_dict.items(), key=lambda i: i[1])
    else:  # If it's none of the above options then user went out of scope and we inform the user and return to menu.
        print('Invalid setting selected for "sort" setting in project.ini.')
    out_file = open(
        outputfile_path, "a"
    )  # Opens output file to append data to it and assigns it to a variable.
    print(
        "Displaying occurances of alphabet in data_file.txt in " + sort + " order.",
        file=out_file,
    )
    print("Max number of output values selected: " + max_output + "\n", file=out_file)
    for f in range(
        int(max_output)
    ):  # for loop parses through the list until it reaches max_output allowed
        if f < 26:
            print(sorted_dict[f], file=out_file)
        else:  # Just in case user tries to give a max_output of more than 26.
            break  # Stops the loop
    print(
        "Finished counting occurances of certain alphabets in "
        + datafile_path
        + ". Outputted a maximum of "
        + max_output
        + " values."
    )
    out_file.close()  # Close file that was opened for appending.


def headers():  # Function for printing headings(username/date)
    print("Script ran by: " + os.getlogin(), file=output_file)
    print("Date: " + str(get_time()), file=output_file)
    print("\n", file=output_file)


fdir = create_folder(dir)  # Creates the folder to house all data/output.
# Appends filenames to directory and assigns them to variables.
datafile_path = fdir + "/" + c["data_file"]
outputfile_path = fdir + "/" + c["output_file"]

data_file = create_file(datafile_path)  # Create data file.
while (
    True
):  # Menu loop that lets user select specified options and stop the script if user hits enter with no input.
    print("\n1 = Create data file.")
    print("2 = Delete files in a directory and generate output file.")
    print("3 = Count occurances of certain alphabets in data file.")
    user_input = input(
        "\nInput desired integer as selection or leave empty to stop script: "
    )
    if (
        user_input == "1"
    ):  # Calls functions for outputting raw cpu info data and creates data file.
        print("Selected Option 1.\n")
        get_cpu_inforaw()
        with open(datafile_path) as x:
            num_lines = sum(1 for _ in x)
        print(
            "Total number of lines written: " + str(num_lines)
        )  # Tells user number of lines written.
    elif (
        user_input == "2"
    ):  # Calls functions for creating output file and also allows user to select a directory to delete folders from.
        print("Selected Option 2.\n")
        output_file = create_file(outputfile_path)  # Create output file
        headers()  # Print headings
        delete_files()  # Calls delete files function
        get_cpu_info()  # Calls cpu info function that takes data from data file and outputs a filtered/formatted version to output file.
        messagebox.showwarning(
            "projectscript.py",  # Shows user what was just printed to the output file.
            "Printing how much data was written to console after this prompt.",
        )
        output_file.close()  # Close file
        file_size = Path(outputfile_path).stat().st_size  # Gets size of file
        print(
            "\nFile size of " + outputfile_path + ": " + str(file_size) + " Bytes."
        )  # Tells user size of file.
    elif (
        user_input == "3"
    ):  # Counts data and calls function, uses config file settings appropriately.
        print("Selected Option 3.\n")
        countdata(c["sort"], c["max_output"])
    elif (
        user_input == ""
    ):  # If user input is empty, stops the script and informs on terminal and data/log file.
        print("\nUser chose to stop script, stopping script.")
        os.system(
            "echo User chose to stop script, script halted at this point. >> "
            + datafile_path
        )
        break
    else:
        print(
            "Not a valid selection, please try again"
        )  # If it's anything except the other options tells user it wasn't a valid selection.

# Tries to close files if they're still open then stop the script, catches exception if they are already closed and stops the script.
try:
    data_file.close()
    output_file.close()
    sys.exit(0)
except NameError:
    sys.exit(0)
