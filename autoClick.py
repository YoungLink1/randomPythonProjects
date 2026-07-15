import mouse as m, keyboard as k, random as r, winsound as wp
from mainLibrary import clear_console

print("============\n Auto Click\n============\n")
print("Controls:\n[Ctrl] & [Space] - Start auto clicker in current position.\n\nWhile auto clicker is on:\n[Enter] - End auto clicker.")

while True:
    #clear_console()
    pos1 = m.get_position()
    x = pos1[0]
    y = pos1[1]
    #print(f"{x}, {y}")

    if k.is_pressed("control") and k.is_pressed("space"):
        wp.PlaySound("C:\Windows\Media\Speech On.wav", 0)

        while not k.is_pressed("enter"):
            m.move(x, y, True, 0)
            m.click("left")

        wp.PlaySound("C:\Windows\Media\Speech Off.wav", 0)

"""while True:
    x = r.randint(0, 1919)
    y = r.randint(0, 1079)
    
    if k.is_pressed("/"):
        m.move(x, y, True, 0)"""