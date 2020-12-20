# Importing Necessary Libraries
import os
import datetime
import time

# Defining Necessary Variables
keyphrase_ncode = {'a': 'm', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'q', 'j': 'o',
                   'k': 'p', 'l': 'a', 'm': 's', 'n': 'd', 'o': 'f', 'p': 'g', 'q': 'h', 'r': 'j', 's': 'k', 't': 'l',
                   'u': 'z', 'v': 'x', 'w': 'c', 'x': 'v', 'y': 'b', 'z': 'n',

                   'A': 'P', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'M', 'J': 'O',
                   'K': 'Q', 'L': 'A', 'M': 'S', 'N': 'D', 'O': 'F', 'P': 'G', 'Q': 'H', 'R': 'J', 'S': 'K', 'T': 'L',
                   'U': 'Z', 'V': 'X', 'W': 'C', 'X': 'V', 'Y': 'B', 'Z': 'N',

                   '1': '*', '2': '@', '3': '$', '4': '#', '5': '%', '6': '!', '7': '&', '8': '^', '9': '(', '0': ')',

                   '!': '5', '@': '7', '#': '1', '$': '4', '%': '3', '^': '6', '&': '9', '*': '8', '(': '0', ')': '2',

                   '`': '~', '~': '`', '[': '}', ']': '{', '}': '[', '{': ']', '-': '+', '_': '=', '=': '-', '+': '-',
                   '\'': '\"', '\"': '\'', '.': '?', '?': '.', ',': '/', '/': ',', '<': '>', '>': '<', ':': ';',
                   ';': ':', '|': '\\', '\\': '|',

                   ' ': ' '
                   }
keyphrase_dcode = dict([(value, key) for key, value in keyphrase_ncode.items()])
ncode_history = 'History/ncode_history.txt'
dcode_history = 'History/dcode_history.txt'
logfile = 'History/log.txt'


# Function to encode the data
def encoder(data):
    logcat('Received ' + data + ' as the input to be process at the encoder', 'ncode', False)
    encoded = ''
    encode = ''
    for item in data:
        if item in keyphrase_ncode:
            encoded += keyphrase_ncode.get(item)
            encode = encoded

        else:
            encoded += item
            encode = encoded
    logcat('Outputing ' + encode + ' as the processed output from the encoder', 'ncode', False)
    return encode


# Function to Decode the data
def decoder(data):
    logcat('Received ' + data + ' as the input to be process at the decoder', 'dcode', False)
    decoded = ''
    decode = ''
    for charc in data:
        if charc in keyphrase_dcode:
            decoded += keyphrase_dcode.get(charc)
            decode = decoded

        else:
            decoded += charc
            decode = decoded
    logcat('Outputing ' + decode + ' as the processed output from the decoder', 'ncode', False)
    return decode


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
def writehis(historytext, origin):
    if origin == 'ncode':
        n_history = open(ncode_history, 'a')
        n_history.write(historytext)
        n_history.write('\n')
        n_history.close()

    elif origin == 'dcode':
        d_history = open(dcode_history, 'a')
        d_history.write(historytext)
        d_history.write('\n')
        d_history.close()

    elif origin != 'dcode' or origin != 'ncode':
        errorhandler(1, origin)


# Function to clear specific history
def clearhistory(origin):
    if origin == 'ncode':
        d_history = open(ncode_history, 'w')
        d_history.truncate(0)
        d_history.close()

    elif origin == 'dcode':
        d_history = open(dcode_history, 'w')
        d_history.truncate(0)
        d_history.close()

    elif origin != 'dcode' or origin != 'ncode':
        errorhandler(1, origin)
    logcat('Cleared History', origin, False)


# Function to Load specific History and print it
def loadhistory(origin):
    # Checking if the requested history is from Encoder or Decoder
    if origin == 'ncode':
        # Doing a filecheck to check if the history file does not exist or the history file is empty
        if filecheck(ncode_history, 'ncode'):
            ln_history = open(ncode_history, 'r')
            print("Loading History for Encoder")
            print('\n')
            for item in ln_history:
                print(item)
        else:
            print("There is no history for encoder")
    elif origin == 'dcode':
        # Doing a filecheck to check if the history file does not exist or the history file is empty
        if filecheck(dcode_history, 'dcode'):
            ld_history = open(dcode_history, 'r')
            print('Loading History for Decoder')
            print('\n')
            for item in ld_history:
                print(item)
        else:
            print('There is no history for decoder')
    elif origin != 'dcode' or origin != 'ncode':
        errorhandler(1, origin)
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
