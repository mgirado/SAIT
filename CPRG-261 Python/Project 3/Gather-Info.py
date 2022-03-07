# Gather-Info.py
# 2021 - 02 - 01, Updated 2021 - 03 - 31
# Matthew Girado
# Project 3 - CPRG 261

# Import Modules
import os
import re
import socket
import sys


# Assign filenames to temporary files.

PASSWD_FILENAME = "passwd_output.txt"
GROUP_FILENAME = "group_output.txt"
SERVICES_FILENAME = "services_output.txt"

current_user = (
    os.getlogin()
)  # Get current user on the machine, used for creating a directory.

temp_folder = (
    "/home/" + current_user + "/cronscript/"
)  # Assigns desired directory for output.
os.mkdir(temp_folder)  # Uses os module to create the directory.


desired_name = "output.txt"

master_file = os.path.join(
    temp_folder, desired_name
)  # Combines desired output directory & filename.
master_output = open(
    master_file, "w"
)  # Creates and opens a new file at desired directory.


def print_hostname():  # Function that gets and prints machine name/hostname to a file.
    print("Machine name/Hostname: " + socket.gethostname(), file=master_output)


def get_cpu_info():  # Function that tries to read /proc/cpuinfo and output it to a file if successful.
    cpu_info = ["processor", "vendor_id", "model", "model name", "cache size"]
    try:
        info_file = open("/proc/cpuinfo", "r")
    except FileNotFoundError:
        print(
            'Could not find "/proc/cpuinfo" file, stopping script.', file=master_output
        )
        sys.exit(0)
    info_lines = info_file.readlines()

    for info in cpu_info:
        for line in info_lines:
            if re.search(info, line):
                print(line, file=master_output)
                break


print("")  # Empty line
print_hostname()  # Calling function to get & print hostname
print("\nPrinting processor info from /proc/cpuinfo\n", file=master_output)
get_cpu_info()  # Calling function to read /proc/cpuinfo and send output to file at master_output.

print("\nPrinting users and their associated groups below: \n", file=master_output)
# Outputs said string to file at master_output.

temp_passwd = os.path.join(temp_folder, PASSWD_FILENAME)
os.system("getent passwd > " + temp_passwd)
try:
    passwd_file = open(temp_passwd, "r")
except FileNotFoundError:
    print('Could not find "' + temp_passwd + '", stopping script.', file=master_output)
    sys.exit(0)
user_info = passwd_file.readlines()
# Code uses getent command in linux to take passwd file info and output it to a file.

count_user = len(user_info)  # Counts number of lines to use in for loops.

# Assign empty lists to be used for data later.
user_lines = []
user_names = []
group_names = []
group_ids = []

# For loop parses through passwd info and takes usernames and group IDs and appends them to lists.
for x in range(count_user):
    user_names.append(user_info[x].split(":")[0])
    group_ids.append(user_info[x].split(":")[3])

# Used for creating a file in the directory we created earlier.
temp_group = os.path.join(temp_folder, GROUP_FILENAME)

# For loop uses getent group command to get more detailed info on groups and redirects output to a file.
for z in range(count_user):
    os.system("getent group " + group_ids[z] + " >> " + temp_group)

# Opens file and reads it, also checks if file exists.
try:
    group_file = open(temp_group, "r")
except FileNotFoundError:
    print('Could not find "' + temp_group + '", stopping script.')
    sys.exit(0)
group_info = group_file.readlines()

# Used for counting lines of file to be used in for loops.
count_group = len(group_info)

# For loop parses through file and takes group name and appends it to a list.
for y in range(count_group):
    group_names.append(group_info[y].split(":")[0])

# For loop outputs user and group info in the format of "User: (username), Associated Group: (group name)"
# and sends it to file at master_output.
for n in range(count_group):
    print(
        "User: " + user_names[n] + ", Associated Group: " + group_names[n],
        file=master_output,
    )

# Outputs string to file at master_output.
print("\nPrinting services and their status.\n", file=master_output)

# Desired location and file name gets assigned to services_list.
services_list = os.path.join(temp_folder, SERVICES_FILENAME)

# Uses linux command that lists services and status and writes it to file at services_list.
os.system("systemctl list-unit-files --type service > " + services_list)

# Tries to open file at services_list, otherwise prints to file that it could not be found.
try:
    services_file = open(services_list, "r")
except FileNotFoundError:
    print(
        'Could not find "' + services_list + '", stopping script.', file=master_output
    )

# Reads from file and assigns it to a variable.
services_info = services_file.read()

# Sends output of services file to the master output file.
print(services_info, file=master_output)

# Closes files.
group_file.close()
passwd_file.close()
services_file.close()
master_output.close()

# Can uncomment these next 3 lines of code if user decides they do not want to keep the temporary files.
os.remove(temp_passwd)
os.remove(temp_group)
os.remove(services_list)

print("Script successfully run")