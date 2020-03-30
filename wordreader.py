import glob
import string
import re

# contains list of words
word_list = []
# dictionary containing words and word count 
word_count = {}
# common words that might not be worth counting
banned_words = ["a", "an", "and", "are", "as", "at", "be", "but", "by", "can", "for", "if", "in", "is", "it", "its", "like", "of", "or", "on", "that", "the", "this", "to", "with"
				,"you", "your", "they", "have", "their"]

# Adds words to word list, like it says
def add_to_list(file):
	with open(file, 'r') as f:
		for line in f:
			for w in line.split():		
				w = re.sub(r'[\W_]+', '', w)
				w = w.lower()
				if w not in banned_words:
					word_list.append(w)

# Grabs all files in the directory
list_of_files = glob.glob("*.txt")

print(list_of_files)

for each in list_of_files:
	add_to_list(each)

for word in word_list:
	if (word not in word_count):
		word_count[word] = word_list.count(word)

#create list of of tuples sorted by index 1 
list_of_tuples = sorted(word_count.items(), reverse = True, key= lambda x: x[1])

for each in list_of_tuples:
	if each[1] > 3:
		print(each)


	