
#Determine if two strings are permutations of each other 

import sys

#includes an extra data structure
def Solution1(firstString, secondString):
	#if the strings are different length, they cannot be permutations 
	if(len(firstString) != len(secondString)):
		return False; 
	#Inserts both strings into dictionary and compares them. Takes O(n) time. 
	fStringDict = {}
	sStringDict = {}
	for firstLetter, secondLetter in zip(firstString, secondString):
		if(firstLetter in fStringDict):
			fStringDict[firstLetter] += 1 
		else:
			fStringDict[firstLetter] = 1 

		if(secondLetter in sStringDict):
			sStringDict[secondLetter] += 1
		else:
			sStringDict[secondLetter] = 1

	return fStringDict == sStringDict 

#does not include an extra data structure
def Solution2(firstString, secondString):
	if(len(firstString) != len(secondString)):
		return False; 

	#sorts both strings and compares them to see if they are equal. Takes O(nlogn) time. 
	sortedFirstString = ''.join(sorted(firstString))
	sortedSecondString = ''.join(sorted(secondString))

	return sortedFirstString == sortedSecondString

#Checks to make sure only two arguments were entered
if(len(sys.argv) > 3):
	print("That is too many arguments! Please enter in only two words")
elif(len(sys.argv) < 3):
	print("That is too few arguments! You need at least two words")
else:
	if(Solution1(sys.argv[1], sys.argv[2])):
		print("Using a dictionary, we find these are permutations! Solution takes O(n) time and O(n) space.")
	else:
		print("Using a dictionary, we know these are not permutations! Solutions take O(n) time and O(n) space.")

	if(Solution2(sys.argv[1], sys.argv[2])):
		print("Without using another data structure, we find these are permutations! Solution takes O(nlogn) time and O(1) space.")
	else:
		print("Without using another data structure, these are not permutations! Solution takes O(nlogn) time and O(1) space.")



