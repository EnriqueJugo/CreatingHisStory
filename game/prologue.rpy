# This file contains the script for the very start of the visual novel game.

define config.default_textshader = "typewriter"

label prologue:
    play music "prologue_Music.mp3"
    scene bg black with dissolve
    
    nar "..."

    nar "Hello there. What is your name?"

    $ name = renpy.input("Enter your name: ", "Amos")
    $ name = name.strip()
    
    show bg prologue dark with dissolve
    nar "What is wrong %(name)s? You seem concerned."
    
    pause(2)

    show bg prologue light with vpunch
    char "I don’t know. I'm in a never-ending loop of thoughts."
    show bg prologue light with vpunch
    char "Nothing is going my way."
    show bg prologue light with vpunch
    char "I wish I could just {shader=jitter}REWRITE HISTORY{/shader}."
 
    nar "Would you like to see if history was rewritten?"

    menu:
        "{font=VCRMono.ttf}Yes{/font}":
            play audio "choiceEffect.ogg" volume 0.25
            stop music fadeout(1.0)
            jump chapterFish

    return
