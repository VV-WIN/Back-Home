# Characters
define h = Character("[housename]", color="#fb77cf")

# Choices
default greenworldlanding = False
default wastelandlanding = False

label start:
    scene bg space with fade
    """
        Far, far away, on a planet unlike our own, there was a species of beings who looked quite like...
        well, {i}houses{/i}. 
        
        They called themselves the {b}Home Bodies{/b} and were sentient beings, capable of thought and emotion.
        Just because they were houses, didn't mean they were any less intelligent than you or I.

        In fact, they were quite advanced in their own way!
        You see, every house had a purpose, a reason for being. 

        Some were cafes, some were schools, some were hospitals.
        Some were even libraries or museums.
        
        And they all worked together to create a harmonious society.
        For the Home Bodies, the concept of {b}home{/b} was a {i}precious{/i} thing.
        Something that's very important and not to be treated carelessly.

        A home was more than just a building.
        A home was a place of safety, of comfort, of love.
        A home is a place where you belong and can live in peace.
    
        Quickly, the Home Bodies realize that their planet was home to many other beings.
        A single tree could be a home to hundreds of creatures, a river could be a home to thousands of fish.
        
        The Home Bodies believed that it was their duty to protect and care for their world and everything on it.
        Every living thing on the Home World was precious to them.
        And every living thing had a right to a home.
        
        If their plant was a home to so many, then the universe must be home to countless more.
    """
    scene bg suburbia with fade

    """
        In the middle of suburbia, there was a house that was different from the others.
        In a sea of identical beige houses, there was one which had a bright pink roof.
    """
    python:
        housename = renpy.input("What is the house's name?", length=32)
        housename = housename.strip()

        if not housename:
            housename = "Pinky"

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
    scene bg space with fade
    """
        You jump off the planet and into the vast unknown. You're floating through space, and you can see the stars and planets all around you.
        As you drift further and further away from Earth, you feel a sense of peace and calm wash over you.
        
        [housename] closes their eyes and lets themselves drift away, content in the knowledge that they will find their way home.

        After some time, [housename] finds themselves drifting towards two planets. 
        
        One is a lush green world with crystal clear waters, and the other is a barren wasteland.

        Which planet will [housename] choose to land on?
    """

menu:
    "Lush green world" if not greenworldlanding:
        $ greenworldlanding = True
        jump greenworld

    "Barren wasteland" if not wastelandlanding:
        $ wastelandlanding = True
        jump wasteland

label greenworld:
    h "This planet looks beautiful. I think I'll land here."
    "[housename] landed on the lush green world. They were surrounded by vibrant colors and exotic plants."
    "The air is fresh and clean, and you can hear the sound of birds chirping in the distance."
    h """
        Wow! This planet is so lush. It reminds me of how Earth used to be.
        Hellow Geen World! I'm [housename] and I'm here to explore!
    """
    "As [housename] explores the green world, they find themselves feeling more at home than they ever did on Earth."
    "The creatures "
    jump greenworldlanding

label wasteland:
    h "This planet looks desolate. I think I'll land here."
    jump wastelandlanding
