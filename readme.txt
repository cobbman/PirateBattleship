readme.txt

This game is not finished and still in production!!!
Comments or questions can be emailed to me: hello@bigwilliam.com

If you want to try it for what I have so far, run in your terminal: python playgame.py

Files:
PLAY.py - interacts with the user and calls the other modules
boat.py - boat class, creates a boat object
gameboard.py - creates a board that can be different sizes (default is 10x10)
player.py - creates a player. Right now the game is only 1 player


To Do:
- Add visual ASCII when boat is hit or miss to make it more fun (overall user experience needs improving)
- validate inputs, so if user makes an invalid move it won't break
- add feature to create boats of different sizes
- clean up PLAY.py - code there is messy
- when entering coordinates above 5 it doesn't line up with the board

Fixed:
- DONE, AND SIMPLIFIED: some of the boats have negative coordinates… need to fix (boat.py)
- DONE: Update board draw method so it shows coordinate headers that the user can see
- DONE: put checks in place to make sure boats don't overlap!
