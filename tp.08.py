#! Think Python, Chapter 08, Strings
# 20160203WED

# 8.1 fruit[n]
print("\n8.1, strings as sequences")
fruit = 'banana'
print(fruit)
print(fruit[1])

# 8.2 len()
print("\n8.2, len function")
print("length of banana:", len(fruit))
print(fruit[len(fruit)-1])
print("or use negative indicies")
print(fruit[-1])

# 8.3 traversal with for loop
print("\n8.3 loop traversal")
index = 0
while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index += 1
	
# 8.3 E1, backwards print
print("\n8.3 E1, print letters backwards")
index = 1
while index <= len(fruit):
	letter = fruit[-index]
	print(letter)
	index = index + 1
	
# 8.3 E2, fix name spelling outputs
print("\n8.3 E2, fixing name spelling outputs")
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
	if letter in ['O', 'Q']:
		print(letter+'u'+suffix)
	else:
		print(letter+suffix)
		
# 8.4 string slices
print("\n8.4 string slices")
s = 'Monty Python'
print(s[0:5])
print(s[6:12])

# 8.4 E3, slicing
print("\n8.4 E3, what happens when first and second indexes are omitted")
print(fruit[:]) # means the entire string

# 8.5 immutable strings
print("\n8.5 immutable strings")
greeting = "hello, world!"
print(greeting)
print("greeting[0] = 'J', does not work")
print("cannot change the string, but you can create a new one")
new_greeting = 'J' + greeting[1:]
print(new_greeting)

# 8.6 searching
print("\n8.6 searching")
def findd(word, letter, n=0):
	index = n
	print("Looking for", letter, "in", word, ":")
	while index < len(word):
		if word[index] == letter:
			print(letter, "found at position", index+1)
		index += 1
	return -1
findd("correlation", "o")

# 8.7 looping and counting
print("\n8.7 looping and counting")
word = 'banana'
count = 0
for letter in word:
	if letter == 'a':
		count += 1
print("count of 'a':", count)

# 8.7 E5, encapsulating count code and generalize
print("\n8.7 E5, count as a function")
def count(word, letter):
	w = word.lower()
	l = letter.lower()
	num = 0
	for unit in w:
		if unit == l:
			num += 1
	print("Count of", letter, "in", word, ":", num)
count("Augustus", "u")
count("Augustus", "a")

# 8.7 E6, rewrite count func to use find func
print("\n8.7 E6, rewrite count to use find")
def count(word, letter, start=0):
	w = word.lower()
	l = letter.lower()
	loc = []
	while start < len(w):
		n = w.find(l,start)
		loc.append(n)
		start += 1
	return set(loc)
output = count("Augustus", "u", 0)
print(output) # still prints out -1, when it reaches past the last letter to find, returns -1

# 8.8 string methods
print("\n8.8 string methods")
print("\n8.8 E7, modified E6 for total counts")
def count(word, letter, start=0):
	w = word.lower()
	print(w)
	l = letter.lower()
	print(l)
	l_l = len(l)
	loc = []
	while start < len(w):
		n = w.find(l,start)
		if n == -1:
			loc.append(-1) # non matches will output -1 so need to account for extra element in output
			break
		loc.append(n)
		start = n + l_l
	return set(loc)
output = count("banananan", "na", 0)
print(output)
if -1 in output:
	print("number found:", len(output)-1)
else:
	print("number found:", len(output))
	
# 8.9 in operator
print("\n8.9, in operator")
def in_both(word1, word2):
	for letter in word1:
		if letter in word2:
			print(letter)
in_both("orangesa", "apples") # will print out an extra 'a' at the ends

# 8.10 string comparison
print("\n8.10, string comparison")
def compare():
	word = input("type in a word: ")
	if word == "banana":
		print('OKAY, banana!')
	elif word < 'banana':
		print(word, "comes before banana")
	elif word > 'banana':
		print(word, "comes after banana")
compare()

# 8.11 debugging
print("\n8.11, debugging")
print("8.11 E10, errors debugged from reverse func"
def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False
	i = 0
	j = len(word2)-1

	while j > -1:
		if word1[i] != word2[j]:
			return False
		i = i + 1
		j = j - 1

	return True
output = is_reverse("stop", "pots")
print("Is reverse?", output)
