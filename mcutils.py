import os

# Clears the Console.
def clear_console():
    """Removes all Text from the Output that contains this program.
    Works for Windows and Linux. Don't know about MacOS."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Reloads the Program.
def reload_program(current_filename=os.path.basename(__file__)):
    """Runs this program again. If ran in the middle of a program, the program that ran this function will continue after the ran function is over.
    
    Args:
        current_filename: The filename of this Python file.

    Returns:
        Runs the called Python file and then resumes the Python file that called it, once done.
    """
    os.system("python " + current_filename)


GLOBAL_updateLOGS = ['''v0.1.1 / Mini-Update:
- FCSMP // "Create Shop Sign" has been split into 2 modes: Sell / Buy Items
- FCSMP // "Create Shop Sign [Buy Items]" has been added and implemented.
- You can now read this update log within the program.''', '''v0.1.0 / Initial Version:
- FCSMP // "Create Shop Sign" has been added and implemented.
- "Make Shapeless Recipe" has been planned as an option, but I'm tired and haven't added it yet.''']


while True:
    try:
        option = int(input("""Minecraft Utilities | v0.1.0
   -1. Close Program.
    0. Read the Update Log. [Newest to Oldest]
    1. FCSMP // Create Shop Sign [Sell Items]
    2. FSCMP // Create Shop Sign [Buy Items] X
    -- -- -- -- -- -- -- -- -- --
    > """))
        if type(option) is int:
            break
    except ValueError:
        clear_console()
        print(f'Syntax Error: Not an integer.\n-----------------------------------')



clear_console()
match int(option):
    case -1:
        print("Closing Program...")
        exit()

    case 0:
        temp = 0
        while temp + 1 <= len(GLOBAL_updateLOGS):
            print(GLOBAL_updateLOGS[temp])

            print("-----------------------------------")
            if temp + 1 == len(GLOBAL_updateLOGS):
                input("No more update logs.\nPress [ENTER] to reload.")
                clear_console()
                reload_program()
                exit()
            else:
                while True:
                    temp1 = input("Read prior update log? (y/n) > ")

                    if temp1 == "y":
                        temp =+ 1
                        break
                    elif temp1 == "n":
                        exit()
                    else:
                        continue
                        clear_console()
                        print(GLOBAL_updateLOGS[temp])

            clear_console()

    case 1:
        while True:
            try:
                value1 = input("What item are you wanting to sell?\n> ")
                if type(int(value1)) is int:
                    raise SyntaxError

            except ValueError:
                if value1 == "":
                    clear_console()
                    print("Error: No value given.\n-------------------------")
                else:
                    break

            except SyntaxError:
                clear_console()
                print(f'Syntax Error: Need item name, not ID.\nEX: "oak_log" instead of "{value1}".\n-----------------------------------')
          
                
        clear_console()
        while True:
            try:
                value2 = int(input(f'How much of "{value1}" will you sell at a time?\n> '))

                if type(value2) is int:
                    break
                else:
                    raise ValueError

            except ValueError:
                clear_console()
                print("Syntax Error: Not an integer.\n-----------------------------------")
        
        clear_console()
        while True:
            try:
                value3 = int(input(f'How much "{value1}" do you want to sell in total?\nYou MUST have this amount or more on sign creation.\nRestock by right-clicking the sign with {value1}.\n> '))

                if type(value3) is int:
                    break
                else:
                    raise ValueError

            except ValueError:
                clear_console()
                print("Syntax Error: Not an integer.\n-----------------------------------")
            
        clear_console()
        while True:
            try:
                value4 = float(input(f'How much will you sell "{value2}x {value1}" for?\n> '))

                if type(value4) == str:
                    raise ValueError
                else:
                    value4 = round(value4*100)/100
                    break

            except ValueError:
                clear_console()
                print("Syntax Error: Must be a numerical value.\n-----------------------------------")

        clear_console()
        input("Sign shop is ready to create!\nIf your sign doesn't work after this, then your item name is invalid.\nPress [ENTER], then copy and paste onto your sign!")
        clear_console()
        print(f"[Trade]\n${value4}\n{value2} {value1}:{value3}")
        input()
        reload_program()

    case _:
        input("Invalid Feature.")