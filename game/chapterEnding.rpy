#defining characters here

define y = Character("You")
define n = Character("Narrator", color = "#797777")

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

#scene begins here
label chapterEnding:
    #Fades back into present
    play music "presentDayAudio.ogg" volume 0.5
    n "So what did you think?"

    scene bg bar with dissolve:
        zoom 1.85
    
    show splashscreen3 trans at right with dissolve:
        zoom 2.5
    y "That was stupid."

    n "Huh?!"

    y "I couldn’t change anything"

    n "…"

    y "…  but that was the point. Wasn’t it?"

    n "Yes."

    n "There are things in the past that we wish we could change but ultimately we can’t…"

    y "We can only bring the lessons from the past to alter our future"

    n "Exactly."

    #this is the final quote change as necessary

    scene bg black with dissolve:
    stop music
    play audio "lachlanGod.ogg"
    show lachlanOff at truecenter with dissolve:
        zoom 1.5
    pause(2.7)
    scene bg white with dissolve
    scene bg black with None
    show lachlanOn at truecenter:
        zoom 1.5
    "'We cannot change what could have been, but we can change what can be'"

    pause(2)