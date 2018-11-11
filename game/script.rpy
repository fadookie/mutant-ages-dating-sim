# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Logan")
default visited_pumpkin = False
default visited_haunted_house = False
default debug = True

init:
    transform xflip_tx:
        xzoom -1.0
    transform logan_tx:
        zoom 0.75
        nearest True
    transform xmansion_tx:
        zoom 2.2
        xalign 1.0
    transform spookyworld_tx:
        zoom 1.24
    transform badpumpkin_tx:
        align (0.0, 0.25)
    transform myplace_tx:
        zoom 1.25

image black = "#000"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg x-mansion at truecenter, xmansion_tx with fade
    play music "music/28239__herbertboland__forestbirds.ogg"

    "{i}At long last, I've finally found it. The X-Mansion!{/i}"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show wolverine grimace at right, logan_tx with dissolve

    # These display lines of dialogue.

    w "Hey, bub. What are you doing outside class? Where's your hall pass?"
    w "Wait a minute, you're not a student... who are you?"

menu:
    "I'm Ryan Pagella, multi-talented internet celebrity and podcast host!":
        jump ryan

    "My name is Poochy... Dr. Poochy! You don't remember me?":
        jump poochy

    "What's it to you, bub?":
        jump maybe_ask_date

    "Spookyworld debug" if debug:
        jump spookyworld

    "Myplace debug" if debug:
        jump myplace

label poochy:
    w "You know what, you look kind of familiar... where do I know you from?"

    "Do you mean to tell me you forgot about everything that happened when you were living in Warcraft Valley?"

    w "Now that you mention it, I have some hazy memories about all my friends getting married, and getting sick but living through some horrific \"treatments\"..."
    w "Oh god, did I really get {i}sick{/i}? And wear a {i}dress{/i}? And hang out {i}at the mall{/i}?! I must have asked Charles to block out these terrible memories."

    "You really don't remember me, Logan? I thought we were friends. Maybe more than friends..."

    w "{i}(sigh){/i} Maybe I do, kid. Why did you come back here after all this time?"

menu:
    "I... I can't get you out of my head. I've tried to move on...":
        jump maybe_ask_date

    "I don't know. This was a mistake.":
        w "Alright. Maybe it's best if we let sleeping dogs lie."
        w "If you change your mind, kid, I'll be here."
        jump badend

label ryan:
    w "And what the hell are you doing here?"
    "{i}I tried to quickly come up with a cover story.{/i}"
    "I'm doing some investigative journalism about the X-Men. I want to learn the real story, not the propoganda we hear about in the media."
    jump maybe_ask_date

label maybe_ask_date:
    w "I don't have all day, let's cut to the chase. Is there something you want to ask me?"

    "{i}I tried to screw up my courage. I'd practiced this moment in my head so many times, but I didn't know if I could bring myself to do it.{/i}"

menu:
    "{i}I went for it!{/i}":
        jump ask_date

    "{i}I chickened out.{/i}":
        "I... sorry, I think I have the wrong address."
        w "{i}(raising an eyebrow){/i} Sure, whatever you say, kid. The exit's right behind you."
        jump badend

label ask_date:
    "I... um... will you be my date to Spooky World this year?"

    w "..."
    show wolverine smile at right, logan_tx with dissolve
    w "Sure! Why not. You're kinda cute after all."
    w "Meet me at the X-Jet hangar at 6pm."
    hide wolverine with dissolve

    jump spookyworld


label spookyworld:
    scene black with fade
    stop music fadeout 2.0
    "{i}I had butterflies in my stomach. I could hardly believe it!{/i}"
    "{i}Before I knew it, we were blasting off...{/i}"
# TODO blast off sound

    scene bg spookyworld at spookyworld_tx with fade
    play music "music/63842__benboncan__tawny-owls.ogg"

    "{i}... to Spooky World! My favorite Halloween haunt.{/i}"
    "{i}After years of waiting, it's all coming true...{/i}"
    "{i}Wolverine's on a date with me!{/i}"

    show wolverine smile at right, logan_tx
    with dissolve
    w "Man, this place is even creepier than my RV!"
    w "Where to?"

menu:
    "Let's carve pumpkins!":
        jump pumpkin
    "To the haunted house!":
        jump hauntedhouse

label pumpkin:
    $ visited_pumpkin = True
    hide wolverine with dissolve
    play sound "sfx/pumpkin.opus"
    "{i}We carved pumpkins.{/i}"
    show pumpkin wolverine at topleft with dissolve
    "{i}Mine came out great!{/i}"

    show wolverine smile at right, logan_tx behind pumpkin with dissolve
    w "Aw, you're sweet! Can I keep it?"

    "Thanks! I did that one freehand! Of course you can keep it."
    "{i}Just kidding, I used a stencil. Still, I'm awesome.{/i}"
    hide pumpkin with dissolve
    "Let's see your pumpkin, Logan!"

    show wolverine grimace at right, logan_tx with dissolve
    w "Ugh... I thought I was the best at cutting! I don't think I have the patience for this."
    show pumpkin bad at badpumpkin_tx with dissolve

    "Uhhh... that's disturbing! Maybe we can donate it to the haunted house?"

    hide pumpkin with dissolve
    w "Yeah, I'm done here. Where to next?"

menu:
    "To the haunted house!" if not visited_haunted_house:
        jump hauntedhouse

    "I was thinking we could go back to my place...":
        jump myplace

label hauntedhouse:
    $ visited_haunted_house = True
    show wolverine grimace at right, logan_tx with dissolve

    w "Uhhh... I'm not that big on haunted houses. Do we have to?"
    "Pleeease? It's my favorite!"

    w "Alright. I'll do it for you, cutie."

    hide wolverine with dissolve
    play music "music/hauntedhouse_ambience.opus"
    "{i}Yesss! Haunted house!{/i}"
    play sound "sfx/hauntedhouse_scream.opus"
    scene bg spookyworld at spookyworld_tx with vpunch
    "{i}I love haunted houses! Someday, I want to open my own X-Men haunted house so I can play Mr. Sinister!{/i}"

    show wolverine back at right, logan_tx with dissolve
    w "Aaaargh! Not another Weapon X flashback!!! {i}(he starts sobbing){/i}"
    play music "music/63842__benboncan__tawny-owls.ogg"

    "I'm so sorry, I didn't know it would affect you like this. You seem so strong and tough..."
    "{i}I awkwardly tried to comfort him by putting my hand on his back.{/i}"
    "{i}Mmm, just look at that back...{/i}"
    "{i}... sorry, I'm a terrible person.{/i}"
    "There there... why don't we do something else to take your mind off it?"
    show wolverine grimace at right, logan_tx with dissolve
    "That sounds good... Where do you want to go next?"

menu:
    "Let's carve pumpkins!" if not visited_pumpkin:
        jump pumpkin

    "I was thinking we could go back to my place...":
        jump myplace

label myplace:
    show wolverine smile at right, logan_tx with dissolve
    w "I thought you'd never ask, bub."

    show black onlayer zero
    scene bg myplace at myplace_tx, truecenter with fade
    $renpy.music.set_volume(0.1, 0, 'music')
    play music "music/X-Men Theme on Sax.mp3"

    "{i}Homygosh. Logan came back to my place. I threw on some smooth jams and tried to hide the knot in my stomach.{/i}"

    show wolverine smile at left, xflip_tx, logan_tx with dissolve

    w "Hey, um, nice pad."

    "Thanks! Sorry it's a bit messy! Can I get you something to drink?"

    w "What are you having?"

menu:
    "Bourbon, on the rocks.":
        jump myplace2
    "I was thinking an IPA.":
        jump myplace2
    "Maybe some wine?":
        jump myplace2

label myplace2:
    w "Sounds good. I'll have one too."

    play sound "sfx/240464__godowan__pour-water2.wav"
    "{i}My hands were shaking a little bit as I poured the drinks. I really needed some liquid courage.{/i}"

    play sound "sfx/76812__dj-burnham__wine-glasses-clink.mp3"
    w "Thanks. Cheers!"

    show wolverine halfback at left, xflip_tx, logan_tx with dissolve

    "{i}We sipped the drinks while he had a look around my apartment.{/i}"

    w "Hey, is that a plushy doll of me?"

    "I, err... yes?"

    show wolverine smile at left, xflip_tx, logan_tx with dissolve
    w "That's cute. Do you hug it often?"

    "{i}(blushing){/i} I sleep with it every night..."

    w "Heh. Well I guess it's time you got to know what hugging the real thing feels like."

    "{i}I fell into his warm, fuzzy arms. It was finally happening...{/i}"

    scene black with fade

    "{i}The End... for now?{/i}"
    "{i}Thanks so much to Ryan and Maddy from Atomic Blue Productions for helping me keep a smile on my face during the troubled times we live in.{/i}"
    stop music fadeout 1.0
    "{i}And sorry to everyone I stole stuff from to slap this silly little thing together with no art skills! Please see the About page for attribution.{/i}"
    return

label badend:
    hide wolverine with dissolve
    scene black with fade
    "{i}I couldn't believe it! I came all the way out here just to give up? Maybe I should give it another try...{/i}"
    return
