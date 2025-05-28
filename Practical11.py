"""
Practical 11: Object Oriented Programming Basic Class Exercises
"""

# Step 1: Basic Person Class
class Person:
    # __init__ is the constructor method that gets called when creating a new instance
    # 'self' refers to the instance being created
    def __init__(self, name, age):
        self.name = name  # public attribute
        self.age = age    # public attribute

# Test Step 1
p1 = Person("Johnson", 36)
print(p1)  # Output: <__main__.Person object at 0x...> - default string representation

# Step 2: Adding Instance Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method - can access and modify instance attributes
    def hello(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")

# Test Step 2
p1 = Person("Johnson", 36)
p1.hello()  # Calls the instance method

# Step 3: Adding __str__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")

    # __str__ is a special method that returns a string representation of the object
    # Called by print(), str() and format() functions
    def __str__(self):
        return f"{self.name}({self.age})"

# Test Step 3
p1 = Person("Johnson", 36)
print(p1)  # Now uses our __str__ method: "Johnson(36)"

# Step 4: Implementing protected variable with getter/setter
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Single underscore indicates protected variable

    def hello(self):
        print(f"Hello my name is {self.name} and my age is {self._age}")

    # @property decorator creates a getter method
    # Allows us to access with instance.age instead of instance._age
    @property
    def age(self):
        return self._age

    # @age.setter creates a setter method
    # Allows us to set with instance.age = value
    @age.setter
    def age(self, newAge):
        self._age = newAge

    def __str__(self):
        return f"{self.name}({self.age})"  # Note: uses the property getter

# Test Step 4
p1 = Person("Johnson", 36)
print(p1.age)     # Uses getter: 36
p1.age = 20       # Uses setter
print(p1)         # "Johnson(20)"
print(p1._age)    # Still accessible directly (Python doesn't enforce protected)

# Step 5: Implementing a subclass
class Dancer(Person):
    def __init__(self, name, age, genre):
        # super() calls the parent class's __init__ method
        super().__init__(name, age)
        self.genre = genre  # New attribute specific to Dancer

    # New method specific to Dancer
    def dance(self):
        print(f"Hello my name is {self.name} and my favorite dance is {self.genre}")

    # Overriding the parent's __str__ method
    def __str__(self):
        return f"{self.name}({self.age}) does {self.genre}"

# Test Step 5
d1 = Dancer("Johnson", 36, "chachacha")
print(d1)          # Uses Dancer's __str__: "Johnson(36) does chachacha"
d1.hello()         # Inherited from Person
d1.dance()         # Dancer-specific method
print(d1.age)      # Inherited property getter
d1.age = 40        # Inherited property setter
print(d1)          # "Johnson(40) does chachacha"

# Step 6: Public, Protected, Private Variables
class MyClass:
    def __init__(self, name, age, salary):
        self.name = name    # Public variable - accessible anywhere
        self._age = age     # Protected variable - convention says "don't access directly"
        self.__salary = salary  # Private variable - name mangling makes it harder to access

    # Method to access private variable
    def display_salary(self):
        print(f"Salary: {self.__salary}")

# Test Step 6
obj = MyClass("Johnson", 30, 50000)
print(obj.name)        # Public - works fine: "Johnson"
print(obj._age)        # Protected - works but shouldn't be accessed directly: 30
obj.display_salary()   # Accessing private through method: "Salary: 50000"

try:
    print(obj.__salary)  # This will raise AttributeError
except AttributeError as e:
    print(f"Expected error accessing __salary: {e}")

# Name mangling demonstration - private vars can still be accessed with _ClassName prefix
print(f"Access through name mangling: {obj._MyClass__salary}")  # Not recommended!

# Step 7: Class Method vs Static Method
class Calculator:
    @classmethod
    # cls refers to the class (Calculator), not the instance
    # Can access class attributes but not instance attributes
    def add(cls, num1, num2):
        return num1 + num2
    
    @staticmethod
    # No cls or self parameter - just a function inside the class namespace
    # Can't access class or instance attributes
    def multiply(num1, num2):
        return num1 * num2

# Test Step 7
# Can call without creating an instance
print(Calculator.add(2, 3))        # 5
print(Calculator.multiply(2, 3))   # 6

# Also works with instances
calc = Calculator()
print(calc.add(5, 7))             # 12
print(calc.multiply(5, 7))        # 35