import os
from collections import Counter
import nltk

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path to paragraphs.txt
file_path = os.path.join(script_dir, "paragraphs.txt")

# Load English stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

# Read the contents of paragraphs.txt
with open(file_path, 'r') as file:
    text = file.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Filter out stopwords from the words
filtered_words = [word for word in words if word.lower() not in stop_words]

# Join the filtered words back into text
filtered_text = ' '.join(filtered_words)

# Count the occurrences of each word
word_counts = Counter(filtered_words)

# Print each word and its count
for word, count in word_counts.items():
    print(f"{word}: {count}")