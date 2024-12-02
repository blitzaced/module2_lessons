# Regular Expressions

""" Regular Expressioins, often abbreviated as Regex, are a powerful tool for matching patterns in text. 
    Essentially, Regex allows you to search, match, and manipulate strings based on defined patterns, making 
    it an essential feature for text processing and data extraction in Python. Regular expressions are especially 
    useful in situations such as data validation, web scraping, and parsing large volumes of data for specific 
    formats, like email addresses or phone numbers. Regex can significantly simplify compl;ex string operations, 
    helping developers work smarter and more efficiently."""

# Use Cases of Regex in Python

""" Validation:                 Checking if a string fits a particular format, such as validating emails or phone numbers.
    Data Extraction:            Extracting useful data such as hashtags, email address, or phone numbers from raw text.
    Test Replacement:           Replacing text, such as anonymizing user data.
    String Splitting:           Breaking up text based on specific delimiters.
    Searching for Patterns:     Finding occurences of a particular pattern within a text."""

# Literal Characters, Metacharacters, and Special Sequences

""" Regex utilizes combinations of differen characters and letters to define patterns. In order to utilize and 
    undestand Regex effectively, we'll need to understand some terminology first.
    
    Literal Characters: These are characters tha match exactly what they represent. For instance, the letter 'a'
        will match the character 'a' in a string.
    Metacharacters: These are characters with special meaning in regex patterns. Some ecamples include:
        - '.':  Matches any character except a newline.
        - '^':  Matches the start of a new string.
        - '$':  Matches the end of a string.
        - '[]': Matches any one of the charaters inside the brackets.
    Special Sequences: These are combinations of a backslash '\' followed by a character that has special meaning:
        - '\d': Matches any digit (equivalent to [0-9]).
        - '\w': Matches any word character (equivalent to [a-zA-Z0-9_]).
        - '\s': Matches any whitespace characters (spacesm tabs, line breaks)."""

# Reference Guide: Regex Metacharacters, Special Sequences, & Positional Operators

# Regex in Python 
""" Python provides the 're' module to work with regular expressions. To utilize the Regex module, 
    you'll need to import it first usines 'import re' ."""

"""Understanding Regex Method (function) Parameters
    When working with regex in Python, the 're' module provides several methods that allow you to search, 
    match, split, or substitute text based on patterns. In almost all these methods, two essential 
    parameters are required:
    
    -Pattern: This is the regular expression that defines the text pattern you want to search for or manipulate.
     The pattern should typically be constructed using a raw string (prefixing the string with'r'), i.e., r"pattern".
     Using a raw string ensures that special characters like backslashes (\) are treated as literal characters in the
     pattern and not as escape sequences by Python, and that metacharacters and special sequences are recognized.
     
     -Text: This is the string where you want the regex engine to apply the pattern. The text is evaluated to find
      or manipulate occurences of the pattern.""" 


# Finding All Matches with re.findall()
# -The re.findall() function is used to find all non-overlapping matches of a pattern within a string. 
#   It returns all matches.

""" re.findall(pattern, text)
    -Pattern: The regular expression pattern you're searching for. It can contain literal characters, metacharacters, 
    and special sequences.
        -Example: r"and" to find all of the word "and", i.e. all the occurences of the literal characers "a", "n", and 
        "d" next to each other.
    
    -Text: The string where the search for matches will happen.
        -Example: "Hi my name is Travis, and I like to go and do things and stuff"."""

import re                       #Counting 'and' in a Setnence
text = "Hi my name is Travis, and I like to go and do things and stuff"
ands = re.findall(r"and", text)
print(ands)
print(len(ands))

import re
post = "I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Code"
tags = re.findall(r"#\w+", post)
print(tags)

# Exercise 4.1

import re
tweets = [
    "Loving the #sunset! So peacerful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax"
]
tags = []
for tweet in tweets:
    tags.extend(re.findall(r"#\w+", tweet))
print(tags)


# Searching for Patterns with re.search()
""" The re.search() function searches through a string for the first occurence of a pattern and returns 
    a match object if a match is found. It only finds the first matcvh, making it ideal for validation purposes, 
    like checking if and email address is valid. If no match is found, it returns 'None'."""

""" EXAMPLE - Validating and email input using re.search(pattern, text)"""

email = "kareem33-34-28@gmail.com"
found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
if found:
    print(f"{found.group()} is a valid email! Please click continue!")
    
""" Pattern: r"[\w.-]+@[\w-]+\.[a-z]{2,3}" ensures the format of the email, with the username containing word 
    character (\w), periods (.), or hyphens (-), followed by an @, domain name, and a valid domain extension 
    of 2 to 3 characters.
    
    Text: The string "kareem33-34-28@gmail.com" is checked, and the match is found, indicating that the email is valid."""



""" EXAMPLE - Finding all email addresses using re.findall()"""

text = "You can contact me at t.p@gmail.com or travis-p2@codingtemple.com, traviscpeck@email.com"
emails = re.findall(r"[\w.-]+@[\w-]+.[a-z]{2,3}", text)
print(emails)

""" Pattern: the same pattern r"[\w.-]+@[\w-]+\.[a-z]{2,3}" is used to match the emails.
    
    Text: The string contains multiple email addresses, and re.findall() extracts them into a list."""

""" re.search() finds the first match and retuns a match object, which is useful for validation, while re.findall()
    finds all matches and returns a list, ideal for extracting multiple occurences of a pattern."""
    

# Matching Patterns at the Start of a String with re.match()

""" The re.match() function checks whether the beginning of a string matches a specificed pattern, This method is
    different from re.search() becuase re.match() only checks the start of the string. If the pattern is found
    at the beginning, a match object is returned; otherwise, it retuns 'None'. This makes re.match() ideal for 
    tasks like validating that a string starts with a certain prefix (e.g., checking if a URL is secure)."""
    
""" EXAMPLE - Checking for HTTPS using re.match()"""

url = "https://something.com"
secure = re.match(r"https", url)
if secure:
    print("This link goes to a secure website!")

""" Pattern: The pattern r"https" is used to match the string "https" at the beginning of the URL.
    
    Text: The URL "https://something.com" starts with "https", so a match is found."""



# Splitting Text with re.split()

""" The re.split() function splits a string into a list of substrings based on occernces of a specified pattern.
    It's similar to Python's built-in str.split(), but with re.split(), you can use regular expressions to define
    more complex splitting rules, such as splitting based on multiple delimiters or patterns.""" 

""" EXAMPLE - Splitting Text on Multiple Delimiters using re.split()"""

text = 'Python,Regex;Splitting-Example. Fun, right?'
words = re.split(r"[,.;\s-]+", text)
print(words)



# Substituting Text with re.sub(pattern, replacer, text)

""" The re.sub() function in Pythong allows  you to search for occurences of a pattern in a string and replace
    them with a specified replacement string. This is particularly useful for tasks like formatting data or
    anonymizing sensitive information in text. The function will replace all occurences of the pattern unless a
    "count" argument is provided to limit the number or replacements.
    
    Syntax:
    re.sub(pattern, replacer, text)
        -Pattern:   The regular expression pattern to match.
        -Replacer:  The string that will replace the matched patterns.
        -Text:      The string where the substitution will take place."""

""" EXAMPLE 1 - Formatting Phone Numbers using re.sub()"""
number = "(770)888-1180"
formatted_number = re.sub(r"\D",'', number)
print(formatted_number)

""" Pattern:    r"\D" matches any character that is not a digit. \D is the inverse of \d, which matches digits.
    Replacer:   An empty string (''). meaning we're removing all non-digit characters.
    Text:       The string "(770)888-1180, which includes parenthese, spaces, and a hyphen that we want to remove.
    
    The reular expression \D matches all non-digit characters, and re.sub() replaces those characters with an empty string.
    As a result, we get "7708881180". a clean string containing only the digits of the phone number."""


"""EXAMPLE 2 - Anonymizing Chat User Mentions using re.sub()"""
chat = '''
@Yve-bee123: "I think I love Regex"
@Travis: "Aren't you married?"
@Yve-bee123: "Its just not the same"
@Travis: "They better not see this!"
'''
anon_chat = re.sub(r"@[\w-]+", '@user-anon', chat)
print(anon_chat)

""" Pattern:    r"@[\w-]+" matches any username that starts with an @ symbol, followed by word character (letters,
                digits, underscores) or hyphens. This captures typical usernames like @Yvee-bee123 or @Travis.
    Replacer:   The string @user-anon, which will replace eachm atched username.
    Text:       The multiline chat conversation where we want to anonymize the usernames.
    
    The reular expression @[\w-]+ looks for any text that starts with @ and is followed by word characters (letters, 
    digits, and underscores) or hyphens, Teh re.sub() function replaces each match (i.e., the usernames) with 
    @user-anon. The result is an anonymized chat log."""


# Grouping with Regex

""" Grouping in regular expressions allows you to capture specific parts of a match for later use. Parenthese () 
    are used to define groups, and each group can be accessed individually. This is especially useful when you 
    need to extract mutliple parts of a string that match a pattern.
    
    Once you have defined a group using parenthese, you can refer to each group by its index, starting from '1'.
    The full match is represented by group(0), and individual groups are accessed with group(1), group(2), etc...
    
    Syntax:
    re.search(pattern, text).group(n)
        -Pattern:   A regular expression pattern that includes parenthese () to define groups.
        =Text:      The string where the pattern is being searched.
        -n:         The group number (starting from 1) to access the captured content."""

""" Example - Capturing Parts of a Phone Number"""
text = "123-456"
pattern = r"(\d+)-(\d+)"
thematch = re.search(pattern, text)
if thematch:
    print(f"Group 1: {thematch.group(1)}")
    print(f"Group 2: {thematch.group(2)}")
    
""" Pattern: r"(\d+)-(\d+) uses two groups:
        - (\d+): The first group captures one or more digits before the hyphen (123).
        - (\d+): The second group captures one or more digits after the hyphen (456).
    Text: The string "123-456" contains a hyphen between two sets of digits.
    
    Why Use Grouping"
    Grouping is essential when you need to extract and manipulate specific parts of a string. 
    For instance, is you are working with structured text like phone numbers, dates, or URLs, 
    grouping allows you to isolate and use specific components of the match. For example:
        -In phone numbers, you can capture the area code, central office code, and line number separately.
        -In dates, you can capture the day, month, and year separately."""


# Final Challenge

import re
emails = [
    "correct.email@example.com",
    "incorrect-email-at-example.com",
    "another.correct.email@example.org"
]

for email in emails:
    match = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
    if match:
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")
        
        
