# OBJECT -OREINTED PROGRAMMING (OOP)

# Key Concepts of OOP:
""" 
    1. Classes and Objects:
        - Class: A blueprint or template that defines the attributes and methods that the objects created from it will have.
        - Object: An instance of a class, representing a specific entity with its own unique data. Multiple objects can be created
            from the same class.
    2. Attributes and Methods:
        - Attributes: Characteristics or properties of an object (e.g., color, size, name).
        - Methods: Actions or behaviors that an object can perform (e.g., drive, speak, calculate).
    3. The Four Pillars of OOP:
        - Encapsulation: Bundling data and methods that operate on that data within a single unit (class). It also involves direct
            access to some of the object's components for data protection.
            (Wrapping up your data)
        - Abstraction: Hiding complex implementation details and exposing only the necessary functionality to the user.
            (Showing only essential features)
        - Inheritance: Creating new classes from exising ones, allowing code reuse and the extension of functionalities.
            (Like inheriting something from your parents)
        - Polymorphism: The ability to use a single interface or method to represent different underlying forms 
            (e.g., different objects can have a method with the same name but behave differently).
            (An object can have many different forms, kind of like cloning)
"""

# Why Use OOP?
""" 
    1. Modularity: OOP allows for better organization of code by breaking it down into (reusable) pieces (classes and objects).
    2. Reuse: Once we build a class, we can  reuse it to create multiple obejcts, reducing redundancy.
    3. Scalability: Reusing code enables us to scale applications more efficiently.
    4. Maintenance: OOP makes it easier to update specific instances of an object rather than modifying the entire catalog
        if data, or the entire codebas.
"""


# Classes & Objects

"""
    Classes: The blueprint that outlines the attributes and functionality of an object.
        -Look at strings, dictionaries, lists. These are all classes in Python with their own methods and attributes.
    Objects: Unique instances of a class, created based on the blueprint.

    WE'VE BEEN WORKING WITH CLASSES AND OBJECTS THIS ENTIRE TIME!!!
"""

str1 = str()
list1 = list()
dictionary1 = dict()

print(type(str1))
print(type(list1))
print(type(dictionary1))

"""
    Python naming convention: Classes we make ourselves are always created in title case.
"""

class Car:                              # Note that "Car" is in title case
    pass

my_car = Car()
print(type(my_car))   


# Attributes

"""
    Attributes define the qualities of our objects and are stored in variables within a class.
        - Class Attributes: Shared by all instances of the class. They are defined directly within the class body,
            outside of any methods.
        - Instance Attributes: Attributes that may vary between different instances. They are defined within a special method
            called '__init__()', which is used to initialize the object when it is created.
"""

class Car:  
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
        
car1 = Car('Toyota', 'Corolla')
car2 = Car('Honda', 'Civic')

print(car1.wheels)
print(car1.make)
print(car2.model)

""" In this example, the 'wheels' attribute is a vlass attribute, and the 'make' and 'model' attributes are instance attributes:
    -This means every instance of the 'Car' class will have the same value for 'wheels'. All 'Car' objects will share this attribute.
    -'self.make' and 'self.model' store the values specific to each instance of the 'Car' class. These attributes can vary
        from one object to another.
    When we create 'car1' and 'car2', each instance has its own unique 'make' and 'model', but both share the same 'wheels' attribute.

    Accessing the Attributes:
    -When we access 'car1.wheels', we get 4 becuase 'wheels' is a class attribute share by all instances.
    -'car1.make' outputs 'Toyota' becuase it's an instance attribute unique to 'car1'.
    -'car2.model' outputs 'Civic' because it's an instance attribute unique to 'car2'.
"""


# Understanding the '__init__' Method

"""
    The '__init__' method is a special method in Python used to initialize new objects when they're created. It is our
    class constructore, responsible for adding attributes to an object when creating a new instance of a class.
    This is what allows us to initialize individual instances of a class with unique data (attributes) for each object.
"""

# Syntax of the __init__ Method

"""
    The __init__ method is defined inside of a callas with the following syntax:

EXAMPLE

def __init__(self, parameter1, parameter2, ...)         # Initialization code

    self.attribute1 = parameter1
    self.attribute2 = parameter2
    ...

    Key Points:
        1. The 'self' Parameter:
            -The first paramete of the __init__ method is always 'self', which is a reference to the current instance of the class.
            -It is used to access and assign values to the instance's attributes. The name 'self' is a convention, not a keyword,
            but it should always be used to maintain consistency.
        2. Additional Parameters:
            -The __init__ method can take additional parameters after 'self', which are used to initialize the instance attributes.
            -When creating an object, these parameters are passed to the class to set up the inital state of the object.
        3. Creating Instance Attributes:
            -Inside the __init__ method, instance attributes are created using 'self.attribute_name = value'.
            -These attributes are then unique to each instance and define the state of the object.
"""


# How the __init__ Method is Used

"""
    When you create a new instance of a class, the __init__ method is automatically called. This allows you to pass arguments to
    the class, which are then used to initialize the object's attributes.

EXAMPLE

class Car:
    def __init__(self, make, model, year):
        # Instance Attributes
        self.make = make                    #The make of the car (e.g., 'Toyota')
        self.model = model                  #The model of the car (e.g., 'Corolla')
        self.year = year                    #The year of manufacture (e.g., 2020)
        
# Creating instances of the 'Car' class
car1 = Car('Toyota', 'Corolla', 2020)
car2 = Car('Honda', 'Civic', 2018)

# Accessing the instance attributes
print(car1.make)                            #Output: Toyota
print(car1.model)                           #Output: Corolla
print(car1.year)                            #Output: 2020

print(car2.make)                            #Output: Honda
print(car2.model)                           #Output: Civic
print(car2.year)                            #Output: 2018
"""

# Example Breakdown

"""
    1. Defining the Class and __init__ method:
        -The 'Car' class is defined with an __init__ method that takes 'make', 'model', and 'year' as parameters.
        -Inside the __init__method, the instance attributes 'self.make', 'self.model', and 'self.year' are initialized
            with the provided values.
    2. Creating Objects ('car1' and 'car2'):
        -When car1 = Car('Toyota', 'Corolla', 2020) is executed, the __init__ method is called with 'self' referencing
            the new 'car1' object, 'make' set to 'Toyota', 'model' set to 'Corolla', and 'year' set to '2020'.
        -The same happens for 'car2', but with different attribute values.
    3. Accessing Attributes:
        -After the objects are created, we can access their attributes using dot notation (e.g., 'car1.make'), showing
            the individual state of each object.
"""


# Why is __init__ Method Important?

"""
    Initialization: It allows setting the initial state of an object when it is created.
    Flexibility: You can create objects with different initial values, which makes the class reusable in different scenarios.
    Encapsulation: It keeps the internal state of the object separate and provides a controlled way to initialize it.
    
    # IMPORTANT NOTES
        - The __init__ method does not return anything. In fact, it returns 'None' by default.
        - It is not requried to have an __init__ method in every class, but without it, you won't be able to initialize
            instance attributes when creating objects.
            
EXAMPLE - Using default values

class Car:
    def __init__(self, make, model, year=2021):
        self.make = make
        self.model = model
        self.year = year

car1 = Car('Toyota', 'Corolla')
car2 = Car('Honda', 'Civic', 2018)

print(car1.year)                    #Output: 2021 (default value used)
print(car2.year)                    #Output: 2018 (provided value used)

In this example, if the 'year' is not specified when an object is created from this class, it defaults to '2021'.
"""            


# Understading Methods in Python Classes

""" 
    How are Methods Different from Regular Functions?
    -Location: Methods are defined insides a class, while regular functions can be defined anywhere in the code.
    -Usage of 'self': Methods have a special first parameter called 'self', which refers to the instance of the 
        class calling the method. Regular functions do not have this requirement.
    -Access to Instanced Data: Methods can access and modify the attributes of the object that calls them, while
        regular runctions do not have access to an objects data unless explicitly passed..
"""
        

# Focusing on Instance Methods

""" Instance methods are the most common type of methods in Python classes. They operate on an instance of the class,
    allowing objects to perform actions or interact with their own data(attributes). When we talk about"methods" in the context
    of Object-Oriented Programming, we are usually referring to instance methods.
    
    Key Characteristics of Instance Methods
        1. Defined within a class: Instance nethods are defined inside a class and typically operate on the data contained
        within that instance.
        2. First Parameter is 'self'" The first parameter for an instance method is always 'se;f', which refers to the instance 
        of the class calling the methog. This allows the methos to access and modify the object's attributes.
        3. Accessing and Modifying Attributes: Instance methods can read and chance the values of the instance's attributes, 
        making them suitable for defining behaviors or operations specific to each object. 

EXAMPLE of an Instance Method

class Car:
    def __init__(self, make, model, mileage=0)
        #Instance attributes
        self.make = make
        self.model = model
        self.mileage = mileage
        
    #Instance method to display care information
    def display_info(self):
        return f"{self.make} {self.model}, Mileage: {self.mileage} miles"
    
    #Instance method to update the mileage
    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} miles. Total mileage is now {self.mileage} miles."
        
#Creating an instance of the Car class
my_car = Car('Toyota', 'Corolla', 10000)

#Calling instance methods
print(my_car.display_info())                #Output: Toyota Corolla, Mileage: 10000 miles
print(my_car.drive(150))                    #Output: Drove 150 miles. Total mileage is now 10150 miles

EXAMPLE BREAKDOWN
    1. Defining the Class and Attributes:
        - The Car class has an __init__ method that initializes three instance attributes: 'make', 'model', and 'mileage'.
        - When 'my_car' is created, it gets its own 'make', 'model', and 'mileage' values.
    2. Instance Methods ('display_info' and 'drive'):
        -'display_info': This instance method returns a string with the car's information. It uses 'self' to access the instance's 
            attributes ('self.make', 'self.model', 'self.mileage').
        -'drive': This instance method increases the 'mileage' attribute by the number of miles passed as an argument. It modifies 
            the state of the 'my_car' object by updating 'self.mileage'.
    3. Calling Instance Methods:
        -When 'my_car.display_info()' is called, it returns a formatted string with the car's details.
        =When 'my_car.drive(150)' is called, it increments the mileage by 150.
"""

# Exercise 6.1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):                                        # Method to greet the person
        return f"Hello, my name is {self.name}!"
    
    def have_birthday(self):                                # Method to simulate a birthday       
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old."
    
person1 = Person("Alice", 25)                               # Creating an instance of a person

print(person1.greet())                                      # Output: Hellp, my name is Alice!
print(person1.have_birthday())                              # Output: Happy Birthday! You are now 26 years old.


