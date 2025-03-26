

# Variable : 
# Data Structure : fixed size can only store one data type

# lists & array
# Array :defined size (c++)
# Can store multiple data types 
# List : same as array but not fixed size

# (NT IN MOdule)Linked list - an array with elements that know what comes after it.

# Inbuilt functions 
# Sth that comes with python by default (Default features)
# Eg. 
# 	•  print (a.len()) - checks the total number of elements in an array
# 	• .count - 
# 	• .find
# 	• .push - 
# 	• Append- add things to an array (BUT, )
# Append and push can make changes in the array
# 	• Lower and upper -  

# INDEX - Excessing things from inside an array . (Just that the first index of the elements starts with zero)

# Print - only prints does not save , usually just the way of checking things.
# Len - 
# Only by assigining things can we save the value
#EXAMPLE
newArray = ["Puppies" , 2 , True , None , 1.5 ]
firstArrayLen = len(newArray)
newArray.append ("Sunflowers")
print (len(newArray))
secondArrayLen = len(newArray)
print (firstArrayLen - secondArrayLen)

# Ø When we have to do something repeatedly= loops
# Ø FOR AND WHILE LOOPS
# ……………………..
# The value of for loop always starts from ZERO and go until one less than the maximum value

newArray = ["Puppies" , 2 , True , None , 1.5 ]
arraylen = len(newArray)
# For Loop - to excess all elements in an array
for index in range (arraylen):
    print(newArray[index])

# Ø While loop - it will keep on running until the condition is true
# ' ' - because pythons way of telling that it’s a string

sampleArray = ["ECE","ICE","EE","SWE","IT","WE","ME","CE","EG","A"]
arraylen = len(sampleArray)
newArray = []
for index in range (arraylen):
    allElement = sampleArray[index]
    newArray.append (allElement.lower())

for secondIndex in range (len(newArray)):
    print (newArray[secondIndex])


