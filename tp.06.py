# think python chp06, fruitful functions
# 20160129FRI

import math

#6.1 return values
def area(radius):
	temp = math.pi * radius**2 
	return temp	
	
#6.1 E1, compare function
def compare(x,y):
	if x > y:
		return 1
	elif x==y:
		return 0
	else:
		return -1

#6.2 incremental development
print("6.2 incremental development")
def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	return math.sqrt(dsquared)

#6.2 E2, right triangle hypotenuse
def hypotenuse(left, right):
	left_sq = left*left
	right_sq = right*right
	hypo_sq = left_sq + right_sq
	return math.sqrt(hypo_sq)

def hypotenuse_prompt():
	a=float(input("leg 1 length: "))
	b=float(input("leg 2 length: "))
	h=hypotenuse(a, b)
	print("the hypotenuse is: ", h)
	return h 
	
hypotenuse_prompt()

#6.3 composition of functions within each other
def circle_area(xc, yc, xp, yp):
	return area(distance(xc, yc, xp, yp))
	
#6.4 boolean functions
def is_between(x,y,z):
	if y>=x and y<=z:
		return True
	else:
		return False
		
#6.5 more recursion	
print("6.5 factorials")
def factorial(n):
	if n==0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		print(result)
		return result

factorial(4)

# 6.7 fibonacci, one more example
print("6.7 fibonacci seq")
def fibonacci(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
		
num = fibonacci(7)
print(num)

# 6.8 checking types
print("6.8 factorial with type check")
def factorial(n):
	if not isinstance(n, int):
		print("Factorial is only defined for integers.")
		return None
	elif n < 0:
		print("Factorial is not defined for negative integers.")
		return None
	elif n == 0:
		return 1
	else:
		return n * factorial(n-1)
		
factorial('hello')
factorial(2.3333333)
factorial(-53)	