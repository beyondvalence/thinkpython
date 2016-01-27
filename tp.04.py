#! think python chp04, interface design

#4.01
import tkinter
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

wait_for_user()

#E.4.3.1
def square(t):
	for i in range(4):
		fd(t, 100)
		lt(t)

square(bob)

#E.4.3.2
def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

square(bob, 100)

#E.4.3.3
def polygon(t, length, n):
	angle=360.0/n 
	for i in range(n):
		fd(t, length)
		lt(t, angle)

polygon(bob, 100, 4)

#E.4.3.4, circle
from math import pi
def circle(t, radius):
	cir = 2 * pi * radius
	n = int(cir/3)+1 
	angle=360.0/n
	length=cir/n	
	polygon(t, length, n)

circle(bob, 150)

#E.4.3.5, arc
from math import pi
def arc(t, radius, a):
	angle=360.0/200 
	length=(pi/100)*radius
	arc=int((a/360.0)*200)
	for i in range(arc):
		fd(t, length)
		lt(t, angle)

arc(bob, 150, 300)

#4.7 refactoring using polyline
def polyline(t, length, n, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)
		
def arc(t, radius, angle):
	arc_l = 2 * pi * radius * angle / 360 
	n = int(arc_l/3)+1
	step_l = arc_l / n 
	step_angle = float(angle) / n 
	polyline(t, length=arc_l, n, angle=step_angle)

def circle(t, r):
	arc(t, r, 360)