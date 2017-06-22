import sys 

#Determine if two strings are one edit away from each other

def oneAway(stringOne, stringTwo):
	#Set the variables 
	counter = 0
	indexOne = 0
	indexTwo = 0 
	length = 0 
	longerString = ""
	shorterString = ""
	diffLength = False

	#Equal strings are not one edit away 
	if(stringOne == stringTwo):
		return False 

	#If the length differs by more than one, they cannot be one edit away 
	if(len(stringOne) - len(stringTwo) > 1 or len(stringOne) - len(stringTwo) < -1):
		return False

	#Determine which string is shorter and which is longer and whether or not they have different lengths 
	if(len(stringOne) > len(stringTwo)):
		length = len(stringOne)
		longerString = stringOne
		shorterString = stringTwo
		diffLength = True
	elif(len(stringOne) < len(stringTwo)):
		length = len(stringTwo)
		longerString = stringTwo
		shorterString = stringOne
		diffLength = True
	else:
		diffLength = False 
		length = len(stringOne)
		longerString = stringOne
		shorterString = stringTwo

	#Iterate through the strings and count the number of different characters
	for indexOne in range(0, length):
		if(counter > 1):
			return False
		elif(longerString[indexOne] != shorterString[indexTwo]):
			counter += 1
			if(len(stringOne) == len(stringTwo)):
				indexTwo += 1
		else:
			indexTwo += 1

	#If the number of different characters is more than one, return false 
	if(counter <= 1):
		return True
	else:
		return False; 
if(len(sys.argv) > 3):
	print("Please enter the proper number of strings")
elif(oneAway(sys.argv[1], sys.argv[2])):
	print("These strings are one edit away! The solution takes O(n) time and O(n) space.")
else:
	print("These strings are not one edit away! The solution takes O(n) time and O(n) space.")


