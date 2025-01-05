# This file contains the script for the final chapter.

define config.default_textshader = "typewriter"

# ====================== initialize new characters ====================== #

# NA

# ====================== initialize character animations ====================== #

image lachlanOff:
    "lachlan off.png"
    parallel:
        linear 0.01 xoffset 5
        linear 0.01 xoffset -5
        repeat

    parallel:
        linear 0.01 yoffset 1
        linear 0.01 yoffset -1
        repeat

image lachlanOn:
    "lachlan on.png"

# ====================== scene ====================== #

label chapterEnding:
    #Fades back into present
    play music "presentDayAudio.ogg" volume 0.5
    nar "So what did you think?"

    scene bg bar with dissolve:
        zoom 1.85
    
    show lachlan sitting at right with dissolve:
        zoom 2.5
    char "That was stupid."

    nar "Huh?!"

    char "I couldn’t change anything"

    nar "…"

    char "…  but that was the point. Wasn’t it?"

    nar "Yes."

    nar "There are things in the past that we wish we could change but ultimately we can’t…"

    char "We can only bring the lessons from the past to alter our future"

    nar "Exactly."

    #this is the final quote change as necessary

    scene bg black with dissolve
    stop music
    play audio "lachlanGod.ogg"
    show lachlanOff at truecenter with dissolve:
        zoom 1.5
    pause(2.7)
    scene bg white with dissolve
    scene bg black with None
    show lachlanOn at truecenter:
        zoom 1.5
    "{b}'We cannot change what could have been, but we can change what can be'{/b}"

    pause(2)