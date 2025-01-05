# This file contains the script for the Newton chapter.

define config.default_textshader = "typewriter"

# ====================== initialize new characters ====================== #

define Newton = Character("Isaac Newton", color = "#797777")

# ====================== initialize character animations ====================== # 
# [Black scene]
image newton:
    "lachlan isaac.png"
    zoom 2
    animation
    parallel:
        linear 0 xzoom 1.0
        easeout 2 xoffset 50
        linear 0 xzoom -1.0
        easeout 2 xoffset -50
        repeat
    parallel:
        easein 0.5 yoffset 5
        easeout 0.5 yoffset -5
        repeat

image newtonChill:
    "lachlan isaac.png"
    zoom 1.5
    animation
    parallel:
        linear 0 xzoom 1.0
        easeout 2 xoffset 20
        linear 0 xzoom -1.0
        easeout 2 xoffset -20
        repeat
    parallel:
        easein 0.5 yoffset 2
        easeout 0.5 yoffset -2
        repeat

image applefalls:
    "apple.png"
    zoom 1.5
    linear 0 yoffset -900

    parallel:
        linear 1 yoffset 600
    parallel:
        linear 0.5 rotate 360
        repeat

# ====================== scene ====================== #

label chapterNewton:
    play music "issac_Piano.ogg"
    nar "Through countless ages of standing tall, the monkeys have shed their simplicity, evolving into what we now call humans."

    scene bg sunnyfield with dissolve:
        zoom 2.5
    char "Wait…"
    char "{shader=jitter}Is… Is that…{/shader}"
    char "{size=*2}{b}Isaac Newton?!{/b}{/size}"

    show newton at center with dissolve
    nar "Why yes it is"
    menu:
        "{font=VCRMono.ttf}Act excited{/font}":
            char "Holy crap! That’s Isaac Newton!"
            pause(1)
        "{font=VCRMono.ttf}Comment on Newton's appearance{/font}":
            char "Doesn’t he look a little off??"
            char "He kind of looks like the monkey from before."
            nar "No, no, he looks perfectly normal"
            char "Are you sure??"
            nar "Yes, trust me"
            pause(1)

    char "Alright………. Anyway, Why are you showing me him?" 

    nar "Why? Because he’s among the greatest minds to ever exist—the one who revealed the secrets of {b}gravity{/b} itself."

    char "Everyone knows that. I wish I could have done something like that…"

    nar "You can"

    char "I can’t, I’m just not good enough"

    nar "Perhaps oberserving Newton will help you understand"

    Newton "…"

    Newton "Hmmmm….."

    Newton "I have a hypothesis as to why objects fall to the ground. Yet, I cannot be certain of its truth. What if I am entirely mistaken? I should be ridiculed as a fool."

    char "Obviously he isn’t wrong, in the present we know that he was right"

    nar "Ah, but such knowledge was beyond his grasp in those days—impossible for him to foresee."

    char "I guess so…"

    menu:
        Newton "Perhaps I ought to seek a quiet place to refine my hypothesis. Mayhap I shall uncover something to prove it true. Or perchance I am simply chasing madness… Perhaps I should return home."
        "{font=VCRMono.ttf}Find somewhere to study{/font}":
            Newton "No, I am certain there is more to this. I must press on."

        "{font=VCRMono.ttf}Go home{/font}":
            Newton "I'm probably wrong, I’ll just go home…"
            scene bg black with dissolve
            show bg background light with dissolve
            nar "Even flawed action surpasses flawless inaction."
            nar "Belief in oneself is the first step to earning the belief of others."
            nar "The future remains forever out of reach."
            nar "Shall we try again?"
            scene bg black with dissolve
            jump chapterNewton

    char "Of course he should look into it more, he’s on the way to making a huge breakthrough"

    nar  "Ah, that’s the crux of it. He may not know it now, but he is on the verge of something truly extraordinary."

    nar "Others may not see it now, but if you believe in yourself and press forward, it may very well lead to something extraordinary in the end."

    char "…"

    nar "You just have to believe in yourself. Even just a little is enough"

    char "I think I understand"

    menu:
        Newton "Aye, I shall see this through! The fire within me cannot be quelled. Where shall I take my seat and work further?"
        "{font=VCRMono.ttf}Sit under a palm tree{/font}":
            scene bg black with dissolve
            nar "{shader=jitter}{size=*1.5}{b}DEATH BY NUT{/b}{/size}{/shader}"
            nar "Shall we try again?"
            jump chapterNewton
        "{font=VCRMono.ttf}Sit under an apple tree{/font}":
            nar "Newton sat under the Apple tree"
            scene bg appletree with dissolve:
                zoom 1.85
            
    show newtonChill at right
    nar "You know what happens from here. Let us witness history unfold."
    pause(1)
    
    nar  "Newton sits beneath the apple tree, lost in thought, his hypothesis still taking shape."
    nar "As he ponders, an apple falls from the tree and strikes him upon the head."
    show applefalls at right with dissolve
    nar "And so, {b}history is made{/b}."
    pause(1)
    nar "Now, let us return to the present…"
    scene bg black with dissolve
    stop music fadeout(1.0)
    jump chapterEnding
    return