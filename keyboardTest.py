import keyboard as key, os, mainLibrary as _
current_filename = os.path.basename(__file__)
testFlag = 6

# Functions go in between here:


# and here.

'''
test = input("reload? (y/n)\n> ")
if test == "y":
    _.clear_console()
    _.reload_program(current_filename)
else:
    _.sleep(0)
'''

if testFlag == 1:
    # Checks for one key.
    keyChoice = input("What key are you wanting to check?\n (Keys that require modifiers like Shift, are testable.)\n (Also, numPad keys are treated the same as their non-numPad counterparts.)\n (Function Keys count as well.)\n> ")

    if keyChoice == None or keyChoice == "":
        _.clear_console()
        _.reload_program(current_filename)
    else:
        _.clear_console()

    while True:
        try:  # used try so that if user pressed other than the given key error will not be shown
            if key.is_pressed(str(keyChoice)):  # if key chosen by keyChoice is pressed 
                print(f'You pressed the "{keyChoice}" key!\n')
                _.sleep(1)
                break  # finishing the loop
        except:
            input(f'Aw, the "{keyChoice}" is not a testable key. \nMay work if another name for this key is used.')
            break  # if user pressed a key other than the given key the loop will break, instead only works if the key is not a recognized key

elif testFlag == 2:
    # Checks for multiple keys
    print("waiting until keys are pressed")
    _.wait_til_keys_pressed("a", "b", "a", "b")

elif testFlag == 3:
    while True:
        print(key.read_key())
        _.sleep(0.25)
        _.clear_console()

elif testFlag == 4:
    key.block_key('f11')
    while True:
        print('no fullscreen for you.')
        _.clear_console()

elif testFlag == 5:
    while True:
        backtick_state = key.is_pressed("`")
        tilda_state = key.is_pressed("~")
        one_state = key.is_pressed("1")
        exclam_state = key.is_pressed("!")
        two_state = key.is_pressed("2")
        atsign_state = key.is_pressed("@")
        three_state = key.is_pressed("3")
        pound_state = key.is_pressed("#")
        four_state = key.is_pressed("4")
        dollarsign_state = key.is_pressed("$")
        five_state = key.is_pressed("5")
        percent_state = key.is_pressed("%")
        six_state = key.is_pressed("6")
        caret_state = key.is_pressed("^")
        seven_state = key.is_pressed("7")
        and_state = key.is_pressed("&")
        eight_state = key.is_pressed("8")
        asterik_state = key.is_pressed("*")
        nine_state = key.is_pressed("9")
        lParnth_state = key.is_pressed("(")
        zero_state = key.is_pressed("0")
        rParnth_state = key.is_pressed(")")
        dash_state = key.is_pressed("-")
        undScore_state = key.is_pressed("_")
        equals_state = key.is_pressed("=")
        plus_state = key.is_pressed("+")
        backspace_state = key.is_pressed("backspace")
        tab_state = key.is_pressed("tab")
        a_state = key.is_pressed("a")
        b_state = key.is_pressed("b")
        shift_state = key.is_pressed("shift")

        shift_row_1 = f"{tilda_state} | {exclam_state} | {atsign_state} | {pound_state} | {dollarsign_state} | {percent_state} | {caret_state} | {and_state} | {asterik_state} | {lParnth_state} | {rParnth_state} | {undScore_state} | {plus_state} | {backspace_state}"
        row_1 = f"{backtick_state} | {one_state} | {two_state} | {three_state} | {four_state} | {five_state} | {six_state} | {seven_state} | {eight_state} | {nine_state} | {zero_state} | {dash_state} | {equals_state} | {backspace_state}"
        _.sleep(0.5)

elif testFlag == 6:
    while True:
        key.block_key("a")
        if key.is_pressed("a"):
            print("test")
            _.sleep(2)
            key.send("a")