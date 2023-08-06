# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define char = Character("You")
define nar = Character("Narrator", color = "#797777")

default name = "Amos"


# The game starts here.

label prologue:
    play music "prologue_Music.mp3"
    scene bg black
    
    nar "..."

    nar "Hello there. What is your name, child?"

    $ name = renpy.input("Enter your name: ", "Amos")
    $ name = name.strip()

    
    nar "What is wrong %(name)s? You seem concerned."
    show splashscreen3 with dissolve
    pause(2)

    char "I don’t know. I am in a never ending loop of thoughts. Nothing is going my way. I wish that things went differently. I wish I could just rewrite history."

    nar "Would you like to see if history was rewritten?"

    menu:
        "Yes":
            stop music fadeout(1.0)
            jump chapterFish
    # This ends the game.

    return
