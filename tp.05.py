#! Thinking Python, Chp05, conditionals and recursion

#5.1 modulus operator
print("5.1")
print("156%100=")
print(156%100)

#5.9 E2 stack diagrams for recursive functions
print("5.9 E2")
def do_n(f,n):
	if n<=0:
		return
	f()
	do_n(f, n-1)

def print_now(s='now'):
	print(s)

do_n(print_now,6)

#5.11 keyboard input
print("5.11")
text=input('type a number here:\n')
print(text)


#5.14 exercises
#5.14 E3, Fermat's Last Theorem
def fermat_check(a=1,b=1,c=1,n=3):
	a=int(input('a= '))
	b=int(input('b= '))
	c=int(input('c= '))
	n=int(input('n= '))
	if a < 1 or b < 1 or c < 1:
		print("a,b,c need to be positive integers")
		fermat_check()
	elif n < 3:
		print("n needs to be greater than 2:")
		fermat_check()	
	left=a**n+b**n
	right=c**n
	yn = (left==right)
	return yn
	
def fermat_prompt():
	result = fermat_check()
	if result:
		print("Holy smokes, Fermat was wrong!")
		return
	else:
		print("No, that doesn't work. Theorem still holds.")
		text = input('Try again? ')
		if text=='yes':
			fermat_prompt()
		else:
			return
			
#5.14 E4, Triangles
def is_triangle(a=3,b=4,c=5):
	a=float(input("a= "))
	b=float(input("b= "))
	c=float(input("c= "))
	if a < 1 or b < 1 or c < 1:
		print("a,b,c must be positive integers")
		is_triangle()
	elif (a >= b + c) or (b >= a + c) or (c >= a + b):
		print("Sides values not viable")
		is_triangle()
	else:
		print("Sides make a valid triangle!")
		return True
	

if __name__ == "__main__":			
	print("5.14 E3, Fermat's Last Theorem")
	fermat_prompt()
	print("5.14 E4, Triangles")
	is_triangle()