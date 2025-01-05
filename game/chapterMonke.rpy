# This file contains the script for the ape chapter.

define config.default_textshader = "typewriter"

# ====================== initialize monke characters ====================== #

define m1 = Character("Monkey 1", color = "#eb3131")
define m2 = Character("Monkey 2", color = "#e62aec")
define m3 = Character("Monkey 3", color = "#31ec69")
define m4 = Character("Monkey 4", color = "#424ef7")

# ====================== initialize character animations ====================== # 

image monkey:
    "monkey.png"
    zoom 3
    easeout 0.1 yoffset 5  
    easein 0.1 yoffset -5
    repeat

image monkey2:
    "monkey.png"
    zoom 2.9

image monkey3:
    "monkey.png"
    zoom 2.9

image monkey4:
    "monkey.png"
    zoom 2.5

# ====================== scene ====================== #
label chapterMonke:

    play music "monkeyNoises.ogg" volume 0.5
    scene bg black
    scene bg forest with fade:
        zoom 5
    
    nar "The fish’s offspring evolved, becoming countless land creatures, each unique in its own way. Just like you and me, %(name)s."

    char  "That’s not true. Every one of us has different experiences, different choices—different outcomes. No two lives are the same."

    nar "But I’ll never do anything big enough to really change the world."

    nar "Few do. The Earth spins on, indifferent to most of us. But that doesn’t mean your impact is meaningless."

    nar "Even bettering the lives of your friends, your family, or your community—that is enough. Changing their world matters more than you think."

    char "..."

    char "You really think so?"

    nar "I know so."
    pause 1.0

    nar " Oh look! Right on time."

    show monkey at center with moveinleft:
        xoffset -300
    show monkey2 at left with moveinleft

    menu:
        nar "Can you tell the difference between them, %(name)s?"

        "{font=VCRMono.ttf} Yes {/font}":
            char "I think so."
            nar "I knew you do have a good eye."
        "{font=VCRMono.ttf} No {/font}":  
            char "How the {b}hell{/b} am I supposed to know?"
            nar  "The other monkeys recognize each of their own differences, the things that make them unique."

    nar "Be quite and watch."

    m1 "Oo oo"

    m2  "Ah?"

    m1 "Oo ah ah OO OO!!!"

    m1 "{shader=jitter}HAHAHAHAHAHAH!!!{/shader}"
    m2 "{shader=jitter}HAHAHAHAHAHAH!!!{/shader}"

    nar "Ah, laughter, life’s universal delight!"

    m1 "Oo oo ah. (Wait let me show you something)"

    m2 "Oo?"

    nar "Oh! Let us see another event that changed the world!"

    # m1 stands
    #Monkeys are happy!

    char "Why are they so happy? The monkey is just standing…"

    nar "If it wasn’t for this monkey, you would probably still be walking on all fours."

    #Other monkeys enter the scene
    show monkey3 at center with moveinright:
        xoffset 300
    show monkey4 at center with moveinright:
        xoffset 700
    m3 "Oo ooooo… ahh (Look at that dude… He’s trying so hard to be different.)"

    m4 "Oo ah. (Yeah I know right…)"

    m1 "Oo… (Feeling embarrassed)"

    m2 "Hmm…"

    menu:
        nar"The monkey hesitates, unsure of its new skill. But its friend... they have an idea. What’s your next move, %(name)s?"
        "{font=VCRMono.ttf}Stand up for its friend{/font}":
            play audio "choiceEffect.ogg" volume 0.25
            nar "The monkey stands up for its friend. Monkey 1 feels better and more confident. Other monkeys leave."
            m3 "Oooo.. (Let's leave these losers.)"
            m4 "Ahh.. (Yeah, let's go.)"
            hide monkey3 with dissolve
            hide monkey4 with dissolve

            char "What a good monkey!"
            nar "That is right. It stood up for its friend, and changed its life."
            scene bg black with dissolve
            stop music fadeout(1.0)
            jump chapterNewton

            
        "{font=VCRMono.ttf}Blend in with the crowd{/font}.":
            play audio "choiceEffect.ogg" volume 0.25
            show monkey2 at right with move
            nar "Monkey 2 leaves monkey 1 to join other monkeys. Monkey 1 feels sad and sits back down. Humans are never to stand on 2 feet again."
            char "Is that person actually a friend?"
            nar "No. It betrayed. It changed its life forever. Monkeys will never learn to stand on 2 feet again."
            hide monkey2 with dissolve
            hide monkey3 with dissolve
            hide monkey4 with dissolve
            scene bg black with dissolve
            hide monkey with dissolve
            jump sadMonkey

    label sadMonkey:
        stop music fadeout(1.0)
        play music "prologue_Music.mp3"
        show bg prologue light with dissolve
        nar "Oo ah ah. (Have faith in yourself—you’ve got this.)"
        nar "The future is always just out of reach."
        nar "Let's go back..."
        jump chapterMonke

    return
