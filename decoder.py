# Importing Necessary Modules
import module

# Defining Necessary Variables
decode = str('')
code = 0
exitcall = 0

# Writing to the log file about program startup
module.logcat('Program Started', 'dcode', False)

# The main loop, which will run until the program ends
while module.errorhandler(code, 'dcode') == 0:
    # Ask the user for a statement or command
    mainstg = str(input("What do you want to decode?: "))

    # Add the command to the logcat
    module.logcat('Command Entered- ' + mainstg, 'dcode', False)

    # Command 'close' or 'exit' to end the program
    if mainstg.lower() == 'close' or mainstg.lower() == 'exit':
        code = module.errorhandler(0.5, 'dcode')

    # Command for clearing history
    elif mainstg.lower() == 'clear /h' or mainstg.lower() == 'clear/h' or mainstg.lower() == 'clear /history'\
            or mainstg.lower() == 'clear/history':
        module.clearhistory('dcode')
        print('History cleared successfully!')

    # Command for clearing the on-screen text
    elif mainstg.lower() == 'clear' or mainstg.lower() == 'cls':
        module.clear()

    # Command for loading the history
    elif mainstg.lower() == 'history' or mainstg.lower() == 'show /h' or mainstg.lower() == 'show/h' \
            or mainstg.lower() == 'show /history' or mainstg.lower() == 'show /history':
        module.loadhistory('dcode')

    # Command for clearing everything that can be cleared
    elif mainstg.lower() == 'clear /a' or mainstg.lower() == 'clear/a' \
            or mainstg.lower() == 'clear /all' or mainstg.lower() == 'clear/all':
        module.clearhistory('dcode')
        module.clear()
        module.clearlog()
        module.logcat('Cleared all', 'dcode', False)

    # Command for clearing the logs
    elif mainstg.lower() == 'clear /logs' or mainstg.lower() == 'clear/logs' \
            or mainstg.lower() == 'clear /l' or mainstg.lower() == 'clear/l':
        module.clearlog()
        module.logcat('Cleared Log', 'dcode', False)

    # Main code that will decode the statement
    else:
        decode = module.decoder(mainstg)
    
    # Printing Handler
    if decode != '':
        print(decode)
        module.logcat('Decoded value is- ' + decode, 'dcode', False)
        
        # Writing to History
        module.writehis(decode, 'dcode')
        module.logcat('Added ' + decode + ' to the history', 'dcode', False)
    else:
        pass

    # Reset the variables for using again
    if code == 0:
        decode = ""
        module.logcat('RESET', 'dcode', False)
    else:
        module.logcat('Program exit', 'dcode', False)
        exitcall = 1

# Checks to see if the exit was intentional, if there was no exit call
if exitcall == 0 and code == 0:
    errorinp = str(input('The program ended without giving us a exit call. Was this exit intentional? (Y/N): '))
    if errorinp.lower() == 'y' or errorinp.lower() == 'yes':
        module.errorhandler(2, 'dcode')
    else:
        pass   
else:
    pass
