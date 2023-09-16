import re
file = open("C:/Users/BIPIN T P/Desktop/java script/python/level1/level2/file.txt" , "r")
word_counts=dict()
for line in file:
     # Remove the leading spaces and newline character
    line = line.strip()
    line = line.lower()
    # Split the line into words.
    words = re.split("\W+", line)
    # Iterate over the words.
    for word in words:
        # Check if the word is already in the dictionary.
        if word not in word_counts:
            # Add the word to the dictionary.
            word_counts[word] = 1
        else:
            # Increment the count for the word.
            word_counts[word] += 1
# Sort the dictionary by word.
word_counts = sorted(word_counts.items(), key=lambda x: x[0])
for word, count in word_counts:
    print(f"{word}: {count}")
file.close()