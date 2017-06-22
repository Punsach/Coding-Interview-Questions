#Replace all spaces in a string with the string "%20"
import sys 

def URLify(someString, trueLength):
	#Create a version of the string without spaces at the end 
	originalString = someString[0:trueLength]
	someStringLen = len(someString)
	#Create index to iterate through the string 
	index = trueLength - 1
	#Convert to character array so we can manipulate it 
	someStringArray = list(someString)
	i = someStringLen - 1

	#Use a while loop to iterate through the character array from end to beginning. While 
	#loop makes it easier to manage our index 
	while(i > 0):
		#If there is a space, set the next three spots to the string %20
		if(originalString[index] == " "):
			someStringArray[i] = "0"
			someStringArray[i-1] = "2"
			someStringArray[i-2] = "%"
			i = i - 3
		#Otherwise, copy the original character
		else:
			someStringArray[i] = originalString[index]
			i = i - 1
		index -= 1

	return ''.join(someStringArray)

if(len(sys.argv) != 3):
	print("Incorrect number of inputs, please enter in two values!")
else:
	print("The modified string is: " + URLify(sys.argv[1],int(sys.argv[2])) + "." + "The solution took O(n) time and O(n) space")
	

	