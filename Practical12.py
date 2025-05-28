"""
Step 1: Basic Inheritance
Demonstrates how child classes inherit from parent classes using super()
"""
class Person:
    def __init__(self, name, idnumber):
        # __init__ is the constructor method called when object is created
        self.name = name  # self refers to the instance, name is an attribute
        self.idnumber = idnumber # Instance variable for ID number

    def display(self):
        # Simple method to display attributes
        print(self.name)
        print(self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  # Calls parent class construct 
        # super - allows us to call methods from the parent class
        # super() calls parent class's __init__()
        self.salary = salary # Additional attribute specific to Employ
        self.post = post

# Test Step 1
employee1 = Employee("Sonam", 22404, 60000, "student")
employee1.display()  # Calls inherited method from Person
print(employee1.salary)  # Access child class attribute


"""
Step 2: Data Abstraction
ABC module helps create abstract base classes that can't be instantiated directly
"""
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model, year):
        # Constructor for common car attributes
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod  # Decorator marks this as abstract - must be implemented by child classes
    def printDetails(self):
        pass
    
    def accelerate(self):  # Concrete method - has implementation
        print("Speed up ...")  

class Hatchback(Car):
    def printDetails(self):  # Implements abstract method
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Test Step 2
# car1 = Car("Toyota", "Prius", "2004")  # Will raise TypeError (abstract class)
hatch1 = Hatchback("Toyota", "Prius", "2004")
hatch1.printDetails()  # Calls implemented abstract method
hatch1.accelerate()  # Calls inherited concrete method
hatch1.sunroof()  # Calls child class method


"""
Step 3: Class Polymorphism (Runtime Polymorphism)
Method overriding allows different behavior in child classes
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self):
        print(self.name, " is studying Python.")

class HighSchoolStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age) # Calls parent constructor 
        self.grade = grade
    
    def study(self):  # Overrides parent class method
        print(self.name, " is studying Mathematics.")

# Test Step 3
Karma = Student("Karma", 25)
Karma.study()  # Calls parent class method

Sonam = HighSchoolStudent("Sonam L", 20, 12)
Sonam.study()  # Calls overridden child class method


"""
Step 4: Function Polymorphism
Built-in len() demonstrates polymorphism - works with different types
"""
# Test Step 4
print(len("Programiz"))  # Works with strings
print(len(["Python", "Java", "C"]))  # List item count - Works with lists
print(len({"Name": "John", "Address": "Nepal"}))  # Dictionary key count - Works with dictionary


"""
Step 5: Operator Polymorphism
Operator overloading by defining special methods (__add__ in this case)
"""
class complex:
    def __init__(self, a, b): # Complex number with real (a) and imaginary (b) parts
        self.a = a
        self.b = b
    
    def __add__(self, other):  # Overloads + operator - Defines behavior for + operator
        return self.a + other.a, self.b + other.b  # Adds corresponding components

# Test Step 5
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2  # Calls __add__ method
print(Ob3)  # Returns tuple (3, 5) - with component-wise sum



"""
Step 6: SOLID - Single Responsibility Principle
Each class has one responsibility
"""
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # Special method for string representation
        return f'Person(name={self.name})'

class PersonDB:
    def save(self, person):
        print(f'Save the {person} to database')

# Test Step 6
p = Person("John")
db = PersonDB()
db.save(p)  # Separate class handles database operations


"""
Step 7: SOLID - Open/Closed Principle
Open for extension, closed for modification using abstraction
"""
from abc import ABC, abstractmethod

class PersonStorage(ABC): # Abstract base class
    @abstractmethod
    def save(self, person):
        pass # Implementation in child classes

class PersonDB(PersonStorage):
    def save(self, person): # Database storage implementation
        print(f'Save the {person} to database')

class PersonJSON(PersonStorage):
    def save(self, person): # JSON storage implementation
        print(f'Save the {person} to JSON file')

# Test Step 7
p = Person("Jane")
db = PersonDB()
db.save(p)

json = PersonJSON()
json.save(p)


"""
Step 8: SOLID - Liskov Substitution Principle
Subclasses should be substitutable for their parent classes
"""
class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass # Abstract notification method

class Email(Notification):
    def __init__(self, email):
        self.email = email
    def notify(self, message):
        print(f'Send "{message}" to {self.email}')

class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone
    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')

class Contact:
    def __init__(self, name, email, phone): # Contact information container
        self.name = name
        self.email = email
        self.phone = phone

class NotificationManager:
    def __init__(self, notification): # Works with any Notification type
        self.notification = notification
    def send(self, message): # Delegates to the notification object
        self.notification.notify(message)

# Test Step 8
contact = Contact('John Doe', 'john.com', '1234567890')
sms_notification = SMS(contact.phone)
email_notification = Email(contact.email)

manager = NotificationManager(sms_notification)
manager.send('Hello John')  # Uses SMS notification

manager.notification = email_notification
manager.send('Hi John')  # Uses Email notification


"""
STEP 9: Interface Segregation Principle (ISP)
- Split interfaces to avoid forcing clients to implement unused methods
"""
class Movable(ABC):  # Base interface for moving objects
    @abstractmethod
    def go(self):  # Only requires movement capability
        pass

class Flyable(Movable):  # Extends Movable for flying objects
    @abstractmethod
    def fly(self):  # Adds flying capability
        pass 

class Aircraft(Flyable):  # Implements both interfaces
    def go(self):  # Ground movement implementation
        print("Taxiing")
    def fly(self):  # Flying implementation
        print("Flying")

class Car(Movable):  # Only needs ground movement
    def go(self):  # Implements only required method
        print("Going")

# Testing ISP:
plane = Aircraft()  # Can both go and fly
plane.go()  # Uses Movable interface
plane.fly()  # Uses Flyable interface

car = Car()  # Only needs to go
car.go()  # Correctly implements only Movable
# car.fly()  # Properly unavailable - follows ISP


"""
STEP 10: Dependency Inversion Principle (DIP)
- High-level modules depend on abstractions, not concrete implementations
"""
class CurrencyConverter(ABC):  # Abstract interface
    def convert(self, from_currency, to_currency, amount) -> float:
        pass  # Defines conversion contract

class FXConverter(CurrencyConverter):  # Concrete implementation 1
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Using FX API')  # Specific implementation
        print(f'{amount} {from_currency} = {amount * 1.15} {to_currency}')
        return amount * 1.15  # FX conversion rate

class AlphaConverter(CurrencyConverter):  # Concrete implementation 2
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Using Alpha API')  # Different implementation
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2  # Alpha conversion rate

class App:  # High-level module
    def __init__(self, converter: CurrencyConverter):  # Depends on abstraction
        self.converter = converter  # Works with any CurrencyConverter
    
    def start(self):
        self.converter.convert('EUR', 'USD', 100)  # Uses abstract interface

# Testing DIP:
converter = AlphaConverter()  # Can swap with FXConverter easily
app = App(converter)  # App depends on abstraction, not concrete class
app.start()  # Uses whichever converter was injected