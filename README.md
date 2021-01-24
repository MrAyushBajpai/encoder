# Encoder Decoder
This software is made for the purpose of Encoding/Decoding Messages and Statements. It allows you to keep history of the data you encode/decode. You can use multiple commands to manipulate everything. The file main.py is the file you are supposed to run. The module.py only contains all the essential function, it does not have a use of its own, however it needs to be in the same directory/folder of the main.py.

# Basic Syntax
<process> <task>
  
Processes include:-
  1. 'cmd'(case and space insensitive process):- Used to enter a command
  2. 'encode'(case and space insensitive):- Used to encode a given task
  3. 'decode'(case and space insensitive):- Used to decode a given task
  
  It should be noted that the process itself is insensitive of case and space, meaning you can write as:- EnCodeHello World. It will be treated as encode Hello World

# Commands(to be used with cmd)
These are the current commands. To use these command, write cmd followed by the command. The commands are not dependant upon the case and space, meaning that cLeAr /hiStory is the same as clear/history. More commands will be added in the future as per the requirement.
1. 'exit' or 'close' to close the program
2. 'clear /history' or 'clear /h' to clear the history
3. 'clear/logs' or 'clear /l' to clear the logs
4. 'clear' or 'cls' to clear the on-screen text
5. 'clear /all' or 'clear /a' to clear everything that can be cleared
6. 'show /history' or 'show /h' for viewing the history
7. 'show /errors' or 'show /e' for viewing all the errors in the logfile. It should be noted that if you clear the logs, the error will also be cleared.

# Encode
The 'encode' process allows to encode a given task. Say you want to encode 'Hello World'. To do this, simply type "encode Hello World" (without double quotes). It will encode whatever follows the 'encode' process-name. It will output 'Itaaf Cfjar' on the console.

# Decode
The 'decode' process allows to decode a given task. Say you want to decode 'Itaaf Cfjar'. To do this, simply type "decode Hello World" (without double quotes). It will decode whatever follows the 'decode' process-name. It will output 'Hello World' on the console.
