#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
# 2. Split the sentence
words = sentence.split()
print("The list of words used in your sentence are: ", words)
# 3. Create lists to store words and their corresponding frequencies.
new_words = []
frequencies = []
punctuation = (".,!?;:")
new_sentence = ""
for char in sentence:
 if char not in punctuation:
  new_sentence += char      
# 4. Iterate through words and update frequencies
for w in words:
   if w not in new_words:
       index = new_words.index(w)
       frequencies[index] += 1
   else:
        new_words.append(w)
        frequencies.append(1)
        
for i in range(len(new_words)):
    print(new_words[i], ":", frequencies[i])
print("Words: ", new_words)
print("Frequencies: ", frequencies)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")
    
