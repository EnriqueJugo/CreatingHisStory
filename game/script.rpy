# This file contains the first script of the game. 
# This is set up character objects and set up the screen and background for the game, before the prologue is shown.

define char = Character("You", color = "#f0df45")
define nar = Character("Narrator", color = "#797777")

# The game starts here.

label start:

    stop music
    show bg black with dissolve
    jump prologue

    return
