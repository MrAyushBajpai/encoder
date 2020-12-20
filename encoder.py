# Importing Necessary Libraries
import module

# Defining Necessary Variables
encode = str('')
code = 0
exitcall = 0

# Writing to the log file about program startup
module.logcat('Program Started', 'ncode', False)

# Main Loop. Runs until the program ends
while module.errorhandler(code, 'ncode') == 0:
    # Ask the user for statement or command
    mainstr = str(input("What do you want to encode?: "))

    # Add the command to the logcat
    module.logcat('Command Entered- ' + mainstr, 'ncode', False)

    # Command 'close' or 'exit' for ending the program
    if mainstr.lower() == 'close' or mainstr.lower() == 'exit':
        code = module.errorhandler(0.5, 'ncode')

    # Command 'clear /h' or 'clear /history' for clearing all the history of encoder
    elif mainstr.lower() == 'clear /h' or mainstr.lower() == 'clear/h' or mainstr.lower() == 'clear /history'\
            or mainstr.lower() == 'clear/history':
        module.clearhistory('ncode')
        print('History cleared successfully!')

    # Command for loading the history of encoder
    elif mainstr.lower() == 'history' or mainstr.lower() == 'show /h' or mainstr.lower() == 'show/h' \
            or mainstr.lower() == 'show /history' or mainstr.lower() == 'show /history':
        module.loadhistory('ncode')

    # Command for clearing everything that can be cleared
    elif mainstr.lower() == 'clear /a' or mainstr.lower() == 'clear/a' \
            or mainstr.lower() == 'clear /all' or mainstr.lower() == 'clear/all':
        module.clearhistory('ncode')
        module.clear()
        module.clearlog()
        module.logcat('Cleared all', 'ncode', False)

    # Command for clearing the on-screen text
    elif mainstr.lower() == 'cls' or mainstr.lower() == 'clear':
        module.clear()
        module.logcat('Cleared the data on-screen', 'ncode', False)

    # Command for clearing the logs
    elif mainstr.lower() == 'clear /logs' or mainstr.lower() == 'clear/logs' \
            or mainstr.lower() == 'clear /l' or mainstr.lower() == 'clear/l':
        module.clearlog()
        module.logcat('Cleared Log', 'ncode', False)

    # Main Code that will encode the statement
    else:
        encode = module.encoder(mainstr)

    # Printing Handler
    if encode != '':
        print(encode)
        module.logcat('Encoded value is- ' + encode, 'ncode', False)

        # Writing to the history
        module.writehis(encode, 'ncode')
        module.logcat('Added ' + encode + ' to the history', 'ncode', False)
    else:
        pass
            
    # Reset the variables for using again
    if code == 0:
        encode = ""
        module.logcat('RESET', 'ncode', False)
    else:
        module.logcat('Program exit', 'ncode', False)
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
