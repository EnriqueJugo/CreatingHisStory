define y = Character("You")
define n = Character("Narrator", color = "#797777")
define Newton = Character("Isaac Newton", color = "#797777")

# [Black scene]

image newton:
    "issaclachy.png"
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
    "issaclachy.png"
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

label chapterNewton:
    play music "issac_Piano.ogg"
    n "As a result of standing for millions of years, monkeys have now transformed into slightly more intelligent beings called humans."

    scene bg sunnyfield with dissolve:
        zoom 2.5
    y "Wait… Is… Is that…. Isaac Newton?!"

    show newton at center with dissolve
    n "Why yes it is"
    menu:
        "Doesn’t he look a little off??":
            pause(1)
        "He kind of looks like the monkey from before.":
            pause(1)

    n "No, no, he looks perfectly normal"

    y "Are you sure??"

    n "Yes, trust me"

    y "Alright………. Anyway, Why are you showing me him?" 

    n "Well, he is one of the greatest scientists of all time, he is the one who discovered gravity"

    y "Everyone knows that. I wish I could have done something like that…"

    n "You can"

    y "I can’t, I’m just not good enough"

    n "Well, have a look at this"

    Newton "…"

    Newton "Hmmmm….."

    Newton "I have a hypothesis of why things fall to the ground. But I don’t know if I am right. What if I am completely wrong? I’d be treated like an idiot."

    y "Obviously he isn’t wrong, in the present we know that he was right about gravity"

    n "Well, we only know that now, but it was impossible for him to know at the time"

    y "I guess so…"

    menu:
        Newton "I should find somewhere quiet to work more on my hypothesis? Maybe I can figure something out that proves my hypothesis. I don’t know. Maybe  I should just go home, I am just going crazy."
        "Go home":
            "I'm probably wrong, I’ll just go home…"
            scene bg black with dissolve
            show splashscreen3 with dissolve
            "Imperfect action is better than perfect inaction"
            "For others to believe in you, you have to believe in yourself first"
            "Future is to never come."
            "Let's do it again."
            scene bg black with dissolve
            jump chapterNewton

        "Find somewhere to study":
            Newton "No I believe there is something more to this, I want to keep going"

    y "Of course he should look into it more, he’s on the way to making a huge breakthrough"

    n "That's the point. He doesn’t realise it yet, but he is about to do something incredible"

    y "But how would anyone know?"

    n "People might not realise it yet at the time, but if you just believe in yourself and keep going, it can lead to something incredible in the end."

    y "…"

    n "You just have to believe in yourself. Even just a little is enough"

    y "I think I understand"

    menu:
        Newton "I think I can do this, I’ll keep going, where should I sit to keep working?"
        "Sit under the palm tree":
            scene bg black with dissolve
            "Death by nut"
            "Let's do it again."
            jump chapterNewton
        "Sit under the apple tree":
            "Newton sit under the Apple tree"
            scene bg appletree with dissolve:
                zoom 1.85
            
    show newtonChill at right
    n "Let us watch history happen."
    pause(1)
    scene bg black with dissolve
    "Newton sits under the apple tree and continues to work on his hypothesis."
    "While he is working, an apple falls from the tree and hits him on the head."
    "History has been made."
    pause(1)
    "Let's head back to the present..."
    scene bg black with dissolve
    stop music fadeout(1.0)
    jump chapterEnding
    return