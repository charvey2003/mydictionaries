codes = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '6', 'D': '*', 'd': '7',
        'E': '^', 'e': '1', 'F': '&', 'f': '2', 'G': '(', 'g': '3', 'H': ')', 'h': '4',
        'I': '_', 'i': '5', 'J': '-', 'j': '=', 'K': '+', 'k': '/', 'L': '{', 'l': '}',
        'M': '[', 'm': ']', 'N': '|', 'n': '>', 'O': ':', 'o': ';', 'P': '"', 'p': "'",
        'Q': '<', 'q': ',', 'R': '.', 'r': '?', 'S': '`', 's': '~', 'T': '$', 't': '0',
        'U': 'u', 'u': 'v', 'V': 'w', 'v': 'x', 'W': 'y', 'w': 'z', 'X': 'X', 'x': 'Y',
        'Y': 'Z', 'y': 'A', 'Z': 'B', 'z': 'C', ' ': ' '  
    }

rev_codes = {}

for key, value in codes.items():
    rev_codes[value] = key

with open('encrypted.txt','r') as infile:
    encrypted_txt = infile.read()

dec_text = ""

for char in encrypted_txt:
    if char in rev_codes:
        dec_text += rev_codes[char]

    else:
        dec_text += char

print(dec_text)