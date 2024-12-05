# Advanced OOP

"""
    1. Special methods, also called magic or dunder methods (__repr__ & __str__)
    2. Class methods (@classmethod)
    3. Static methods (@staticmethod)
"""


# Special Methods __repr__ & __str__

"""
    Special methods (also called 'magic methods') allow your objects to interact seamlessly with Python's 
    built-in functions and operators. These methods are essential for making your classes work well with 
    debugging, printing, and other operations.
    
        -__repr__: Returns a precise string representation meant for developers, typically used for debugging.
        -__str__: Returns a readable string meant for end users, often when pringing an object.
"""

""" EXAMPLE: E-commerce Product Class"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"
        
    def __str__(self):
        return f"{self.name}: ${self.price} (Quantity: {self.quantity})"
    
# Developer view (using __repr__):
p = Product("Laptop", 999.99, 5)
print(repr(p))                                                      # Output: Product(name='Laptop', price=999.99, quantity=5)

# User view (using __str__)
print(p)                                                            # Output: Laptop: $999.99 (Quantity: 5)

"""
    In this example:
        - __repr__ gives a detailed description that includes all necessary information for debugging.
        - __str__ outputs a cleaner version that's appropriate for displaying to end users.
"""


# Class Methods: Managing Class_Level Behavior

"""
    Class methods are designed to work at the class level rather than the instance level. These methods can modify class attributes, 
    create alternative constructors, or manage shared data that applies to all instances of the class.
"""

""" EXAMPLE: Managing a Fleet of Cars"""

class Car:
    total cars = 0                                                  # Class attribute to track the number of cars
    
    def __init__(self, model, year):
        self.model = model
        self.year = year
        Car.total_cars += 1                                         # Increment class-level counter when a car is created
        
    @classmethod
    def from_csv(cls, csv_data):
        model, year = csv_data.split(',')                           # Alternative constructor to create cars from CSV-like data
        return cls(model,int(year))
    
    @classmethod
    def total_produced(cls):
        return cls.total_cars
    
# Creating instances the regular way
car1 = Car('Toyota Corolla', 2020)
           
# Creating an instance using class method
car2 = Car.from_csv('Honda Accord,2018')

print(Car.total_produced())                                         # Output: 2

"""
    -The from_csv class methdo allows for an alternative wat to create a Car object from a string.
    -The total_produced class method provides a way to retrieve the total number of Car instances created.
"""

# Static Methods: Utility Functions within Classes

"""
    Static methods are used when you need a method that velings to a class logically but doesn't need to access
    class or instance data. They are good for utility functions that can logically belong to a class but don't
    modify class or instance variables.
"""

""" EXAMPLE: Utility Method for Temperature Conversion"""

class WeatherStation:
    
    def __init__(self, location, temperature_f):
        self.location = location
        self.temperature_f = temperature_f
        
    def __repr__(self):
        return f"WeatherStation(location={self.location}, temperature_f={self.temperature_f})"
    
    @staticmethod
    def fahrenheit_to_celcius(f_temp):
        return (f_temp - 32) * 5.0/9.0
    
    @staticmethod
    def celcius_to_fahrenheit(c_temp):
        return (c_temp * 9.0/5.0) + 32
    
# Usage of static methods:
temp_f = 77
temp_c = WeatherStation.fahrenheit_to_celcius(temp_f)
print(f"{temp_f}F is {temp_c:2f}C")                                 # Output: 77F is 25.00C

temp_back_f = WeatherStation.celcius_to_fahrenheit(temp_c)
print(f"{temp_c:2f}C is {temp_back_f:2f}F")                         # Output: 25.00 is 77.00F

"""
    Static methods allow the conversion between Fahrenheit and Celsius, a task that doesn't require any access to the specific
    instance of the WeatherStation class.
"""

"""
    Conclusion
        -Special methods (__repr__, __str__): Enhance how objects behave with built-in functions and allow better control over 
        debugging and user output.
        -Class methods: Provide shared behavior across the class, helping you manage class-level data or provide alternative 
        ways to instantiate objects. 
        -Static methods: Useful for utility functions that don't need access to class or instance data but logically belong to 
        the class.
"""