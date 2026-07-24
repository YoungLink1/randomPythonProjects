# Function and Library importing:
from time import sleep
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

# Converts between a Boolean and Binary output for simplicity.
def state_convert(var):
    """Converts a Binary (1 or 0) / Boolean (True or False) to the opposite form.
    
    Args:
        Requires a variable being plugged into this.

    Returns:
        var.type == "int" <===> var.type == "bool"
    """
    if var is int:
        if var == 1:
            var = True
        elif var == 0:
            var = False
    elif var is bool:
        if var == True:
            var = 1
        elif var == False:
            var = 0
    return var

# Check if the user has pygame-ce.
try:
    import pygame
    clear_console()
    # Run a check to see if they have pygame or pygame-ce.
    while True:
        try: # If they have pygame-ce, continue on, if not, run code below.
            if getattr(pygame, "IS_CE", False):
                break
            else: # Found pygame installed but not pygame-ce.
                DEBUG_testItem = input("You have 'pygame' installed but not 'pygame-ce' which contains additional features and tweaks.\nThis program is built with 'pygame-ce' in mind so installing is mandatory. Install now? (y/n) ")

                if DEBUG_testItem == "y":
                    clear_console()
                    print("Uninstalling pygame...")
                    os.system("pip uninstall pygame")
                    clear_console()
                    print("Installing pygame-ce...")
                    os.system("pip install --ignore-installed --no-deps pygame-ce")
                    clear_console()
                    input("'pygame-ce' is now installed! Press [ENTER] to continue.")
                    clear_console()
                    break
                elif DEBUG_testItem == "n":
                    print("This program will now close.")
                    sleep(1)
                    exit()
                else:
                    raise ValueError("Not an accepted answer of 'y' or 'n'")
        except ValueError as error:
            clear_console()
            input(f"Invalid input: {error}. Please try again.")
            clear_console()

except ImportError:
    while True:
        try:
            DEBUG_testItem = input("You are missing the 'pygame-ce' library.\nWould you like to install it? (y/n) ")

            if DEBUG_testItem == "y":
                clear_console()
                os.system("pip install pygame-ce")
                sleep(0)
                clear_console()
                input("'pygame-ce' library is now installed! Press [ENTER] to continue.")
                clear_console()
                break
            elif DEBUG_testItem == "n":
                print("This program will now close.")
                sleep(1)
                exit()
            else:
                raise ValueError("Not an accepted answer of 'y' or 'n'")
        except ValueError as error:
            clear_console()
            input(f"Invalid input: {error}. Please try again.")
            clear_console()
# End of Library / Function Importing.

# Start of Global Pygame Related Functions / Classes:
def poll_mouse(value=int()):
        """Gives an easy to read and use output of various mouse actions.
        Supports 3 & 5 button mice.
        Outputs as a boolean.

        MOUSE POSITION:
        -1 = Mouse X [WINDOW]
        -2 = Mouse Y [WINDOW]
        -3 = Combined WINDOW Mouse X & Y
        -4 = Mouse X [DESKTOP]
        -5 = Mouse Y [DESKTOP]
        -6 = Combined DESKTOP Mouse X & Y
        \n
        BUTTONS:
        1 = Left Mouse Button
        2 = Middle Mouse Button (clicked, no scroll)
        3 = Right Mouse Button
        4 = Button 4 (Side Button 1)
        5 = Button 5 (Side Button 2)
        6 = Scroll Wheel
        7 = Scroll Wheel [Alt Method; Less Precise]
        """
        from pygame import MOUSEWHEEL, MOUSEBUTTONDOWN

        WINDOW_mousePos = pygame.mouse.get_pos(desktop=False) # tuple
        DESKTOP_mousePOS = pygame.mouse.get_pos(desktop=True) # tuple
        mouse_buttons = pygame.mouse.get_pressed(num_buttons=5, desktop=False) # tuple

        # print(f'Window: {WINDOW_mousePos}\nScreen: {DESKTOP_mousePOS}')
        # print(mouse_buttons)

        match value:
            case -1:
                return(WINDOW_mousePos[0])
            case -2:
                return(WINDOW_mousePos[1])
            case -3:
                return(WINDOW_mousePos)
            case -4:
                return(DESKTOP_mousePOS[0])
            case -5:
                return(DESKTOP_mousePOS[1])
            case -6:
                return(DESKTOP_mousePOS)
            case 1:
                return(mouse_buttons[0])
            case 2:
                return(mouse_buttons[1])
            case 3:
                return(mouse_buttons[2])
            case 4:
                return(mouse_buttons[3])
            case 5:
                return(mouse_buttons[4])
            case 6:
                for event in pygame.event.get():
                    if event.type == MOUSEWHEEL:
                        return int(event.y)  # Returns positive for up, negative for down
                return 0  # Return 0 if no scrolling happened this frame
            case 7:
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 4:
                            return 1
                        elif event.button == 5:
                            return -1
                return 0
            case _:
                return('Invalid Poll Action in FUNC: "poll_mouse()"')

class Polygon:
        """Class meant for creating objects within pygame off of a list of points.
        -------------------------------------------------------
        def __init__(self, points, screen_size=(480, 360)):
            self.points = points

            self.surface = pygame.Surface(screen_size, pygame.SRCALPHA)
            pygame.draw.polygon(self.surface, (255, 255, 255), self.points)
            self.mask = pygame.mask.from_surface(self.surface)

        def is_hovered(self, position):
            return bool(self.mask.get_at(position))
            
        def is_clicked(self, position):
            return self.is_hovered(position) & poll_mouse(1)"""

        def __init__(self, points, screen_size=(480, 360)):
            self.points = points

            # 1. Bake the surface & mask it ONCE on creation.
            self.surface = pygame.Surface(screen_size, pygame.SRCALPHA)
            pygame.draw.polygon(self.surface, (255, 255, 255), self.points)
            self.mask = pygame.mask.from_surface(self.surface)

        # When called, checks on the mask if the position has a pixel or not.
        def is_hovered(self, position):
            """Check for collision using the pre-baked mask, to see if there's overlap with the given position."""
            return bool(self.mask.get_at(position))

        def is_clicked(self, position):
            """Check if object is hovered and then clicked. Uses 'is_hovered()' to check collision."""
            return self.is_hovered(position) & poll_mouse(1)

class DragPolygon(Polygon):
        "Subclass of Polygon meant for dragable objects."
        def __init__(self, points, neededHold):
            self.held, self.offset_x, self.offset_y = 0, 0, 0
            self.draggable = True
            prior_x = 0
            prior_y = 0
            current_x = poll_mouse(-1)
            current_y = poll_mouse(-2)
            
            while self.draggable:
                prior_x = current_x
                prior_y = current_y
                current_x = poll_mouse(-1)
                current_y = poll_mouse(-2)

                if self.is_clicked((current_x, current_y)) & self.held > neededHold:
                    return "dragging"
                elif self.is_clicked((current_x, current_y)):
                    self.held += 1
                else:
                    self.held = 0

# End of Global Pygame Related Functions / Classes.

PS4_button_ref = ["Cross Button", "Circle Button", "Square Button", "Triangle Button", "Share Button", "PS Button", "Options Button", "Left Stick", "Right Stick", "Left Bumper", "Right Bumper", "D-Pad Up", "D-Pad Down", "D-Pad Left", "D-Pad Right", "Touch Pad"]
PS4_axis_ref = ["LS X-Axis", "LS Y-Axis", "RS X-Axis", "RS Y-Axis", "Left Trigger", "Right Trigger"]

DEBUG_testItem = int(input(f"pygame-ce {pygame.ver}\nWhat test do you want?\n> "))
clear_console()

if DEBUG_testItem == 0:
    os.system("%USERPROFILE%/AppData/Roaming/Python/Python310/site-packages/pygame/docs/generated/ref/draw.html")
    os.system("%USERPROFILE%/AppData/Local/Programs/Python/Python310/Lib/site-packages/pygame/docs/generated/ref/draw.html")
    reload_program()

elif DEBUG_testItem == 1:
    #try to make an interactive UI/GUI
    from pygame import MOUSEWHEEL

    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    clock = pygame.time.Clock()
    running = True


    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        debugInfo = f"""{poll_mouse(-3)}
        LMB = {poll_mouse(1)}
        MMB = {poll_mouse(2)}
        RMB = {poll_mouse(3)}
        4MB = {poll_mouse(4)}
        5MB = {poll_mouse(5)}
        SCROLL = {poll_mouse(6)}
        """

        clear_console()
        sleep(0)
        print(debugInfo)

        pygame.display.flip()
        clock.tick(30) # limits FPS to 30
    
    pygame.quit()

elif DEBUG_testItem == 2:
    from pygame import MOUSEWHEEL

    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    clock = pygame.time.Clock()
    running = True

    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #elif event.type == MOUSEWHEEL:
                #print(event.y)

        clear_console()
        print(pygame.event.poll())
        pygame.display.flip()
        clock.tick(30) # limits FPS to 30

    pygame.quit()

elif DEBUG_testItem == 3:
    pygame.init()
    window1 = pygame.Window(position=(0, 0), size=(1920, 1080), borderless=True)
    window1.get_surface()
    clock = pygame.time.Clock()
    running = True

    def close(a):
        if a == 0:
            sleep(0)
        elif a == 1:
            window1.destroy()
            quit()

    while running:
        a = pygame.display.message_box(" ", "How did you get here?", "info", window1, ('OK', "Wha?"))
        close(a)
        a = pygame.display.message_box(" ", "Seriously, how tf did you get here?", "info", window1, ('OK', "Wha?"))
        close(a)

        window1.flip()
        clock.tick(30) # limits FPS to 30

elif DEBUG_testItem == 4:
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (200, 50, 50), (100, 150, 200, 50))
        pygame.display.flip()
        clock.tick(30) # limits FPS to 30

elif DEBUG_testItem == 5:
    pygame.init()
    pygame.display.set_caption("Mouse Buttons")
    screen = pygame.display.set_mode((480, 360))
    clock = pygame.time.Clock()
    running = True

    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        poly_LMB = [(44.5, 89), (44.5, 0), (33.375, 2.225), (24.475, 6.675), (15.575, 13.35), (8.9, 24.475), (3.56, 37.825), (0.89, 57.85), (0, 89)]
        poly_RMB = [(44.5, 89), (44.5, 0), (55.625, 2.225), (64.525, 6.675), (73.425, 13.35), (80.1, 24.475), (85.44, 37.825), (88.11, 57.85), (89, 89)]
        poly_MMB = [(37, 15), (52, 15), (52, 55), (37, 55)]
        poly_SCWU = poly_MMB[0:1] + [(52, 35), (38, 35)]
        poly_SCWD = [(52, 35), (38, 35)] + poly_MMB[2:3]


        screen.fill((30, 30, 30))

        scroll = poll_mouse(6)
        #print(f"Pos: {poll_mouse(-3)}; Scroll: {scroll}")


        if poll_mouse(1):
            pygame.draw.polygon(screen, (200, 50, 50), poly_LMB, 0)
        else:
            pygame.draw.polygon(screen, (50, 50, 50), poly_LMB, 0)

        if poll_mouse(3):
            pygame.draw.polygon(screen, (200, 50, 50), poly_RMB, 0)
        else:
            pygame.draw.polygon(screen, (50, 50, 50), poly_RMB, 0)

        pygame.draw.polygon(screen, (80, 80, 80), poly_LMB, 2)
        pygame.draw.polygon(screen, (80, 80, 80), poly_RMB, 2)


        if poll_mouse(2):
            pygame.draw.polygon(screen, (200, 50, 50), poly_MMB, 0)
        else:
            pygame.draw.polygon(screen, (50, 50, 50), poly_MMB, 0)

        if scroll > 0:
            pygame.draw.polygon(screen, (200, 50, 80), poly_SCWU, 0)
            #input("scroll is above 0")
        elif scroll < 0:
            pygame.draw.polygon(screen, (200, 50, 80), poly_SCWD, 0)
            #input("scroll is below 0")
        #elif poll_mouse(6) == 0:
            #input("scroll is 0")

        pygame.draw.polygon(screen, (80, 80, 80), poly_MMB, 2)


        #print(poll_mouse(6))


        pygame.display.flip()
        clock.tick(30) # limits FPS to 30

elif DEBUG_testItem == 6:
    from pygame import Color
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    clock = pygame.time.Clock()
    running = True
    
    # This dict can be left as-is, since pygame-ce will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}

    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Handle hotplugging; from pygame-ce Documentation
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connected. {joysticks[joy.get_instance_id()].get_name()}")

            if event.type == pygame.JOYDEVICEREMOVED:
                if event.instance_id in joysticks:
                    del joysticks[event.instance_id]
                    print(f"Joystick {event.instance_id} disconnected")
                else:
                    print(
                        f"Tried to disconnect Joystick {event.instance_id}, "
                        "but couldn't find it in the joystick list"
                    )

            # Handle Button Inputs
            if event.type == pygame.JOYBUTTONDOWN:
                input(event)
                print(f"[Joystick '{event.instance_id}'] {PS4_button_ref[event.button]} pressed.") # PS4 Support

            if event.type == pygame.JOYBUTTONUP:
                print(f"[Joystick '{event.instance_id}'] {PS4_button_ref[event.button]} released.") # PS4 Support

            # Handle Joystick / Trigger Inputs
            if event.type == pygame.JOYAXISMOTION:
                #input(event)
                if event.axis < 4:
                    continue
                else:
                    print(f"[Joystick '{event.instance_id}'] {PS4_axis_ref[event.axis]}: {event.value}") # PS4 Support

        pygame.display.flip()
        clock.tick(30) # limits FPS to 30

    pygame.joystick.quit()
    pygame.quit()

elif DEBUG_testItem == 7:
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    clock = pygame.time.Clock()
    running = True

    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clear_console()
        if pygame.key.get_pressed()[pygame.K_a]:
            print("aajgjhagjsgagsjh")
        else:
            print("ahh")

        pygame.display.flip()
        clock.tick(30)

elif DEBUG_testItem == 8:
    pygame.init()
    pygame.display.set_caption("Collision Testing")
    screen = pygame.display.set_mode((480, 360))
    clock = pygame.time.Clock()
    running = True

    poly_LMB = [(44.5, 89), (44.5, 0), (33.375, 2.225), (24.475, 6.675), (15.575, 13.35), (8.9, 24.475), (3.56, 37.825), (0.89, 57.85), (0, 89)]
    btn_LMB = DragPolygon(poly_LMB, 5)
    LMB_held = 0

    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))

        mouse_pos = poll_mouse(-3)
        clear_console()
        if btn_LMB.is_clicked(mouse_pos):
            LMB_held += 1
            if LMB_held >= 10:
                pygame.draw.polygon(screen, (90, 90, 105), poly_LMB, 0)
                print(f"held click {LMB_held}")
            else:
                pygame.draw.polygon(screen, (90, 90, 90), poly_LMB, 0)
                print(f"clicked {LMB_held}")
        elif btn_LMB.is_hovered(mouse_pos):
            pygame.draw.polygon(screen, (70, 70, 70), poly_LMB, 0)
            LMB_held = 0
            print(f"hovered {LMB_held}")
        else:
            pygame.draw.polygon(screen, (50, 50, 50), poly_LMB, 0)
            LMB_held = 0
            print(f"none {LMB_held}")

        pygame.draw.polygon(screen, (160, 160, 160), poly_LMB, 2)

        pygame.display.flip()
        clock.tick(30) # limits FPS to 30