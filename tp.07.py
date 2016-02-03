#! Think Python Chp07 Iteration
# 20160129FRI

# 7.1 multiple assignment

# 7.3 while statement
print("7.3 while statement")
def countdown(n):
	while n > 0:
		print(n)
		n = n-1
	print('Blastoff!')

countdown(10)

# 7.4 break
print("7.4 breaks")
def done():
	while True:
		line = input("> ")
		if line == "done":
			break
		print(line)
	print('Done!')
done()

# 7.5 square roots
print("7.5 square roots")
def sq(a, x, delta):
	print("estimating square root of", a)
	print("with error less than", delta)
	while True:
		y = (x + (a/x))/2 
		error = abs(x-y)
		if abs(x-y) < delta:
			print("estimated square root:", y)
			print("error: ", error)
			break
		x = y 
		print("estimated square root:", y)
		print("error: ", error)
		
sq(14, 3, .00001)