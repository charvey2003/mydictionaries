
with open('sometext.txt','r') as infile:
    text = infile.read()
    words = text.split()

frequency ={}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
    
for word, count in frequency.items():
    print(f"{frequency}")
    

