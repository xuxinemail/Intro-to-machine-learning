import string
word_counts = {}

line = "Hello, world! I love python. hello, marry. love"
line = line.translate(None, string.punctuation)
line = line.lower()
data = line.strip().split(" ")
for word in data:
    if word not in word_counts.keys():
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print word_counts