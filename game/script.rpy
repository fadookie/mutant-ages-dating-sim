# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Logan")

label __init_variables:
    python:
        pass
    return

init:
    transform logan_tx:
        zoom 0.75
        nearest True
    transform xmansion_tx:
        zoom 2.2
        xalign 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg x-mansion at truecenter, xmansion_tx
    with fade
    play music "music/28239__herbertboland__forestbirds.ogg"

    "At long last, I've finally found it. The X-Mansion!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show wolverine grimace at right, logan_tx
    with dissolve

    # These display lines of dialogue.

    w "Hey, bub. What are you doing outside class? Where's your hall pass?"

    w "Wait a minute, you're not a student... who are you?"

    # This ends the game.

    return
