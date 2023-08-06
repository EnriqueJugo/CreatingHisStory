# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define l = Character("Lachlan")
define n = Character("Narrator", color = "#797777")



# The game starts here.

label chapterApe:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg forest:
        zoom 5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lachlan monke happy

    # These display lines of dialogue.

    l "Oo oo Aa aa! CoOl tOy!" 

    l "Wut me do?!"

    l "i ShaVe"

    menu:
        n "What should Lachlan shave with his new toy?"
        "Shave his head":
            jump shaveHead
        "Shave his body":
            jump shaveBody

    label shaveHead:
        l "Me liKe tHis lOok!"
        l "I keEp doIng thIs fOr a wHilE!"

        n "Sometimes you just make te wrong choice. But we have to live with it."
        return

    label shaveBody:
        scene bg land
        n "I nO fEel hOt"
        n "you have to take risks somethimes."
        jump issacnewtie

    


    # This ends the game.

    return
