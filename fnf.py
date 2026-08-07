# Start of Function and Library Importing:
from time import sleep
import pygame, os

import pygame.display

# Starts a Python script.
def reload_python(current_filename=os.path.basename(__file__)):
    """Runs a Python script.
    If ran in the middle of a program, the program that ran this function will continue after the ran function is over.
    
    Defaults to running the current Python script.
    
    Args:
        {optional} current_filename: The filename of this Python file. Can be changed to load other program.

    Returns:
        Runs the called Python file and then resumes the Python file that called it, once done.
    """
    os.system("python " + current_filename)

# Start of Global Pygame Related Functions / Classes:
def poll_mouse(value=int()):
        """Gives an easy to read and use output of various mouse actions.
        Supports 3 & 5 button mice.
        
        Args:
            value: What info should be polled from the mouse.

            - MOUSE POSITION:
            ⤷ -1 = Mouse X [WINDOW]
            ⤷ -2 = Mouse Y [WINDOW]
            ⤷ -3 = Combined WINDOW Mouse X & Y
            ⤷ -4 = Mouse X [DESKTOP]
            ⤷ -5 = Mouse Y [DESKTOP]
            ⤷ -6 = Combined DESKTOP Mouse X & Y
        \n
            - BUTTONS:
            ⤷ 1 = Left Mouse Button
            ⤷ 2 = Middle Mouse Button (clicked, no scroll)
            ⤷ 3 = Right Mouse Button
            ⤷ 4 = Button 4 (Side Button 1)
            ⤷ 5 = Button 5 (Side Button 2)
            ⤷ 6 = Scroll Wheel
            ⤷ 7 = Scroll Wheel [Alt Method; Less Precise]"""
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

def printImage(surface:pygame.Surface, position:tuple=(0, 0), loadMode:int=0, file_image:str=None, crop:bool=False, cropPos:tuple=(0,0), cropArea:tuple=(64, 64), scale:bool=False, scaleMode:float=None, scaleAmount:tuple|float=None):
    """Load an image onto a pygame Surface.
    
    Args:
        surface: A pygame Surface for the image to be loaded onto.
        position: The position on the given Surface on which the image will be drawn to.
        loadMode: The method in which a image will be loaded.
          ⤷ 0 = File Path
          ⤷ 1 = pygame.image
        file_image: The file or image to be loaded. Supports most modern formats.

        crop: Should the image be cropped?
        cropPos: The topright position within the image from which it will be cropped.
        cropArea: The width and height of the croppped area.

        scale: Should the image be scaled?
        scaleMode: The scale mode to be used.
          ⤷ 0 / 0.1 = Scale to (x, y) OR by XXX%.
          ⤷ 1 / 1.1 = Smoothly Scale to (x, y) OR by XXX%. Looks similar to Bilinear or Bicubic.
        scaleAmount: The amount for the image to be scaled to or by."""
    # Loads the image, checking if it's from a file, or a passed in pygame.image.
    if loadMode == 0:
        file_image = pygame.image.load(f"{file_image}").convert_alpha()
    elif loadMode == 1:
        file_image = file_image.convert_alpha()

    # Crops the image, starting from the topright 'cropPos' value given, and extending by the given cropArea values.
    if crop is True:
        file_image = file_image.subsurface(pygame.Rect(cropPos[0], cropPos[1], cropArea[0], cropArea[1])).copy()

    # Scales the image, choosing between pure and smooth scaling. Or not, if not scaling.
    if scale is True:
        if scaleMode == 0:
            file_image = pygame.transform.scale(file_image, scaleAmount)
        elif scaleMode == 0.1:
            file_image = pygame.transform.scale_by(file_image, scaleAmount[0] if type(scaleAmount) is tuple else scaleAmount)
        elif scaleMode == 1:
            file_image = pygame.transform.smoothscale(file_image, scaleAmount)
        elif scaleMode == 1.1:
            file_image = pygame.transform.smoothscale_by(file_image, scaleAmount[0] if type(scaleAmount) is tuple else scaleAmount)

    surface.blit(file_image, position)

def printText(surface:pygame.Surface, font:str='arial', color:tuple=(255, 255, 255), text:str=None, position:tuple=(0, 0), antiAlias=True, bgColor:tuple=None):
    """Load text onto a pygame Surface.
    
    Args:
        surface: A pygame Surface for the text to be loaded onto.
        font: The font to be rendered. | Needs a pygame.font.Font().
        color: The color for text be rendered.
        text: The text to be rendered.
        position: The position on the given Surface on which the text will be drawn to."""
    bgColor == pygame.SRCALPHA if bgColor is None else bgColor == bgColor
    surface.blit(font.render('test', antiAlias, color, bgColor), position)

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

            # 0. Check if the the usual "screen" Surface exists to grab screen size if not already specified.
            screen_size = (screen.get_width(), screen.get_height()) if 'screen' in globals() else screen_size
            self.screen_size = screen_size

            # 1. Bake the surface & mask it ONCE on creation.
            self.surface = pygame.Surface(screen_size, pygame.SRCALPHA)
            pygame.draw.polygon(self.surface, (255, 255, 255), self.points)
            self.mask = pygame.mask.from_surface(self.surface)


        # When called, checks on the mask if the position has a pixel or not.
        def is_hovered(self, position=tuple):
            """Check for collision using the pre-baked mask, to see if there's overlap with the given position."""
            # Makes sure the given position is within bounds as to not crash the program.
            if position[0] < 0:
                x = 0
            elif position[0] > (self.screen_size[0] - 1):
                x = (self.screen_size[0] - 1)
            else:
                x = position[0]

            if position[1] < 0:
                y = 0
            elif position[1] > (self.screen_size[1] - 1):
                y = (self.screen_size[1] - 1)
            else:
                y = position[1]

            # Actual check to make sure the given position is hovering over the polygon.
            return bool(self.mask.get_at((x, y)))

        def is_clicked(self, position):
            """Check if object is hovered and then clicked. Uses 'is_hovered()' to check collision."""
            return self.is_hovered(position) & poll_mouse(1)
# End of Global Pygame Related Functions / Classes.


pygame.init()
pygame.display.set_caption("Friday Night Funkin' - v0.0.1")
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
running = True

playState = 0 # 0 = Main Menu; 1 = Options; 2 = Playing Song; 3 = Paused Song
initialFrame = True
a = 0 # variable for handling animations, usually a table to handle multiple animation timers at once
fullscreen = False

while running:
# poll for events
# pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle switching between game states.
    if pygame.key.get_pressed()[pygame.K_1]:
        playState = 0
        initialFrame = True
    elif pygame.key.get_pressed()[pygame.K_2]:
        playState = 1
        initialFrame = True
    elif pygame.key.get_pressed()[pygame.K_3]:
        playState = 2
        initialFrame = True
    elif pygame.key.get_pressed()[pygame.K_4]:
        playState = 3
        initialFrame = True

    # Fullscreen Toggle Logic
    if pygame.key.get_just_pressed()[pygame.K_F11] and fullscreen is False:
        fullscreen = True
        pygame.display.set_mode((1280, 720))
        pygame.display.toggle_fullscreen()
        sleep(0)
    elif pygame.key.get_just_pressed()[pygame.K_F11] and fullscreen is True:
        fullscreen = False
        pygame.display.toggle_fullscreen()
        pygame.display.set_mode((640, 360))
        sleep(0)

    # Clear the screen.
    screen.fill(pygame.SRCALPHA)

    # Check and run code for each game state.
    match playState:
        case 0:
            if initialFrame:
                a = [0]
                initialFrame = False
            
            # Print to Console the Game State
            print('Main Menu')

            # Print the background.
            printImage(screen, (-58.5, -10), 0, r"D:\Games\FNF 0.8.4 (Collab Update)\assets\images\menuBG.png", False, 0, 0, True, 0.1, 0.59)
            
            # Progress Animations
            if a[0] == 6:
                a[0] = 1
            else:
                a[0] += 1

            # Options Button Animation
            if a[0] <= 2:
                printImage(screen, (167.5, 133.5), 0, r"D:\Games\FNF 0.8.4 (Collab Update)\assets\images\mainmenu\options.png", True, (0, 329), (610, 163), True, 1.1, 0.5)
            elif a[0] <= 4:
                printImage(screen, (167.5, 133.5), 0, r"D:\Games\FNF 0.8.4 (Collab Update)\assets\images\mainmenu\options.png", True, (0, 167), (610, 163), True, 1.1, 0.5)
                print("f2")
            elif a[0] <= 6:
                printImage(screen, (167.5, 133.5), 0, r"D:\Games\FNF 0.8.4 (Collab Update)\assets\images\mainmenu\options.png", True, (0, 0), (610, 163), True, 1.1, 0.5)
                print("f3")
        case 1:
            if initialFrame:
                a = [0, 0]
                initialFrame = False

            print('Options')
        case 2:
            if initialFrame:
                a = [0, 0]
                initialFrame = False

            print('Playing Song')
        case 3:
            if initialFrame:
                a = [0, 0]
                initialFrame = False

            print('Paused Song')

    pygame.display.flip()
    clock.tick(60)