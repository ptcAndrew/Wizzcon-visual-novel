﻿# The script of the game goes in this file.

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
    zoom 0.4
    ypos 1.0
    "millicent neutral.png"

image millicent positive:
    zoom 0.4
    ypos 1.0
    "millicent positive.png"

image millicent negative:
    zoom 0.7
    ypos 1.3
    "millicent negative.png"

image white = "#FFFFFF"

# Transform/transitions
transform resetzoom:
    zoom 1.0

transform slow_moveinbottom(duration=5.0):
    ypos 1.5  # Start from below the screen (adjust based on your layout)
    linear duration ypos 1.0  # Move to the final position over `duration` seconds

define flash = Fade(.25, 0.0, .75, color="#fff")

define move_quick = MoveTransition(0.2)

# Character definitions
define a = Character("Attendant", color="#3a6ad3", image="attendant")
define maudlin = Character("Maudlin Thistlewood", color="#34eb77", image="maudlin")
define shade = Character("Shadé Ravenstar", color="#6b357c", image="shade")
define millicent = Character("Millicent Smolders", color="#810e06", image="millicent")

# Audio definitions
define audio.bg_noise = "audio/convention_ambience.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/amber2023-30599665/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=262687">Amber</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=262687">Pixabay</a>
define audio.milli_whoosh = "audio/fireball_whoosh.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/floraphonic-38928062/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=179125">floraphonic</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=179125">Pixabay</a>
define audio.sparkle = "audio/sparkling_star.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=99656">freesound_community</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=99656">Pixabay</a>
define audio.punch = "audio/punch.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=41105">freesound_community</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=41105">Pixabay</a>
define audio.boom = "audio/boom.mp3"  # No credits needed ;)
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

    "Of course, OSHA regulations are followed and everyone has an invisible shield around them protecting them from {i}serious{/i} damage,"
    
    "But you're not sure if those shields will hold up against {color=#810e06}one particularly enthusiastic Dragonborn{/color} that seems hellbent on watching the world burn."
    
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
    millicent "Coward."
    
    menu:
        "Respectfully, my lady, I do not wish to end up crispy.":
            millicent "Accept the challenge, coward."
    
    "The handful of onlookers collectively ooooh, with one of them remarking, \“{i}You gonna let that stand?{/i}\”"

    "Crumbling under the Weight of peer pressure, you hesitantly take up her challenge."

    jump millicent_scene_2

label accept_millicent_challenge:

    show millicent at resetzoom
    "The onlookers all collectively ooooh, and Millicent assesses you with an approving nod."

    millicent "Prepare yourself, wizard! Let us see what you are made of."
    
    jump millicent_scene_2

label millicent_scene_2:
    play audio milli_whoosh volume 0.8
    show millicent negative at resetzoom:  # For some reason if these 2 lines arent included she flies in from the top of the screen
        ypos 1.3
    show millicent negative with move_quick:
        xpos 0.9
        ypos 1.3
    with vpunch

    "She wastes no time, charging up and letting loose a fearsome fireball aimed straight at you."

    "You expertly sidestep to the left. The fireball hits a dummy instead, way off in the distance."

    millicent "You are a clever one."

    menu:
        "{i}That wasn't particularly hard...{/i}":
            millicent "I will enjoy peeling back all the layers till you are nothing and I have your warm guts in my hands!"

        "There's more to me than my good looks, you know.":
            millicent "We shall see about that! I will enjoy peeling back all the layers till you are nothing and I have your warm guts in my hands!"
    
    menu:
        "That's disgusting!":
            $ f_smolders -= 1
            millicent "You are but a weakling. Your bloodline will die with you."

            menu:
                "She may have a point. It didn't exactly work out with my last girlfriend...":
                    jump millicent_scene_3
                
                "Your words may hurt my feelings but your spells won't ever touch me!":
                    jump millicent_scene_3
        
        "Let's actually not do that, I like my guts where they belong.":
            # Neutral, no change to f score
            jump millicent_scene_3
        
        "Bold of you to assume {i}you{/i} won't be the one skinned alive!":
            $ f_smolders += 1
            show millicent:
                ypos 1.0
            millicent "HA! Let's see you try!"
            
            show millicent negative:
                ypos 1.3
            millicent "You will fall like all the rest. You have neither the strength nor the wit to stand against me."

            menu:
                "You called me clever. So if you keep fighting like you have been, I will continue to outsmart you!":
                    jump millicent_scene_3

label millicent_scene_3:

    play audio milli_whoosh volume 0.8
    show millicent negative at resetzoom:  # For some reason if these 2 lines arent included she flies in from the top of the screen
        ypos 1.3
    show millicent negative with move_quick:
        xpos 0.2
        ypos 1.3
    with vpunch
    
    millicent "It does not matter what you say.{w} Your doom is inevitable.{w} I will concave your head.{w} I shall fashion your corpse into an armchair.{w} I will sear you from existence so thoroughly not even ash will remain!"

    menu:
        "Would you not rather save this sort of vehemence for the Wizzowski Wizarding Open?":
            millicent "There is enough rage within me to do both!"
    
    play audio sparkle volume 0.7
    scene white with dissolve
    "She casts Sneaky Sparks Attack and you are momentarily disoriented by all the sudden, small, bright fireballs assaulting your vision."

    scene placeholder with dissolve
    show millicent negative with dissolve
    "It lasts but a second, but as your vision fades back in, so does her fist straight to your nose."
    
    menu:
        "Few Wizards abandon their spells in favour of an old fashioned fistfight . . . ":
            play audio punch
            with vpunch
            "You fall flat on your ass, crying out."
    
    millicent "With my mighty fists I shall beat you bloody!"

    "She follows you down and it turns into a grappling contest that you, a human, are ill equipped to win against a Dragonborn. She’s got her tail wrapped around your ankle and her tops of her wings pin you to the ground. You attempt to squirm out but she's got a solid hold on you."

    "Feeling trapped and panicky, you rummage through your brain for a spell but only one springs to mind,{w} and it's the worst one you know."

    "Definitely overkill for a {i}\"friendly\"{/i} Wozard fight, but the light is fading..."

    
    hide millicent with flash
    play audio boom
    with vpunch
    "You cast <SPELLNAME>!"

    menu:
        "{i}*cough* *cough*{/i}":
            "Millicent is a couple feet away, slowly and painfully prying all her various limbs off the floor. You yourself managed to survive unscathed."

        "That was awful.":
            "Millicent is a couple feet away, slowly and painfully prying all her various limbs off the floor. You yourself managed to survive unscathed."
    
    menu:
        "We've both had enough. Let's call it a tie and end it here.":
            $ f_smolders -= 1
        
        "Your defeat has been a long time coming and I'm glad I could deliver it to you.":
            $ f_smolders += 1
    
    "But she weakly struggles to her feet. A couple emotions pass across her face–confusion, despair, rage–and finally settles on resignation. But she seems ready to continue the fight."

    show millicent negative with moveinbottom
    millicent "The battle is not over yet, wizard."

    menu:
        "{i}Does she ever give up?{/i}":
            menu:
                "Save your strength and sign up for the Wizarding Open tomorrow. With you as my partner, we have a chance to win it.":
                    millicent ". . ."
    
    show millicent positive
    millicent "You have been a worthy opponent. I shall consider it."

    show millicent
    menu:
        "I wonder if there is more to you, Millicent Smolders. What is it that simmers behind all that fiery rage?":
            show millicent negative
            if f_smolders == 3:
                millicent "A long list of injustices."
            else:
                millicent "An even {b}hotter{/b} rage."
    
    show millicent
    menu:
        "... Fair enough.":
            menu:
                "You'll be able to find me at the Rummaging Rat at Summoning Hour tomorrow.":
                    "You don't wait for her response before turning around and walking away."
    
    scene black with dissolve
    return

label artifacts:

    return
