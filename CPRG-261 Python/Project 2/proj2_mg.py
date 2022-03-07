# Matthew Girado
# March 9, 2021
# Project 2 - CPRG 261

import win32api  # Use win32api to get time/hostname/username.
import win32file  # Use win32file for making a directory/file handling.
import win32evtlog  # Use win32evtlog to export event viewer log files to a directory for quick retrieval.
import win32net  # Use win32net to get a quick summary of current user's information.
import servicemanager  # Use servicemanager to log a message in the event viewer for verification purposes.

print(
    "\nREMINDER: Script must be run as administrator, needs permission to export event viewer files."
)


def get_hostname():
    return win32api.GetComputerName()


def get_username():
    return win32api.GetUserName()


def get_userinfo():
    print(win32net.NetUserGetInfo(get_hostname(), get_username(), 1))


# Refer to http://timgolden.me.uk/pywin32-docs/PyUSER_INFO_1003.html for information on parameter 3 on information levels. Some information may seem to be missing but it really is that way.

raw_time = win32api.GetLocalTime()
formatted_time = (
    str(raw_time[0])  # Year
    + "-"
    + str(raw_time[1])  # Month
    + "-"
    + str(raw_time[3])  # Day (Not shown is #2, is for day of week)
    + "-"
    + str(raw_time[4])  # Hour (24 Hr format)
    + "-"
    + str(raw_time[5])  # Minute
    + "-"
    + str(raw_time[6])  # Second
)
# Time gets printed in YYYY-MM-DD-HH-MM-SS/YYYY-M-D-H-M-S formats, or a combination of sorts, double digits get reduced to single digits where possible.

# Assign variable the absolute path of the directory that gets created.
directory = (
    "C:/Users/"
    + get_username()  # Call function for username
    + "/Documents/"
    + get_hostname()  # Call function for hostname
    + "_"
    + formatted_time  # Append date/time
    + "_pyscript"
)


def create_directory():  # Function that creates a directory in the documents folder of current user, folder is prefixed with machine hostname and date/time.
    win32file.CreateDirectory(
        directory,
        None,
    )
    print("\nCreating directory with this absolute path: " + directory)


def export_logs():
    servicemanager.LogInfoMsg(
        "proj2_mg.py script ran, this message is here for verification purposes."
    )  # Logs a message to the event viewer, can be used to verify if log files get updated correctly.

    log_filenames = [
        "Application",
        "Security",
        "System",
    ]  # List of filenames that we want to take.
    for x in range(
        len(log_filenames)
    ):  # Uses length of list as a count and then parses through the list and uses those filenames to export desired files.
        filename = log_filenames[x]
        win32evtlog.EvtExportLog(  # Use of API for actual exporting
            "C:/Windows/System32/winevt/Logs/" + filename + ".evtx",
            directory + "/" + filename + ".evtx",
            2,
        )
    print(  # Tell user files were successfully exported to desired directory.
        "\nEvent viewer files successfully exported to this directory: C:/Users/"
        + get_username()
        + "/Documents/"
        + get_hostname()
        + "_"
        + formatted_time
        + "_pyscript"
    )


# Function uses win32evtlog to export .evtx event log files to a directory.

print(
    "\nMachine Hostname: " + get_hostname()
)  # Retrieves machine hostname and prints in terminal.
print(
    "\nCurrently logged in as user: " + get_username()
)  # Retrieves current user and prints in terminal.

print(
    "\nPrinting summary of " + get_username() + " information: "
)  # Uses get_username() function again and also uses get_userinfo()
print(get_userinfo())  # function to print summary of details on current user.

print(
    "\nWill be attempting to export Application.evtx, Security.evtx, and System.evtx event viewer files."
)

create_directory()  # Creates directory at desired location that later gets used to store exported files.
try:
    export_logs()  # Attempts to export logs if the script was run with appropriate permissions.
except win32evtlog.error:  # If unsuccessful and is the cause of a win32evtlog.error which would most likely be due to a permissions error, it will inform user.
    print(
        "\nwin32evtlog module had an error, most likely cause: Script was not run as administrator, lacks the proper permissions, could not export event viewer files, exiting script, please make sure you're running script as administrator. If already doing so, please check comment on line 153 of code."
    )
    # If still getting this error message, adjust code accordingly to get rid of the exception handling and run again to double check what win32evtlog error said.