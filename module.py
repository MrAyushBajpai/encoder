# Importing Necessary Libraries
import os
import datetime
import configparser

# Setting up the configuration file processor
configparser = configparser.ConfigParser()
configfilepath = 'parameters.cfg'
configparser.read(configfilepath)

# Defining Necessary Variables
historyfile = str(configparser.get('history-parameter', 'history-file'))
logfile = str(configparser.get('log-parameter', 'log-file'))


# Function for keeping logs, in case something goes off hand
def logcat(event, iserror):
    if str(configparser.get('log-parameter', 'keep-log')) == 'True':
        now = datetime.datetime.now()
        current = now.strftime('[%d-%m-%Y||%H:%M:%S]')
        if iserror:
            logs = open(logfile, 'a+')
            logs.seek(0)
            data = logs.read(100)
            if len(data) > 0:
                logs.write('\n')
            logs.write('!@' + current + '--' + event)
            logs.close()
        else:
            logs = open(logfile, 'a+')
            logs.seek(0)
            data = logs.read(100)
            if len(data) > 0:
                logs.write('\n')
            logs.write(current + '--' + event)
            logs.close()
    else:
        pass


def checkindex(key, index):
    if 97 <= ord(key[index]) < 109:
        set1 = True
    elif 109 <= ord(key[index]) < 122:
        set1 = False
    elif 65 <= ord(key[index]) < 77:
        set1 = False
    elif 77 <= ord(key[index]) < 90:
        set1 = True
    elif 48 <= ord(key[index]) < 53:
        set1 = True
    elif 53 <= ord(key[index]) < 57:
        set1 = False
    else:
        set1 = True
    return set1


# Function to encode the data
def encoder(data, key):
    logcat('Received ' + data + ' as the input to be process at the encoder', False)
    try:
        keysum = 0
        for v in key:
            keysum += ord(v)
        keysum //= len(key)
        a = ''
        if checkindex(key, 0):
            for i in data:
                a += chr((ord(i) + int(keysum)) % 127)
        else:
            for i in data:
                a += chr((ord(i) - int(keysum)) % 127)
        logcat('Outputing ' + a + ' as the processed output from the encoder', False)
        return a
    except TypeError:
        errorhandler(3)


# Function to Decode the data
def decoder(data, key):
    logcat('Received ' + data + ' as the input to be process at the decoder', False)
    try:
        keysum = 0
        for v in key:
            keysum += ord(v)
        keysum //= len(key)
        a = ''
        if checkindex(key, 0):
            for i in data:
                a += chr((ord(i) - int(keysum)) % 127)
        else:
            for i in data:
                a += chr((ord(i) + int(keysum)) % 127)
        logcat('Outputing ' + a + ' as the processed output from the decoder', False)
        return a
    except TypeError:
        errorhandler(3)


# Function to check if the file exists and if it is empty or not
def filecheck(path):
    # Checking if file exists at the given path
    logcat('Doing a filecheck on ' + path, False)
    try:
        if os.path.exists(path):
            # Checking if the file size is 0, meaning its empty
            if os.path.getsize(path) > 0:
                toreturn = True
            else:
                toreturn = False
        else:
            toreturn = False
        logcat('Outputing ' + str(toreturn) + ' in the file filecheck on path' + path, False)
        return toreturn
    except TypeError:
        errorhandler(3)
        return False


# Function to clear the screen
def clear():
    # Check the OS, and runs the command accordingly
    if os.name == 'nt':
        # Windows
        _ = os.system('cls')
    else:
        # Linux and Mac, and other similar dependancies
        _ = os.system('clear')


# Function to write history to the history file
def writehis(historytext, towrite, origin):
    if towrite:
        fhistory = open(historyfile, 'a')
        fhistory.write('Source - ' + origin + '-- ' + historytext)
        fhistory.write('\n')
        fhistory.close()

    else:
        pass


# Function to clear specific history
def clearhistory():
    fhistory = open(historyfile, 'w')
    fhistory.truncate(0)
    fhistory.close()
    print('Cleared History Successfully!')
    logcat('Cleared History', False)


# Function to Load specific History and print it
def loadhistory():
    # Checking if the requested history is from Encoder or Decoder
    # Doing a filecheck to check if the history file does not exist or the history file is empty
    if filecheck(historyfile):
        ln_history = open(historyfile, 'r')
        print("Loading History.")
        print('\n')
        for item in ln_history:
            print(item)
    else:
        print("There is no history.")

    logcat('Loaded History', False)


# Function to clear log
def clearlog():
    log = open(logfile, 'w')
    log.truncate(0)
    log.close()
    print('Cleared Logs Successfully.')


# Function for handling errors
def errorhandler(errorcode, optionalspecs=''):
    # When no error is present
    if errorcode == 0:
        return 0

    # If the user specified command is not found
    elif errorcode == 1:
        logcat('Error Code: 1: Command Not Found! Command Entered was: "' + optionalspecs + '"', True)

    # If the user specified process is not found
    elif errorcode == 2:
        logcat('Error Code: 2: Process Not Found! Process Entered was: "' + optionalspecs + '"', True)

    # Internal Issue: When a TypeError Occurs
    elif errorcode == 3:
        logcat('Error Code: 3: Internal Program Issues: TypeError!', True)


# Function for checking if the log size is higher than 2 Mb
def logsize():
    if os.stat(logfile).st_size > 2097152:
        clearlog()
        logcat('Flushed the logfile because size exceeded: 2097152 Bytes', False)


def logerror():
    a = False
    log = open(logfile, 'r')
    for n in log:
        if n[0:2] == '!@':
            print(n)
            a = True
        else:
            continue
    if not a:
        print("No Errors found in the logfile! Great!")
    log.close()


# If the user enters a command, this will be used to check the command
def commander(text):
    try:
        text = list(text)
        text.remove('c')
        text.remove('m')
        text.remove('d')
        while ' ' in text:
            text.remove(' ')
        text = ''.join(text)
        if text.lower() == 'exit' or text.lower() == 'close':
            return 'exit'
        elif text.lower() == 'clear/h' or text.lower() == 'clear/history':
            return 'clearhistory'
        elif text.lower() == 'history' or text.lower() == 'show/h' or text.lower() == 'show/history':
            return 'showhistory'
        elif text.lower() == 'clear/a' or text.lower() == 'clear/all':
            return 'clearall'
        elif text.lower() == 'cls' or text.lower() == 'clear':
            return 'clearscreeen'
        elif text.lower() == 'clear/logs' or text.lower() == 'clear/l':
            return 'clearlog'
        elif text.lower() == 'errors' or text.lower() == 'show/errors' or text.lower() == 'show/e':
            return 'logerrors'
        else:
            return text
    except TypeError:
        errorhandler(3)


# Function to remove 'n' number of items from the start of text
def cleaner(text, toclean):
    try:
        text = list(text)
        logcat('Cleaned ' + ''.join(text[0:toclean]) + ' from ' + ''.join(text), False)
        del text[0:toclean]
        if len(text) > 0 and text[0] == ' ':
            del text[0]
        text = ''.join(text)
        return text
    except TypeError:
        errorhandler(3)
        return ''
