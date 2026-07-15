import os, time, keyboard, sys, colorama, base64
from colors import *
# from mainLibrary import current_filename | this is code for importing only specific variables


# Converts a Boolean (True or False) Variable into Binary for Simplicity.
def boolean_convert(var):
    """Converts a Boolean (True or False) into Binary (1 or 0).
    > Must be used within
    
    Args:
        Requires a variable being plugged into this.

    Returns
    """
    if var == True:
        var = 1
    elif var == False:
        var = 0
    return var

# Get current file location of running script.
def get_file_path():
    """Gets the current File Path."""
    global current_filename
    current_filename = os.path.basename(__file__)

# Sleep for X time.
def sleep(sTime):
    """Sleeps for X amount of time."""
    time.sleep(sTime)

# Clears the Console.
def clear_console():
    """Removes all Text from the Output that contains this program.
    Works for Windows and Linux. Don't know about MacOS."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Types out the given text.
def type(text, delay=0.1):
    """Types out text with a 0.1 delay by default.

    Args:
        text: The text to be typed out.
        delay (optional): The delay between keys being pressed. Default is 0.1 seconds.

    Returns:
        
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after printing the text

# Reloads the Program.
def reload_program(current_filename=os.path.basename(__file__)):
    """Runs this program again. If ran in the middle of a program, the program that ran this function will continue after the ran function is over.
    
    Args:
        current_filename: The filename of this Python file.

    Returns:
        Runs the called Python file and then resumes the Python file that called it, once done.
    """
    os.system("python " + current_filename)

# Runs another python script.
def run_another_script(file_name):
    """Runs another python script.

    Args:
        file_name: The filename of the called Python script.
    
    Returns:
        Runs the selected Python script and resumes this script once done.
    """

    os.system(f"python {file_name}")

# Checks for mutiple keys pressed at once.
def wait_til_keys_pressed(key1, key2, key3, key4):
    """Halts the program until all keys are pressed.
    > Maximum of 4 Keys at a time.

    Args:
        key1 (required): First key needed to be pressed in order to continue.
        key2 (required): Second key needed to be pressed in order to continue.
        key3 (optional): Third key needed to be pressed in order to continue.
        key4 (optional): Fourth key needed to be pressed in order to continue.

    Returns:
        Unhalts the program once all keys are pressed.
    """

    # if key3 or key4 isn't used
    if key3 is None and key4 is None:
        key3 = "NULL"
        key4 = "NULL"
        input(f"key3 and key4 aren't bound. Just set them to {key1} and {key2} respectively.")
    elif key4 is None:
        key4 = "NULL"
        input(f"key4 isn't bound. Just set it it to {key2}.")
    elif key3 is None:
        key3 = "NULL"
        input(f"key3 isn't bound. Just set it it to {key1}.")


    while True:
        if key3 == "NULL" and key4 == "NULL":
            input(f"key3 and key4 aren't bound. Just set them to {key1} and {key2} respectively.")
        elif key4 == "NULL":
            input(f"key4 isn't bound. Just set it it to {key2}.")
        elif key3 == "NULL":
            input(f"key3 isn't bound. Just set it it to {key1}.")
        else:
            if keyboard.is_pressed(str(key1)) and keyboard.is_pressed(str(key2)) and keyboard.is_pressed(str(key3)) and keyboard.is_pressed(str(key4)):
                print("All keys have been pressed.\n")
                break

def execute_function_by_name(function_name, i2=0):
    """Check if the function name exists in the global namespace then runs it.
    > Returns a message on function completion.
    > Returns a message if function doesn't exist.
    """

    # i2 = input("what shall be passed into it")

    if function_name in globals():
        globals()[function_name](i2)() # Call the function by name
        input(f"{function_name} was ran succesfully.")
    else:
        print(f"No function named '{function_name}' exists.")

def decode(encoded_string="SGVsbG8gV29ybGQh"):
    #encoded_string="SGVsbG8gV29ybGQh"
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')

    #input(f"Decoded: {decoded_string}")  # Output: Hello World!
    return decoded_string










"""
print('''mainLibrary.py | Debug\n
1. Open a file in local directory.
2. Test a function. \n
close - Close this file.''')
DEBUG_CHOICE = input("> ")

if DEBUG_CHOICE == "1":
    clear_console()
    run_another_script(input("File Name of the Python Script to be ran?\n> "))

elif DEBUG_CHOICE == "2":
    clear_console()
    execute_function_by_name(str(input("Function Name? (No () are needed.)\n> ")), input("\nFunction Input? (leave blank if no input is needed)\n> "))

clear_console()

if DEBUG_CHOICE == "close":
    exit()
else:
    reload_program(os.path.basename(__file__))"""