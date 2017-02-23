import string
word_counts = {}

line = "Hello, world! I love python. hello, marry. love"
data = line.strip().split(" ")
for word in data:
    word = word.translate(None,string.punctuation).lower()
    if word not in word_counts.keys():
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print word_counts