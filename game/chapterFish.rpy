# This file contains the script for the fish chapter.
# The fish chapter is the first chapter of the game. It's about the origin of life and the first step of evolution.

define config.default_textshader = "typewriter"

# ====================== initialize character animations ====================== # 
# lachlandfish moves 
image fishIdle:
    "lachlan fish.png"
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

# lachlan fish positions them self to jump out of the water animation
image fishSurface:
    "lachlan fish.png"
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
        linear 2 rotate -40.0

# lachlan fish jumps out of the water animation 
image fishJump:
    "lachlan fish.png"
    parallel:
        linear 0.01 rotate -40.0
        easein 1.5 yoffset -1000

# ====================== scene ====================== #

label chapterFish:
    play music "waterAudio.ogg" volume 0.5
    scene bg black with fade
    nar "A very very long time ago, we all came from the same origin."

    nar "We all came from the sea."
    
    show bg underwater with dissolve
    pause(0.5)

    show fishIdle at truecenter with moveinleft:
        zoom 3.0

    pause(0.5)

    char "It would’ve been nice if we were all like this fish. Not a care in the world; aimlessly swimming the sea. Such a simple creature."

    nar "You are no simple creature—and neither is this fish. It swims with purpose. And, like you, it is deeply concerned."

    # Minor choice
    menu:
        nar "It is concerned for its life, its health, its future. Worrying means it cares—about something, someone. That something is special."

        # go to fishLearn
        "{font=VCRMono.ttf}Be curious{/font}":
            char "Maybe theres something more to this fish."
            jump fishLearn
        
        # go to fishPurpose
        "{font=VCRMono.ttf}Be pesimistic{/font}":
            char "But what a sad life it is, then. If its sole purpose is merely to survive... it might as well not exist."
            jump fishPurpose

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
        "{font=VCRMono.ttf}Agree{/font}":
            char "I guess it is. It’s a risk worth taking."
            pause(1)

        "{font=VCRMono.ttf}Disagree{/font}":
            char "I don’t know. I don’t think it’s worth it."
            pause(1)

    nar "Hmm..."

    pause(1)

    # Major choie
    label majorFishChoice:
        menu:
            nar "Will you let the fish swim endlessly, drifting until its end? Or will you take the risk to take the first step in all of history?"
            "{font=VCRMono.ttf}Risk it all{/font}":
                char "I’ll take the risk."
                play audio "choiceEffect.ogg" volume 0.25
                jump goodFish
            "{font=VCRMono.ttf}Stay in the water{/font}":
                char "I think I'm happy staying here."
                play audio "choiceEffect.ogg" volume 0.25
                jump badFish

    label goodFish:
        hide fishIdle
        show fishSurface at truecenter:
            zoom 3.0
    
        pause(1)
        show bg white onlayer overlay with dissolve
        scene bg white onlayer overlay
        hide fishSurface

        show fishJump at truecenter:
            zoom 3.0
        nar "The fish took a leap of faith."
        nar "It took a risk." 
        nar "{shader=jitter}It took the first step in all of history{/shader}."
        nar "Let's go forward together."
        show bg white onlayer overlay with dissolve
        scene bg white onlayer overlay
        jump chapterMonke
    
    label badFish:
        scene bg black with dissolve
        hide fishIdle with dissolve
    
    label sadFish:
        scene bg black
        nar "History has shifted. The fish swims on, blind to the other side of the water."
        nar "Land animals? A myth. We are all fish now."
        show splashscreen3 with dissolve
        nar "%(name)s, there’s no time to grieve your fins"
        nar "Let's go back..."
        jump chapterFish


    return
