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

    return



"""
CASTING GROUND
#
#
#
#
"""


label casting_ground:

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
