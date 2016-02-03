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