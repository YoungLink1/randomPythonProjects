def readByte(text:str, byte:int, output:int=0, mode:int=0, multiple:bool=False, ebytes:int=None) -> int | str:
    """Reads a specific Byte (or Nybble) from the given text. Can read multiple bytes.
    Meant to parse a file that's a pure binary / hex file.
    !! Because of Python syntax, the first Byte would be position 0.
    !! When reading multiple bytes, output is ALWAYS a string and no longer hex.
    
    Args:
        text: Bytes to be referenced.
        byte: First / Only Byte to be read. Starts at 0.
        output: 0 - Output an int. 1 - Output as hex. 2 - Output as str.
        mode: 0 - Read a Byte. 1 - Read the Low Nybble. 2 - Read the High Nybble.
        multiple: Should multiple bytes be read?
        ebytes: Amount of bytes to read."""
    if multiple is False:
        text = text[(2*byte):(2*byte)+2] # Parse the wanted byte.
        if mode == 1: # Switch to Low Nybble.
            text = text[0]
        elif mode == 2: # Switch to High Nybble.
            text = text[1]
    elif multiple is True:
        i = 0
        output = ""
        while i < ebytes: # while under the amount of bytes checked
            byte_pos = 2*(byte+i)
            output = output + bytes.fromhex(text[(byte_pos):(byte_pos)+2]).decode("utf-8") # Gets the current byte, converts to a UTF-8 string, then is added to the output.
            i += 1 # increases counter for which byte to grab.
        return output

    if output == 0: # Output as int.
        if mode != 0:
            return int(f"0x0{text}", 16)
        else:
            return int(f"0x{text}", 16)
    elif output == 1: # Output as str.
        return str(text)
    elif output == 2:
        input(f"d - {text}; ${byte}")
        return bytes.fromhex(f"0x{text}").decode('utf-8')

with open(r"D:/Coding/Misc/hexTest", "rb") as f:
    h = f.read().hex()

'A Nybble is one half of a byte (EX: $0F). EX: High Nybble of $0F, is $0.'

'''Header of my Hex file:
First 36 bytes are ALWAYS reserved.
Nybble 1 - Map Type: $0/4 - Overworld, $1/5 - Cavern, $2/6 - Forest, $3/7 - Indoor; if int is greater than 3, area is a dungeon.
Nybble 2 - Tileset: $0-F defines the tileset. Some tiles are global / commands. [see below for more]
Bytes 2 & 3 - Width & Height: Defines the width and height of a map in terms of tiles.
Bytes 4 to 11 - Defines the maps North, East, South, and West of current map, while also defining what map entry will be used.
   - Formatted as [Byte1, Byte2] / [Map, Entry].
   - Value of 0xFF is empty.
   - IMPORTANTLY, these can also be used for extra, constant data storage, or imported data. Does mean that any data here could be used for wrong-warping / crashes.
Byte 12 - Defines what music will play in this area.
Bytes 13 to 36 - Name of the map within 24 characters.'''

'''Handling Tiles:
All Visible Tiles are reffered by $00-EF in map data.
    - $C0-EF are Global Tiles, and can be referenced regardless of tileset.
$F0-FF are special command tiles.
    - $F0-FC: Imported data or extra map data will define logic / variables.
    - $FD-$FF: Temporarily go back ($FE) or forward ($FF) in the list of tilesets until reset ($FD).'''

mapType = ["World", "Cave", "Forest", "Indoor", "D_World", "D_Cave", "D_Forest", "D_Indoor"]
tilesets = ["GenericWorld", "Cave", "GenericIndoor", "PokeInterior", "Gym"]

print(f"hex - {h}")
print(mapType[readByte(h, 0, mode=1)])
print(tilesets[readByte(h, 0, mode=2)])
print(f"Width: '{readByte(h, 1)}', Height: '{readByte(h, 2)}'")
print(f"Exits: [{readByte(h, 3)}.{readByte(h, 4)}, {readByte(h, 5)}.{readByte(h, 6)}, {readByte(h, 7)}.{readByte(h, 8)}, {readByte(h, 9)}.{readByte(h, 10)}]")
print(f"Music Track: {readByte(h, 11)}")
print(f"Map Title: '{readByte(h, 12, 0, 0, True, 24)}'")

tiles = [""]