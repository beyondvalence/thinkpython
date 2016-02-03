#! Think Python, Chapter 08, Strings
# 20160203WED

# 8.1 fruit[n]
print("8.1, strings as sequences")
fruit = 'banana'
print(fruit)
print(fruit[1])

# 8.2 len()
print("8.2, len function")
print("length of banana:", len(fruit))
print(fruit[len(fruit)-1])
print("or use negative indicies")
print(fruit[-1])

# 8.3 traversal with for loop
print("8.3 loop traversal")
index = 0
while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index += 1
	
# 8.3 E1, backwards print
print("8.3 E1, print letters backwards")
index = 1
while index <= len(fruit):
	letter = fruit[-index]
	print(letter)
	index = index + 1
	
# 8.3 E2, fix name spelling outputs
print("8.3 E2, fixing name spelling outputs")
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
	if letter in ['O', 'Q']:
		print(letter+'u'+suffix)
	else:
		print(letter+suffix)
		
# 8.4 string slices
print("8.4 string slices")
s = 'Monty Python'
print(s[0:5])
print(s[6:12])

# 8.4 E3, slicing
print("8.4 E3, what happens when first and second indexes are omitted")
print(fruit[:]) # means the entire string

# 8.5 immutable strings
print("8.5 immutable strings")
greeting = "hello, world!"
print(greeting)
print("greeting[0] = 'J', does not work")
print("cannot change the string, but you can create a new one")
new_greeting = 'J' + greeting[1:]
print(new_greeting)

# 8.6 searching
print("8.6 searching")
