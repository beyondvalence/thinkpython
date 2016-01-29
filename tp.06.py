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

#6.3 composition
