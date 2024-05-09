define h = Character("[housename]", color="#fb77cf")

label start:
    scene bg suburbia with fade
    """
        A very long time ago, before the world was as we know it, there was a moment of creation.
        On the Home World, there was a family of beings who looked quite like...well, houses.
        
        These beings would spend their days wandering the planet, exploring and learning about the world around them.

        They were happy, but they were also curious. They wanted to know what else was out there, beyond the Home World. 
        And if they could be a home for someone else.
        
        Then one day, a house found themselves in a strange place.
        
        In the middle of suburbia on a planet called Earth, there is a house.
        
        This house is quite peculiar, as it is the only one in the neighborhood with a pink roof.
    """

    python:
        housename = renpy.input("What's the house named?", length=32)
        housename = housename.strip()

        if not housename:
            housename = "Jupiter"

    show house with dissolve
    h "Manicured lawns, white picket fences, and yet there is something off."
    show house at right with wiperight
    h "This planet that I've landed on is so different from my own."
    show house at left with wipeleft
    h "Although I look like every other house I know this isn't home, I'm alone."
    show house at center with dissolve
    h "I gotta get back to the Home World, but how?"
    
menu:
    "Jump off the planet!":
        jump hop

    "Ask for help from the other houses.":
        jump help

label hop:

    """
        With all your might, you jump off the planet Earth!
    """

    jump spacejump

label help:

    h "HELP! I NEED TO GET BACK TO THE HOME WORLD!"
    "Despite [housename]'s pleas, the other houses ignore them. If they can even hear them at all."
    h "I guess I'm on my own. No other choice but to jump off the planet!"

    jump hop

label spacejump:

    """
        You jump off the planet and into the vast unknown. You're floating through space, and you can see the stars and planets all around you.
        As you drift further and further away from Earth, you feel a sense of peace and calm wash over you.
        
        [housename] closes their eyes and lets themselves drift away, content in the knowledge that they will find their way home.

        After some time, [housename] finds themselves drifting towards two planets. 
        
        One is a lush green world with crystal clear waters, and the other is a barren wasteland.

        Which planet will [housename] choose to land on?
    """
menu:
    "Lush green world":
        jump greenworld

    "Barren wasteland":
        jump wasteland
label greenworld:
    h "This planet looks beautiful. I think I'll land here."
    jump landing
label wasteland:
    h "This planet looks desolate. I think I'll land here."
    jump landing
label landing: