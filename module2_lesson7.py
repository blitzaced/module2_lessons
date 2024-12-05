# OOP Principles

"""
Key Principles of OOP
    Encapsultaion - the practice of bundling data (attributes)  and methods (functions) that work on data into a single unit,
        or class. It also restricts direct access to some of an abjects components, which helps prevent the accidental
        modification of data.
            -EXAMPLE: Use of private attributes in Python (_attribute).
    
    Abstraction - abstraction simplifies complex systems by hiding unnecessary details and exposing only the essential parts.
        It allows a user to interact with objects without needing to understand all their internal complexities.
            -EXAMPLE: A car object hides the complex working os its engine and exposes simple methods like 'start()' and 'drive()'.
    
    Inheritence - allows a new class (subclass) to inherit attributes and methods from an existing class (superclass), promoting
        code reuse and a hierarchical structure.
            -EXAMPLE: A 'Vehicle' class could be a parent class, while 'Car' and 'Bike' are child classes inheriting its properties.
            
    Polymorphism - allows methods to do different things based on the object calling them, even if they share the same name.
            -EXAMPLE: Different classes ('Dog' and 'Cat') might have the same method 'speak()', but with different outputs
                (e.g., 'Woof!' vx. 'Meow!').
"""
                

# Encapsulation

""" Encapsulation ensures that the internal representation of an object is hidden from the outside world. By controlling access 
    to attributes and methods through access modifiers, we protect an object's state and behavior. In Python, encapsulation is
    achieved using naming conventions like private (__attribute) and protected (_attribute) attributes.
    
        Key Concepts:
            -Private Attributes and Methods: Only accessible within the class.
            -Protected Attributes and Methods: Can be accessed by the class and its subclasses.
            -Public Attributes and Methods: Accessible from outside the class.
            
        Private, Public, and Protected Attributes
            In OOP, controlling access to attributes is key to ensuring encapsulation. Python allows us to control this access 
            through public, protected, and private attributes 
"""


# Public Attributes

"""
    Definition: Public attributes are accessible and modifiable from anywhere. Public attributes are the default in Python and
        are commonly used when there's no need to restrict access.
    
    Characteristics:
        -Direct Access: Public attributes can be accessed or modified from anywhere, including outside the class.
        -No Underscore: Public attributes are defined without any leading underscores.
        
    When to Use:
        -Use public attributes when the attribute needs to be accessible and modifiable without restrictions.
        -For data that doesn't need protection from external changes.
"""

""" EXAMPLE of Public Attributes(BankAccount):"""

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder                # Public Attribute
        self.balance = balance                              # Public Attribute

account = BankAccount("Alice", 1000)                        # Public Attribute

# Accessing and modifying public attributes
print(account.account_holder)                               # Output: Alice
account.balance += 500                                      # Directly modifying the balance
print(account.balance)                                      # Output: 1500
        

""" EXAMPLE of Public Attributes(Video Game Character):"""

class Character:
    def __init__(self, name, health, level):
        self.name = name                                    # Public attribute
        self.health = health                                # Public attribute
        self.level = level                                  # Public attribute

player1 = Character("Archer", 100, 1)                       # Creating a new character)

# Accessing and modifying public attributes
print(player1.name)                                         # Output: Archer
player1.level += 1                                          # Leveling up
print(player1.level)                                        # Output: 2

""" Discussion:
        -In both examples, 'account_holder', 'balance', 'name', 'health', and 'level' are all public attributes that can
            be freely accessed and modified.
        -Public attributes are great for data that doesn't need control, suchs as game character stats or account information
            that can be modified externally.
"""

# Protected Attributes

"""
    Definition: Protected attributes are intended for use within the class and its subclasses. In Python, protected attributes
    are marked with a singel leading underscore (_attribute). They are accessible from outside the class, but this is discouraged
    by convention.

    Characteristics:
        -Limited Access: Accessible within the class and its subclasses, but should not typically be accessed from outside.
        -Single Underscore Prefix: Protected attributes are marked with a sinlge underscore(_attribute).
        -Not Fully Private: Protected attributes are not hidden but are intended to be internal.
        
    When to Use:
        -Use protected attributes when you want to allow access to an attribute in subclasses but discourage direct access
            from external code.
        -For internal data that needs to be inherited by subclasses but shouldn't be modified directly.
"""

"""EXAMPLE of Protected Attributes"""

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder                        # Public attribute
        self._balance = balance                                     # Protected attribute
        
    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def add_interest(self, interest_rate):
        self._balance += self._balance * interest_rate

# Create a savings account
savings = SavingsAccount("Bob", 2000)
savings.add_interest(0.05)
print(savings.get_balance())                                        # Output: 2100    

"""
    Discussion:
        -In this example, '_balance' is protected, allowing access within the 'BankAccount' class and its subclass 'SavingsAccount'.
        -This shows how protected attributes can control internal state changes while allowing subclasses to extend functionality
            (like adding interest).
""" 

 # Protected Attributes
 
"""
    Definition: Private attributes are fully hidden from outside the class and can only be accessed within the class itself.
    They are marked with a double underscore (__attribute). Python uses name mangling to make it difficult to access these attributes
    from outside.

    Characteristics:
        -Strict Access Cotrol: Private attributes can only be accessed from within the class.
        -Double Underscore Prefix: Private attributes are marked with a double leading underscore(__attribute).
        -Name Mangling: Python automatically changes the name to '_ClassName__attribute', making it harder to access externally.
    
    When to Use:
        -Use private attributes for data that needs to be fully protected and hidden from external access.
        -For sensitive or critical information that should only be accessible from within the class.
"""

""" EXAMPLE of Private Attributes (BankAccount):"""

class BankAccount:
    def __init__(self, account_holder, balance, password):
        self.account_holder = account_holder                        # Public attribute
        self.__balance = balance                                    # Private attribute
        self.__password = password                                  # Private attribute
    
    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "Access denied"
        
# Create a bank account with a private balance and password
account = BankAccount("Charlie", 5000, "mypassword")

# Accessing balance with the correct password
print(account.get_balance("mypassword"))                            # Output: 5000

# Trying to access private attribute directly (will raise an AttributeError)
# print(account.__balance)                                          # Raises AttributeError

# Accessing private attribute via name mangling (not recommended)
print(account._BankAccount__balance)                                # Output: 5000


""" EXAMPLE of Private Attributes (Social Media Profile):"""

class SocialMediaProfile:
    def __init__(self, username, email, password):
        self.username = username                                    # Public attribute
        self.__email = email                                        # Private attribute
        self.__password = password                                  # Private attribute
        
    def verify_password(self, input_password):
        if input_password == self.__password:
            return "Password verified"
        else:
            return "Invalid password"
        
    def get_email(self, input_password):
        if input_password == self.__password:
            return self.__email
        else:
            retun "Access denied"


# Create a social media profile
profile = SocialMediaProfile("user123", "user@example.com", "securepassword")

# Accessing private email with correct password
print(profile.get_email("securepassword"))                          # Output: user@example.com

# Accessing private attribute directly (raises AttributeError)
# print(profile.__email)                                            # Raises AttributeError

# Accessing private attribute via name mangling (not recommended)
print(profile._SocialMediaProfile__email)                           # Output: user@example.com

"""
    Discussion:
        -In the BankAccount example, the __balance and __password attributes are private, ensuring that only the correct 
        password allows access to the balance.
        -In the SocialMediaProfile example, __email and __password are private, and the profile's sensitive information is 
        only accessible through password verification.

    Name Mangline:
        -Python implements private attributes with name mangling. Even though it's technically possible to access these
        attributes using _ClassName__attribute, this is strongly discourages as it breaks encapsulation, so we won't demonstrate
        it in this lesson.
"""

# Attribute Access Levels Compared

"""
    Access Level            Syntax          Access From Outside Class           Typical Use Case
    --------------------------------------------------------------------------------------------------------------------------------
    -Public                 'attribute'     Fully acessible                     General-purpose attributes that should be visible
    
    -Protected              '_attribute'    Accessible, but not recommended     Internal attributes that subclasses may need to modify
    
    -Private                '__attribute'   Not directly accessible             Sensitive or critical data that must be fully hidden


    Why Use These Attribute Types?
        -Public: Use for attributes and methods that are meant to be accessed or modified by external code.
        -Protected: Use when you want to discourage access from outside but still allow subclasses to modify the behavior.
        -Private: Use to hide internal data that shouldn't be directly accessed or modified.
"""

# Exercise 7.1

class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name                                      # Public attribute
        self.__steps = 0                                                # Private attribute
        self.__calories_burned = 0.0                                    # Private attribute
        
    def add_steps(self, steps):
        if steps > 0:
            self.__steps += steps
            print(f"{steps} steps added. Total steps: {self.__steps}.")
        else:
            print("Steps must be positive.")
    
    def get_steps(self):
        return self.__steps

    def add_calories(self, calories):
        if calories > 0:
            self.__calories_burned += calories
            print(f"{calories} calories burned, Total calories burned: {self.__calories_burned}.")
        else:
            print("Calories must be positive.")
            
    def get_calories_burned(self):
        return self.__calories_burned
    
    def reset_tracker(self):
        self.__steps = 0
        self.__calories = 0.0
        print("Tracker reset to 0 steps and 0.0 calories burned.")
        
# Create an instance of FitnessTracker
tracker = FitnessTracker("John")

# Track steps and calories
tracker.add_steps(5000)                                     # Output: Steps: 5000
tracker.add_calories(300)                                   # Output: Calories: 300.0

# Display current progress
print(f"Steps: {tracker.get_steps()}")                      # Output: Steps: 5000
print(f"Calories: {tracker.get_calories_burned}")           # Output: Calories" 300.0

# Reset the tracker
tracker.reset_tracker()                                     # Output: Tracker rest to 0 steps and 0.0 calories burned



# Understanding Inheritance and Polymorphism

"""
    Inheritance
        A fundametnal concept in OOP that allows one class (the child or subclass) to inherit the attributes and methods of
        another class (the parent or superclass). This enables code reuse and helps create a logical hierarchy between classes.
        
        Key Concepts:
            -Superclass (Parent Class): The class that is being inherited from.
            -Subclass (Child Class): The class that inherits attributes and methods from the superclass.
            -Super(): A built-in Python function used to call a method, usually the __init__ method, from the parent class in 
            a child class.
            -Method Overriding: A subclass can override a method defined in the parent class to provide specific behavior for 
            that subclass.
"""

""" EXAMPLE: Inheritance in a Video Game Character System"""

class Character:                                                        # Parent class
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def move(self):
        print(f"{self.name} is moving!")
        
    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power!")
        
class Warrior(Character):                                               # Subclass: Warrior
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)                    # Call the parent class constructor
        self.armor = armor

    def use_shield(self):
        print(f"{self.name} blocks the attack with a shield!")
        
class Mage(Character):                                                  # Subclass: Mage
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)                    # Call the parent class constructor
        self.mana = mana
        
    def cast_spell(self):
        print(f"{self.name} casts a powerful spell!")
        
# Creating instances
warrior.move()                                                          # Output: Conan is moving!
warrior.attack()                                                        # Output: Conan attacks with 20 power!
warrior.use_shield()                                                    # Output: Conan blocks the attack with a shield!

mage.move()                                                             # Output: Gandalf is moving!
mage.attack()                                                           # Output: Gandalf attacks with 25 power!
mage.cast_spell()                                                       # Output: Gandalf casts a powerful spell!

"""
    Discussion:
        -Here, the Warrior and Mage classes inherit common methods (move() and attack()) from the Caracter class.
        -Each subclass adds its own specific methods (use_shield() for Warrior and cast_spell() for Mage), showcasing how
        we can extend the functionality of a parent class.
        -The super() function calls the parent class contructor, allowing us to reuse its initialization logic while adding
        new properties (like 'armor' or 'mana').
"""


# Method Overriding Inheritance

"""
    When a subclass need to change or extend the behavior of a method from its parent class, it can override that method
    by defining a new version of it in the subclass.
    
    EXAMPLE - Method Overriding Inheritance
"""

class Character:                                                        # Parent class
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def attack(self):
        print(f"{self.name} attacks with {self.attack_power} power!")
        
class Warrior(Character):
    def attack(self):                                                                   # Override the parent class method
        print(f"{self.name} slashes with a sword, dealing {self.attack_power}")         
        
class Mage(Character):
    def attack(self):                                                                   # Override the parent class method
        print(f"{self.name} casts a fireball, dealing {self.attack_power} damage!")

# Creating instances
warrior = Warrior("Conan", 100, 20)
mage = Mage("Gandalf", 80, 25)

# Calling the overriden methods
warrior.attack()                                                # Output: Conan slashes with a sword, dealing 20 damage!
mage.attack()                                                   # Output: Gandalf casts a fireball, dealing 25 damage!

"""
    Discussion:
        -Method overriding allows subclasses to provide their own implementation of the attack() method.
        -Both Warrior and Mage inherit from Character, but they each perform the attack() action in a different way,
        depending on their class-specific abilities.
        
    Advantages of Inheritance:
        -Code Reuse: Avoid redundancy by using commong code in a parent class and extending or overriding it in child classes.
        -Maintainability: Changes to shared logic can be made in the parent class and automatically reflected in subclasses.
        -Extensibility: You can easily add new subclasses (like and Archer or Rogue) that inherit common functionality but 
        introduce new behaviors.
"""


# Polymorphism

"""
    Polymorphism allows different types of objects to be treated as if they are instances of the same class. In Python, this is
    usually achieved through method overriding, where a method is redefined in a subclass to provide differen behavior while
    maintaining te same interface
    
    Key Concepts:
        -Same Interface, Different Behavior: Polymorphism allows you to use the same method name across multiple classes
        but with differen implementations.
        -Flexibility: Polymorphism lets you write more flexible and reusable code by treating objects of different types
        in the same way.
        -Synamic Typing: Python's dyamic typing makes polymorphism especially powerful since objects are identified by their 
        behavior (methods) rather than their specific class.

EXAMPLE: Polymorphism with Game Characters
"""

class Character:
    def attack(self):
        pass                                                # Defined as a placeholder to be overriden by subclasses

class Warrior(Character):
    def attack(self):
        print(f"Warrior attacks with a sword!")
        
class Mage(Character):
    def attack(self):
        print("Mage casts a fireball!")
        
class Archer(Character):
    def attack(self):
        print("Archer shoots an arrow!")
        
# Using polymorphism in a function
def perform_attack(character):
    character.attack()                                      # Calls the correct method based on the object's class

# Creating instance of different character types
warrior = Warrior()
mage = Mage()
archer = Archer()

# Using polymorphism
perform_attack(warrior)                                     # Output: Warrior attacks with a sword!
perform_attack(mage)                                        # Output: Mage casts a fireball!
perform_attack(archer)                                      # Output: Archer shoots an arrow!


"""
    Discussion"
        -Polymorphism allows us to call the attack() method on any character type (Warrior, Mage, Archer) without
        knowing the specific class in advance.
        -Each character type provides its own implementation of attack(), but the function perform_attack() trates them all the
        same. This makes the code more flexbile and extendable.
        -New character types can easily be added in the future, and the perform_attack() function will work with them without
        modification.
"""

""" EXAMPLE: Polymorphism in a Social Media Platform"""

pythonCopy codeclass User:
    def post_content(self):
        pass                                                # Placeholder to be overidden

class RegularUser(User):
    def post_content(self):
        print("Posting a photo as a regular user.")
        
class Influencer(User):
    def post_content(self):
        print("Posting a sponsored video as an influenceer.")
        
class Brand(User):
    def post_content(self):
        print("Posting an ad as a brand.")
        
# Polymorphic behavior
def publish_post(user):
    user.post_content()

# Creating instances
user1 = RegularUser()
user2 = Influencer()
user3 = Brand()

# Using polymorphism
publish_post(user1)                                                     # Output: Posting a photo as a regular user.
publish_post(user2)                                                     # Output: Posting a sponsored video as an influencer.
publish_post(user3)                                                     # Output: Posting an ad as a brand.

"""
    Discussion:
        -In this eample, polymorphism allows us to treat all User objects the same way when publishing posts, even though
        each user type posts content differently.
        -This kind of flexibility is especially useful in large-scale systems where different types of objects (e.g., users)
        need to interact with the same methods bu behave in unique ways.
"""


# Advanced Concepts in Inheritance and Polymorphism

"""
    Multiple Inheritance
        Python allows classes to inherit from more than one class, which is know as multiple inheritance. This can be
        powerful, but it can also lead to complexities such as the 'diamond problem', where methods from multiple pranet
        classes might conflict.
        
EXAMPLE of Multiple Inheritance
"""
class Flyer:
    def fly(self):
        print("Flying high!")
        
class Swimmer:
    def swim(self):
        print("Swimming fast!")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

# Creating an instance of Duck
duck = Duck()
duck.fly()                                                      # Output: Flying high!
duck.swim()                                                     # Output: Swimming fast!
duck.quack()                                                    # Output: Quack!

"""
    Discussion:
        -In this example, the Duck class inherits both the fly() method from Flyer and the swim() methods from Swimmer, 
        demonstrating multiple inheritance.
        -Multiple inheritanve can be useful, but it should be used carefully to avoid complexity, especially when two parent
        classes define the same method (which can lead to ambiguity).
"""


# Key Takeaways

"""
1. Encapsulation
    -Encapsulation bundles data and methods into a class, controlling access to an object's internal state.
    -Public, Protected, and Private Attributes control access:
        >Public (attribute): Accessible anywhere.
        >Protected (_attribute): Accessible within the class and its subclasses.
        >Private (__attribute): Hidden from external access.
    - Getters and Setters provide controlled access to priacte attributes, enforcing data protection.
    
2. Inheritance
    -Inheritance allows subclasses to reuse and extend functionality from a parent class.
    -Method Overidding lets subclasses redefine parent methods for specific behavior.
    -Multiple Inheritance allows a class to inherit from more than one parent, combining features from multiple sources.
    
3. Polymorphism
    -Polymorphism allows different objects to respond to the same methos in their own way, providing flexibility.
    -Python's dynamic typing supports polymorphism naturally, making it easy to treat objects of different types uniformly.
    
4. Advanced OOP Techniques
    -Method Overriding allows subclasses to customize parent methods, key for polymorphism.
    -Multiple Inheritance enables a class to inherit from more than one parent, but requires careful management
    to avoid conflicts.
    
    
Benefits of OOP
    -Modularity: Encapsulation creates self-contained, organized code.
    -Reusability: Inheritance avoids code duplication.
    -Flexibility: Polymorphism enables diverse behavior through a consistent interface.
    -Maintainability: OOP principles improve the structure and scalability of code.
"""