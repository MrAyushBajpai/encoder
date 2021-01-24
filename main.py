# Importing Necessary Files
import module

# Defining necessary variables
processed = ''
code = 0
exitcall = 0

# Writing to logfile for program startup
module.logcat('Program Started', False)

# Does a one time check if the logfile is larger than 2 MBs
module.logsize()

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

# Main Loop. Runs until the program ends
while module.errorhandler(code) == 0:
    # Ask the user for statement or command
    mainstr = str(input("Enter the desired command: "))

    # Adding the entered data to logcat
    module.logcat('User Entered - ' + mainstr,  False)

    # Some Necessary Local Variables
    data = ''
    out = ''
    org = ''

    # Checking if the user entered a command by using cmd
    if mainstr[0:3].lower() == 'cmd':
        out = module.commander(mainstr)

        if out == 'exit':
            code = module.errorhandler(0.5)
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
            print('Error Code - 3: Unable to locate command: "' + out + '"')
            module.errorhandler(3, out)
    elif mainstr[0:6].lower() == 'encode':
        module.logcat('Calling the encode function with data ' + mainstr, False)
        data = (module.encodeprocess(mainstr))
        org = 'encode'

    elif mainstr[0:6].lower() == 'decode':
        module.logcat('Calling the decode funcion with data ' + mainstr, False)
        data = (module.decodeprocess(mainstr))
        org = 'decode'

    else:
        module.errorhandler(4, mainstr)
        print('Please enter a vaild process to be undertaken.')
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

# Reset the variables for using again
    if code == 0:
        encode = ""
        module.logcat('RESET', False)
    else:
        module.logcat('Program exit', False)
        exitcall = 1

# Checks to see if the exit was intentional, if there was no exit call
if exitcall == 0 and code == 0:
    errorinp = str(input('The program ended without giving us a exit call. Was this exit intentional? (Y/N): '))
    if errorinp.lower() == 'y' or errorinp.lower() == 'yes':
        module.errorhandler(2, 'ncode')
    else:
        pass
else:
    pass
