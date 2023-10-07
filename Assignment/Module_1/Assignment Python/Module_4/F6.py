import re

def longest_word(sentence):
	words = re.findall(r'\b\w+\b', sentence) 
	return max(words, key=len) 

sentence = "be confident and be yourself"
print(longest_word(sentence))
