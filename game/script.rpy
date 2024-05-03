define h = Character('house', color="#fb77cf")
define player = Character("[playername]")

label start:
    scene bg house_day
    "In the middle of suburbia, there is a house."
    
    show sylvie green surprised
    h "*sigh*"

    "Says the house. It's a house that's seen better days."
    python:
        playername = renpy.input("What is your name?", length=32)
        playername = playername.strip()

        if not playername:
            playername = "Jupiter"
    player "My name is [playername]"