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

image maudlin neutral:
    zoom 0.4
    ypos 0.9
    "maudlin neutral.png"

image maudlin positive:
    zoom 0.4
    ypos 0.9
    "maudlin positive.png"

image maudlin negative:
    zoom 0.4
    ypos 0.9
    "maudlin negative.png"

image maudlin small:
    zoom 0.15
    ypos 0.7
    "maudlin neutral.png"

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

image pippy:
    #zoom 0.6
    ypos 1.1
    "pippy neutral.png"

image pippy positive:
    #zoom 0.7
    ypos 1.1
    "pippy positive.png"

image pippy negative:
    #zoom 0.7
    ypos 1.1
    "pippy negative.png"

image white = "#FFFFFF"

image bg plaza = "bg plaza.jpg"

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
define pippy = Character("Pippy", color="ec2c5d", image="pippy")
define speaker = Character("Announcement", color="#82b2ff")

# Audio definitions
define audio.bg_noise = "audio/convention_ambience.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/amber2023-30599665/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=262687">Amber</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=262687">Pixabay</a>
define audio.milli_whoosh = "audio/fireball_whoosh.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/floraphonic-38928062/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=179125">floraphonic</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=179125">Pixabay</a>
define audio.sparkle = "audio/sparkling_star.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=99656">freesound_community</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=99656">Pixabay</a>
define audio.punch = "audio/punch.mp3"  # Credits: Sound Effect by <a href="https://pixabay.com/users/freesound_community-46691455/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=41105">freesound_community</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=41105">Pixabay</a>
define audio.boom = "audio/boom.mp3"  # No credits needed ;)

init -1 python:
    #global values for the friendship with each character

    maudlin_given_name = "John Doe"
    plan_revealed = False
    helped_maudlin = False
    pippy_upset = False

    f_thisslewood = 0
    f_smolders = 0
    f_ravenstar = 0

    #millicent dialogue trigger
    disgusting = False

    #where the player has visited
    locations_visited = 0
    zoo_visitied = False
    casting_visited = False
    expo_visited = False

    #who is your partner if you get one at the end
    chosen_partner = ""
    team_name = "Wizzards of Oz"

# The game starts here.

"""
INTRO
"""

label start:
    play music "wizzcon theme.mp3"
    queue music "wizzcon theme loop.mp3"

    "{cps=30}The time has come for the 350th annual {w}{size=*2}{cps=*0.25}WIZZCON{/cps}{/size} {p}where wizards, witches, mages, and sorcerers from all over the world come together for a weekend of magical extravaganza!"

    scene bg outside with dissolve

    "While thoughts of exotic creatures, peculiar potions, and spectacular spells do excite you; you've come here for one specific reason..."

    "...to find a partner to compete with in the Wizzowski Wizarding Open."

    "At the conventions end, the fiercest duos duke it out in the name of wizarding glory, and that glory you {i}must{/i} achieve."

    jump intro_pippy

label intro_pippy:

    show pippy positive with dissolve

    pippy positive "I'm so excited! It's the first time I'm here!"

    pippy neutral "We've been best friends for a year and you always talk about this. I'm happy I could come with you."

    m "I'm telling you, I’m gonna get it this time! That glory will be mine!"

    pippy positive "I never doubted you!"

    pippy neutral "But you do need a partner for this thing."

    m "This is what today is for. I will find my partner, and they will help me win!"

    pippy ". . ."

    pippy ". . . I could be your partner."

    menu:

        "*laugh* You? But you're so small! You'll seriously be out of your league here.":
            
            $ pippy_upset = True
            jump pippy_not_happy

        "Pippy, I love you, but you just started learning this year and you'll be up against crazy good wizards that have honed their craft for decades.":

            jump pippy_happy

label pippy_not_happy:

    pippy negative ". . ."

    m "I'm more likely to lose with you than without you. You'd just be a hindrance."

    pippy negative "I was kidding anyways. I'm not delusional, I know I'm not good enough yet."

    m "Maybe next year, then, okay?"

    "Pippy nods stiffly and trails behind you."

    hide pippy with dissolve

    jump inside

label pippy_happy:

    pippy neutral "Good thing I was kidding then! Could you imagine? I'm so not ready, it looks so scary."

    pippy "But I'll be cheering you on!"

    m "And I'm really grateful for your support! I can always count on you to be there."

    m "You're a really great friend to have and I'm glad I met you."

    pippy positive "Me too! I'm really excited for you. Let's go!"

    hide pippy with dissolve
    
    jump inside


label inside:

    play sound bg_noise volume 0.2 loop # adjust volume as needed

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

    a "For the battlemage type, the {color=#db4c04}Casting Ground{/color} is down the hall. {w}If you're thinking of joining the Wizzowski Wizarding Open, that's the place to go. Just watch your head for rouge fireballs, haha. "

    a "Finally, the {color=#946bc9}Artifacts Expo{/color} has magical items from all over the world on display! {w}Some of the things in there really give me the creeps..."

    a positive "Well, make sure to take a brochure. I hope you enjoy your time at Wizzcon!"

    hide attendant with dissolve

    jump check_in_with_pip

label dialogue2:

    a "Oh, do you have a partner to compete with?"

    a @ negative "..."

    a "Well, the Wizzowski Wizarding Open has always been a doubles event... {w}but I'm sure you can find someone looking to join you!"

    a "If you're looking for someone who can handle creatures, the {color=#00b347}Petting Zoo{/color} is your best bet. The rules do allow for one animal partner after all."

    a "Of course, the {color=#db4c04}Casting Ground{/color} will be where the real fighting types hang out. Some of them might be a bit... fiery though."

    a "Or maybe you're looking for someone unexpected... {w}the {color=#946bc9}Artifacts Expo{/color} has all sorts of things, you never know who might be poking around there."

    a positive "Well, make sure to take a brochure. I hope you enjoy your time at Wizzcon!"

    hide attendant with dissolve

    jump check_in_with_pip

label check_in_with_pip:

    "Pippy is scanning the place with big eyes, broshure clutched in her hand."

    if pippy_upset:

        show pippy negative with dissolve

        pippy "Alight then, good luck with the hunt. I'm gonna go get bubbling tea and wander around. {w}See you tomorrow."

        m "Have fun!"

        "She gives you a half-hearted wave as she disappers in the crowd."

    else:

        

        show pippy positive with dissolve

        pippy "Wooooowwww, there's so much here to see! I'm so excited!"

        m "You gonna wander off?"

        pippy "Yup! And get bubbling tea . . ."

        "She checks the broshure, scrunching her brow."

        pippy neutral "It's gotta be here somewhe— Yup! Ok! I'm off! Have fun!"

        m "See you tomorrow!"

        "She waves back as she runs away into the crowd."

    hide pippy with dissolve

    jump where_to_go

label where_to_go:
#TODO:
#add conditionals for already visiting the locations

    scene bg inside with dissolve

    if locations_visited == 0:
        
        "{i}I guess I better start checking this place out...{/i}"
    
    if locations_visited < 3:

        show brochure with moveinbottom

        menu:

            "{i}Where should I go...{/i}"

            "{color=#00b347}Petting Zoo{/color}" if zoo_visitied == False:
                $ zoo_visitied = True
                $ locations_visited += 1
                hide brochure
                jump petting_zoo

            "{color=#db4c04}Casting Ground{/color}" if casting_visited == False:
                $ casting_visited = True
                $ locations_visited += 1
                hide brochure
                jump casting_ground

            "{color=#946bc9}Artifacts Expo{/color}" if expo_visited == False:
                $ expo_visited = True
                $ locations_visited += 1
                hide brochure
                jump artifacts

    elif locations_visited == 3:

        jump second_day

"""
ENDING
"""

label dream:

    scene black

    "Having had your fill of the convention for one day, you retire to your quarters in the nearby Best Wizztern Inn."

    "As you nod off for the night, you start to reflect on your day..."

    "...your reflections turn to dreams, and soon..."

    if f_thisslewood > f_smolders and f_thisslewood > f_ravenstar:
        # best result is maudlin
        "...you see a small green figure surrounded by beasts of all shapes and sizes..."
        "...together, they move with the grace and accuracy of an orchestra..."
        "...shadowy figures opposing the green figure and it's mighty menagerie are overwhelmed..."
        "...then, with a sudden flash and whiff of barnyard smell, you awaken."
    elif f_smolders > f_thisslewood and f_smolders > f_ravenstar:
        # best result is millicent
        "...you see a large winged figure towering over you, while shadowed masses seem to surround you..."
        "...the mighty figure whips their wings and snaps there fingers, and a fiery vortex appears on all sides of you..."
        "...but the heat doesn't burn you. Instead, you feel a fierce passion for victory well up from within you..."
        "...the shadowed masses slowly dwindle and retreat, and you wake up to a subtle smell of brimstone"
    elif f_ravenstar > f_thisslewood and f_ravenstar > f_smolders:
        # best result is shade
        "...you find yourself surrounded by headstones, under an impossibly grey and colorless sky..."
        "...you catch the presence of a slender, graceful figure out of the corner of your eye..."
        "...you try to call out to them, but the very air around you seems to swallow up your voice..."
        "...the slim figure floats towards you as you struggle to speak, and with a gentle thrust of their palm on your chest, you awake suddenly with a start and a deep breath."
    else:
        # there was a tie
        "...you are suddenly surrounded by an impossibly large crowd seated in a colosseum. The excitement of this audience is palpable..."
        "...you see that you are square in the center of the colosseum's combat zone, and from every wall a shadowy figure seems to appear..."
        "...fear overtakes your heart, and you can't help but think that your end is surely near..."
        "...but then, a hand touches your shoulder. You look around and see a familiar face, but you suddenly awaken before you can fully recognize them."
    
    jump ending

label second_day:

    scene black

    "Having had your fill of the convention for one day, you retire to your quarters in the nearby Best Wizztern Inn."

    "You tuck in for the night, taking the time to reflect on all the interesting people you've met, and promptly falling asleep."

    "You wake up to the morning sun peaking through your window. It is the day of the Wizzowski Wizarding Open and you would like to get Pippy's opinion on who she thinks you should partner with."

    "You can always trust her judgement."

    "You dress and make your way over to the Rummaging Rat plaza."

    scene bg plaza with dissolve

    "You spy Pippy chilling in the shade of a big tree with a massive drink in hand."

    if pippy_upset:

        show pippy negative with dissolve

        m "You're not still sulking about yesterday are you?"

        pippy "I'm not sulking."

        "She takes a long pull from her drink's straw."

        m "Okay good! Because I need your help!"

        pippy neutral "Did you find your partner?"

        m "See, that's the thing, I'd like your advice!"

        "Pippy takes another long pull of her drink."

        pippy "Alright. Let's hear it."

        "You recount your previous day's escapades while she listens patiently."

        m "Sooooo, what do you think?"

        "Pippy swirls her straw along the bottom of her drink. She seems dour and moody."
    
        if f_thisslewood > f_smolders and f_thisslewood > f_ravenstar:
            # best result is maudlin
            pippy "Maudlin sounds like a bad choice. He clearly doesn't follow any rules but his own." 
            
            pippy negative "I don't think you'd like someone unpredictable like that as a partner."

            if f_smolders > f_ravenstar:

                pippy neutral "I think you might've best hit it off with Shadé, honestly. I'm sure they'll be a joy to partner with."

            else:

                pippy neutral "But Millicent sure sounds powerful enough to achieve victory. Tho you should be careful she doesn't eat you."

        elif f_smolders > f_thisslewood and f_smolders > f_ravenstar:
            # best result is millicent

            pippy "I'm not sure I like Millicent's attitude to be honest. She seems like the type that would wouldn't play nice in a duo."

            pippy negative "She's too violent and unpredictable, and you might get trampled under her while she's in battle rage."

            if f_thisslewood > f_ravenstar:

                pippy neutral "Shadé sure sounded {i}fun{/i} tho."
            
            else:

                pippy neutral "Now the gnome seems the most reliable. I don't think you could go wrong asking him for help."

        elif f_ravenstar > f_thisslewood and f_ravenstar > f_smolders:
            # best result is shade

            pippy "You are so right! That elf Shadé sure sounds like a shifty creature."

            pippy negative "They sounds ready to leave you for dead and then not bring you back. I wouldn't trust them."

            if f_thisslewood > f_smolders:

                pippy neutral "Now the Dragonborn Millicent, she wears her emotions on her sleeve, I think she's someone you'd be able to trust."

            else:

                pippy neutral "Now Maudlin had a wonderful attitude, he really wasn't shy about accomplishing his goals. I think he would help you best!"
        else:
            # there was a tie

            pippy neutral "Oh. {w}They all sound like they could work . . ."

            pippy neutral "I think you should trust your judgement on this."

            pippy positive "Any one of them would make a wonderful candidate, I'm sure."

        m "I don't know, Pip . . ."

        m "This is such a hard decision, I don't want to pick wrong."

        m "I really need to win it this year!"

        pippy neutral "I'm sure you'll do worderfully."

        hide pippy with dissolve

        jump ending

    else:

        show pippy positive with dissolve

        pippy "Hi! Sleep well? Ready for this?"

        m "A little nervous now that it's happening, but optimistic."

        "She offers you a sip of her drink which you gracefully accept."

        pippy "Sooooo! Tell me about it! How did it go with all the potential candidates yesterday?"

        show pippy neutral with dissolve

        "You recount your previous day's escapades while she listnes patiently."

        pippy neutral "Oh boy, you met quite the cast of characters, huh."

        "She takes a moment to think over her answer."

        if f_thisslewood > f_smolders and f_thisslewood > f_ravenstar:
            # best result is maudlin

            pippy neutral "Maudlin is the obvious choice. He can summon beasts of all shapes and sizes to help you out in your fight."

            pippy "With his graceful movements and fabulous accuracy, nothing would be able to stand in your way."

            pippy positive "You, him, and your mighty menagerie will certainly overwhelm the opponents!" 

        elif f_smolders > f_thisslewood and f_smolders > f_ravenstar:
            # best result is millicent

            pippy neutral "Millicent is the obvious choice. She's so strong and fierce and you clearly impressed her."

            pippy "She'll just whip her wings and snap her fingers and engulf you in a fiery vortex on all sides."

            pippy positive "And bam. You'll win."

        elif f_ravenstar > f_thisslewood and f_ravenstar > f_smolders:
            # best result is shade

            pippy neutral "Shadé is the obvious choice. Their  necromatic abilities sound like they'll really help you in the battle."

            pippy "They'll suck the life spirit from your oponents and weaken their resolve."

            pippy positive "And then you'll go in with the finishing blow!"

        else:
            # there was a tie

            if f_thisslewood == f_smolders:

                pippy "Oh! I think either Maudlin or Millicent would make for a good partner."

            if f_smolders == f_ravenstar:
                
                pippy "Oh! I think either Shadé or Millicent would make for a good partner."

            if f_ravenstar == f_thisslewood:

                pippy "Oh! I think either Maudlin or Shadé would make for a good partner."

            pippy positive "I think they both liked you enough that they'll help you win this year!"

        m "Thanks, Pip. I knew you'd have intelligent things to say about it. I can always trust your judgement!"

        pippy positive "You know it! You can always rely on me to give you the best advice! I won't lead you astray."

        hide pippy with dissolve
        
        jump ending


label ending:

    scene bg plaza with dissolve

    "Pippy finishes giving her advice just in time to hear an annoucement boom across the convention center."

    speaker "Greeting witches and wizards alike! I hope everyone’s been having a magical time!" 
    speaker "It’s almost time for our main event, {p}{size=+20}the Wizzowski Wizarding Open!{/size}"
    speaker "Signups close soon, so be sure to come drop by right away!"

    show pippy neutral with dissolve

    pippy "That's my cue! I'm gonna head in to the arena and find a spot."

    pippy "Good luck!"

    hide pippy with dissolve

    scebe black

    m "{i}There's only time to seek out one potential partner before the signups close. I'll have to choose carefully.{/i}"

    # good and bad endings for each partner
    
    menu:
        "{i}Who should I choose as my partner...?{/i}"

        "{color=#34eb77}Maudlin Thistlewood{/color}":
            scene bg plaza with dissolve
            "You search the Rummaging Rat Plaza for Maudlin."
            "Tracking him down isn't easy, considering both his short stature and his need to lay low after the petting zoo incident yesterday."
            "Luckily, you spot him sitting up in a tree on the outskirts of the plaza sharing an Apple with Barnabus."
            if f_thisslewood > 0:
                jump maudlin_good_ending
            else:
                jump maudlin_bad_ending
        "{color=#810e06}Millicent Smolders{/color}":
            scene bg plaza with dissolve
            "You barely get a chance to scan the Rummaging Rat plaza when you catch Millicent stalking towards you."
            "{i}Well, hey. She saved you the effort of trying to find her.{/i}"
            if f_smolders > 0:
                jump millicent_good_ending
            else:
                jump millicent_bad_ending
        "{color=#6b357c}Shadé Ravenstar{/color}":
            scene bg plaza with dissolve
            "You're patiently scanning the crowd from Rummaging Rat's many public benches."
            "You're trying to catch a glimpse of Shadé. You hope they took you up on the invitation and will come be your partner."
            "It's getting close to the sign-up deadline and you're starting to lose hope."
            "You close your eyes and make a deep regretful sigh."
            scene black with dissolve
            $ renpy.pause(2.0)
            scene bg plaza with dissolve
            show shade with dissolve
            "You open them and Shadé is standing right in front of you."
            if f_ravenstar > 0:
                jump shade_good_ending
            else:
                jump shade_bad_ending

    return

label maudlin_good_ending:
    show maudlin neutral with dissolve
    $ chosen_partner = "Maudlin"
    if helped_maudlin:
        maudlin "Ah, there's my accomplished accomplice!"
        show maudlin positive
        maudlin "I do so appreciate the aid you provided yesterday, my friend. Those animals will live a life of luxury now thanks to you!"
        show maudlin neutral
        maudlin "I can't in good concious let you go without aiding you in kind. Let us show those other wizards what a fine and dandy team we make!"
    elif plan_revealed:
        maudlin "Well hello again friend! I'm happy to report that my rescue mission was a moderate success! I appreciate your discretion in the matter."
        maudlin "Despite your reluctance to aid me, and while it's not exactly my usual scene..."
        show maudlin positive
        maudlin "I feel compelled to aid you in your aspiration to win Wizzowski Wizarding Open. Let us join forces!"
    else:
        maudlin "What a delight to run into you again, [maudlin_given_name]! Come to try your luck in the open?"
        show maudlin positive
        maudlin "While we might not know eachother well, I can't help but have a good feeling about you. and Barnabus agrees!"
        maudlin "I think this is the start of an auspicious friendship. Let us make it truly noteworthy by winning the Wizzowski Wizarding Open, together!"
    jump final_good_ending

label maudlin_bad_ending:
    show maudlin negative
    maudlin "Well then, if it isn't [maudlin_given_name]! I had hoped to have seen the last of you yesterday"
    maudlin "If it hadn't been for your tedious distraction, my all-important rescue mission might not have gone awry!"
    maudlin "I have YOU to blame for those petting zoo animals not making it to my intended destination."
    m "So I guess you wont be interested in joining me in the Wizzowski Wizarding open then?"
    maudlin "Certainly not! You and your laughable ambitions are of no concern to me!"

    jump final_bad_ending

label millicent_good_ending:
    show millicent with dissolve
    millicent "You were a worthy opponent. I shall be your partner for the Wizzowski Wizarding Open."
    m "Oh! That's—"
    show millicent positive
    millicent "We shall roast our enemies like pigs over a fire!{w} They will regret ever facing us!{w} With your wit and my strenth we shall burn them to the ground!"
    m "That's the spirit!"
    show millicent
    "She grabs your arm and tugs you up."
    millicent "Come now, wizard. Let us cast our names into the Wizarding Open. No time to waste!"
    "She drags you behind her to the sign up desks."

    $ chosen_partner = "Millicent"
    jump final_good_ending

label millicent_bad_ending:
    show millicent negative with dissolve
    millicent "I can never face the battle with the likes of you!{w} You are an embarrassment to wizard-ome.{w} You should be ashamed!"
    m "You could just say no. You don't have to be mean about it."
    millicent "Pathetic! You won't make it past the first round. You thought I'd join you? How can I join such a weakling?"
    "She violently turns around and stalks off."
    hide millicent with dissolve

    jump final_bad_ending

label shade_good_ending:
    m "I'm so glad you chose to show up!"
    shade "I'm only here to spectate."
    m "Are you sure? I can use a partner."
    "Shadé stares at you with that typical way that makes you want to squirm."
    "{i}But why are they here if they're not planning on joining you?{i}"
    shade ". . ."
    shade "Alright."
    show shade positive
    shade "But only because you impressed me yesterday."
    m "You won't regret it!"
    show shade
    shade "I wouldn't get your hopes up. I don't think we're going to win."
    m "No, no. I'm optimistic. This will be the year!"
    "You both head off to the sign up desk."

    $ chosen_partner = "Shadé"
    jump final_good_ending

label shade_bad_ending:

    m "I'm so glad you chose to show up."
    shade "This is where all the activity is."
    m "True, true. Will you be participating?"
    shade "I'm only here to spectate."
    m "Come onnnnn. Join me."
    shade "..."
    m "I need a partner. I'm going to win it this year! I think we can do it together."
    show shade negative
    "Shadé stares at you until it becomes super awkward. You clear your throat and shift your weight uncomfortably."
    m "Alright alright, I'll leave you be."

    jump final_bad_ending


label final_good_ending:

    scene bg inside

    "Frantically racing inside the convention center, you look for the desk with the attendant that helped you yesterday."

    a "Attention everyone! This is the last call to signup for the Wizzowski Wizarding Open!"

    "Rushing through the crowd to the sound of their voice, you finally arrive at the desk."

    show attendant with dissolve

    a "Hey, nice to see you again! Have you found a partner for the tournament?"

    m "As a matter of fact, {w}I have."

    show attendant positive
    
    a "Well that's great! Now all I need from you is a team name, and we'll send you right into the competitor's area!"

    "You turn toward [chosen_partner] with a smug grin. They give you a begruding nod."

    show attendant
    $ team_name = renpy.input("What is your team name?")

    show attendant positive
    a "Well [team_name], you're all set! Just head down that marked hallway and prepare for your match. Good luck!"
    
    hide attendant with dissolve

    "The attendant points you toward a corridor on the edge of the main hall. [chosen_partner] tailing behind you, the excitement within you overflowing like a bubbling cauldron."

    "At the end of the hallway, you pull back a curtain into what is most certainly the competitor waiting area."

    "It seems that the first battles have already begun, the sounds of sparks cracking and a roaring crowd muffled by the building walls."

    "You glance around the room at your soon-to-be opponents. Robes, hats, and wands of any imaginable type belonging to wizards awaiting their chance of glory."

    "All of sudden, you here someone call out..."

    a "Alright, [team_name], you're up next!"

    "This is it."

    scene bg arena

    "You and [chosen_partner] follow the attendant through an arched gate, and at the end of the tunnel you see the entrance to the arena."

    a "Good luck out there!"

    "The arena gate opens and the sounds of the crowd flood the tunnel like a tidal wave."
    
    "The crowd grows louder and louder as you walk into the arena. Spotlights flash across your eyes and the cheer of the crowd turns into a formless muffle."

    speaker "...and our newest challengers are [team_name]! They seem like newcomers to the Wizzowski Wizarding Open, but that's no reason to count them out! {p}May the best wizards win!"

    "You take a moment to look at your opponents on the opposite end of the arena. {p}But it doesn't matter what spells they throw at you, or what strange magic they may be masters of."

    "Glancing over at [chosen_partner], reflecting on how not a day prior you were complete strangers, and are now working together in the wizarding fight of your life..."

    "...you know you have what it takes to win."

    scene white with dissolve
    $ renpy.pause(2.0)

    "It's time to get down to Wizz-ness."

    return 

label final_bad_ending:

    "{i}I- I just blew it.{/i}"

    "{i}Surely there's still time to find someone else...{/i}"

    scene bg inside

    "Heading inside the convention center, you desperately ask any wizards who pass by."

    "Unfortunately, all of them either already have a partner or are simply not interested."

    "You know that Pippy might agree out of pity but she really {i}is{/i} just starting out and wont be any help."

    "Your hopes draining by the second, you suddenly hear a voice echo through the convention hall."

    speaker "And with that, our 350th Wizzowski Wizarding Open is officially under way! Please make your way to the Conjuring Coliseum to cheer on these brave warlocks."

    scene black with dissolve

    "The announcement rings through your ears like a dagger to the heart."
    
    scene bg arena with dissolve

    "Sad and defeated you slowly make your way to the spectator seats unable to stop thinking about what could have been."

    "You find Pippy and sit beside her. She spends the whole time sneaking pitying glances at you."

    "The sounds of the crowd cheering, sparks flying, and flames roaring fills you with a crushing feeling of melancholy, despite how engaging the battles are."
    
    scene black with dissolve
    
    "Oh well, maybe next year."

    return

"""
PETTING ZOO
#
MAUDLIN THISTLEWOOD ARC
"""

label petting_zoo:
    
    scene bg inside with dissolve
    
    "You make your way towards the petting zoo. As you walk through the convention center, you spot a merry band of wiz-bards performing a jaunty tune."
    
    "These magical musicians are the source of the music you've been hearing since you entered the convention. The bards' magic lets their music extend to every room in the convention center."

    "You are soon distracted from the music as the familiarily pungent odor of domesticated animals starts to fill your nose. The petting zoo must be near."

    scene petting zoo with dissolve

    "You find the petting zoo, and catch glimpses of a variety of fantastical, if somewhat harmless, beasts and critters. There are more shapes, sizes and colors of them than you've ever seen."

    "In the center of the largest pen, you spot a small green-haired gnome jubilantly frolicking around."
    
    show maudlin small

    "His antics have the nearby petting zoo operators and conventiongoers shooting awkward looks his way, but he is unphased." 
    
    "Being a public spectacle enjoyer, you decide to enter the petting zoo for a closer look at this eccentric gnome."

    show maudlin neutral

    "You notice the gnome has a jackelope familiar, who catches a whiff of you not long after you enter the pen."
    
    "As if through some deep connection, the gnome whips around to face you the very moment your presence is clocked by the jackelope..."

    show maudlin positive

    maudlin "Well would you look at that Barnabus, a new friend has found us! Well met, fellow wizard! I am known as Maudlin Thistlewood, friend to all creatures and zoomancer extraordinare!"

    show maudlin neutral

    maudlin "And to whom do I have the pleasure of meeting on this beauteous day of wizzardly comradery!"

    $ maudlin_given_name = renpy.input("What is your name?")
    $ maudlin_given_name = maudlin_given_name.strip()

    show maudlin negative

    maudlin "WHAT!? [maudlin_given_name]!? Well that's the most obviously FAKE name I've ever heard. And don't try to tell me it isn't, because I'll have you know, I can read minds!"

    maudlin "..."

    show maudlin neutral

    maudlin "Ha! Just kidding my good chum. I can't read minds. In fact, I can't do much of anything magical other than zoomancy." 
    
    maudlin "Coming to these big wizard gatherings always makes me feel self-concious. But how could I stay away from this great gathering of beautiful beasts!"
    
    "Maudlin begins spinning in circles with his arms outstretched, humming along to the bards' tune. All the animals in the petting zoo seem to perk up."
    
    maudlin "Tell me, new friend, what is it that you seek amongst these hallowed halls?"

    m "I'm looking to join the Wizzowski Wizarding Open this year, but I don't have a partner, {i}yet.{/i}"

    menu:
        m "I'm looking for someone who..."


        "...seeks honor and glory in the heat of battle.":
            m "When we've crushed all those who oppose us with our awesome and deadly magic, We will surely be victorious!"
            $ f_thisslewood -= 1
            show maudlin negative
            maudlin "Hmph! Another violent brute with more muscles than brain cells, I see. Not to be rude, but I don't much care for bullies who think that might makes right."

        "...is a wise and trustworthy wizarding companion.":
            m "If my teammate and I are to succeed, it will surely take all our combined wits."
            $ f_thisslewood += 1
            show maudlin positive
            maudlin "A wise and prudent strategy! With wizardly cunning like that, I should hope to not be on the wrong end of your wand should our paths cross in the tournament."

    jump maudlin_scene_2

label maudlin_scene_2:

    show maudlin neutral
    
    "You hear Maudlin's jackelope, Barnabus, make a squeaking sound that instantly causes Maudlin's ears perk up."
    
    "He leans down to the critter and listens closely to it's sounds, then whispers something in it's ear before returning to face you."

    show maudlin positive

    maudlin "If you hope to succeed in the Open, you'll need a potent and effective companion. I believe that I, the magnanimous Maudlin, could be such a companion!"
    
    show maudlin neutral

    maudlin "But first, I must of course make sure you meet MY very discerning requirements!"

    maudlin "I'm curious, [maudlin_given_name], what do you know of zoomancy?"

    menu:
        "Zoomancy is the school of magic that grants dominion over all of the feywilde beasts of our realm.":
            $ f_thisslewood += 1
            show maudlin positive
            maudlin "Why, that is exactly correct! You must have read that seminal Zoomancy reference text 'Zoomancy for Dummies'. I never leave home without it!"

        "Nothing really. What is it, something to do with zooming in on things?":
            # no change to opinion
            show maudlin neutral
            maudlin "Well, uh... no, that's not quite it, but I appreciate your...creative interpretation of the name! It is, in fact, 'the school of magic that grants dominion over all of the feywilde beasts of our realm.'. Now you'll know better for our next first encounter!"
        
        "Zoomancy is pitiful childsplay for the magically inept. Good for nothing except hanging out in dingey petting zoos.":
            $ f_thisslewood -= 1
            show maudlin negative
            maudlin "WOW! That has to be one of the mostly outlandishly rude and antagonistic responses you could have possibly chosen! It's like you WANT me to dislike you!"

    show maudlin negative

    maudlin "There are those who would look down upon the humble arcana with which I ply my trade."
    
    maudlin "I've heard things like 'Why talk to animals? It's not like they have anything interesting worth saying'..."
    
    maudlin "...or 'Why summon some dumb animal when I can just summon a massive fireball'..."
        
    maudlin "...or even 'Who is that weird green guy hugging all our sheep?'. No one seems to think my magic has any value, but they're WRONG!"

    show maudlin neutral

    maudlin "The natural world holds so many treasures. Every beast, from the smallest insectoids to the mightiest Megalomightisaurodons, is a valuable part of the collective soul of our world."

    "You catch Barnabus making another subtle signal to Maudlin. You also notice some petting zoo operators shifting around after having been sat idly nearby since you arrived."

    maudlin "Zoomancers are closely attuned to the natural world. Barnabus here and I have been a bonded pair since I was just a wee gnomeling, barely big enough to frolic through the microgreen pastures of my homeland." 
    
    maudlin "We have an unbreakable trust and understanding! If we are to be companions in the Wizarding Open, Barnabus will need to approve. Could I ask you to let him get a good, long sniff of you? He's harmless, I assure you!"
    
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
                    maudlin "Ah, got the zoomancitis eh? My ex-wife had the same thing. Oh well, I guess no getting sniffed for you!"
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
                    "Fair enough, [maudlin_given_name]. I shall honor your desires. But Barnabus will surely catch a good whiff of you sooner or later!"
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
    maudlin " ~ Abracadoodle and Scoodlydee ~ "
    maudlin " ~ Get all dander away from thee! ~ "

    "As Maudlin's unhinged magic words take effect, you start to feel an electrifying tingle in the air around you."
    "Then, you feel a sudden jolt of energy and see a brilliant flash of light, and a tingling sensation flows beneath your skin..."
    "When your senses finally return to you, you look around and see a ring of hair on the floor around your feet. Maudlin's spell has caused all your hair to fall out!"
    
    show maudlin neutral
    maudlin "...Well uhh, looks like this spell needs some work! I've only ever tested it on other gnomes, not whatever it is you are."

    show maudlin positive
    maudlin "The good news is that our little sniff test is a moot point now. We wanted to know if we could trust you, but I think you've earned a free pass."
    
    maudlin "Sorry about your hair! If it makes you feel any better, I think you look rather dashing with no eyebrows!"
    
    jump maudlin_scene_3

label maudlin_sniff:
    "Barnabus gently hops over to you and starts sniffing around your feet. He's hardly at it for a minute before he hops back over to Maudlin, who again leans down close and listens carefully to his familiar's squeeks."

    show maudlin neutral

    maudlin "I have an important question for you, [maudlin_given_name]. Are there any other wizards you are considering as your partner for the Open?"
    
    menu:
        "Yes":
            $ sniff_response = True
            if casting_visited == True or expo_visited == True:
                show maudlin positive
                if casting_visited == True and expo_visited == True:
                    maudlin "Delightful! Barnabus informed me he smelled traces of both a half-elf and a dragonborn on you. We greatly appreciate you being forthcoming with the truth. Honesty is the best policy after all!"
                elif casting_visited == True:
                    maudlin "Delightful! Barnabus informed me he smelled traces of a dragonborn on you. We greatly appreciate you being forthcoming with the truth. Honesty is the best policy after all!"
                else:
                    maudlin "Delightful! Barnabus informed me he smelled traces of a half-elf on you. We greatly appreciate you being forthcoming with the truth. Honesty is the best policy after all!"
                $ f_thisslewood += 1
            else:
                show maudlin neutral
                maudlin "Is that so? How curious! Barnabus tells me that you have the scent of fresh air upon you, as if to suggest you only just arrived. Who might be your other considerations? Regardless, we've got all the information we need now. Thank you kindly for your cooperation!"

        "No":
            $ sniff_response = False
            if casting_visited == True or expo_visited == True:
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

    maudlin "Well my dear [maudlin_given_name], as much as I would like to prance and cavort with these fantastical beasts all the live-long day, my time here has almost come to an end..."

    if f_thisslewood <= -3:
        $ plan_revealed = False
        # maudlin doesn't trust you
        maudlin "...so if you'll excuse me, I'll be returning my most important work!"
        "Maudlin beings skipping too and fro and singing a song in a language you don't understand. The petting zoos' creatures appear to be moving in time with him."
        jump maudlin_no_rescue
    else:
        $ plan_revealed = True
        # maudlin wants your help with his plan
        maudlin "...but perhaps a wizard of your stature might care to aid me in a noble cause of the utmost importance."
        maudlin "You see, I've come to this so called petting zoo with ulterior motives. As a zoomancer, I can feel the emotions of the wild creatures of our world."
        show maudlin negative
        maudlin "And let me tell you, the beasts and critters you see here experience deep pain and suffering daily!"
        maudlin "They are packed into tight quarters, given minimal food of questionable nutritional value, and paraded about to be gawked at and groped by the unwashed masses."
        maudlin "It's an affront to nature, and I intend to stop it!"
        show maudlin neutral    
        maudlin "I have a plan to rescue all these creatures, but I'll need your help. Could you distract the petting zoo staff momentarily?"
        maudlin "I need time to perform the ritual for my ultimate spell: 'Mass Beast Teleportation'!"
        maudlin "With it, all of these creatures will be safely transported to the Thistlewood Beast and Critter Sanctuary, my family's nature preserve."
        maudlin "These petting zoo goons are in the midst of a shift change — the perfect time to strike!"
        menu:
            "Sure, I'll help you with your scheme! Let's save the animals!":
                if f_thisslewood < 1:
                    $ f_thisslewood = 1
                else:
                    $ f_thisslewood += 1
                jump maudlin_rescue
            "Sorry Maudlin, I don't think I can get involved in this. But your secret plan is safe with me.":
                maudlin "I see..."
                maudlin "Well, I would be lying if I said I wasn't disappointed, but I've still got to try, even without your help."
                maudlin "I'd recommend getting out of here sooner than later, things could get pretty intense once my spell takes effect."
                maudlin "If you want to find out how things went, Come and find me at the Rummaging Rat plaza at Summoning Hour tomorrow!"
                jump maudlin_no_rescue
            "You can't just zap away the petting zoo! These creatures are the property of Wizzcon!":
                $ f_thisslewood -= 1
                show maudlin negative
                maudlin "Keep your voice down you buffoon! If you don't care to take part then so be it, but I'll be quite upset if you ruin this for me."
                maudlin "And how dare you refer to these noble beasts as property. They're living things!"
                if f_thisslewood >= 0:
                    maudlin "You might not be cut out to help me here, but if you still want to enter the Wizarding Open together, come and find me at the Rummaging Rat plaza at Summoning Hour tomorrow. Now beat it!"
                else:
                    maudlin "Now get out of here before you spoil everything!"
                jump maudlin_no_rescue
    
label maudlin_no_rescue:
    if plan_revealed:
        "You leave Maudlin to execute his daring rescue operation."
    else:
        "You leave Maudlin to his odd ritual and make your way out of the petting zoo."

    scene black with dissolve

    "As you return to the common area of the convention center and the farm animal smell disappates, you hear a loud bang and a bright flash coming from the petting zoo."
    if plan_revealed:
        "It would appear Maudlin found some success casting 'Mass Animal Teleport', though it seems the spell didn't have the effective range he had intended..."
    
    "You notice that the animals previously housed in the petting zoo area have now been spread out to all corners of the convention center."
    
    "Most of the creatures hardly seem phased by the change, but you do see a group of Wiz-gaurds make their way towards the petting zoo hall."
    
    if plan_revealed:
        "Hopefully Maudlin has a plan to escape capture!"

    jump where_to_go

label maudlin_rescue:
    $ helped_maudlin = True
    show maudlin positive
    
    maudlin "Oh joyous day! Oh splendid tidings indeed! Barnabus was right about you, [maudlin_given_name]! Now then, go on and create a scene to distract these cursed beast jailers, and I will begin the ritual!"
    
    play audio sparkle volume 0.7
    "Noticing a large pheldagriff standing next to one of the petting zoo attendants nearby, you cast a subtle, low-level electro-shock spell aimed directly at the beast's rump."
    play audio punch
    "Instinctively, it kicks it's hind legs and connects with the attendant, sending them flying accross the room!"
    "The pheldagriff begins bucking, rampaging and fluttering around, attracting every staff member in the vicinity to try and calm it. Convention goers are panicking and only making things worse."
    
    maudlin "The ritual is almost complete! Next stop, FREEDOOOOOM!"

    "As Maudlin cries out in victory, a loud bang and a bright flash fill the room, completely overwhelming you."
    "When you come to your senses, Maudlin, Barnabus, and all the petting zoo's inhabitants are gone. You find a note in your pocket that says..."
    "{i}If you wish to find the same success in the tournament as we did with our fun little rescue mission, come find me at the Rummaging Rat plaza outside the convention center tomorrow! - Maudlin Thisslewood{/i}"

    scene black with dissolve
    jump where_to_go

"""
CASTING GROUND
#
MILLICENT SMOLDERS
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
    
    "The handful of onlookers collectively {i}ooooh{/i}, with one of them remarking, \“{i}You gonna let that stand?{/i}\”"

    "Crumbling under the weight of peer pressure, you hesitantly take up her challenge."

    jump millicent_scene_2

label accept_millicent_challenge:

    show millicent at resetzoom
    "The onlookers all collectively {i}ooooh{/i}, and Millicent assesses you with an approving nod."

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
        "That is disgusting. {s}Please seek therapy.{/s}":
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
    
    m ". . . {w}Fair enough."
    m "You'll be able to find me at the Rummaging Rat plaza at Summoning Hour tomorrow."
    "You don't wait for her response before turning around and walking away."
    
    play sound bg_noise volume 0.2 loop
    scene black with dissolve
    jump where_to_go

"""
ARTIFACTS EXPO
#
SHADÉ RAVENSTAR
"""

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

    "The vendor looks at you, deadpan and unimpressed. Their name tag reads {color=#6b357c}\"Shadé Ravenstar\".{/color}"

    shade "I don't know what you're talking about."

    m "That was an Orb of Reanimate One Dead Dude. You sold one of those to that guy. You can't lie to me."

    show shade negative
    shade "I really don't know what you're talking about about. Did you just come from Wizard Dick's booth of Seeing Things?"

    "{i}What a frustrating being.{/i}"

    m "No, haven't had the pleasure yet. But I think you should go check out The Booth of How To Tell Better Lies."

    shade ". . ."

    m ". . ."
    show shade
    shade "What do you want?"

    "Now that you're asked the question, you're not sure how to answer it. "

    menu:
        
        "I should report you to the authorities.":
            $ f_ravenstar -= 1
            shade ". . ."
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
            "Shadé gives you a long look. {w}You do not squirm. {w}You don’t."

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
    shade ". . ."
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
            m "H-hey! {w}I know enough to know that you're selling illegal shit under the table!"

            shade "I'm not sure I trust you to tell one Necromancy scroll from another, to be honest."
            m "B-b-"
            shade "Ironically, I think you'd kill {i}yourself{/i} trying to reanimate someone."

            "By this point you are thoroughly embarrassed and regret ever getting involved."

            m "{size=-20}Whatever.{/size}"

            show shade
            shade "May I recommend The Booth of How To Tell Better Lies? I guess we both have a reason to go check it out."
        
    
    jump shade_scene3

label shade_scene3:   

    m "Fine. I don't know much. {w}But you are shady, Shadé Ravenstar. You have the vibes."

    shade "Don't you think you're being a little prejudiced?"

    m ". . ."

    shade "Necromancy is a respectable school of magic, you know. It's not all corpses and villainy."

    m "Uh-huh."

    show shade positive
    shade "Well, it's all corpses and villainy to {i}me{/i}."

    m "See?! I knew it!"

    show shade
    shade "You don't do it for the fame and fortune it brings."

    m ". . ."
    m "What {i}do{/i} you do it for?"

    if f_ravenstar >= 2:
        shade ". . ."

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

    shade ". . ."

    show shade
    shade "Right, okay."

    show shade negative
    shade "Get out of my booth."

    show shade
    m "I'll be there tomorrow by the Rummaging Rat plaza at Summoning hour. If you feel like throwing off some of that nihilism, come join me. {w}And bring another Orb of Reanimate One Dead Dude."

    if f_ravenstar >= 2:

        
        shade "You said it yourself, it's illegal."

        m "Since when did that stop you?"

        shade "Ugh...fine,. you're right. But the one I {i}theoretically{/i} just sold was the only one I had."

        m ". . ."
        m "Liar."

    hide shade with dissolve
    "You shake your head, smile cryptically, and walk away."
    if f_ravenstar >= 2:
        "You're confident they'll show up."

    scene black with dissolve
    jump where_to_go