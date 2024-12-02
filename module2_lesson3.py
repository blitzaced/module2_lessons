# Dictionaries

"""Dictionaries in Python are defined using curly braces {} and consist of key-value pairs. 
Each key in a dictionary must be unique and immutable, while the values can be of any data type and can be duplicated.

Example of a Python dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

In this example, the dictionary my_dict contains three key-value pairs. The keys are 'name', 'age', and 'city',
and their respective values are 'Alice', 25, and 'New York'. """


# Accessing  Values in a Dictionary - you can access the values stores in a dictionary by using the keys.

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict['name'])

""" The .get() method & avoiding missing keys
        If you try to access a key that does not exist, Python will raise a "KeyError". To avoid this, you can use the
        .get() method, which will return "None" (or a default value you speciffy) if the key doesn't exist.
        The .get() method is particularly useful for preventing errors when accessing keys that may/may not be in
        the dictionary."""
        
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict.get('age'))
print(my_dict.get('address', 'Not Available'))


"""Adding, Modifying, and Removing Elements - dictionaries are dynamic, meaning you can add, modify, or remove elements
    at any time
    
    To add a new key-value pair, simply assign a value to a new key.
    
    my_dict['profession'] = 'Engineer' """
    
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict)
my_dict['profession'] = 'Engineer'          #adding
print(my_dict)
my_dict['age'] = 26                         #modifying
print(my_dict)
del my_dict['city']                         #removing key-value pair
print(my_dict)
removed_value = my_dict.pop('profession')   #remove an item and also return its value to use elsewhere in code
print(removed_value)


# Dictionary Methods

""" .keys(): Return a view object that displays a list of all the keys in the dictionary. 
    It can be converted to a list if needed."""

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict)
my_dict['profession'] = 'Engineer'          #adding
print(my_dict)
my_dict['age'] = 26                         #modifying
print(my_dict)
del my_dict['city']                         #removing key-value pair
print(my_dict)
removed_value = my_dict.pop('profession')   #remove an item and also return its value to use elsewhere in code
print(removed_value)
print(list(my_dict.keys()))
print(list(my_dict.values()))
for key, value in my_dict.items():
    print(f"{key}: {value}")
    

# Exercise 3.1

book = {
    'title': '1984',
    'author': 'Georde Orwell',
    'year': 1949,
    'genre': 'Dystopian'
}

book['publisher'] = 'Secker & Warburg'      #addong a new key for publisher
book['year'] = 1950
print(book)


# Looping Through Dictionaries
#   Allows you to access and manipulate data efficiently. Here are differen looping approaches:

""" Looping through Keys only: You can loop through only the keys in a ditionary using a 'for' loop
    Looping through Values only: Use the .values() method to loop through the values
    Loops through Key-Value Pairs: Use the .items() mothod to loop through both jeys and values"""
    
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict)
my_dict['profession'] = 'Engineer'          #adding
print(my_dict)
my_dict['age'] = 26                         #modifying
print(my_dict)
del my_dict['city']                         #removing key-value pair
print(my_dict)
removed_value = my_dict.pop('profession')   #remove an item and also return its value to use elsewhere in code
print(removed_value)
print(list(my_dict.keys()))
print(list(my_dict.values()))
for key, value in my_dict.items():
    print(f"{key}: {value}")
for key in my_dict:                         #key only loop
    print(key)
for value in my_dict.values():              #value only loop
    print(value)
for key, value in my_dict.items():          #key-value pair loop
    print(f"{key}: {value}")
    

""" Nested Dictionaries
    You can nest dictionaries inside other dictionaries. This concept is incredibly useful when you're dealing with complex
    data that needs to be structures in multiple layers. For example, storing information about users in a system,
    where each user has multiple properties such as their name, age, and a nest dictionary for their address."""
    
users = {
    'user1': {
        'name': 'Alice',
        'age': 25,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'zipcode': '10001'
        }
    },
    'user2': {
        'name': 'Bob',
        'age': 30,
        'address': {
            'street': '456 Elm St',
            'city': 'San Francisco',
            'zipcode': '94107'
        }
    }
}

city_user1 = users['user1']['address']['city']      #accessing nested dictionary city data
print(city_user1)
users['user2']['address']['zipcode'] = '94109'      #modifying nested dictionary zipcode
print(users['user2']['address']['zipcode'])
users['user1']['phone'] = '555-1234'                #adding new key-pair to nested dictionary
print(users['user1']['phone'])
for user, info in users.items():                    #looping through the outer dictionary
    print(f"User ID: {user}")
    for key, value in info.items():                 #looping through the inner dictionary for each user
        print(f" {key}: {value}")
        

""" A List of Dictionaries
    In some cases, you may have multiple dictionaries that you need to manage together as a group. One of the most
    common ways to do this is by storing dictionaries in a list. Each dictionaryy in the list represents an individual
    record or item."""
    
students = [
    {
        'name': 'Alice',
        'age': 25,
        'major': 'Physics'
    },
    {
        'name': 'Bob',
        'age': 22,
        'major': 'Computer Science'        
    },
    {
        'name': 'Charlie',
        'age': 23,
        'major': 'Mathematics'
    }
]

first_student_major = students[0]['major']              #accessing major of first stundent in the list
print(first_student_major)
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")     #looping through list

favorite_books = {                                                          #storing list within a dictionary
    'Alice': ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice'],
    'Bob': ['The Great Gatsby', 'Catch-22', 'Moby Dick'],
    'Charlie': ['The Hobbit', 'Harry Potter', 'War and Peace']
}

alice_books = favorite_books['Alice']               #accessing Alice's favorite books
print(alice_books)
second_favorite_bob = favorite_books['Bob'][1]      #accessing Bob's second favorite book
print(second_favorite_bob)
for person, books in favorite_books.items():        #looping through lists inside a dictionary
    print(f"{person}'s favorite books:")
    for book in books:
        print(f" - {book}")


# Final Challenge

students = {
    'Alice': 85,
    'Bob': 42,
    'Charlie': 68,
    'David': 49
}

for student, grade in students.items():
    if grade >= 50:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")