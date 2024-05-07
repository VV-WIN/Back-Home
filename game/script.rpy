define h = Character('house', color="#fb77cf")
define player = Character("[playername]", color="#78acd9")

label start:
    scene bg suburbia with fade
    "A very long time ago, before the world was as we know it, there was a moment of creation."
    "On the Home World, there was a family of beings who looked quite like...well, houses."
    "These beings would spend their days wandering the planet, exploring and learning about the world around them."
    "They were happy, but they were also curious."
    "They wanted to know what else was out there, beyond the Home World. And if they could be a home for someone else."
    "Then one day, a house found themselves in a strange place."

    "In the middle of suburbia on a planet called Earth, there is a house with a pink roof."
    "This house is quite peculiar, as it is the only one in the neighborhood with a pink roof."
    
    show house
    h "Here again, I find myself in this strange place."
    "Manicured lawns, white picket fences, and yet there is something off."
    "This planet that I've landed on is so different from my own."
    "Although I look like every other house I know this isn't home, I'm alone."
    
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