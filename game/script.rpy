define h = Character('house', color="#fb77cf")
define player = Character("[playername]")

label start:
    scene bg suburbia with fade
    "In the middle of suburbia, there is a house with a pink roof."
    
    show house at left
    h "*sigh*"

    python:
        playername = renpy.input("What is your name?", length=32)
        playername = playername.strip()

        if not playername:
            playername = "Jupiter"
    player "My name is [playername]"