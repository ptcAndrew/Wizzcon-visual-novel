# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -1 python:
    #global values for the friendship with each character

    f_thisslewood = 0
    f_smolders = 0
    f_ravenstar = 0

# The game starts here.

label start:

    "{cps=20}The time has come for the 1328th annual {w}{size=*2}{cps=*0.25}WIZZCON{/cps}{/size} {p}where wizards, witches, mages, and sorcerers from all over the world come together for 3 days of magical extravaganza!"

    scene bg outside with dissolve

    "While thoughts of exotic creatures, peculiar potions, and spectacular spells do excite you; you've come here for one specific reason..."

    "...to find a partner to compete with in the (NAME OF WIZARD TOURNAMENT)"

    "At the conventions end, the fiercest duos duke it out in the name of wizarding glory, and that glory you {i}must{/i} achieve."


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # This ends the game.

    return
