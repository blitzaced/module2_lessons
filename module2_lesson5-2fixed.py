import re

# Function to write TV shows to a file
def write_show(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

# Function to read TV shows from a file
def read_shows():
    shows_list = []
    with open('shows_list.txt', 'r') as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            if data:
                shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    return shows_list

# Function to add a new TV show
def add_show(shows_list):
    title = input("Enter the TV Show Title: ").strip()
    platform = input("Enter the Platform (e.g., Netflix, Hulu): ").strip()
    genre = input("Enter the Genre: ").strip()
    
    # Add the new show to the list
    shows_list.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows_list)  # Save updated list to file
    print(f"'{title}' has been added to the list!\n")

# Function to remove a TV show
def remove_show(shows_list):
    title = input("Enter the Title of the TV Show to Remove: ").strip()
    
    # Filter the list to exclude the show with the matching title
    updated_list = []    
    for show in shows_list:
        if show["Title"].lower() != title.lower():
            updated_list.append(show)
    
    if len(updated_list) < len(shows_list):
        write_show(updated_list)  # Save updated list to file
        print(f"'{title}' has been removed from the list!\n")
    else:
        print(f"'{title}' was not found in the list.\n")

# Function to view all TV shows
def view(shows_list):
    if shows_list:
        print("\n--- List of TV Shows ---")
        for show in shows_list:
            print(f"Title: {show['Title']}, Platform: {show['Platform']}, Genre: {show['Genre']}")
        print("-------------------------\n")
    else:
        print("No TV Shows found. Add some first!\n")

# Main function to run the TV show manager
while True:
    shows_list = read_shows()  # Read the current list of shows from the file
    action = input('''
Options
-----------------------
1 - Add a TV Show
2 - Remove a TV Show
3 - View List of TV Shows
4 - Quit
''')
    if action == '1':
        add_show(shows_list)  # Add a new show
    elif action == '2':
        remove_show(shows_list)  # Remove a show
    elif action == '3':
        view(shows_list)  # View the list of shows
    elif action == '4':
        print("Thanks for using this app!")
        break
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.\n")
