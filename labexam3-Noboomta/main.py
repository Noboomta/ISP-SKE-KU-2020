import re
from word_counter import WordCounter

# pattern for splitting words
PATTERN = "[\d\W\s_]+"

wc = WordCounter()

with open('README.md', 'r') as file:
    for line in file:
        for word in re.split(PATTERN, line.strip()):
            if word:
                wc.add_word(word)
               
# display the word counts
for word in sorted(wc):
    print(f"{wc[word]:3}  {word}")
