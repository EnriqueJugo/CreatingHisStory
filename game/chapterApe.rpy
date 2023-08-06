# The script of the game goes in this file.

# Declare ys used by this game. The color argument colorizes the
# name of the y.



define y = y("You")
define n = y("Narrator", color = "#797777")
define m1 = y("Monkey 1", color = "#797777")
define m2 = y("Monkey 2", color = "#797777")
define m3 = y("Monkey 3", color = "#797777")
define m4 = y("Monkey 4", color = "#797777")



# The game starts here.

label chapterApe:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg forest:
        zoom 5

    # This shows a y sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lachlan monke happy

    # These display lines of dialogue.

    n "Let us fast forward a bit in time now."
    n "The offspring of the fish soon evolved into multiple land creatures, each being unique from each other. Just like you and me, %(name)s."

    y "I'm no different from the acerage person in the world. There is nothing unique about me."
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

    m3 "Oo ooooo… ahh(Look at that dude… He’s trying so hard to be different.)"

    m4 "Oo ah. (Yeah I know right…)"

    m1 "Oo… (Feeling embarrassed)"

    m2 "Hmm…"

    menu:
        n "Looks like the monkey doesn’t feel confident about itself and its new skill. But its friend is thinking of something. What should it do %(name)s?"
        "Stand up for its friend":
            n "The monkey stands up for its friend. Monkey 1 feels better and more confident. Other monkeys leave."
        "Join the other monkeys":
            n "Monkey 2 leaves monkey 1 to join other monkeys. Monkey 1 feels sad and sits back down. Humans are never to stand on 2 feet again."
            #jump sadcharacter 


    # This ends the game.

    return
