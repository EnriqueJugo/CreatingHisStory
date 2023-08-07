# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

image fishIdle:
    "lachlanfish.png"
    parallel:
        easeout 1.5 xoffset 10
        easein 1.5 xoffset -10
        repeat
    parallel:
        easeout 0.5 yoffset 5
        easein 0.5 yoffset -5
        repeat
    parallel:
        easeout 2 rotate 2.0
        easein 2 rotate -2.0
        repeat

image fishSurface:
    "lachlanfish.png"
    parallel:
        linear 0.01 xoffset 5
        linear 0.01 xoffset -5
        repeat

    parallel:
        linear 0.01 yoffset 1
        linear 0.01 yoffset -1
        repeat

    parallel:
        linear 0.01 rotate 0.1
        linear 0.01 rotate -0.1
        repeat
    parallel:
        linear 2 rotate -20.0

label chapterFish:
    play music "waterAudio.ogg" volume 0.5
    scene bg black with fade
    nar "A very very long time ago, we all came from the same origin."

    nar "We all came from the sea."
    
    show bg water with dissolve
    pause(1)

    show fishIdle at truecenter with moveinleft:
        zoom 3.0

    pause(1)

    char "It would’ve been nice if we were all like this fish. Not a care in the world; aimlessly swimming the sea. Such a simple creature."

    nar "But you are no simple creature, and so is this fish. This fish is swimming with purpose. And like you, it is very concerned."

    # Minor choice
    menu:
        nar "It is concerned for its life; its health; its future. Being worried shows that you care about something, and that something is special to you."
        "What a sad life it is then. It might as well just not exist if its only purpose is to live.":
            jump fishPurpose
        
        "Maybe I can learn from this fish.":
            jump fishLearn

    # Branch
    label fishPurpose:
        nar "Why yes, %(name)s, but no. This fish’s only purpose is not just to live."
        jump commonPurpose
    
    label fishLearn:
        nar "Why yes, %(name)s. We all can learn from the simplest things. Now lets see this fish’s true purpose."
        jump commonPurpose

    # Merge choices
    label commonPurpose:
        char "What is this fish’s true purpose then?"

    nar "Its purpose is to take a step forward. Find its way out of the water."

    char "Now that’s just stupid. It’s going to die, a very slow… and painful death."

    nar "It is a risk worth taking is it not?"

    menu:
        "No.":
            pause(1)
        "Hmm... I guess so.":
            pause(1)

    nar "Hmm..."

    pause(1)

    # Major choie
    label majorFishChoice:
        menu:
            nar "Would you rather let this fish swim on forever until it dies? Or would you rather take a risk, and take the first step in all of history?"
            "Take the risk":
                play audio "choiceEffect.ogg" volume 0.25
                jump goodFish
            "Let's stay in a safe place":
                play audio "choiceEffect.ogg" volume 0.25
                jump badFish

    label goodFish:
        hide fishIdle
        show fishSurface at truecenter:
            zoom 3.0
    
        pause(1)
        jump happyFish
    
    label happyFish:
        scene bg white with dissolve
        hide fishSurface with dissolve
        nar "The fish took a leap of faith. It took a risk. It took the first step in all of history."
        scene bg black with dissolve
        stop music fadeout(1.0)
        jump chapterApe
    
    label badFish:
        scene bg black with dissolve
        hide fishIdle with dissolve
    
    label sadFish:
        scene bg black
        nar "The course of history is now changed. The fish will swim on forever, until it dies. It will never know what is on the other side."
        nar "There is no such thing as land animals, and we all become fish."
        show splashscreen3 with dissolve
        "Sometimes in life, we have to take risks."
        "The future is never to come."
        "Let's try again..."
        jump chapterFish


    return
