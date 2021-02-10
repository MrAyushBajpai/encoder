# Importing Necessary Files
import sys
import time
import configparser
try:
    import module
except ModuleNotFoundError:
    print('The File Module.py was not found! Are you sure it is in the same directory as the main.py?')
    time.sleep(5)
    sys.exit()

# Setting up the configuration file processor
configparser = configparser.ConfigParser()
configfilepath = 'parameters.cfg'
configparser.read(configfilepath)

# Writing to logfile for program startup
module.logcat('Program Started', False)

# Does a one time check if the logfile is larger than 2 MBs
module.logsize()

# Take the key for the session from the user
while True:
    key = str(input('Please enter the Key for this entire session: '))
    # Checks if the key has more than or 8 characters
    if int(configparser.get('key-parameter', 'minkeylen')) <= len(key):
        # Checks if the key has less than or 16 characters
        if len(key) <= int(configparser.get('key-parameter', 'maxkeylen')):
            break
        else:
            print('Please enter a key with 16 or lesser character.')
            print(' ')
            continue
    else:
        print('Please enter a key with 8 or more characters.')
        print(' ')
        continue
module.logcat('The Key for the session is ' + key, False)

# Check if the user wants to keep history
while True:
    tokeeph = str(input('Do You want to keep history? Y/N: '))
    if tokeeph.lower() == 'y':
        tokeeph = True
        break
    elif tokeeph.lower() == 'n':
        tokeeph = False
        break
    else:
        print('Please choose a valid option! Enter Y or N.')
        continue

if tokeeph:
    module.logcat('Keeping the history for the session.', False)
else:
    module.logcat('Not Keeping History for this session', False)

# Main Loop. Runs until the program ends
while True:
    # Ask the user for statement or command
    mainstr = str(input("Enter the desired command: "))

    # Adding the entered data to logcat
    module.logcat('User Entered - ' + mainstr, False)

    # Some Necessary Local Variables
    data = ''
    out = ''
    org = ''

    # Checking if the user specified process was cmd
    if mainstr[0:3].lower() == 'cmd':
        out = module.commander(mainstr)

        if out == 'exit':
            sys.exit()
        elif out == 'clearhistory':
            module.clearhistory()
        elif out == 'showhistory':
            module.loadhistory()
        elif out == 'clearall':
            module.clearhistory()
            module.clearlog()
            module.clear()
            module.logcat('Cleared all', False)
        elif out == 'clearscreen':
            module.clear()
        elif out == 'clearlog':
            module.clearlog()
        elif out == 'logerrors':
            module.logerror()
        else:
            print('Error Code - 1: Unable to locate command: "' + out + '"')
            module.errorhandler(1, out)

    # Checking if the user specified process was encode
    elif mainstr[0:6].lower() == 'encode':
        module.logcat('Calling the encode function with data ' + mainstr, False)
        data = module.encoder(module.cleaner(mainstr, 6), key)
        org = 'encode'

    # Checking if the user specified process was decode
    elif mainstr[0:6].lower() == 'decode':
        module.logcat('Calling the decode funcion with data ' + mainstr, False)
        data = module.decoder(module.cleaner(mainstr, 6), key)
        org = 'decode'

    # Checking if the user specified process was key
    elif mainstr[0:3].lower() == 'key':
        c = module.cleaner(mainstr, 3)
        c = ''.join(c)
        module.logcat('User changed the key from' + key + 'to ' + c, False)
        key = c
        print('The key was changed to ' + key + ' for this session.')

    # If the user did not specify any valid process
    else:
        module.errorhandler(2, mainstr)
        print('Error Code - 2: Please enter a vaild process to be undertaken.')
    print(' ')

    # Printing Handler
    if data != '':
        print(data)
        if tokeeph:
            module.writehis(data, True, org)
        else:
            pass
    else:
        pass

    # Logcat Program End
    module.logcat('RESET', False)
