"""
Exception Handling and Unit Testing Lab

This lab covers:
1. Basic exception handling with try-except blocks
2. Raising exceptions
3. Creating custom exceptions
4. Writing unit tests with unittest module
"""

# ==================== Step 1: Simple Exception Handling ====================
#Basic exception handling for common error types

# Test cases for simple exception examples
def test_simple_exceptions():
    # ZeroDivisionError - occurs when dividing by zero
    try:
        res = 10 / 0  # This will raise ZeroDivisionError
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: Can't divide by zero!")
    
    # ValueError - occurs when operation receives wrong type of value
    try:
        float('z')  # Can't convert 'z' to float
    except ValueError:
        print("Caught ValueError: Invalid conversion to float")
    
    # IndexError - occurs when accessing non-existent index
    try:
        x = []
        print(x[2])  # No index 2 in empty list
    except IndexError:
        print("Caught IndexError: List index out of range")
    
    # TypeError - occurs when operation on wrong type
    # AttributeError - occurs when attribute doesn't exist
    try:
        a = 1
        print('a = ' + a)  # Can't concatenate str with int
        length(a)          # Undefined function
        a._x               # int has no _x attribute
    except (TypeError, NameError, AttributeError) as e:
        print(f"Caught {type(e).__name__}: {e}")

# ==================== Step 2: Catching Specific Exceptions ====================
# Shows how to handle different exception types separately

def dividefunction(x, y):
    """
    Division function with comprehensive exception handling
    - try: block contains code that might raise exceptions
    - except: handles specific exceptions
    - else: runs if no exceptions occur
    - finally: always runs regardless of exceptions
    """
    try:
        z = x/y  # Potential division operation that could fail
    except TypeError:
        print("Type Error: Cannot divide number by string")
    except ZeroDivisionError:
        print("Zero Division Error: Cannot divide by zero")
    except Exception as e:  # Catch-all for other exceptions
        print(f"Unknown Error: {e}")
    else:
        print(f"Division result: {z}")  # Only runs if try succeeds
    finally:
        print("Division operation attempted")  # Always runs

# Test cases for dividefunction
def test_dividefunction():
    print("\nTesting dividefunction:")
    dividefunction(10, 2)    # Successful division
    dividefunction(10, 0)    # ZeroDivisionError
    dividefunction(10, "a")  # TypeError
    dividefunction("10", 2)  # TypeError

# ==================== Step 3: Raising Exceptions ====================
# Demonstrates how to raise exceptions manually

def set_age(age):
    """
    Function that raises ValueError for invalid ages
    - raise: keyword to trigger exceptions
    - ValueError: built-in exception for invalid values
    """
    if age < 0:
        raise ValueError("Age cannot be negative.")  # Raise exception
    print(f"Age set to {age}")

# Test cases for set_age
def test_set_age():
    print("\nTesting set_age:")
    try:
        set_age(25)   # Valid age
        set_age(-5)   # Will raise ValueError
    except ValueError as e:
        print(f"Caught exception: {e}")

# ==================== Step 4: User Defined Exceptions ====================
# Shows how to create and use custom exceptions

class InvalidAgeError(Exception):
    """
    Custom exception class for age validation
    - Inherits from base Exception class
    - __init__: custom constructor with additional attributes
    - __str__: custom string representation
    """
    def __init__(self, age, msg="Age must be between 0 and 120", error_code=1001):
        self.age = age
        self.msg = msg
        self.error_code = error_code
        super().__init__(msg)  # Initialize base Exception
    
    def __str__(self):
        return f"[Error {self.error_code}] {self.age} -> {self.msg}"

def set_custom_age(age):
    """Function using custom exception"""
    if age < 0 or age > 120:
        raise InvalidAgeError(age)  # Raise custom exception
    print(f"Age set to: {age}")

# Test cases for custom exception
def test_custom_exception():
    print("\nTesting custom exception:")
    try:
        set_custom_age(25)    # Valid age
        set_custom_age(150)    # Raises InvalidAgeError
        set_custom_age(-10)    # Raises InvalidAgeError
    except InvalidAgeError as e:
        print(f"Caught custom exception: {e}")

# ==================== Step 5: Unit Testing Example ====================
# Basic unit test example without exception testing

def triangle(height):
    """
    Generates a triangle pattern of stars
    - range(): generates sequence of numbers
    - str +=: string concatenation
    """
    pattern = ''
    for i in range(1, height + 1):      # Outer loop for rows
        for j in range(i):              # Inner loop for stars
            pattern += "* "
        pattern += '\n'                 # Newline after each row
    return pattern

# ==================== Step 6: Unit Test with Exception Testing ====================
# Enhanced unit test that checks for raised exceptions

def triangle_with_validation(height):
    """
    Enhanced triangle function with input validation
    - type(): checks variable type
    - isinstance(): alternative for type checking
    - raise: raises exceptions for invalid input
    """
    pattern = ''
    if not isinstance(height, (int, float)):  # Check for numeric type
        raise TypeError("Height must be a number")
    if height < 0:                           # Check for positive value
        raise ValueError("Height cannot be negative")
    for i in range(1, int(height) + 1):      # Generate pattern
        pattern += "* " * i + '\n'
    return pattern

# ==================== Main Execution ====================
if __name__ == "__main__":
    # Run all test functions
    test_simple_exceptions()
    test_dividefunction()
    test_set_age()
    test_custom_exception()
    
    # Demo the triangle functions
    print("\nTriangle output (height=3):")
    print(triangle(3))
    
    print("\nTriangle with validation (height=4):")
    print(triangle_with_validation(4))
    
    # Test exception cases for triangle_with_validation
    try:
        print(triangle_with_validation(-2))  # Should raise ValueError
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    
    try:
        print(triangle_with_validation("three"))  # Should raise TypeError
    except TypeError as e:
        print(f"Caught TypeError: {e}")