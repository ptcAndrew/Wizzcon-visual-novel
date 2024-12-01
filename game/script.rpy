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
define m = Character("Me")
define q = Character("???")
define a = Character("Attendant", color="#3a6ad3", image="attendant")
define maudlin = Character("Maudlin", color="#34eb77", image="maudlin")
define shade = Character("Shadé", color="#6b357c", image="shade")
define millicent = Character("Millicent", color="#810e06", image="millicent")

# Audio definitions
define audio.bg_noise = "audio/convention_ambience.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/amber2023-30599665/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=262687">Amber</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=262687">Pixabay</a>
define audio.milli_whoosh = "audio/fireball_whoosh.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/floraphonic-38928062/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=179125">floraphonic</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=179125">Pixabay</a>
define audio.sparkle = "audio/sparkling_star.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=99656">freesound_community</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=99656">Pixabay</a>
define audio.punch = "audio/punch.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=41105">freesound_community</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=41105">Pixabay</a>
define audio.boom = "audio/boom.mp3"  # No credits needed ;)
init -1 python:
    #global values for the friendship with each character

    maudlin_given_name = ""

    smolders_met = False
    ravenstar_met = False

    f_thisslewood = 0
    f_smolders = 0
    f_ravenstar = 0

    #millicent dialogue trigger
    disgusting = False

    #where the player has visited
    locations_visited = 0
    zoo_visitied = False
    casting_visiting = False
    expo_visited = False

# The game starts here.

"""
INTRO
"""

label start:

    "{cps=30}The time has come for the 350th annual {w}{size=*2}{cps=*0.25}WIZZCON{/cps}{/size} {p}where wizards, witches, mages, and sorcerers from all over the world come together for 3 days of magical extravaganza!"

    scene bg outside with dissolve

    

    "While thoughts of exotic creatures, peculiar potions, and spectacular spells do excite you; you've come here for one specific reason..."

    "...to find a partner to compete with in the Wizzowski Wizarding Open."

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
        
        "How can I enter the Wizzowski Wizarding Open?":

            jump dialogue2


label dialogue1:

    a "Not sure where to start, huh? I totally get it. {w}The Wizzcon Directory has everything you need, but I'll tell you the highlight spots."

    a "If you're into fantasical creatures, you've {i}got{/i} to check out the {color=#00b347}Petting Zoo.{/color} {w}I heard they have a baby Taratooth there this year, so cute!"

    a "For the battlemage type, the {color=#db4c04}Casting Ground{/color} is down the hall. {w}If you're thinking of joining the (WIZARD BATTLE), that's the place to go. Just watch your head for rouge fireballs, haha. "

    a "Finally, the {color=#946bc9}Artifacts Expo{/color} has magical items from all over the world on display! {w}Some of the things in there really give me the creeps..."

    a positive "Well, make sure to take a brochure. I hope you enjoy your time at Wizzcon!"

    hide attendant with dissolve

    jump where_to_go

label dialogue2:

    a "Oh, do you have a partner to compete with?"

    a @ negative "..."

    a "Well, the (WIZARD BATTLE) has always been a doubles event... {w}but I'm sure you can find someone looking to join you!"

    a "If you're looking for someone who can handle creatures, the {color=#00b347}Petting Zoo{/color} is your best bet. The rules do allow for one animal partner after all."

    a "Of course, the {color=#db4c04}Casting Ground{/color} will be where the real fighting types hang out. Some of them might be a bit... fiery though."

    a "Or maybe you're looking for someone unexpected... {w}the {color=#946bc9}Artifacts Expo{/color} has all sorts of things, you never know who might be poking around there."

    a positive "Well, make sure to take a brochure. I hope you enjoy your time at Wizzcon!"

    hide attendant with dissolve

    jump where_to_go

label where_to_go:
#TODO:
#add conditionals for already visiting the locations

    scene bg inside with dissolve

    if locations_visited == 0:
        
        "{i}I guess I better start checking this place out...{/i}"
    
    show brochure with moveinbottom

    menu:

        "{i}Where should I go...{/i}"

        "{color=#00b347}Petting Zoo{/color}" if zoo_visitied == False:
            $ zoo_visitied = True
            $ locations_visited += 1
            hide brochure
            jump petting_zoo

        "{color=#db4c04}Casting Ground{/color}" if casting_visiting == False:
            $ casting_visiting = True
            $ locations_visited += 1
            hide brochure
            jump casting_ground

        "{color=#946bc9}Artifacts Expo{/color}" if expo_visited == False:
            $ expo_visited = True
            $ locations_visited += 1
            hide brochure
            jump artifacts


label petting_zoo:
    
    scene black
    
    "As you make your way accross the convention center towards the petting zoo, you spot a merry band of wiz-bards performing a jaunty tune. These magical musicians are the source of the music you've been hearing since you entered the convention. Their magic lets the bards' music extend to every room in the convention center."

    "You are distracted from the music as the familiarily pungent odor of farm animals starts to fill your nose. The petting zoo must be near."
    
    scene petting zoo

    "You find the petting zoo, and catch glimpses of a variety of fantastical, if somewhat harmless, beasts and critters. There are more shapes, sizes and colors of them than you've ever seen."

    "In the center of the largest pen, you spot a small green-haired gnome jubilantly frolicking around. His antics have the nearby petting zoo operators and conventiongoers shooting awkward looks his way, but he is unphased. Being a public spectacle enjoyer, you decide to enter the petting zoo for a closer look at this eccentric gnome"

    show maudlin neutral
    
    "You notice the gnome has a jackelope familiar, who catches a whiff of not long after you enter the pen. As if through some deep connection, the gnome whips around to face the very moment your presence is clocked by the jackelope..."

    show maudlin positive

    maudlin "Well would you look at that Barnabus, a new friend has found us! Well met, fellow wizard! I am known as Maudlin Thistlewood, friend to all creatures and zoomancer extraordinare!"

    show maudlin neutral

    maudlin "And to whom do I have the pleasure of meeting on this beauteous day of wizzardly comradery!"

    $ given_name = renpy.input("What name will you give to Maudlin?")
    $ given_name = given_name.strip()  #
    $ maudlin_given_name = given_name

    show maudlin negative

    maudlin "WHAT! [given_name]! Well that's the most obviously FAKE name I've ever heard. And don't try to tell me it isn't, because I'll have you know, I can read minds!"

    maudlin "..."

    show maudlin neutral

    maudlin "Ha! Just kidding my good chum. I can't read minds. In fact, I can't do much of anything magical other than zoomancy. Coming to these big wizard gatherings always makes me feel self-concious. But how could I stay away from this great gathering of beautiful beasts!"
    
    "Maudlin begins spinning in circles with his arms outstretched, humming along to the bards' tune. All the animals in the petting zoo seem to perk up."
    
    Maudlin "Tell me, new friend, what is it that you seek amongst these hallowed halls?"

    menu:
        "I seek honor and glory in the heat of battle. I'm entering the Wizzowski Wizarding Open, and when I've crushed all those who oppose me with my awesome and deadly magic, I will surely be victorious!":
            $ f_smolders -= 1
            jump maudlin_bad_first_impression

        "I'm seeking a wise and trustworthy wizarding companion so I can enter the Wizzowski Wizarding Open. If I and my teammate are to succeed, it will surely take all our combined wits.":
            $ f_smolders += 1
            jump maudlin_good_first_impression

    return

label maudlin_bad_first_impression:
    
    show maudlin negative
    
    maudlin "Hmph! Another violent brute with more muscles than brain cells, I see. Not to be rude, but I don't much care for bullies who think that might makes right."
    
    jump maudlin_scene_2

label maudlin_good_first_impression:
    
    show maudlin positive
    
    maudlin "A wise and prudent strategy! With wizardly cunning like that, I should hope to not be on the wrong end of your wand should our paths cross in the tournament."
    
    jump maudlin_scene_2


label maudlin_scene_2:
    
    "You hear the jackelope Barnabus make a squeaking sound that instantly makes Maudlin's ears perk up. He leans down to the critter and listens closely to it's sounds, then whispers something in it's ear before returning to face you."

    show maudlin neutral

    maudlin "If you hope to succeed in the Open, you'll need a potent and effective companion. I believe that I, the magnanimous Maudlin, could be such a companion! But first, I must of course make sure you meet MY very discerning requirements!"

    maudlin "I'm curious, [given_name], what do you know of zoomancy?"

    menu:
        "Zoomancy is the school of magic that grants dominion over all of the feywilde beasts of our realm.":
            $ f_thisslewood += 1
            show maudlin positive
            maudlin "Why, that is exactly correct! You must have read that seminal Zoomancy reference text 'Zoomancy for Dummies'. I never leave home without it!"

        "Nothing really. What is it, something to do with zooming in on things?":
            # no change to opinion
            show maudlin neutral
            maudlin "Well, uh... no, that's not quite it, but I appreciate your...creative interpretation of the name! It is, in fact, 'the school of magic that grants dominion over all of the feywilde beasts of our realm.'. Now you'll know better for our next first encounter!"
        
        "Zoomancy is pitiful childsplay for the magically inept. Good for nothing except hanging out in dingey petting zoos":
            $ f_thisslewood -= 1
            show maudlin negative
            maudlin "WOW! That has to be one of the mostly outlandishly rude and antagonistic responses you could have possibly chosen! It's like you WANT me to dislike you!"

    show maudlin negative

    maudlin "There are those would look down upon the humble arcana with which I ply my trade. I've heard things like 'Why talk to animals? It's not like they have anything interesting worth saying', or 'Why summon some dumb animal when I can just summon a massive fireball'..."
        
    maudlin "...or even 'Who is that weird green guy hugging all our sheep?'. No one seems to think my magic has any value, but they're WRONG!"

    show maudlin neutral

    maudlin "The natural world holds so many treasures. Every beast, from the smallest insectoids to the mightiest Megalomightisaurodons, is a valuable part of the collective soul of our world"

    "You notice Barnabus make another subtle signal to Maudlin. You notice that some of petting zoo operators are shifting around after having sitting idly nearby since you arrived."

    maudlin "Zoomancers are closely attuned to the natural world. Barnabus here and I have been a bonded pair since I was just a wee gnomeling, barely big enough to frolic through the microgreen pastures of my homeland. We have an breakable trust and understanding! If we are to be companions in the Wizarding Open, Barnabus will need to approve. Could I ask you to let him get a good, long whiff of you? He's harmless, I assure you!"
    
    menu:
        "What?! No way! I'm not letting that little monster get anywhere near me.":
            $ f_thisslewood -= 1
            show maudlin negative
            maudlin "He is NOT a monster, he's a Jackelope! If you weren't comfortable with getting sniffed, you could have just said so without any name-calling!"
            jump maudlin_scene_3

        "I can't, I'm...uh...allergic? Yeah, I'm allergic...":
            # allergy spell bit
            show maudlin neutral
            maudlin "Allergic, you say? I see..."
            show maudlin positive
            maudlin "That sounds like just the job for one of my signature spells, 'Danderbane'! It removes all pet dander within a 5 foot sphere of effect. I could cast it on you if you'd like!"
            menu:
                "Getting blasted by random spells is my favorite weekend activity. Let's do it!":
                    $ f_thisslewood += 1
                    jump maudlin_danderbane

                "If you really think this is necessary, then do what you must":
                    $ f_thisslewood += 1
                    jump maudlin_danderbane

                "I'm ... uh ... also allergic to having zoomancy spells cast on me...?":
                    show maudlin neutral
                    maudlin "Ah, got the zoomancitis eh? By ex-wife had the same thing. Oh well, I guess no getting whiffed for you!"
                    jump maudlin_scene_3

                "'Danderbane'?? What kind of ridiculous spell is that? Forget it!":
                    $ f_thisslewood -= 1
                    show maudlin negative
                    maudlin "Well then, pardon me for trying to be helpful!"
                    jump maudlin_scene_3

        "Why does he need to sniff me? Can't he smell me from here? Why is this even necessary?":
            show maudlin neutral
            maudlin "That's just his way of getting to know you! He can't really get to know you without getting really close. Please, this will only take a moment, and it will make us all more effective wizard collaborators!"
            menu:
                "Sorry, that sounds a little bit to intimate for me. Maybe once we get to know each other better...":
                    # no change to opinion
                    "Fair enough, [given_name]. I shall honor your desires. But Barnabus will surely catch a whiff of you sooner or later!"
                    jump maudlin_scene_3

                "Very well, whiff away.":
                    $ f_thisslewood += 1
                    jump maudlin_sniff

        "Sure! Getting sniffed by a Jackelope is hardly the strangest experience I've had today.":
            $ f_thisslewood += 1
            jump maudlin_sniff

label maudlin_danderbane:
    show maudlin positive
    
    maudlin "Alrighty then, it's SPELL CASTING TIME!"
    maudlin " ~ Abracadoodle and Scoodlydee ~ Get all dander away from thee! ~ "

    "As Maudlin's unhinged magic words take effect, you start to feel an electrifying tingle in the air around you."
    "Then, you feel a sudden zap and see a brilliant flash of light, and feel that tingling sensation flow beneath your skin..."
    "When your senses finally return to you, you look around and see a ring of hair on the floor around your feet. Maudlin's spell has caused all your hair to fall out!"
    
    show maudlin neutral
    maudlin "...Well uhh, looks like this spell needs some work! I've only ever tested it on other gnomes, not whatever it is you are."

    show maudlin positive
    maudlin "The good news is that Barnabus little sniff test is a moot point now. We wanted to know if we could trust you, but I think you've earned a free pass. Sorry about your hair! If it makes you feel any better, I think you look rather dashing with no eyebrows!"
    jump maudlin_scene_3

label maudlin_sniff:
    "Barnabus gently hops over to you and starts sniffing around your feet. He's hardly at it for a minute before he hops back over to Maudlin, who again leans down close and listens carefully to his familiar's squeeks."

    show maudlin neutral

    maudlin "I have an important question for you, [given_name]. Are there any other wizards you are considering as your partner for the Open?"
    
    menu:
        "Yes":
            $ sniff_response = True
            if smolders_met == True or ravenstar_met == True:
                show maudlin positive
                if smolders_met == True and ravenstar_met == True:
                    maudlin "Delightful! Barnabus informed me he smelled traces of both a half-elf and a dragonborn on you. We greatly appreciate you being forthcoming with the truth. Honesty is the best policy after all!"
                elif smolders_met == True:
                    maudlin "Delightful! Barnabus informed me he smelled traces of a dragonborn on you. We greatly appreciate you being forthcoming with the truth. Honesty is the best policy after all!"
                else:
                    maudlin "Delightful! Barnabus informed me he smelled traces of a half-elf on you. We greatly appreciate you being forthcoming with the truth. Honesty is the best policy after all!"
                $ f_thisslewood += 1
            else:
                show maudlin neutral
                maudlin "Is that so? How curious! Barnabus tells me that you have the scent of fresh air upon you, as if to suggest you only just arrived. Who might be your other considerations? Regardless, we've got all the information we need now. Thank you kindly for your cooperation!"

        "No":
            $ sniff_response = False
            if smolders_met == True or ravenstar_met == True:
                show maudlin negative
                maudlin "Bah! I might be small and ridiculous, but I know when I'm being lied to! Barnabus can smell those other wizards you've been cavorting with all over you. I don't know how you can expect us to function as a team when I can't get an honest answer to a simple question from you."
                $ f_thisslewood -= 1
            else:
                show maudlin positive
                maudlin "Delightful! Barnabus informed me that you smell of fresh outdoor air, so you must have just gotten here. Lucky me to be the first wizard you chatted up! Lucky Lucky!!"
                $ f_thisslewood += 1

    jump maudlin_scene_3

label maudlin_scene_3:
    show maudlin neutral

    maudlin "Well my dear [given_name], as much as I would like to prance and cavort with these fantastical beasts all the live-long day, my time here has almost come to an end..."

    if f_thisslewood <= -3:
        $ plan_revealed = False
        # maudlin doesn't trust you
        
    else:
        $ plan_revealed = True
        # maudlin wants your help with his plan
        maudlin "...but perhaps a wizard of your stature might care to aid me in a noble cause of the utmost importance."
        maudlin "You see, I've come to this so called petting zoo with ulterior motives. As a zoomancer, I can feel the emotions of the wild creatures of our world."
        show maudlin negative
        maudlin "And let me tell you, the beasts and critters you see here experience deep pain and suffering daily! They are packed into tight quarters, given minimal food of questionable nutritional value, and paraded about to be gawked at and groped by the unwashed masses. It's an affront to nature, and I intend to stop it!"
        show maudlin neutral    
        maudlin "I have a plan to rescue all these creatures, but I'll need your help. Could you distract the petting zoo staff momentarily? I need time to perform the ritual for my ultiamte spell: 'Mass Beast Teleportation'! With it, all of these creatures will be safely transported to the Thisslewood Family Beast and Critter Sanctuary, my family's nature preserve."
        menu:
            "Sure, I'll help you with your scheme! Let's save the animals!":
                $ f_thisslewood += 2
                jump maudlin_rescue
            "Sorry Maudlin, I don't think I can get involved in this. But your secret plan is safe with me":
                maudlin "I see..."
                maudlin "Well, I would be lying if I said I wan't disappointed, but I've still got to try, even without your help. I'd recommend getting out of here sooner than later, things could get pretty intense once my spell takes effect. Come and find me in the park accross the street from the convention tomorrow if you want to find out how things went!"
                jump maudlin_no_rescue
            "You can't just zap away the petting zoo! These creatures are the property of Wizzcon!":
                $ f_thisslewood -= 1
                show maudlin negative
                maudlin "Keep your voice down you buffoon! If you don't care to take part then so be it, but I'll be quite upset if you ruin this for me. And how dare you refer to these noble beasts as property. They're living things!"
                if f_thisslewood >= 0:
                    maudlin "You might not be cut out to help me here, but if you still want to enter the Wizarding Open together, come find me at the park accross from the convention center tomorrow. Now beat it!"
                else:
                    maudlin "Now get out of here before you spoil everything!"
                jump maudlin_no_rescue
    
label maudlin_no_rescue:
    if plan_revealed:
        "You leave Maudlin to execute his daring rescure operation."

    "As you return to the common areas of the convention center and that farm animal smell disappates, you hear a loud bang and a bright flash coming from the petting zoo."
    if plan_revealed:
        "It would appear Maudlin found some success casting 'Mass Animal Teleport', though it would appear the spell didn't have the effective range he had intended..."
    
    "You can see that the animals previously housed in the petting zoo area have now been spread out to all corners of the convention center. Most of them hardly seem phased by the change, but you do see a group of Wiz-gaurds make their way towards the petting zoo hall. Hopefully Maudlin has a plan to escape capture!"

    scene black with dissolve
    jump where_to_go

label maudlin_rescue:
    show maudlin positive
    
    maudlin "Oh joyous day! Oh splendid tiding indeed! Barnabus was right about you, [given_name]! Now then, go on and create a scene to distract these cursed beast jailers, and I will begin the ritual!"
    
    "Noticing a large pheldagriff standing next to one of the petting zoo attendants nearby, you cast a subtle, low-level electro-shock spell arimed directly at the beast's rump. Instinctively, it kicks it's hind legs instintively and connects with the attendant, sending them flying accross the room."
    "The pheldagriff begins bucking, rampaging and fluttering around, attracting every staff member in the vicinity to try and calm it down. Convention goers are panicking and only making things worse"
    
    maudlin "The ritual is almost complete! Next stop, FREEDOOOOOM!"

    "As Maudlin cries out in victory, a loud bang a bright flash fill the room and completely overwhelm you"
    "When you come to your senses, Maudlin, Barnabus, and all the petting zoo's inhabitants are gone. You find a note in your pocket that says..."
    "{i}If you wish to find the same success in the tournament as we did with our fun little rescue mission, come find me at the park accross from the convention center tomorrow! - Maudlin Thisslewood{/i}"

    scene black with dissolve
    jump where_to_go

"""
CASTING GROUND
#
#
#
#
"""


label casting_ground:
    $ smolders_met = True

    scene casting ground

    "You are curious what the Casting Grounds have to offer this year, so you head that way to check it out."

    "You've always thought of this place as a playground for the more energetically inclined wizards, the ones that love showing off in various flashy ways where they can incur structural damage without getting insurance involved."

    "This is where you'll find all the Evocation Wizards, the ones that love playing around with the elements. {p}Ice Wizards, Water Wizards, Air Wizards, Earth Wizards, Fire Wizards, so many wizards . . . "

    "If you're not careful, you might catch a fireball to the face."

    "Of course, WOSHA regulations are followed and everyone has an invisible shield around them protecting them from {i}serious{/i} damage,"
    
    "But you're not sure if those shields will hold up against {color=#810e06}one particularly enthusiastic Dragonborn{/color} that seems hellbent on watching the world burn."
    
    "You join the handful of observers in her vicinity, mildly curious. She has decimated her opponent with her fire casting, and you watch him dejectedly slink off into the shadows...{p}Which is why you don't notice her scanning the crowd."

    play audio milli_whoosh volume 0.8
    stop sound fadeout 0.1

    show millicent negative
    with moveinright
    
    with vpunch
    q "You!" 

    "She points her clawed hand at you."

    show millicent negative:
        zoom 1.8
        ypos 2.0
    q "Yes, you!"
    
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
    
    
    m "Respectfully, my lady, I do not wish to end up crispy."
    millicent "Accept the challenge, coward."
    
    "The handful of onlookers collectively ooooh, with one of them remarking, \“{i}You gonna let that stand?{/i}\”"

    "Crumbling under the weight of peer pressure, you hesitantly take up her challenge."

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

    
    "{i}That wasn't particularly hard...{/i}"

    millicent "I will enjoy peeling back all the layers till you are nothing and I have your warm guts in my hands!"

    menu:
        "That is disgusting. {s}Please seek therapy. {/s}":
            $ f_smolders -= 1
            $ disgusting = True 
            millicent "You are but a weakling. Your bloodline will die with you."
            "{i}She may have a point. It didn't exactly work out with my last girlfriend...{/i}"
                
            m "Your words may hurt my feelings but your spells won't ever touch me!"
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

            
            m  "You called me clever. So if you keep fighting like you have been, I will continue to outsmart you!"
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

    
    m "Would you not rather save this sort of vehemence for the Wizzowski Wizarding Open?"
    millicent "There is enough rage within me to do both!"
    
    play audio sparkle volume 0.7
    scene white with dissolve
    "She casts Sneaky Sparks Attack and you are momentarily disoriented by all the sudden, small, bright fireballs assaulting your vision."

    scene casting ground with dissolve
    show millicent negative with dissolve
    "It lasts but a second, but as your vision fades back in, so does her fist straight to your nose."
    
    if disgusting:
        "{i}I suppose I did say only her spells won't touch me.{/i}"

    else:
        "{i}Few Wizards abandon their spells in favour of an old fashioned fistfight . . . {/i}"

    play audio punch
    with vpunch
    "You fall flat on your ass, crying out."
    
    millicent "With my mighty fists I shall beat you bloody!"

    "She follows you down and it turns into a grappling contest that you, a human, are ill equipped to win against a Dragonborn."
    
    "She’s got her tail wrapped around your ankle and her tops of her wings pin you to the ground. You attempt to squirm out but she's got a solid hold on you."

    "Feeling trapped and panicky, you rummage through your brain for a spell but only one springs to mind,{w} and it's the worst one you know."

    "Definitely overkill for a {i}\"friendly\"{/i} Wizard fight, but the light is fading..."

    $ spell_name = renpy.input("What spell will you cast?")
    $ spell_name = spell_name.strip()  #

    m "[spell_name]!"
    hide millicent with flash
    play audio boom
    with vpunch
    
    
    m  "{i}*cough* *cough*{/i}"
    "Millicent is a couple feet away, slowly and painfully dragging all her various limbs on the floor. You yourself managed to survive unscathed."

    menu:
        "We've both had enough. Let's call it a tie and end it here.":
            $ f_smolders -= 1
        
        "Your defeat has been a long time coming and I'm glad I could deliver it to you.":
            $ f_smolders += 1
    
    "But she weakly struggles to her feet. A couple emotions pass across her face–confusion, despair, rage–and finally settles on resignation. {w}But she seems ready to continue the fight."

    show millicent negative with moveinbottom
    millicent "The battle is not over yet, wizard."

    "{i}Does she ever give up?{/i}"
        
    m "Save your strength and sign up for the Wizarding Open tomorrow. With you as my partner, we have a chance to win it."
    millicent ". . ."
    
    show millicent positive
    millicent "You have been a worthy opponent. I shall consider it."

    show millicent
    
    m "I wonder if there is more to you, Millicent Smolders. What is it that simmers behind all that fiery rage?"
    show millicent negative
    if f_smolders >= 2:
        millicent "A long list of injustices."
    else:
        millicent "An even {b}hotter{/b} rage."
    
    show millicent
    
    m "... Fair enough."
    m "You'll be able to find me at the Rummaging Rat at Summoning Hour tomorrow."
    "You don't wait for her response before turning around and walking away."
    
    scene black with dissolve
    jump where_to_go

label artifacts:
    $ ravenstar_met = True

    scene artifacts expo

    "It is time for you to check out the Artifacts Expo."

    "There are booths displaying fun wizarding tricks (like nuanced control of Evocation spells to create brilliant elemental artworks) and booths selling neat little gadgets full of fun little magic."

    "Having never strayed far from your own School of Magic, you find the showcases intriguing. You take your time moving from booth to booth, taking in all in."

    "You're watching a skilled Illusion wizard create a hyper-realistic squirrel out of nothing when something catches your attention. {p}Out of the corner of your eye, you spy a vendor one booth over standing a little too close to one of their customers."

    "You watch the customer hand over an envelope full of cash. The vendor surreptitiously slides an Orb of Reanimate One Dead Dude to the customer who quickly pockets it."

    "The customer hastily leaves the booth–you realize it's a Necromancy booth–and the vendor returns to their chair like nothing happened."

    "As far as you know, the Orb of Reanimate One Dead Dude is illegal."

    "You only know what it is because you just finished the chapter on Necromancy in your Histories of Magic Schools for Dummies last night, and it came up. {s}Coincidence?{/s}"

    "Intrigued, you approach the Necromancy booth."



    m "You should really be more careful with how you handle those sorts of transactions."

    show shade with dissolve

    "The vendor looks at you, deadpan and unimpressed. Their name tag reads {color=#6b357c}\"Shade Ravenstar\".{/color}"

    shade "I don't know what you're talking about."

    m "That was an Orb of Reanimate One Dead Dude. You sold one of those to that guy. You can't lie to me."

    show shade negative
    shade "I really don't know what you're talking about about. Did you just come from Wizard Dick's booth of Seeing Things?"

    "{i}What a frustrating being.{/i}"

    m "No, haven't had the pleasure yet. But I think you should go check out The Booth of How To Tell Better Lies."

    shade "..."

    m "..."
    show shade
    shade "What do you want?"

    "Now that you're asked the question, you're not sure how to answer it. "

    menu:
        
        "I should report you to the authorities.":
            $ f_ravenstar -= 1
            shade "..."
            m "What you're doing...that's illegal. "
            show shade negative 
            "Shadé rolls their eyes."
            m "I’m serious! Necromancy can be an abhorrent school of magic and there’s a reason everyone needs to follow the rules around necromantic magical artifacts!"
            jump shade_scene2

        "What else you got?":
            $ f_ravenstar += 1
            shade "..."

            m "You seem super cool and everything, and I wanna win tomorrow's Wizzowski Wizarding Open. {p}If you've got something that can give me an edge in it, that'd be, you know, cool."

            shade "Hm."

            show shade negative
            "Shade gives you a long look. {w}You do not squirm. {w}You don’t."

            show shade
            shade "Okay, let's say I {i}did{/i} have an Orb of Reanimate One Dead Dude–"

            m "You do."

            shade "{i}Hypothetically{/i}. Let's say I did have one. What's a pretty thing like you gonna do with an item like that?"

            menu:
                "Use it to win tomorrow’s Wizarding Open, obviously!":
                    shade "The Orb brings back one conscious being. One {i}dead{/i} conscious being. How does that help you?"

                    m "Uhh..."

                    "You realise that, despite the competition being a battle, there won't be any corpses. No one dies at these things.{p}At least, not usually."

                    m "I'm not sure yet."

                    jump shade_scene2
                "Keep it as a souvenir of having attended Wizzcon 350.":
                    $ f_ravenstar -= 1
                "Resurrect my loved and dearly missed pet rat.":
                    $ f_ravenstar += 1
                    "They take a moment to think about your answer."

                    show shade positive
                    shade "I'm sympathetic to that. But you need the other, more legal, Orb of Reanimate My Dead Pet for that. The Orb of Reanimate One Dead Dude is for conscious beings."

                    m "Yeah... {w}right!"
                    "{i}How did I get that so mixed up? It's literally in the name.{/i}"
                    m "Would you happen to have any of those?"
                    shade "Plenty."
                    "They rummage around in a box and pull out a similar looking orb to the illegal one."

                    m "Right. {w}Um. {w}How do I use it?"
                    jump shade_scene2

                
label shade_scene2:

    show shade negative
    shade "..."
    show shade
    shade "How much do you actually know about the School of Necromancy?"

    menu:
        "Admit it's very little.":
            $ f_ravenstar -= 1
            m "Not very much. It's not my area of expertise and I don't have much of an interest in it, to be honest."

            show shade negative
            "Shadé seems a little let down."

            show shade
            shade "Then how can you tell that what I have is illegal? Do you know what you’re getting yourself into?"

            m "I’ve read all about it in the Histories of Magic Schools for Dummies."
            shade "..."
            shade "Well...{w}You did say you know very little about it all. You did."

        
        "Lie.":
            $ f_ravenstar += 1
            m "Oh, plenty."
            
            show shade positive
            "You begin reciting every detail you can remember from last night's Histories of Magic Schools for Dummies."
            "It's a little rough around the edges, but you feel confident you said enough to convince Shadé that you are NOT a complete idiot."

            show shade
            "Their expression is still and stoic, completely unreadable."
            $ renpy.pause(2.0)

            show shade negative
            shade "So nothing. You know nothing. Actually less than nothing."
            m "H-hey! {p}I know enough to know that you're selling illegal shit under the table!"

            shade "I'm not sure I trust you to tell one Necromancy scroll from another, to be honest."
            m "B-b-"
            shade "Ironically, I think you'd kill {i}yourself{/i} trying to reanimate someone."

            "By this point you are thoroughly embarrassed and regret ever getting involved."

            m "{size=-20}Whatever.{/size}"

            show shade
            shade "May I recommend The Booth of How To Tell Better Lies? I guess we both have a reason to go check it out."
        
    
    jump shade_scene3


label shade_scene3:   

    m "Fine. I don't know much. {p}But you are shady, Shadé Ravenstar. You have the vibes."

    shade "Don't you think you're being a little prejudiced?"

    m "..."

    shade "Necromancy is a respectable school of magic, you know. It's not all corpses and villainy."

    m "Uh-huh."

    show shade positive
    shade "Well, it's all corpses and villainy to me."

    m "See?! I knew it!"

    show shade
    shade "You don't do it for the fame and fortune it brings."

    m "What {i}do{/i} you do it for?"

    if f_ravenstar >= 2:
        shade "..."

        show shade positive
        shade "No one's asked me that before and was actually interested in the answer."

        show shade
        shade "We're all gonna die one day. Our existence is but a blip, and seeing what we're all gonna become keeps me sane. It's peaceful."

        m "Never thought of it that way."

        m "But don't you think, when you bring someone back, you're denying them their rest?"

        shade "They’re not the same. They don't have thoughts. Their soul, or whatever, is gone. It's just their shell and who cares what you do with that?"

    else:

        shade "It's just cooler than all that boring Elemental Magic."

    m "Corpses and villainy, huh. Truly."

    m "Will you be participating in the Wizarding Open?"

    show shade negative
    shade "No. There's very little point to the whole pompous display of power. As if it's not all rigged anyways."

    m "That's a very dour outlook you have there. Sounds like a loser's mindset." 

    shade "It is not!"

    m "I'm just saying, you won't know till you try."

    shade "I {i}have{/i} tried–"

    m "Maybe you just haven't found the right people to do it with yet."

    shade "..."

    show shade
    shade "Right, okay."

    show shade negative
    shade "Get out of my booth."

    show shade
    m "I'll be there tomorrow by the Rummaging Rat plaza at Summoning hour. If you feel like throwing off some of that nihilism, come join me. {p}And bring another Orb of Reanimate One Dead Dude."

    if f_ravenstar >= 2:

        
        shade "You said it yourself, it's illegal."

        m "Since when did that stop you?"

        shade "Ugh...fine,. you're right. But the one I {i}theoretically{/i} just sold was the only one I had."

        m "..."
        m "Liar."

    hide shade with dissolve
    "You shake your head, smile cryptically, and walk away."
    if f_ravenstar >= 2:
        "You're confident they'll show up."

    scene black with dissolve
    jump where_to_go


    return
