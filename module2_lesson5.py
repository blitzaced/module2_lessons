# File Handling

""" Objectives:
        -Understand how to open, read, write, and append to files in Python.
        -Store and retrieve structures data using tect files.
        -Build interactive programs for data management.
        -Practice advanced file handling with real-world examples."""


# Opening and Writing to Files

""" Open a file in 'w' mode to write data
        file = open('new_file.txt', 'w')
        file.write('Writing to a file from Python!\n')
        file.close()         
        
    Appending data to the file without overwriting using 'a' mode
        file = open('new_file.txt', 'a')
        file.write('Adding more content with "a" mode\n')
        file.close()

    Explanation: The 'w'mode overwrites the file is it already exists, while 'a' mode 
    adds data to the file without removing existing content. Always ensure you close the file
    after writing to it using file.close().
"""


# Reading Files

""" Python provides different methods for reading files, such as read(), readline(), and readlines().

    #reading the file with 'r' mode
    with open('new_file.txt', 'r') as file:
        content = file.read()                           #read the entire file content
        print(content)

    #Using 'with open' ensures the file is properly closed after reading, even ir an error occurs in your program.
"""

# Exercise 1

def write_foods(foods):
    with open('foods.txt', 'w') as file:
        for food in foods:
            file.write(food + '\n')

def read_foods():
    foods_list = []
    with open('foods.txt', 'r') as file:
        for line in file:
            foods_list.append(line.strip())
    return foods_list

def main():
    foods = read_foods()
    while True:
        action = input("1 - Add Food, 2 - View Foods, 3 - Remove Food, 4 - Quit\n")
        if action == '1':
            new_food = input("Enter the name of the food: ")
            foods.append(new_food)
            write_foods(foods)
        elif action == '2':
            print("Your favorite foods:")
            for food in foods:
                print(food)
        elif action == '3':
            idx = int(input("Which food to remove?"))
            foods.pop(idx - 1)
            write_foods(foods)
        elif action == '4':
            break

main()