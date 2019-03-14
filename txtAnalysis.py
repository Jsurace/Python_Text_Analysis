"""
Program: txtAnalysis.py
Author: Jenna
Date: 3/14/2019

Computes and displays the flesch index and the grade level equivalent for the readability
of the text file. A .txt file is needed in the current working directory for this program to work.
"""

# Take the inputs 
fileName = input("Enter the file name: ")
inputFile = open(fileName, "r")
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + text.count(':') + text.count(';') + text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0 
vowels = "aeiouAEIOU"

for word in text.split():
	for vowel in vowels:
		syllables += word.count(vowel)
	for ending in ["es", "ed", "e"]:
		if word.endswith(ending):
			syllables -= 1
	if word.endswith("le"):
		syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

level = round(0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59)

# Output the results
print("The Flesch Index is", index)
print("The Grade Level equivalent is", level)
print("This file contained", sentences, "sentences.")
print("It contained", words, "words.")
print("It also contained", syllables, "syllables.")



