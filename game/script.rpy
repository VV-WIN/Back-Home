# Images
image spaceplanet = "images/spaceplanet.png"
image cafe = "images/cafe.png"

# Characters
define h = Character("[housename]", color="#fb77cf")

# Choices
default greenworldlanding = False
default wastelandlanding = False

label start:
    play music "music/back-home.wav"  fadeout 1.0 fadein 1.0
    scene spaceplanet  with fade
    """
        Far, far away, on a planet unlike our own, there was a species of beings who looked quite like...
        well, {i}houses{/i}. 
        
        They called themselves the {b}Home Bodies{/b} and were sentient, capable of thought and emotion.
        Just because they were houses, didn't mean they were any less intelligent than you or I.

        In fact, they were quite advanced in their own way!
        You see, every house had a purpose, a reason for being. 
    """
    scene cafe  with fade
    " Some were cafes, some were schools, some were hospitals."
    """
        Some were even libraries or museums.
        
        And they all worked together to create a harmonious society.
        For the Home Bodies, the idea of {b}home{/b} was a {i}precious{/i} thing.
        Something that's very important and not to be treated carelessly.

        A home was more than just a building.
        A home was a place of safety, of comfort, of love.
        A home is a place where you belong and can live in peace.
    
        Quickly, the Home Bodies realize that their planet was home to many other beings.
        A single tree could be a home to hundreds of creatures, a river could be a home to thousands of fish.
    """
    stop music fadeout 1.0
    """
        The Home Bodies believed that it was their duty to protect and care for their world and everything on it.
        Every living thing on the Home World was precious to them.
        And every living thing had a right to a home.
        
        If their plant was a home to so many, then the universe must be home to countless more.
    """
    scene bg suburbia with fade
    play music "music/intro.wav"  fadeout 1.0 fadein 1.0
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
    h """
        Manicured lawns, white picket fences, and yet there is something off.
        I landed on this planet a long time ago. The natives that lived here were kind and welcoming.

        They respected the land and all the creatures that lived on it. They loved thier home.
        They were the caretakers of this world, and they lived in harmony with nature.

        Who would have thought that such a peaceful world could change so much in such a short time?

        I've seen this world grow from a lush green paradise to fields of concrete and steel.
        I've seen the skies turn gray and the air grow thick with pollution.

        I've seen the diversity of life diminish as more and more species go extinct.
        I've seen the valleys and plains turn into highways, parking lots, and golf courses.
        
        I've seen the oceans fill with trash and the ice caps melt.
        I've seen the rivers run dry and the forests burn.

        I am witnessing the destruction of this world and it breaks my heart.
        And the humans, they just keep building and building, never stopping to think about the consequences of their actions.
    """
    show house at right with wiperight
    h """
        Humans have come and gone, but I've always been here.
        Watching, waiting, hoping that one day they will realize the error of their ways.

        But it's been so long, and I'm starting to lose hope.
        I'm starting to think that maybe they will never change, that maybe they will destroy this world and move on to the next.
        
        And what will happen to my home then?
    """
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
        With all their might, [housename] jumps off the planet Earth!
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
        [housename] jumps off the planet and into the vast unknown. They're floating through space.
        As [housename] drifts further and further away from Earth, they feel a sense of peace and calm wash.
        
        [housename] closes their eyes and let themselves drift. They are weightless, free, and unburdened.

        While they are drifting, they think about all the things they have seen and experienced on Earth.
        All the beauty and wonder, all the destruction and devastation.

        They think about the humans and how they have treated their planet.
    """
    h """ 
        Earth is a beautiful planet, but it is also a fragile one.
        I hope that the humans will realize that before it's too late.

        I'll miss you crow. I'll miss you squirrel. I'll miss you tree.
        I'll miss you river. I'll miss you ocean. I'll miss you bee.
        I'll miss you otter that swims in the river. 
        
        I'll miss you bear and cubs that roam free.
        I'll miss you spider that spins its web. I'll miss you butterfly that flutters by.
        
        I'll miss you whale that sings its song. I'll miss you eagle that soars way up high.
    """

    """
        And with that they fall into a deep sleep. 
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