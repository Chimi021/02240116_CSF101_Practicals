# Array methodes(append, pop,insert, remove) (python list methode)
# Array methods:
# 	• Append will add from back not front.
#     Pop - removes the element with the highest index

blackpink = ['Jennie', 'Lisa', 'Jisoo', 'Rose']
new_stack = []
array_len = len(blackpink)

for index in range (array_len):
    temporary = blackpink.pop(0) # because of the (0) , when thie is no 0 the loop will append the last index first pop the first element
    new_stack.append(temporary)
#print(blackpink)
#print(new_stack)

#CLASS EXERCISE Thu-13-3-15
list1 = [1,2,3,4,5,6,7,8,9,10]
inverse = []
list1_length = len(list1)
for i in range (list1_length):
    x = list1.pop()
    inverse.append(x)
#print(inverse)

inverse_list = [9,8,7,6,5,4,3,2,1,0]
# 

index = 0
while index > list1_length:#decrement logic
    list1.append(list1(pop))
#print(inverse_list)

#if we cannot use pop
index = len(list1) - 1 #

while index >= 0:
    inverse_list.append(-1)
    index -= 1 #decreases 9,8,7,6,5,4,3,2,1,0  += . incrementing same as index = index + 1
#print(inverse_list)

#DEFINING FUNCTIONS
#def my_function(argument:datatype, argument2:datatype) -> datatype:
def my_function(argument:int, argument2:int) -> int:
    product = argument * argument2
    return product
#calling the function
x = 2
y = 12213
result = my_function(x,y)
#print(result)

##Question 1 - define a function named squae function.... 2) take two arguments as input and return the square of the two input arguments

def square_function (length:int) -> int:
    product = length**2
    return product
l = int(input("Length:"))
#print(square_function(l))

 #SETS {} uses squegly brackets
 # datastructure.. is a dictionary
 # advantage - 
 # can only have one copy of it
 # can add#

 #if questions ask to find how many dublicate are there in an array
array = [11,12,13,14,15,13,17,11,19]
sampleset = set(array)
diff = len(array)-len(sampleset)
print("there are",diff," ")

 #TUPLE
 # Used when we want something to be the same through out the code
 #  cannot change inside once in it 
 #Like an array with less things to it but
 # 
 #  #
