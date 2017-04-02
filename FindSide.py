#Function to find any side of a right angled triangle

import math, sys

#Variables boi
opt1 = "hypotenuse"
opt2 = "opposite"
opt3 = "adjacent"


#_______________________________________#

def FindAnySide():
	print "Which side are you trying to find?"
	
	Side = raw_input().lower()
	
	if Side == "hypotenuse":
		while True:
			try:
				prompt1 = "Opposite : "
				o_ask = int(raw_input(prompt1))
				prompt2 = "Adjacent : "
				a_ask = int(raw_input(prompt2))
				break
			except ValueError:
				print "This is not a number... Try again.\n"
			
			
		the_math = a_ask**2 + o_ask**2
		the_math_done = math.sqrt(the_math)
		
		print "This is the hypotenuse : " + str(the_math_done)
		
		print "\nAre you done?"
		askdone = raw_input().lower()
		
		if askdone == "no":
			FindAnySide()
			
		if askdone == "yes":
			print "Goodbye!"
			
			
#______________________________________#			

		
	elif Side == "opposite":
		while True:
			try:
				prompt3 = "Hypotenuse : "
				h_ask = input(prompt3)
				prompt4 = "Adjacent : "
				a_ask2 = input(prompt4)
				break
			except ValueError:
				print "This is not a number... Try again.\n"
		
		did_the_math = h_ask**2 - a_ask2**2
		he_did_the_math = math.sqrt(did_the_math)
		
		print "This is the opposite side : " + str(he_did_the_math)
		
		print "\nAre you done?"
		askdone1 = raw_input().lower()
		
		if askdone1 == "no":
			FindAnySide()
			
		if askdone1 == "yes":
			print "Goodbye!"
			
			
#_______________________________________#
			
			
			
	elif Side == "adjacent":
		while True:
			try:
				prompt5 = "Hypotenuse : "
				h_ask2 = input(prompt5)
				prompt6 = "Opposite : "
				o_ask2 = input(prompt6)
				break
			except ValueError:
				print "This is not a number... Try again.\n"
		
		maths_done = h_ask2**2 - o_ask2**2
		math_is_done = math.sqrt(maths_done)
		
		print "This is the adjacent side : " + str(math_is_done)
		
		print "\nAre you done?"
		askdone2 = raw_input().lower()
		
		if askdone2 == "no":
			FindAnySide()
			
		if askdone2 == "yes":
			print "Goodbye!"
	
	
#______________________________________#
		
		
			
	elif Side != opt1 or opt2 or opt3:
		print "Invalid side.\n"
		FindAnySide()


#______________________________________#			


#The calling of the function, optional
print "Do you want to use the function?"

askiftheydo = raw_input().lower()

if askiftheydo == 'no':
	print "Goodbye!"

elif askiftheydo == 'nope':
	print "Goodbye!"
	
elif askiftheydo == 'yes':
	FindAnySide()
	
elif askiftheydo == 'yeah':
	FindAnySide()

elif askiftheydo == 'yea':
	FindAnySide()
	
else:
	print "Fuck it, you're doing it anyways.\n"
	FindAnySide()
