# WordBlitzBot
## Description
WordBlitzBot is an open-source bot for playing Facebook's WorldBlitz game, entirley written in Python. It's modular design allows it to work on any screen size and language.
## Usage
**Getting started**: Launch calibrate.py and hover your mouse over the tiles in a left-to-right, top-to-bottom fashion (see Tile order). Press shift on each tile. This records the position of your mouse, giving the program a reference for the location of the tiles. After you're done, press Esc.

**Usage**: Launch main.py. At the start of the game, enter the letters on the tiles in a left-to-right, top-to-bottom fashion (see Tile order). After pressing Enter, switch to the browser window, and lean back!

**Pathlist**: The program uses a pre-generated pathlist of all possible paths one can take on a 4x4 grid for faster runtime. However, you can generate the file locally by running path_generator.py.

**Wordlist**: You can import your own language's worldlist by replacing the main.py's CONFIG variable's "wordlist" element with the path to your worldlist.

**Tile order**: The recommended tile order is

1 2 3 4

5 6 7 8

9 10 11 12

13 14 15 16

However, you can use any order of tiles, as long as the order you use for calibrating is the same as the order use for entering letters.
