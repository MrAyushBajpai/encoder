# Importing Necessary Libraries
import os
import datetime
import time

# Defining Necessary Variables
historyfile = 'historyfile'
logfile = 'logfile'


# Fucntion to encrypt the data
def encrypt(msg, key):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)


# Function to Decrypt the Data
def decrypt(enc, key):
    msg = []
    for i, c in enumerate(enc):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)


# Function to check if the file exists and if it is empty or not
def filecheck(path, origin):
    # Checking if file exists at the given path
    logcat('Doing a filecheck on ' + path, origin, False)
    if os.path.exists(path):
        # Checking if the file size is 0, meaning its empty
        if os.path.getsize(path) > 0:
            toreturn = True
        else:
            toreturn = False
    else:
        toreturn = False
    logcat('Outputing ' + str(toreturn) + ' in the file filecheck on path' + path, origin, False)
    return toreturn


# Function to clear the screen
def clear():
    # Check the OS, and runs the command accordingly
    if os.name == 'nt':
        # Windows
        _ = os.system('cls')
    else:
        # Linux and Mac, and other similar dependancies
        _ = os.system('clear')


# Function to write history to their specific history files
def writehis(historytext, origin, towrite):
    if towrite:
        fhistory = open(historyfile, 'a')
        if origin == 'ncode':
            fhistory.write('Encode - ' + historytext)
            fhistory.write('\n')
            fhistory.close()
        elif origin == 'dcode':
            fhistory.write('Decode - ' + historytext)
            fhistory.write('\n')
            fhistory.close()
        elif origin != 'dcode' or origin != 'ncode':
            errorhandler(1, origin)
    else:
        pass


# Function to clear specific history
def clearhistory(origin):
    fhistory = open(historyfile, 'w')
    fhistory.truncate(0)
    fhistory.close()

    logcat('Cleared History', origin, False)


# Function to Load specific History and print it
def loadhistory(origin):
    # Doing a filecheck to check if the history file does not exist or the history file is empty
    if filecheck(historyfile, 'ncode'):
        fhistory = open(historyfile, 'r')
        print("Loading History!")
        print('\n')
        for item in fhistory:
            print(item)
    else:
        print("There is no history for encoder")

    logcat('Loaded History', origin, False)


# Function for keeping basic log in case of failure
def logcat(event, origin, iserror):
    now = datetime.datetime.now()
    current = now.strftime('[%d-%m-%Y||%H:%M:%S]')
    if iserror:
        logs = open(logfile, 'a+')
        logs.seek(0)
        data = logs.read(100)
        if len(data) > 0:
            logs.write('\n')
        logs.write('!@' + current + '--' + origin + '--' + event)
        logs.close()
    else:
        logs = open(logfile, 'a+')
        logs.seek(0)
        data = logs.read(100)
        if len(data) > 0:
            logs.write('\n')
        logs.write(current + '--' + origin + '-- ' + event)
        logs.close()


# Function to clear log
def clearlog():
    log = open(logfile, 'w')
    log.truncate(0)
    log.close()


# Function for handling errors
def errorhandler(errorcode, origin):
    # When no error is present
    if errorcode == 0:
        return 0

    # Used to end the program
    elif errorcode == 0.5:
        return 0.5

    # When there is a problem while defining the source, when calling a function
    elif errorcode == 1:
        logcat('Error on defining the source. CODE-1', origin, True)

    # If the main loop breaks unintenionally
    elif errorcode == 2:
        logcat('Unintentional Exit. Loop was broken. Error Code-2', origin, True)

    # In case of errors, let the user know there's an error, and then end the program
    if errorcode != 0 or errorcode != 0.5:
        print('System Encounterd an error. Error Code-' + errorcode + '. Please refer to the logfile for more info.')
        time.sleep(5)
        return 1


# Function for checking if the log size is higher than 2 Mb
def logsize():
    if os.stat(logfile).st_size > 2097152:
        clearlog()
