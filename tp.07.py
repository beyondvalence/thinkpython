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
		if error < delta:
			print("estimated square root:", y)
			print("error: ", error)
			break
		x = y 
		print("estimated square root:", y)
		print("error: ", error)
		
sq(14, 3, .00001)

# 7.9 E3, print table of square roots, 
# comparing Newton's function and math.sqrt
print("7.9 E3 square root tables")
import math
def test_square_root(n):
	for i in range(1,n+1):
		x = i - 0.5
		while True:
			y = (x + i/x)/2 
			error = abs(x-y)
			if error < 0.00000001:
				break
			x = y
		print(i, y, math.sqrt(i), abs(y-math.sqrt(i)))
		
test_square_root(n=9)