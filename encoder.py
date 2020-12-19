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
toprint = True
encode = str()
encoded = str()
while True:
    mainstr = str(input("What do you want to encode?: "))
    for item in mainstr:
        if item in keyphrase_ncode:
            encoded += keyphrase_ncode.get(item)
            encode = encoded
            toprint = True
        else:
            print("Please enter a valid statement!")
            toprint = False
            break

    if not toprint:
        pass
    else:
        print(encode)
    encode = ""
    encoded = ""
