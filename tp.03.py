#!think python chp03 functions
print("think python chp03, functions")

#E3.4
def do_twice(f,v):
	f(v)
	f(v)
	
def print_twice(s):
	print(s)
	print(s)
	
do_twice(print_twice, 'spam')

def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)
	
do_four(print_twice,'hax')

#E3.5
def print_border(s=0):
	print('+ - - - - + - - - - +')
	
def print_mid(s=0):
	print('|         |         |')
	
def print_repeat(f=0):
	print_border()
	print_mid()
	print_mid()
	print_mid()
	print_mid()
	
def print_grid(n=0):
	print_repeat()
	print_repeat()
	print_border()

print_grid()

def print_border(s=0):
	print('+ - - - - + - - - - + - - - - + - - - - +')
	
def print_mid(s=0):
	print('|         |         |         |         |')

def print_four(f):
	f()
	f()
	f()
	f()
	
def print_repeat(f=0):
	print_border()
	print_four(print_mid)
	
def print_grid(n=0):
	print_four(print_repeat)
	print_border()
	
print_grid()