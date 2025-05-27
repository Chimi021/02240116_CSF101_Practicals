# PYTHON OPRATORS

import random

a = random.randint(0,10)
b = random.randint(10,15)

print("1st Number =", a, "and", "2nd Number =", b)
# + Addition
print("Sum of 1st Number and 2nd Number is", a + b)
# - Subtraction
print("The difference of 1st Number and 2nd Number is", a - b)
# * Multiplication
print("Product of 1st Number and 2nd Number is", a * b)
# / Division (returns float - decimal points included )
print("Division of 1st Number by 2nd Number is", a / b)
# // Floor division (returns integer - excldes decimal ponints)
print("Floor division of 1st Number by 2nd Number is", a // b)
# % Modulus (returns only the remainder)
print("Remainder when 1st Number is divided by 2nd Number is", a % b)
# ** Exponentiation
print("1st Number raised to the power of 2nd Number is", a ** b)

# Comparison operators
# < Less than
print("Is 1st Number less than 2nd Number?", a < b)
# > Greater than
print("Is 1st Number greater than 2nd Number?", a > b)
# <= Less than or equal to
print("Is 1st Number less than or equal to 2nd Number?", a <= b)
# >= Greater than or equal to
print("Is 1st Number greater than or equal to 2nd Number?", a >= b)
# == Equal to
print("Are the numbers equal?", a == b)
# != Not equal to
print("Are the numbers not equal?", a != b)

# Assignment operator (= was used earlier to assign values)
a += b  # Equivalent to a = a + b
print("After a += b, a is now", a)

# Bitwise operators (work on binary representation) # Self note - does not seem that important
x, y = 10, 4
print(f"\nBitwise operators (using x={x}, y={y}):")
# & Bitwise AND
print("x & y =", x & y)
# | Bitwise OR
print("x | y =", x | y)
# ^ Bitwise XOR
print("x ^ y =", x ^ y)
# ~ Bitwise NOT
print("~x =", ~x)
# << Left shift
print("x << 1 =", x << 1)
# >> Right shift
print("x >> 1 =", x >> 1) 

# Logical operators
print("\nLogical operators:")
# and - True if both operands are true
print("a > 0 and b > 10:", a > 0 and b > 10)
# or - True if at least one operand is true
print("a > 10 or b > 10:", a > 10 or b > 10)
# not - Inverts the boolean value
print("not(a > 10):", not(a > 10))

# Identity operators
print("\nIdentity operators:")
# is - True if both variables point to same object
print("a is b:", a is b)
# is not - True if both variables are not the same object
print("a is not b:", a is not b)

# Membership operators
list_example = [1, 2, 3, 4, 5]
print("\nMembership operators (using list [1,2,3,4,5]):")
# in - True if value is found in sequence
print("3 in list_example:", 3 in list_example)
# not in - True if value is not found in sequence
print("6 not in list_example:", 6 not in list_example)



# IF - ELSE STATEMENTS

if a == b:
    print ("1st Number and 2nd Number are equal")
elif a > b:
    print ("1nd Number is greater")
else:
    print ("2nd Number is greater")


# MATCH CASAE STATEMENTS
def temperature_analyzer():
    temperature = float(input("Enter Temperature:")) # in Celsius
    
    match temperature:
        case temp if temp <= 0:
            # Sub-zero temperatures
            print("Freezing!  Wear heavy winter gear.")
        case temp if 1 <= temp <= 10:
            # Cold weather range
            print("Chilly!  Jacket and gloves recommended.")
        case temp if 11 <= temp <= 20:
            # Cool weather range
            print("Moderate.  Light jacket weather.")
        case temp if 21 <= temp <= 30:
            # Comfortable range
            print("Pleasant!  Perfect for outdoor activities.")
        case temp if 31 <= temp <= 40:
            # Warm range
            print("Hot! Stay hydrated and seek shade.")
        case temp if temp > 40:
            # Extreme heat
            print("Dangerously hot! Avoid outdoor exposure.")
        case _:
            # Fallback for unexpected values (though our ranges cover all numbers)
            print("Invalid temperature reading")

# Execute the function
temperature_analyzer()


# WHILE LOOPS
# Simple countdown program using while loop

def countdown():
    count = 5 # Initialize counter
    
    # While loop runs as long as condition is True
    while count > 0:  # Condition checked before each iteration
        print(f"Count: {count}")
        count -= 1  # Decrement counter - crucial to avoid infinite loop
    
    # Loop exits when count becomes 0
    print("Blast off!")

# Call the function
countdown()