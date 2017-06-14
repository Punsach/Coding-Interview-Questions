#Determine if a string is a permutation of a palindrome

import sys

def palindrome(someString):
	#Since we are not concerned with case, we make all letters lower case
	someString = someString.lower()
	spaceCounter = 0 
	characters = {} 
	oddCounter = 0 

	#Store all of the characters in a dictionary, with their corresponding values equal to their frequency 
	for c in someString:
		if(c in characters):
			characters[c] += 1 
		elif(c == " "):
			spaceCounter += 1
		else:
			characters[c] = 1

	#We do not need to worrry about spaces in our permutation 
	palLength = len(someString) - spaceCounter

	#Determine how many characters have an odd number for the frequency 
	for key, value in characters.iteritems():
		if(value % 2 != 0):
			oddCounter += 1

	#Determine if the palindrome has an odd number of characters, and one odd frequency, or even number of characters and zero odd frequencies
	if(palLength % 2 != 0 and oddCounter == 1):
		return True
	elif(palLength % 2 == 0 and oddCounter == 0):
		return True
	else:
		return False

if(len(sys.argv) != 2):
	print("Incorrect number of inputs, please enter in one value!")
elif(palindrome(sys.argv[1])):
	print("The string is a palindrome! Solution took O(n) time and O(n) space")
else:
	print("The string is not a palindrome! Solution took O(n) time and O(n) space")