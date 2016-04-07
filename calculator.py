"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

print "This is a very basic calculator. Enter an operand, and up to two numbers to get your result."
#test
# Your code goes here
while True:
	calc = raw_input(">> ")
	# calc_functions = "+,-,*,/,square,cube,pow,%"
	tokens = calc.split(" ")

	if len(tokens) > 3:
		print "Please enter up to two separate numbers. Ahmad."
		continue
	if tokens[0] == "+":
		a = int(tokens[1])
		b = int(tokens[2])	
		print add(a,b)
	if tokens[0] == "-":
		a = int(tokens[1])
		b = int(tokens[2])		
		print subtract(a,b)

	if tokens[0] == "*":
		a = int(tokens[1])
		b = int(tokens[2])		
		print multiply(a,b)

	if tokens[0] == "/":
		a = int(tokens[1])
		b = int(tokens[2])		
		print divide(a,b)

	if tokens[0] == "square":
		a = int(tokens[1])		
		print square(a)

	if tokens[0] == "cube":
		a = int(tokens[1])			
		print cube(a)

	if tokens[0] == "pow":
		a = (tokens[1])
		b = (tokens[2])			
		print power(a,b)

	if tokens[0] == "%":
		a = int(tokens[1])
		b = int(tokens[2])	
		print mod(a,b)
