from mainLibrary import clear_console
from colors import *

# Just use """code here""" test certain bits

# Testing Object Oriented Programming with a given example and one of my own.
"""
# Example (with slight tweak to account for no name):
class Person:
    species = "Homo Sapiens"

    def __init__(self, name):
        if name == "":
            self.name = "John Doe"
        else:
            self.name = name

person1 = Person("Alex")
person2 = Person("")

print("Name of person 1:", person1.name)
print("Name of person 2:", person2.name)
print("\nSpecies:", Person.species)
print(person1.name, "and", person2.name, "are", Person.species, "\n")
"""
# My 1st Example:
"""
class person:
    def __init__(self, name, age, byear, bmonth, bday, feet, inches, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.feet = feet
        self.inches = inches
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def get_birth(self):
        return f"{self.bmonth}/{self.bday}/{self.byear}"

    def get_height(self):
        return f"{self.feet}'{self.inches}'' or {self.feet} feet & {self.inches} inches''"

    def get_occupation(self):
        return self.occupation

print("Make a Person:\n")
p1 = person(input("Name?\n> "), input("\nAge?\n> "), input("\n\u21B3Year of Birth?\n > "), input("\n\u21B3Month of Birth?\n > "), input("\n\u21B3Day of Birth?\n > "), input("\nHow many feet are you?\n> "), input("\nHow many inches are you?\n> "), input("\nJob?\n> "))

clear_console()
print("Name:", p1.get_name())
print("Age:", p1.get_age())
print("Height:", p1.get_height())
print("Job:", p1.get_occupation())
print("Birth:", p1.get_birth())
print()
"""

# My 2nd Example:
import time, sys, keyboard, time, random

def type(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after printing the text

"""# Example usage
type("Hello there! This is a typing effect in Python.", delay=0.05)"""

class person:
    def __init__(self):
        type("How would you describe yourself? Use numbers.\n1. Smart\n2. Mighty\n3. Innovative\n4. Brave\n5. Kind\n6. Ambitious\n7. Outspoken", delay = 0.025)
        chosenStat = input("> ")
        if chosenStat == "1":
            Intelligence = 4
            Strength = -1
            Creativeness = 2
            clear_console()
            type("Ah a smart one, but yet weak.")
        elif chosenStat == "2":
            Intelligence = -1
            Strength = 4
        elif chosenStat == "3":
            Intelligence = 2
            Creativeness = 4
        elif chosenStat == "4":
            Strength = 1
            Braveness = 4
            Ambition = 2
        elif chosenStat == "5":
            Kindness = 3
            Speech = 2
        elif chosenStat == "6":
            Intelligence = 1
            Braveness = 2
            Ambition = 4
            Speech = 2
        elif chosenStat == "7":
            Intelligence = 1
            Creativeness = 2
            Braveness = 2
            Kindness = 1
            Ambition = 2
            Speech = 4
        else:
            Intelligence = 2
            Strength = 2
            Creativeness = 2
            Braveness = 2
            Kindness = 2
            Ambition = 2
            Speech = 2
        
        # Dice Roll to increase stats.
        Intelligence += round((random.randint(1, 20))/5)
        input(Intelligence)

        # Stat Allocation Process.
        statPoints = 7

        while statPoints != 0:
                clear_console()
                print(f"{Cyan}Stat Points: {Blue}{statPoints}{reset} \n")
                prompt = input(f"{bright_yellow}What stat shall you increase? {reset} \n1. Intelligence \n2. Strength \n3. Creativness \n4. Braveness \n5. Kindness \n6. Ambition \n7. Speech\n> ")
                clear_console()
                if prompt == "1":
                    statPoints = statPoints - 1
                    Intelligence = Intelligence + 1
                    type(f"Intelligence is now {Blue}{Intelligence}{reset}.\n", 0.05)
                    while True:
                        if keyboard.is_pressed("Enter"):
                            time.sleep(0.01)
                            break
                if prompt == "2":
                    statPoints = statPoints - 1
                    Strength = Strength + 1
                    type(f"Strength is now {Blue}{Strength}{reset}.\n", 0.05)
                    while True:
                        if keyboard.is_pressed("Enter"):
                            time.sleep(0.01)
                            break
                if prompt == "3":
                    statPoints = statPoints - 1
                    Creativeness = Creativeness + 1
                    type(f"Creativness is now {Blue}{Creativeness}{reset}.\n", 0.05)
                    while True:
                        if keyboard.is_pressed("Enter"):
                            time.sleep(0.01)
                            break
                if prompt == "4":
                    statPoints = statPoints - 1
                    Braveness = Braveness + 1
                    type(f"Braveness is now {Blue}{Braveness}{reset}.\n", 0.05)
                    while True:
                        if keyboard.is_pressed("Enter"):
                            time.sleep(0.01)
                            break
                if prompt == "5":
                    statPoints = statPoints - 1
                    Kindness = Kindness + 1
                    type(f"Kindness is now {Blue}{Kindness}{reset}.\n", 0.05)
                    while True:
                        if keyboard.is_pressed("Enter"):
                            time.sleep(0.01)
                            break
                if prompt == "6":
                    statPoints = statPoints - 1
                    Ambition = Ambition + 1
                    type(f"Ambition is now {Blue}{Ambition}{reset}.\n", 0.05)
                    while True:
                        if keyboard.is_pressed("Enter"):
                            time.sleep(0.01)
                            break
                if prompt == "7":
                    statPoints = statPoints - 1
                    Speech = Speech + 1
                    type(f"Speech is now {Blue}{Speech}{reset}.\n", 0.05)
                    while True:
                        if keyboard.is_pressed("Enter"):
                            time.sleep(0.01)
                            break
                else:
                    statPoints = statPoints
        clear_console()
        type(f"Intelligence: {Intelligence} \nStrength: {Strength} \nCreativeness: {Creativeness} \nBraveness: {Braveness} \nKindness: {Kindness} \nAmbition: {Ambition} \nSpeech: {Speech}", delay = 0.02)

player = person()