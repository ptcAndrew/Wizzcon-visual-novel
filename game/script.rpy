# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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

define a = Character("Attendant", color="#3a6ad3", image="attendant")
define maudlin = Character("Maudlin Thistlewood", color="#34eb77", image="maudlin")
define shade = Character("Shadé Ravenstar", color="#6b357c", image="shade")
define millicent = Character("Millicent Smolders", color="#810e06", image="millicent")

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

            jump petting_zoo

        "{color=#db4c04}Casting Ground{/color}":

            jump casting_ground

        "{color=#946bc9}Artifacts Expo{/color}":

            jump artifacts


label petting_zoo:

    return

label casting_ground:

    return

label artifacts:

    return
