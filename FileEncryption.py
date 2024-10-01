codes = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '6', 'D': '*', 'd': '7',
        'E': '^', 'e': '1', 'F': '&', 'f': '2', 'G': '(', 'g': '3', 'H': ')', 'h': '4',
        'I': '_', 'i': '5', 'J': '-', 'j': '=', 'K': '+', 'k': '/', 'L': '{', 'l': '}',
        'M': '[', 'm': ']', 'N': '|', 'n': '>', 'O': ':', 'o': ';', 'P': '"', 'p': "'",
        'Q': '<', 'q': ',', 'R': '.', 'r': '?', 'S': '`', 's': '~', 'T': '$', 't': '0',
        'U': 'u', 'u': 'v', 'V': 'w', 'v': 'x', 'W': 'y', 'w': 'z', 'X': 'X', 'x': 'Y',
        'Y': 'Z', 'y': 'A', 'Z': 'B', 'z': 'C', ' ': ' '  
    }

with open('info_security-1.txt','r') as infile:
    text = infile.read()

enc_content = ""

for char in text:
    if char in codes:
        enc_content += codes[char]
    else:
        enc_content += char

with open('encrypted.txt','w') as outfile:
    outfile.write(enc_content)




