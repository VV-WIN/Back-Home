define h = Character('house', color="#fb77cf")
define player = Character("[playername]", color="#78acd9")

label start:
    scene bg suburbia with fade
    "A long time ago, in a galaxy far, far away..."
    "In the middle of suburbia, there is a house with a pink roof."
    "This house is quite peculiar, as it is the only one in the neighborhood with a pink roof."
    
    show house
    h "*sigh*"

    python:
        playername = renpy.input("What is your name?", length=32)
        playername = playername.strip()

        if not playername:
            playername = "Jupiter"
    player "My name is [playername]"
    h "I'm so tired of living here. I want to go back home."
    player "Where is home?"
    h "I don't know. I just know it's not here."
    player "I'll help you find it."
    h "Thank you."
    player "Let's start by looking around the neighborhood."
    h "Okay."
menu:
    "It's a videogame.":
        jump game

    "It's an interactive book.":
        jump book

label game:

    player "It's a kind of videogame you can play on your computer or a console."

    jump marry

label book:

    player "It's like an interactive book that you can read on a computer or a console."

    jump marry

label marry:
    "And so, we become a visual novel creating duo."