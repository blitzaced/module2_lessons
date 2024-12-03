import re

file = open('shows_list.txt', 'w')
def write_show(shows):                                 #Funtion to write TV shows to a file
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")
            
"""Writing Shows:   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -The 'write_show' funtion iterates over a list of dictionaries (shows) and writes each show's details (Titel, Platform, Genre)
        into a file using the '-:-' delimiter.
    -The delimiter helps in separating fields of a show's information for structured storage ad easier parsing during the read operation."""


def add_show(shows):                                    #Function to add a show to our shows list in dictionary format, and wrties it to our file
    title = input("What is the title of the show?")     #with the write_show funtion
    platform = input("Where can we watch it?")
    genre = input("What is the genre?")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows)                                   #Writes to shows file

"""Adding Shows:   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -The 'add_show' function gathers input from the user for each field (Title, Platform, Genre).
    -It appends the new show's details as a dictionary to the 'shows' list and updates the file by calling the 'write_show' function.
    -This ensures the file always reflects the latest state of the shows list."""


def view(shows):                                        #Function to read TV shows from a file
    shows_list = []
    with open('shows_list.txt', 'r') as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            shows_list.appends({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    return shows_list

"""Reading Shows:    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -The 'read_shows' function reads the file line by libe, using a regular expression (re.search) to extract structured data
     (Title, Platform, Genre).
    -The extracted details are stored as dictionaries in a list (shows_list), making it easier to work with the data programmatically."""


def view(shows):                                        #Function to print the list of shows for the user in a formatted way
    print("Shows List")
    print('-------------------')
    for idx, show in enumerate(shows):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if show['Genre'][0].lower() in vowels else 'a'
        print(f"{idx + 1}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")

"""Viewing Shows:   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -The 'view' function provides a user-friendly way to display the 'shows' list.
    -It uses conditional logic to determine whether to use 'a' or 'an' before the genre based on vowel sounds, adding polish to the output."""
    

def remove_show(shows):                                 #Function to show our current list of shows and allow the user to choose which to remove
    view(shows)
    option = int(input("\n\nChoose a number for the show you'd like to remove: "))
    show = shows.pop(option - 1)    #index -1
    print(f"\n{show['Title']} was successully removed!")
    write_show(shows)

"""Removing Shows:  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    -The 'remove_show' function allows the user to selet a show to remove by displayinh the surrent list and prompting for an index.
    -After removing the selected show, the updated list is written back to the file using the 'write_show' function.
    -This ensures the removed show is no longer persisted in the file."""



# Building the Interactive Program
"""The final step is to build an interactive menu for adding, viewing, and removing shows from the list."""

def main():                                             #Main function to run the TV show manager
    while True:
        shows_list = read_shows()                       #Read the current list of shows from the file
        action = input('''
Options
--------------------
1 - Add a TV Show
2 - Remove a TV Show
3 - View List of TV Shows
4 - Quit
''')
        if action == '1':
            add_show(shows_list)                        #Add a new show
        elif action == '2':
            remove_show(shows_list)                     #Remove a show
        elif action == '3':
            view(shows_list)                            #View the list of shows
        elif action == '4':
            print("Thanks for using the app!")
            break

main()

""" Menu System:
    -The main function provides a loop-based interactive menu, allowing users to performa actions like adding, viewing, or removing shows.
    -The menu displays numbered options, making it intuitive for users to interact with the program.
    
    Dynamic Update:
    -Each time an action is performaed (like adding or removing a show), the program updates the list by reading from the file first.
    -This ensures the displayed list is always up to date, even is the file is modified externally.
    
    Action Flow:
    -When the user selects and action:
        1. Triggers 'add_show' to collect data and append it to the list.
        2. Calls 'remove_show', presenting the current list and allowing the user to remove a selected entry.
        3. Invokes 'view' to print the formatted list of shows.
        4. Exits the program gracefully with a thank-you meddage.
    
    Persistence:
    -The combination of reading, modifying, and rewriting the file ensures data persists across sessions.
    -Users can quit the program and return later, with their canges saved and accessible.
    
    This interactive structure transforms the file operations into a user-friendly application, emphasizing the practical utility of Python's file handling
    capabilities. It sets the foundation for more complex file-based systems."""

# Final Challenge