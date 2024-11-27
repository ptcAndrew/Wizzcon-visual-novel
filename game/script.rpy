# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Images
image attendant:
    zoom 0.7
    ypos 1.3
    "attendant.png"

image attendant positive:
    zoom 0.7
    ypos 1.3
    "attendant positive.png"

image attendant negative:
    zoom 0.7
    ypos 1.3
    "attendant negative.png"

image maudlin:
    zoom 0.7
    ypos 1.3
    "maudlin neutral.png"

image maudlin positive:
    zoom 0.7
    ypos 1.3
    "maudlin positive.png"

image maudlin negative:
    zoom 0.7
    ypos 1.3
    "maudlin negative.png"

image shade:
    zoom 0.7
    ypos 1.3
    "shade neutral.png"

image shade positive:
    zoom 0.7
    ypos 1.3
    "shade positive.png"

image shade negative:
    zoom 0.7
    ypos 1.3
    "shade negative.png"

image millicent:
    zoom 0.7
    ypos 1.3
    "millicent neutral.png"

image millicent positive:
    zoom 0.7
    ypos 1.3
    "millicent positive.png"

image millicent negative:
    zoom 0.7
    ypos 1.3
    "millicent negative.png"

# Transform
transform resetzoom:
    zoom 1.0
    ypos 1.3

# Character definitions
define a = Character("Attendant", color="#3a6ad3", image="attendant")
define maudlin = Character("Maudlin Thistlewood", color="#34eb77", image="maudlin")
define shade = Character("Shadé Ravenstar", color="#6b357c", image="shade")
define millicent = Character("Millicent Smolders", color="#810e06", image="millicent")

# Audio definitions
define audio.bg_noise = "audio/convention_ambience.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/amber2023-30599665/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=262687">Amber</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=262687">Pixabay</a>
define audio.milli_whoosh = "audio/fireball_whoosh.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/floraphonic-38928062/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=179125">floraphonic</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=179125">Pixabay</a>

init -1 python:
    #global values for the friendship with each character

    f_thisslewood = 0
    f_smolders = 0
    f_ravenstar = 0

# The game starts here.

label start:

    "{cps=30}The time has come for the 1328th annual {w}{size=*2}{cps=*0.25}WIZZCON{/cps}{/size} {p}where wizards, witches, mages, and sorcerers from all over the world come together for 3 days of magical extravaganza!"

    scene bg outside with dissolve

    "While thoughts of exotic creatures, peculiar potions, and spectacular spells do excite you; you've come here for one specific reason..."

    "...to find a partner to compete with in the (NAME OF WIZARD TOURNAMENT)"

    "At the conventions end, the fiercest duos duke it out in the name of wizarding glory, and that glory you {i}must{/i} achieve."

    jump inside

  

label inside:

    play sound bg_noise volume 0.3 loop # adjust volume as needed

    scene bg inside with dissolve

    "Entering the convention hall, the room is packed to the brim with attendees, pointed hats of all shapes and colors moving around the building."

    "Feeling overwhelmed, you notice a kiosk stacked with brochures reading \"Wizzcon Directory\". {w}That'll be helpful."

    show attendant with dissolve

    a "Greetings, welcome to WizzCon! Is there anything I can help you with?"

    menu:
        
        "What is there to do here?":

            jump dialogue1
        
        "How can I enter the (WIZARD BATTLE)?":

            jump dialogue2


label dialogue1:

    a "Not sure where to start, huh? I totally get it. {w}The Wizzcon Directory has everything you need, but I'll tell you the highlight spots."

    a "If you're into fantasical creatures, you've {i}got{/i} to check out the {color=#00b347}Petting Zoo.{/color} {w}I heard they have a baby Taratooth there this year, so cute!"

    a "For the battlemage type, the {color=#db4c04}Casting Ground{/color} is down the hall. {w}If you're thinking of joining the (WIZARD BATTLE), that's the place to go. Just watch your head for rouge fireballs, haha. "

    a "Finally, the {color=#946bc9}Artifacts Expo{/color} has magical items from all over the world on display! {w}Some of the things in there really give me the creeps..."

    jump where_to_go

label dialogue2:

    a "Oh, do you have a partner to compete with?"

    a @ negative "..."

    a "Well, the (WIZARD BATTLE) has always been a doubles event... {w}but I'm sure you can find someone looking to join you!"

    a "If you're looking for someone who can handle creatures, the {color=#00b347}Petting Zoo{/color} is your best bet. The rules do allow for one animal partner after all."

    a "Of course, the {color=#db4c04}Casting Ground{/color} will be where the real fighting types hang out. Some of them might be a bit... fiery though."

    a "Or maybe you're looking for someone unexpected... {w}the {color=#946bc9}Artifacts Expo{/color} has all sorts of things, you never know who might be poking around there."

    jump where_to_go

label where_to_go:

    a positive "Well, make sure to take a brochure. I hope you enjoy your time at Wizzcon!"

    hide attendant with dissolve

    "{i}I guess I better start checking this place out...{/i}"

    show brochure with moveinbottom

    menu:

        "{i}Where should I go first...{/i}"

        "{color=#00b347}Petting Zoo{/color}":
            hide brochure
            jump petting_zoo

        "{color=#db4c04}Casting Ground{/color}":
            hide brochure
            jump casting_ground

        "{color=#946bc9}Artifacts Expo{/color}":
            hide brochure
            jump artifacts


label petting_zoo:

    return

label casting_ground:

    scene placeholder

    "You are curious what the Casting Grounds have to offer this year, so you head that way to check it out."

    "You've always thought of this place as a playground for the more energetically inclined wizards, the ones that love showing off in various flashy ways where they can incur structural damage without getting insurance involved."

    "This is where you'll find all the Evocation Wizards, the ones that love playing around with the elements. Ice Wizards, Water Wizards, Air Wizards, Dirt Wizards, Fire Wizards, so many wizards . . . "

    "If you're not careful, you might catch a fireball to the face."

    "Of course, OSHA regulations are followed and everyone has an invisible shield around them protecting them from {i}serious{/i} damage,{w} but you're not sure if those shields will hold up against {color=#810e06}one particularly enthusiastic Dragonborn{/color} that seems hellbent on watching the world burn."
    
    "You join the handful of observers in her vicinity, mildly curious. She has decimated her opponent with her fire casting, and you watch him dejectedly slink off into the shadows...{p}Which is why you don't notice her scanning the crowd."

    play audio milli_whoosh volume 0.8
    show millicent negative
    with moveinright
    
    with vpunch
    millicent "You!"

    "She points her clawed hand at you."

    show millicent negative:
        zoom 1.8
        ypos 2.0
    millicent "Yes, you!"
    
    millicent "Face me, the great Millicent Smolders!"

    menu millicent_challenge:
        "Vehemently shake your head no.":
            $ f_smolders -= 1
            jump no_millicent_challenge

        "Gracefully accept.":
            $ f_smolders += 1
            jump accept_millicent_challenge

label no_millicent_challenge:

    show millicent negative at resetzoom
    "Swag!"
    return

label accept_millicent_challenge:

    show millicent negative at resetzoom
    "YOLO! xD"
    return

label artifacts:

    return
