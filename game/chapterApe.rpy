# The script of the game goes in this file.

# Declare ys used by this game. The color argument colorizes the
# name of the y.



define y = Character("You")
define n = Character("Narrator", color = "#797777")
define m1 = Character("Monkey 1", color = "#797777")
define m2 = Character("Monkey 2", color = "#797777")
define m3 = Character("Monkey 3", color = "#797777")
define m4 = Character("Monkey 4", color = "#797777")


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
# The game starts here.

label chapterApe:

    play music "monkeyNoises.ogg" volume 0.5

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg forest:
        zoom 5

    # This shows a y sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    scene bg black
    scene bg forest with fade:
        zoom 5
    n "Let us fast forward a bit in time now."

    show monkey at center with moveinleft:
        xoffset -300
    show monkey2 at left with moveinleft:
    n "The offspring of the fish soon evolved into multiple land creatures, each being unique from each other. Just like you and me, %(name)s."

    y "I'm no different from the average person in the world. There is nothing unique about me."
    n "That is false. We all have different experiences, resulting in different outcomes. We are not the same."
    n "You are better than me in certain tasks, while I may be useful in another."

    y "Yeah… but the world would be no different without me."

    n "That may be true if you're talking about Earth as a whole, as we may not change how the world functions in our lifetime."

    y "..."

    n "However, you will be able to change the world of people you interact with."

    #Fade to monkey here. There are a few monkeys on the screen

    menu:
        n "Can you tell the difference between them, %(name)s?"
        "Not really...":
            n  "Well the other monkeys can differentiate between themselves, because they know what is unique between them."
        "Hmm... I kinda do.":
            n "You do have a good eye."

    n "Let us observe these beings."

    m1 "Oo oo"

    m2  "Ah?"

    m1 "Oo ah ah OO OO!!!"

    m1 "HAHAHAHAHAHAH!!!"
    m2 "HAHAHAHAHAHAH!!!"

    n "Oh, how laughter and joy is universal to all creatures."

    m1 "Oo oo ah. (Wait let me show you something)"

    m2 "Oo?"

    n "Oh! Let us see another event that changed the world!"

    # m1 stands

    #Monkeys are happy!

    y "Why are they so happy? The monkey is just standing…"

    n "If it wasn’t for this monkey, you would probably still be walking on all fours."

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
        n "Looks like the monkey doesn’t feel confident about itself and its new skill. But its friend is thinking of something. What should it do %(name)s?"
        "Stand up for its friend":
            play audio "choiceEffect.ogg" volume 0.25
            "The monkey stands up for its friend. Monkey 1 feels better and more confident. Other monkeys leave."
            m3 "Oooo.. (Let's leave these losers.)"
            m4 "Ahh.. (Yeah, let's go.)"
            hide monkey3 with dissolve
            hide monkey4 with dissolve

            y "What a good monkey!"
            n "That is right. It stood up for its friend, and changed its life."
            scene bg black with dissolve
            stop music fadeout(1.0)
            jump chapterNewton

            
        "Join the other monkeys":
            play audio "choiceEffect.ogg" volume 0.25
            show monkey2 at right with move
            n "Monkey 2 leaves monkey 1 to join other monkeys. Monkey 1 feels sad and sits back down. Humans are never to stand on 2 feet again."
            y "Is that person actually a friend?"
            n "No. It betrayed. It changed its life forever. Monkeys will never learn to stand on 2 feet again."
            hide monkey2 with dissolve
            hide monkey3 with dissolve
            hide monkey4 with dissolve
            scene bg black with dissolve
            hide monkey with dissolve
            jump sadMonkey

    label sadMonkey:
        stop music fadeout(1.0)
        play music "prologue_Music.mp3"
        show splashscreen3 with dissolve
        n "Oo Ah ah (Just have some confidence in yourself. You can do it.)"
        "The future is never to come."
        "Let's go back..."
        jump chapterApe

    # This ends the game.

    return
