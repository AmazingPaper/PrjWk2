# import enumeration from Enum
# check link https://docs.python.org/3/library/enum.html for enumerations in python
from enum import Enum


# enumeration tyoe for type of tile
class TileType(Enum):
	PlayerCorner = 1,
	Fight = 2,
	IdleBlack = 3,
	IdleWhite = 4


# enumeration type for player type
class PlayerType(Enum):
	Red = 1,
	Blue = 2,
	Green = 3,
	Yellow = 4
