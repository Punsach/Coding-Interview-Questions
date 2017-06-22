#Compress a string by using the frequency of each letter 

import sys 
from collections import OrderedDict

def compress(someString):
	#Create a dictionary with each character in the string and its frequency
	characters = OrderedDict()
	for c in someString:
		if(c in characters):
			characters[c] += 1
		else:
			characters[c] = 1

	#Join all the characters and their frequencies in the string 
	result = ''.join(['%s%s' % (key, str(value)) for key, value in characters.iteritems()])

	#Return the shorter of the two strings 
	return min(result, someString, key=len)

if(len(sys.argv) != 2):
	print("Please enter the proper number of inputs")
else:
	print("The result of the string compression is " + compress(sys.argv[1]) + ". Solution took O(n) time and O(n) space")

