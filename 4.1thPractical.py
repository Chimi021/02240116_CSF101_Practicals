
# Array methodes(append, pop,insert, remove) (python list methode)
# Array methods

# 	• Append will add from back not front.
# 	• Pop - removes the element with the highest index
	
blackpink = ['Jennie', 'Lisa', 'Jisoo', 'Rose']
blackpink.pop(1)
print (blackpink)
# Result ………
# ['Jennie', 'Jisoo', 'Rose']
	
# • .insert - puts an element to any specified index
	
blackpink = ['Jennie', 'Lisa', 'Jisoo', 'Rose']
blackpink.insert(1, 'J')
print (blackpink)
	# • Result….. 
    # ['Jennie', 'J', 'Lisa', 'Jisoo', 'Rose']
	# • Remove - will only remove the first … lil doubt

# Stack & Queue 
# Stack	FILO
# Implementation of array	
blackpink = ['Jennie', 'Lisa', 'Jisoo', 'Rose']
new_stack = []
array_len = len(blackpink)
for index in range (array_len):
	temporary = blackpink.pop()
	new_stack.append(temporary)
print(blackpink)
print(new_stack)
	
	# …………………..
	# []
	# ['Rose', 'Jisoo', 'Lisa', 'Jennie']
	

# Queue	FIFO
	
	# Array methodes(append, pop,insert, remove) (python list methode)
blackpink = ['Jennie', 'Lisa', 'Jisoo', 'Rose']
new_stack = []
array_len = len(blackpink)
for index in range (array_len):
	temporary = blackpink.pop(0) # because of the (0) , when thie is no 0 the loop will append the last index first pop the first element
	new_stack.append(temporary)
print(blackpink)
print(new_stack)
	#  ……………………….
	# []
	# ['Jennie', 'Lisa', 'Jisoo', 'Rose']


# Sets
# -can only have unique elements inside

 # data structure..
 # advantage - 
 # can only have one copy of it
 # can add

# Tuple 
# 	- Used when we want something to be the same through out the code
# 	-  cannot change inside once in it 
# 	- Like an array with less things to it but
# 	- Is immutable 
# 	- Can be indexed(called one by one)
# 	- Has no append, sort, ..
