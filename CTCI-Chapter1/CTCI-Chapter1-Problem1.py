#Determine if a string has all unique characters. 

#Assume ASCII characters, so max of 128 distinct characters 

import sys

#Using another Data Structure
def Solution1(someString):
	#By pigeonhole if the string has more than 128 characters, there must be some repeat
	if(len(someString) > 128):
		return True

	#Put characters into a dictionary. If the character is already there, return True.
	characters = {}
	for character in someString:
		if(character in characters):
			return True
		else:
			characters[character] = 1

	return False

#Without using another data structure [j]
def Solution2(someString):
	if(len(someString) > 128):
		return True
	#Sort the string in O(nlogn) time
	sortedString = ''.join(sorted(someString))
	#Since identical characters will now be next to each other, we can see if there are duplicates
	for index in range(0, len(sortedString) - 2):
		if(sortedString[index] == sortedString[index+1]):
			return True
	return False

if(len(sys.argv) != 2):
	print("That is not the correct number of arguments! Please enter in only one word")
else:
	if(Solution1(sys.argv[1])):
		print("Using a dictionary, we find there are dupicates! Solution takes O(n) time and O(n) space.")
	else:
		print("Using a dictionary, we know there are no duplicates! Solutions take O(n) time and O(n) space.")

	if(Solution2(sys.argv[1])):
		print("Without using another data structure, we find there are duplicates! Solution takes O(nlogn) time and O(1) space.")
	else:
		print("Without using another data structure, we know there are no duplicates! Solution takes O(nlogn) time and O(1) space.")






