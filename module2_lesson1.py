# Sets
#-------------------------------------------------------------------------------------------------------------------
""" Sets are a special collection data type in Python, and they're useful for strong unique items.
    Here are some important characteristics:
    
    -Unordered:    You won't know the order of elements.
    -Mutable:      You can change the set's contents by adding or removing items.
    -Unique:       Sets automatically remove duplicate items.
    -No Indexing:  Unlike lists or tuples, sets don't have a defined ordere, so you can't access items using an index."""

# Creating an empty set
""" To create an empty set, we use the 'set()' funtion, because {} is used for dictionaries."""
empty_set = set()       # This creates an empty set
print(type(empty_set))


# Creating a set with values
"""   -We can create a set by listing its values inside curly braces {}. 
        Sets automatically remove any duplicates values:"""
new_set = {'one', 'two', 'three'}
print(new_set)


# Working with Lists, Tuples, and Dictionaries
""" Sets are also great for removing duplicates from other data structures.
    For example, you can convert a list into a set to elimivate duplicate calues:"""
alist = ['item', 'item', 'stuff', 'thing', 'oddity']
set_list = set(alist)   # Converting a list to a set 
print(set_list)

""" You can simply convert tuples and dictionaries into sets to work with their values more effectively."""

# Exercise 1.1 - Practice Creating Sets
hobbies = ['reading', 'gaming','hiking', 'gaming', 'swimming', 'hiking']
hobbies_set = set(hobbies)
print("Original List:", hobbies)
print("Set with Duplicates Removed:", hobbies_set)


# Looping Over Sets
""" Since sets are unordered, we can't access items using an index.
    However, we can still iterate through all items using a 'for' loop."""

aset = {'apple', 'orange', 'banana'}        # Looping through a set
for fruit in aset:
    print(fruit)
    

# Exercise 1.2 - Loopiing Through a Set
favorite_foods = {'Chinese', 'Italian', 'Mexican', 'American', 'German'}
for food in favorite_foods:
    print(food)


# Set methods
""" Membership Checks:
        You can quickly check if an item exists in a set using the 'in' keyword,
        This is one of the most useful features of sets, as it is extremely efficient."""
my_set = {'superman', 'batman', 'wonder woman', 'the flash'}
print('superman' in my_set)
print('spiderman' in my_set)

# Adding items to a set
""" Sets are mutable, so we can add new elements using the '.add()' method.
    If you try to add an element that already exists in the set, it will simply be ignored."""
my_set = {'superman', 'batman', 'wonder woman', 'the flash'}
my_set.add('green lantern')
print(my_set)


# Exercise 1.3 - Set Modification Practice
hobbies = {'tennis', 'pickleball', 'beach', 'bowling'}
hobbies.add('billiards')
print('pickleball' in hobbies)
print(hobbies)


# Advanced Set Methods 
""" When working with two sets, Python provides several advanced methods to compare and analyze
    the relationship between them."""
    
""" Subset and Superset Checks
        -issubset()   : Checks is all elements of one are in another.
        -issuperset() : Checks if one set contains all elements of another."""

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))
print(set2.issuperset(set1))


# Exercise 4 - Comparing Sets
set1 = {'final fantasy', 'tales', 'xenoblade'}
set2 = {'tales', 'legend of zelda', 'final fantasy', 'street fighter', 'xenoblade'}
print(set1.issubset(set2))
print(set2.issuperset(set1))


# Set Operations
""" Set operations allow us to merge or compare sets in a powerful way.
        -Union: Combines all unique items from two sets.
        -Intersection: Returns only the items both sets have in common.
        -Difference: Returns the items found in one set, but not the other.
        -Symmetric Difference: Returns the items that are unique to each set (not shared by both)."""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1.union(set2))                 # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set1.intersection(set2))          # Output: {3, 4}

# Difference
print(set1.difference(set2))            # Output: {1, 2}

# Symmetric Difference
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}


# Exercise 1.5 - Working with Set Operations

set1 = {'paris', 'madrid', 'berlin', 'rust',}
set2 = {'cozumel', 'rust', 'vancouver', 'madrid', 'paris', 'berlin', 'san francisco'}
print("All unique destinations:", set1.union(set2))
print("Common destinations:", set1.intersection(set2))
print("Destinations only in set2:", set2.difference(set1))


# Final Challenge: Email List Duplication

def clean_email_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    #Remove duplicates and merge
    all_unique = set1.union(set2)
    print("All unique emails:", all_unique)
    
    # Common emails
    common_emails = set1.intersection(set2)
    print("Emails in both lists:", common_emails)
    
    # Emails unique to each list
    unique_emails = set1.symmetric_difference(set2)
    print("Emails unique to each list:", unique_emails)
    
email_list1 = ['a@example.com', 'b@example.com', 'a@example.com']
email_list2 = ['b@example.com', 'c@example.com', 'd@example.com']

clean_email_lists(email_list1, email_list2)