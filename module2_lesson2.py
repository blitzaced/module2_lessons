# Tuples

""" What is a Tuple?
    - A tuple is an ordered collection of elements (or items) that are enclosed in parentheses () and separated by
        commas. Tuples can store elements of different data types: integers, strings, floats, or even other tuples!"""

my_tuple = (1, 2, 3)
print(my_tuple)     # Output: (1, 2, 3)

"""Tuple Characteristics:
    -Ordered:           the items in a tuple are indeced starting from 0.
    -Immutable:         you cannot change, add, or remove elements once the tuple is created.
    -Heterogeneous:     you can mix differen data types in the same tuple."""
    
"""Why Use Tuples?
    -Faster:            since tuples are immutable, they are generally faster than lists when it comes to iteration or 
     access.
    -Data Integrity:    if you have a collection of data that shouldn't be changed, use a tuple to ensure that it remains
     constant.
    -Dictionary Keys:   tuples can be used as keys in dictionaries becuase the are immutable, while lists cannot."""
    

# Creating a Tuple

"""Using parentheses () : The most coomon wat to create a tuple is by placing your values inside parentheses
    and separating them with commas"""
    
tuple1 = (10, "Python", and 3.14)
    
"""Without parentheses (tiple packing): Python allows you to create tuples without explicitly using parenthese.
    this is known as tuple packing:"""
    
tuple2 = 10, "Python", 3.14     # In this case 10, "Python", and 3.14 are packed into a tuple atuomatically.
    
   """Single-element tuples (important!): To create a tuple with just one element, add a comma after the element.
    Without the comma, Python will treat the value as a regular variable, not a tuple:"""
    
single_element_tuple = (5,)
print(type(single_element_tuple))   # Output: <class 'tuple'>
    
"""Empty tuples: You can create an empty tuple by using parenthese:"""
   
empty_tuple = ()
    
"""Using the tuple() constructor: You can convert other iterable data types (like lists or strings) into tuples using the 
    tuple() constructor:"""
    
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)     # Output: (1, 2, 3)

# Tuple Manipulation

""" You can access tuple elements by using their index, just like in a list. Idenxing starts from 0:"""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])      # output: "apple"
print(my_tuple[1])      # Output: "banana"

"""Slicing Tuples - you can retrieve multiple elements by using slicing, the same way as with a list:"""

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])          # Output: (2, 3, 4)


"""Looping over Tuples - you can lop over tuples the same way you wouild iterate over items in a list:"""

my_tuple = (1, 2, 3, 4, 5)

for num in my_tuple:
    print(num)              # Output: Python returns all the elements in the tuple, just as it would for a list
    
# Tuple Immutability
"""Since tuples are immutable, tryi8ng to modify their elements directly will raise an error:
my_tuple = (10, 20, 30)
my_tuple[1] = 40     #Error! Tuples cannot be changed

However, you can reassign the entire tuple:
my_tuple = (10, 20, 30)
my_tuple = (40, 50, 60)     #This works, since we're creating a new tuple"""



# Exercise 2.1
my_tuple = (42, "hello", 3.14, True)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
"""my_tuple[1] = "world"   # This would raise an error since tuples are immutable"""


# Packing and Unpacking Tuples

"""Packing is when you take multiple values and group them together into a tuple. 
You can do this by separating the values with commas, either with or without parentheses."""

person_info = "Alice", 30, "Developer"
print(person_info)      # Output: ("Alice", 30, "Developer")


"""Unpacking is the reverse of packing. It's when you take a tuple and assign its values to individual variables.
   The number of variable must match the number of elements in the tuple."""

person_info = "Alice", 30, "Developer"
name, age, profession = person_info
print(name)
print(age)
print(profession)
"""This technique is very useful when dealing with structured data such as coordinates, database records,
   or function return values."""


"""Somtimes, you may want to unpack only a portion of the tuple and store the rest in abother variable.
   You can achieve thisu sing the '*' operator, which allows for extended unpacking."""
   
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(first)                # Output: 1
print(rest)                 # Output: [2, 3, 4, 5]

"""You can also capture values from the and of the tuple:"""

numbers = (1, 2, 3, 4, 5)
*start, last = numbers
print(start)                # Output: [1, 2, 3, 4]
print(last)                 # Output: 5


"""Ignoring Values with Underscore (_)  - When unpacking, if you're not interested in one or more values,
   you can use an underscore '_' as a plaveholder to ignore those values."""

person_info = ("Eve", 35, "Artist", "New York")
name, _, profession, _ = person_info       # This ignores age and location
print(name)             #Output: Eve
print(profession)       #Output: Artist


# Tuple Packing and Unpacking in Functions
"""Tuple packing and unpacking are very useful when working with functions, expecially for returning
   and passing multiple values."""

"""Returning Multuple Values - A function can return multuiple values, packed into a tuple: """

def get_user_info():
    return "Bob", 29, "Engineer"

name, age, profession = get_user_info()     #Unpacking the returned tuple
print(name)                                 #output: Bob


"""Passing Multiple Values with Unpacking - You can pass multiple values to a function by unpacking
   a tuple into arguments:"""

def display_info(name, age, profession):
    print(f"{name} is {age} years old and works as a {profession}.")

info_tuple = ("Charlie", 28, "Designer")
display_info(*info_tuple)


# Tuple Methods
"""Although tuples are immutable, there are a few useful methods you can use with them:
        - .count(): Returns the number of times a specified value appears in the tuple."""

my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))                # Output: 3

"""- .index(): Returns the index of the first occurence of a specified value."""

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))                # Output: 2


# Final Challenge

my_tuple = (10, "Python", 3.14, "Code", 5, "Immutable")         # Create a Tuple
print("Third element:", my_tuple[2])                            # Access and Print Elements
print("Fifth element:", my_tuple[4])
sliced_tuple = my_tuple[1:5]                                    # Slice the Tuple
print("Sliced tuple:", sliced_tuple)
count_code = my_tuple.count("Code")                             # Count Occurences
print("Count of 'Code':", count_code)
a, b, c, d, e, f = my_tuple                                     # Unpack the Tuple
print(a, b, c, d, e, f)
new_tuple = my_tuple + ("New", "Tuple")                         # Concatenate Tuples
print("Concatenated tuple:", new_tuple)