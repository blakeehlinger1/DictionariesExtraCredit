
infile = open('bookofJohntext.txt', 'r')

word_freq = {}

for line in infile:
    line = line.strip()
    line = line.rstrip()
    words = line.split()

    for word in words:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1
    word_freq[word]

print("Father:", word_freq["Father"])
print("God:", word_freq["God"])
print("Christ:", word_freq["Christ"])
print("Spirit:",word_freq["Spirit"])
print("sprit:", word_freq["spirit"])
print("life:", word_freq["life"])
print("man:", word_freq["man"])