# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()


$ bet = 0
define e = Character("Me", callback=type_sound)
define n = Character("Narator")
define l = Character("Lecturer", callback=type_sound)
define d = Character("Dealer", callback=type_sound)
define b = Character("Boss", callback=type_sound)
define s  = Character("Someone")
define dc  = Character("Debt Collector", callback=type_sound)
define dad = Character("Dad", callback=type_sound)

image bg rumah = "bg/Bedroom_Night_Dark.png"
image bg store = "bg/Store_Night_Dark.png"
image bg class = "bg/Class_Night_Dark.png"
image bg street = "bg/Street_Summer_Day.png"
image bg work = "bg/Office.jpeg"
image bg darkstreet = "bg/Street_Darker.png"
image bg corridor = "bg/Corridor.jpeg"
image bg ending1 = "bg/OfficeEnding.png"
image bg ending2 = "bg/BedEnding.png"
#mc
image mc default = "MC/MC Default2.png"
image mc shocked = "MC/MC shocked2.png"
image mc shocked2 = "MC/MC shocked3.png"
image mc cry = "MC/MC crying2.png"
image mc cry2 = "MC/MC crying3.png"
image mc smile = "MC/MC smile2.png"
#lecture
image lecture default = "Lecturer/Lecturer Default.png"
image lecture annoyed = "Lecturer/Lecturer annoyed.png"
image lecture annoyed2 = "Lecturer/Lecturer annoyed2.png"
image lecture dissapointed = "Lecturer/Lecturer disappointed.png"
image lecture semioticAnnoyed = "Lecturer/Lecturer_Semiotic annoyed.png"
image lecture semioticDefault = "Lecturer/Lecturer_Semiotic Default.png"
image lecture semioticDissapointed = "Lecturer/Lecturer_Semiotic disappointed.png"
#dealer
image dealer default = "Dealer/Ball Dealer.png"
image debtcollector = "Dealer/Debt.png"
#dad
image dad default = "Dad/Dad Default2.png"
image dad annoyed = "Dad/Dad Annoyed2.png"
image dad smirk = "Dad/Dad Smirk2.png"
image dad semioticAnnoyed = "Dad/Dad_Semiotic Annoyed 2.png"
image dad semioticDefault = "Dad/Dad_Semiotic Default 2.png"
image dad semioticSmirk =  "Dad/Dad_Semiotic smirk 2.png"
#boss
image boss_default = "boss/Boss.png"
# The game starts here.

label start:
    play music "audio/Whole Tone Limbo - Godmode.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    play sound "audio/doorbell.ogg"
    pause 3.0
    "Kriing, kriing!"

    # These display lines of dialogue.

    e "Ugh."
    e "Shut up"
    play sound "audio/carhonk.ogg"
    "Honk, honk!"

    scene bg rumah with fade
    show mc default at center
    e "..."
    e "Still the same as ever."
    play sound "audio/door.ogg"
    e "\"If you don't pay back the debt in six months, we will take everything.\""

    show mc panning at center
    e "Oh my god. "
    hide mc 

    show mc cry2 at center
    e "The debt collector is going to kill me!"
    e "I still don't have enough money."
    e "What should I do..."
    

    menu:
        "Resolve to Work":
            jump act1_a
        "Hope for Something Good":
            jump act1_b


    label act1_a:
        show mc default at center
        e  "It's now or never."

        $ choice_act1 = "act1_a"  
        jump act1_a1


    label act1_b:
        show mc default at center
        e  "Let's just see what I can do about it.."
        $ choice_act1 = "act1_b" 
        jump act1_b1
        
    stop music

    label act1_a1:
        pause 3.0
        play music "audio/Ost_1.mp3"
        show bg store with fade  
        show mc default at center 
        e  "Looks like this minimarket has an open recruitment."
        show mc smile at center
        e  "Let's ask them."
        "Cashier job is earned."
        # call minigame:Cashier
        jump act1_cont

    label act1_b1:
        show bg store with fade    
        show mc default at center
        e  "I should eat less."
        e  "Let's go with onigiri."
        "You leave with a hungry stomach."
        stop music
        jump act1_cont


    label act1_cont:
        show mc default at center
        e  "What a day..."
        e  "If only there is a way to get easy money..."
        e  "Hmm?"
        show mc shocked at center
        e  "Oh my god, it's time for class!"
        stop music
        hide mc with moveoutright
        # call act_ending_summary

    jump act2
    

    label act2:
        play music "audio/Yoga Style - Chris Haugen.mp3"
        show bg class with fade
        show lecture default at left with fade
        l "So, management (or managing) is the administration of organizations,"
        l "whether they are a business, a nonprofit organization, or a government body through business administration, nonprofit management,"
        l "or the political science sub-field of public administration respectively."
        show mc shocked at right with moveinright
        e  "Hah, hah..."
        show lecture default at left
        l "..."
        show mc shocked2 at right
        e  "Am I late?"
        show lecture annoyed at left
        l  "..."
        show lecture annoyed2 at left
        play sound "audio/school_bell.ogg"
        pause 3.0
        "Bell Rings"
        

        show mc default at right
        e  "Oh..."
        show lecture default at left
        l "Alright, class dismissed. Don't forget to do the task!"
        stop music

        play music "audio/TrueArtRealAffectionPart4 - Noir Et Blanc Vie.mp3"
        show bg corridor with fade
        show lecture annoyed at left
        l  "Why are you late"


        menu:
            "Convince":
                jump act2_a
            "Hide":
                jump act2_b


    label act2_a:
        show mc default at right
        e  "I'm working."
        show lecture default at left
        l  "..."
        l  "Here is the notes and task you missed."
        l  "Don't be late again next time."
        l  "And..."
        l  "Good luck on clearing your debts."
        show mc shocked at right
        e  "..."
        show mc smile at right
        e  "Thank you, Aunty!"
        hide lecture 
        hide mc
        stop music
        jump act2_cont
        


    label act2_b:
        show mc default at right
        e  "Something happen"
        show lecture annoyed at left
        l  "You know that I don't take that as an excuse, right?"
        show lecture dissapointed at left
        l  "How many times has it been? At this rate you're going to fail."
        l  "I can't help you any more than this."
        show mc default at right
        e  "This is..."
        show lecture annoyed at left
        l  "Notes and tasks. This is the last."
        show mc shocked at right
        e  "..."
        hide lecture
        hide mc 
        stop music
        jump act2_cont


    label act2_cont:
        show bg street with fade
        play music "audio/Escapism - Yung Logos.mp3"
        show mc default at center with moveinright
        e "What should I do.."
        show mc default at right
        show dealer default at left
        d  "What should I do.."
        show mc shocked at right
        e  "Hmm?"
        show dealer default at left
        d  "Yeah you. You want easy money?"
        d  "Try this ball game."
        d  "If you can find the ball, you win twice the money you bet. If you fail, I get the money."
        d  "How's that sound?"


    menu:
        "Play the Game":
            jump act2_a2
        "Pass":
            jump act2_b2


label act2_a2:
    show mc smile at right
    "You chose to play"
    e "You bet!"
    $ choice_act2 = "act2_a2"
    d "Alrighty then, how much will you bet?"

    menu:
        "100":
            $ bet = 100
            d "Playing it safe, I see"
            jump BallGameRes

        "200":
            $ bet = 200
            d "Alrighty then, let's start"
            jump BallGameRes

        "500":
            $ bet = 500
            d "Love the spirit, ya either go big or go home"
            jump BallGameRes

label BallGameRes:
    ## Ini rng 0.0-1.0
    $ ballpoint = renpy.random.random()
    if ballpoint >= 0.7:
        d "Looks like lady luck is on your side, kiddo. Here, take it."
        d "See you around, boy."
        e "Phew, I got lucky"
        hide dealer
        hide mc
        stop music
        jump act3
        ## nominal di bet tambahin ke uang
    else:
        d "HAH! More for me"
        d "See you around, boy."
        e "Looks like I'm running out of luck"
        e "Better leave before it's too late"
        hide dealer
        hide mc
        stop music
        jump act3
        ## nominal di bet kurangin dari uang

    show mc default at right
    e "Looks like I'm running out of luck."
    e "Better leave before it's too late."
    # call act_ending_summary
    hide dealer
    hide mc
    stop music
    jump act3

label act2_b2:
    if choice_act1 == "act1_a":
        show mc default at right
        e "Nah, I'll pass."
        show mc shocked at right
        e "Oh."
        show mc default at right
        $ choice_act2 = "act2_b2"
        e "It's time for my work shift!"
        # call minigame_cashier
        show mc default at right
        e "Let's take a rest."
        # call act_ending_summary
        hide dealer
        hide mc
        stop music
        jump act3

    else:
        show mc default at right
        $ choice_act2 = "act2_b2"
        e "Even I know this is a fraud."
        e "Damn, my life is not getting any better..."
        hide dealer
        hide mc
        stop music
        # call act_ending_summary
        jump act3


label act3:
    if choice_act1 == "act1_a":
        play music "audio/Ost_1.mp3"
        show bg store with fade
        show mc smile at right
        e  "Alright, time to perform well today!"
        # call minigame_cashier
        show boss_default at left
        b  "..."
        show mc default at right
        e "Hmm?"
        show boss_default at left
        b  "Hey, you!"
        show mc default at right
        e  "Me?"
        show boss_default at left
        b  "Yeah, you."
        b  "Do this for me!"
        # call minigame_accounting
        show boss_default at left
        b  "I see that you got potential."
        b  "Work for me!"


        menu:
            "Accept the offer":
                stop music
                jump act3_a
            "Decline the offer":
                stop music
                jump act3_b


        label act3_a:
            play music "audio/Tumbling Down Clouds - NoMBe.mp3"
            show mc default at right
            e  "This is my opportunity...!"
            show mc smile at right
            $ choice_act3 = "act3_a"
            e  "I'd be glad to work with you, but can you tell me a bit more about your company?"

            "Both of you proceed to discuss after your shift."
            "You have acquired the accounting job."
            # call act_ending_summary

            hide boss_default
            hide mc
            stop music
            jump act4


        label act3_b:
            $ choice_act3 = "act3_b"
            show mc default at right
            e  "This is sketchy..."
            e  "I'm afraid I'll have to decline, Sir."
            e  "I'm happy with my current job."
            show boss_default at left
            b  "Are you serious? This is your chance."
            show mc default at right
            e  "Sorry, Sir. There's a line behind you.."
            show boss_default at left
            b  "..."
            b  "Fine."
            b  "You'll regret it later!"
            show mc default at right
            $ choice_act3 = "act3_b"
            e  "..."
            show mc shocked at right
            e  "Haah.."
            show mc default at right
            e  "To think I'll have to deal with these customers every day..."
            # call act_ending_summary
            hide boss_default
            hide mc
            stop music
            jump act4


    elif choice_act1 == "act1_b":
        play music "audio/Ost_1.mp3"
        show bg store with fade
        show mc default at right
        e  "Who is he... "
        show boss_default at left
        b  "Hey...!"
        show mc default at right
        e  "The cashier is in real trouble now... "
        e  "It's time to go away."
        # call act_ending_summary
        hide boss_default
        hide mc
        stop music
        jump act4

label act4:
    if choice_act1 == "act1_a" and choice_act3 == "act3_a":
        play music "audio/Ost_1.mp3"
        show bg work with fade
        show mc default at right
        e  "Hmm, is this tidy enough..."
        e "Alright"

        "Knock, knock"
        s  "Yes, come in!"

        show boss_default at left
        b "This is your desk. When someone arrives, please take a look at the accounting journal and review it for me."
        show mc default at right
        e  "I'll do my best."
        show boss_default at left
        b  "Great!"
        b  "Let's start it right away"
        # call minigame_accounting
        play audio "audio/Achievement.ogg"
        "You work as accounting"
        stop audio

        show mc default at right
        e  "Phew."
        e  "Time to go home"
        hide boss_default
        hide mc
        stop music
        jump act4_cont


    elif choice_act1 == "act1_a" and choice_act3 == "act3_b":
        show bg store with fade
        show mc default at right
        e  "Alright."
        e  "Same ol' task."
        e  "Let's get it right away"
        # call minigame_cashier
        
        "You work as cashier"
        show mc default at right
        e  "Time to go home"
        hide boss_default
        hide mc
        stop music
        jump act4_cont


    elif choice_act1 == "act1_b":
        show bg store with fade
        show mc default at right
        e "What should I eat again today..."
        e "Hmm?"
        show mc shocked2 at right
        e "This is a new cashier guy."
        show mc default at right
        e "Did he get fired because of the ruckus?"
        e "..."
        e "Not that I care."
        e "Better think about myself."
        stop music
        jump act4_cont


    label act4_cont:
    play music "audio/19th Floor - Bobby Richards.mp3"
    show bg rumah with fade
    show mc default at right
    e "There's still much left..."
    e "What should I do..."

    menu:
        "Play the Ball game":
            jump act4_a

        "Invest (- sum of money)":
            jump act4_b


    label act4_a:
        show bg street with fade
        show mc default at right
        e  "I hope I can win this time."
        # call minigame_ballgame
        "You lose the game and ..."
        "You leave the site after losing interest."
        # call act_ending_summary
        stop music
        hide mc
        jump act5


    label act4_b:
        show bg rumah with fade
        show mc default at right
        e "I heard that investing is a good idea for unused money."
        e "Let's do a little bit of research."

        "You decided to learn about investment."
        stop music
        hide mc
        # call act_ending_summary
        jump act5

    label act5:
    play music "audio/Landing - Godmode.mp3"
    show bg rumah with fade
    show mc default at right
    e "Alright, time to go out."
    play audio "audio/knock.ogg"
    "Knock, knock."
    stop audio

    show mc default at right
    e "Hm?"
    e "Who's there?"
    e "..."
    show mc default at right
    show mc shocked2 at right
    play audio "audio/gasping.ogg"
    e "Dad."
    stop audio
    show dad default at left
    dad "Son"
    show mc default at right
    e "Why are you here?"
    show dad default at left
    dad "I'm just visiting."
    show mc default at right
    e "Why are you here?"
    show dad default at left
    dad "I'm just visiting."
    show mc default at right
    e "How do you know my place?"
    show dad default at left
    dad "..."
    dad "I had my ways."
    show mc default at right
    e "What do you want from me?"
    show dad default at left
    dad "You're still as clueless as ever. I just want to see you."
    show mc default at right
    e "You know that it's bullshit."
    show dad annoyed at left
    play audio "audio/hit.ogg"
    dad "MANNERS!"
    stop audio
    show mc shocked at right
    e "!!"
    show dad default at left
    dad "..."
    dad "Listen up. You have been ignoring my calls lately."
    dad "..."
    dad "What happened?"


    menu:
        "Confess":
            jump act5_a
        "Lie":
            jump act5_b


    label act5_a:
    show mc shocked at right
    e "Well, ever since Dad stop giving me money, it's been hard."  
    e "At least pay for my tuition please?"
    show dad default at left
    dad "I had my reasons. I can give you money if you promised not to spend irresponsibly."
    show mc default at right
    e "I haven't been able to months ago anyway."
    show mc default at right
    e "Look, if you're not going to trust me, then go away, Dad. I had work to do."
    show dad default at left
    dad "...work?"
    show mc default at right
    e "How else I earn money?"
    show dad default at left
    dad "Fine. Here. Don't dissapoint me again."
    "Dad leaves abruptly."
    show mc default at right
    e "..."
    show mc default at right
    e "This is.."
    "You receive x sum of money"
    hide mc
    hide dad
    # call act_ending_summary
    jump act6


    label act5_b:
    show mc default at right
    e "I'm okay, Dad. It's nothing that should concern you."
    show dad default at left
    dad "I see."
    show mc default at right
    e "Can you leave? I'm going to work."
    show dad default at left
    dad "I had my reasons. I can give you money if you promised not to spend irresponsibly."
    show mc default at right
    e "It's not about that..."
    e "I don't care about that anymore, Dad. I know my wrongdoings."
    show dad default at left
    dad "..."
    dad "Here. Take care of yourself."
    dad "And... I'm sorry."
    "You receive y sum of money"
    hide mc
    hide dad
    # call act_ending_summary
    jump act6

    label act6:
    if choice_act1 == "act1_b" and choice_act2 == "act2_b2":
        show bg corridor with fade
        show mc default at right
        e  "..."
        e  "Huh?"
        e  "Aunty!"
        show lecture default at left
        l  "Don't call me that..."
        l  "..."
        l  "Perfect timing. Do you have time, BOY.?"
        show mc default at right
        e  "?"
        show lecture default at left
        l  "Let's have a talk"
        l  "Did your father visit you yesterday?"
        show mc default at right
        e  "How did you know?"
        show lecture default at left
        l  "Because I am the one who gives your apartment location."
        l  "I'm sorry. I can't lie to your father."
        show mc default at right
        e  "It's okay."
        show lecture default at left
        l  "Did he do something?"


        menu:
            "Confess":
                jump act6a_a1
            "Lie":
                jump act6b_b1


    label act6a_a1:
        show bg corridor with fade
        show mc default at right
        e  "We had a usual quarrel."
        show lecture default at left
        l  "I see."
        show lecture default at left
        l  "I hope that you don't hate your father too much."
        show lecture default at left
        l  "Even if his negligence is... concerning."
        show mc default at right
        e  "..."
        show mc default at right
        e  "I know."
        show mc default at right
        e  "I have always been a bad kid anyway."
        show lecture default at left
        l  "Don't say that."
        show lecture default at left
        l  "Have you really given up on yourself?"
        show mc default at right
        e  "..."
        show lecture default at left
        l  "Alright. I won't say more. Lecturing you is not my plan right now."
        show lecture default at left
        l  "Just call me if you need help."
        show mc default at right
        e  "..."
        show mc default at right
        e  "Fuck !"
        hide lecture
        hide mc 
        jump act6_cont


    label act6b_b1:
        show mc default at right
        e  "Nothing much. Just a hello."
        show lecture default at left
        l  "Hey, I know your father long enough that I can't possibly believe that."
        show lecture default at left
        l  "..."
        show lecture default at left
        l  "Well, I'm not forcing you. However..."
        show lecture default at left
        l  "I hope that you don't hate your father too much."
        show lecture default at left
        l  "Even if his negligence is... concerning."
        show mc default at right
        e  "..."
        show mc default at right
        e  "I know."
        show mc default at right
        e  "I have always been a bad kid anyway."
        show lecture default at left
        l  "Don't say that."
        show lecture default at left
        l  "Have you really given up on yourself?"
        show mc default at right
        e  "..."
        show lecture default at left
        l  "Alright. I won't say more. Lecturing you is not my plan right now."
        show lecture default at left
        l  "Just call me if you need help."
        show mc default at right
        e  "..."
        show mc default at right
        e  "Fuck!"
        hide mc
        hide lecture
        stop music
        jump act6_cont


    if choice_act3 == "act3_b":
        show bg store with fade
        show MC_SMILE
        e "Welcome to our store! We have Bread at discount price!"

        "You serve customers"
        # call minigame_cashier
        show mc default at right
        e "Next customer, please."
        show mc default at right
        e "Huh?"
        show MC_Shocked
        e "Aunty!"
        show lecture default at left
        l "BOY.."
        show lecture default at left
        l  "..."
        show lecture default at left
        l  "Perfect timing. Do you have time, BOY.?"
        show mc default at right
        e  "?"
        show lecture default at left
        l  "Let's have a talk"
        show lecture default at left
        l  "Did your father visit you yesterday?"
        show mc default at right
        e  "How did you know?"
        show lecture default at left
        l  "Because I am the one who gives your apartment location."
        show lecture default at left
        l  "I'm sorry. I can't lie to your father."
        show mc default at right
        e  "It's okay."
        show lecture default at left
        l  "Did he do something?"


        menu:
            "Confess":
                jump act6a_a2
            "Lie":
                jump act6b_b2


    label act6a_a2:
        show mc default at right
        e  "We had a usual quarrel."
        show lecture default at left
        l  "I see."
        show lecture default at left
        l  "I hope that you don't hate your father too much."
        show lecture default at left
        l  "Even if his negligence is... concerning."
        show mc default at right
        e  "..."
        show mc default at right
        e  "I know."
        show mc default at right
        e  "I have always been a bad kid anyway."
        show lecture default at left
        l  "Don't say that."
        show lecture default at left
        l  "I know you're trying hard right now."
        show lecture default at left
        l  "Your father will not believe it, but I will.."
        show lecture default at left
        l  "Remember."
        show lecture default at left
        l  "Hard work pays off."
        show lecture default at left
        l  "Just call me if you need help."
        show mc default at right
        e  "..."
        show mc default at right
        e  "I'll prove to you that I can overcome my problems!"
        hide lecture
        hide mc
        stop music
        # call minigame_cashier
        jump act6_cont


    label act6b_b2:
        show mc default at right
        e  "Nothing much. Just a hello."
        show lecture default at left
        l  "Hey, I know your father long enough that I can't possibly believe that."
        show lecture default at left
        l  "..."
        show lecture default at left
        l  "Well, I'm not forcing you. However..."
        show lecture default at left
        l  "I hope that you don't hate your father too much."
        show lecture default at left
        l  "Even if his negligence is... concerning."
        show mc default at right
        e  "..."
        show mc default at right
        e  "I know."
        show mc default at right
        e  "I have always been a bad kid anyway."
        show lecture default at left
        l  "Don't say that."
        show lecture default at left
        l  "I know you're trying hard right now."
        show lecture default at left
        l  "Your father will not believe it, but I will.."
        show lecture default at left
        l  "Remember."
        show lecture default at left
        l  "Hard work pays off."
        show lecture default at left
        l  "Just call me if you need help."
        show mc default at right
        e  "..."
        show mc default at right
        e  "I'll prove to you that I can overcome my problems!"
        # call minigame_cashier
        hide lecture
        hide mc
        stop music
        jump act6_cont




    if else choice_act3 == "act3_a":
        show bg workplace_day with fade
        show boss_default
        "Boss" "Let's have a great work today as well."
        show mc default at right
        e  "Yes, Sir!"
        # call minigame_accounting
        show mc default at right
        e  "Never thought reviews can be so tiring..."
        show mc default at right
        e  "Let's take a break."
        show mc default at right
        e  "Hmm?"
        show MC_Shocked
        e  "Aunty!"
        show lecture default at left
        l  "?"
        show lecture default at left
        l  "!"
        show lecture default at left
        l  "BOY."
        show mc default at right
        e  "What are you doing here?"
        show lecture default at left
        l  "Oh, I'm just meeting my colleagues."
        show lecture default at left
        l  "Do you work here?"
        show mc default at right
        e  "Yeah, not a while ago"
        show lecture default at left
        l  "I see."
        show lecture default at left
        l  "..."
        show lecture default at left
        l  "Perfect timing. Do you have time, BOY.?"
        show mc default at right
        e  "?"
        show lecture default at left
        l  "Let's have a talk"
        show lecture default at left
        l  "Did your father visit you yesterday?"
        show mc default at right
        e  "How did you know?"
        show lecture default at left
        l  "Because I am the one who gives your apartment location."
        show lecture default at left
        l  "I'm sorry. I can't lie to your father."
        show mc default at right
        e  "It's okay."
        show lecture default at left
        l  "Did he do something?"


        menu:
            "Confess":
                jump act6a_a3
            "Lie":
                jump act6b_b3


    label act6a_a3:
        show mc default at right
        e  "We had a usual quarrel."
        show lecture default at left
        l  "I see."
        l  "I hope that you don't hate your father too much."
        l  "Even if his negligence is... concerning."
        show mc default at right
        e  "..."
        e  "I know."
        e  "I have always been a bad kid anyway."
        show lecture default at left
        l  "Don't say that."
        l  "I know you're trying hard right now."
        l  "Your father will not believe it, but I will.."
        l  "Remember."
        l  "Hard work pays off."
        l  "Just call me if you need help."
        show mc default at right
        e  "..."
        show mc default at right
        e  "I'll prove to you that I can overcome my problems!"

        show bg work
        "You work so hard"
        hide mc
        hide lecture
        stop music
        # call minigame_accounting
        jump act6_cont


    label act6b_b3:
        show mc default at right
        e  "Nothing much. Just a hello."
        show lecture default at left
        l  "Hey, I know your father long enough that I can't possibly believe that."
        l  "..."
        l  "Well, I'm not forcing you. However..."
        l  "I hope that you don't hate your father too much."
        l  "Even if his negligence is... concerning."
        show mc default at right
        e  "..."
        e  "I know."
        e  "I have always been a bad kid anyway."
        show lecture default at left
        l  "Don't say that."
        l  "I know you're trying hard right now."
        l  "Your father will not believe it, but I will.."
        l  "Remember."
        l  "Hard work pays off."
        l  "Just call me if you need help."
        show mc default at right
        e  "..."
        e  "I'll prove to you that I can overcome my problems!"
        show bg work
        "You work so hard"
        # call minigame_accounting
        hide mc
        hide lecture
        stop music
        jump act6_cont


    label act6_cont:
        play music "audio/Street Rhapsody - DJ Freedem.mp3"
        show bg darkstreet with fade
        show mc default at right with moveinright
        e "So tired.."
        e "Hmm?"
        e "Why are the people on my door..?"
        show debtcollector at left with moveinleft
        dc  "Hey, it's him!"
        show mc shocked2 at right
        e "Oh no."
        # call act_ending_summary
        hide mc with moveoutright
        hide debtcollector with moveoutright
        jump act7

        label act7:
        show bg darkstreet with fade
        show mc shocked at center with moveinleft
        show debtcollector at left with moveinleft
        dc "Hey, you! Money, where is it?!"
        show mc shocked at center
        e "Who are you guys?"  
        show debtcollector at left
        dc  "We have come to take your money."
        dc  "It's been too long!"
        dc "We'll take everything if you don't pay right now!"
        show mc shocked at center
        e "Shit."


        menu:
            "Pay":
                jump act7_a  
            "Run Away":
                jump act7_b


    label act7_a:
        stop music
        show mc smile at center
        e "Just kidding!"
        e "Here. Money that I owe you."
        e "Interest included."
        show debtcollector at left
        dc  "...What?"
        show mc default at center
        e "Now go away, or I'll call the police."
        show debtcollector at left
        dc  "Grr. Scram you!"
        show mc default at center
        e "Haah."
        "The debt collector leaves."
        hide debtcollector with moveoutright
        show mc default at center
        e "Finally... It's over."

        #phoneringging
        play audio "audio/phone-ringing.ogg"
        "Kriing, kriing"
        stop audio
        show mc default at center
        e "Hmm?"
        show mc shocked2 at center
        e "I got promoted?!"
        show mc smile at center
        e "Thank you so much!"
        $ choice_act7 = "act7_a"
        stop music
        hide debtcollector
        hide mc
        jump act8


    label act7_b:
        show mc shocked at center
        $ choice_act7 = "act7_b"
        e "You won't catch me!"
        show debtcollector at left
        dc  "You can't run away from me!"
        show debtcollector at left
        dc  "All of you! Seize him!"
        stop music
        hide debtcollector
        hide mc
        jump act9


    label act8:
        if choice_act7 == "act7_a":
            play music "audio/Ost_1.mp3"
            show bg ending1 with fade
            "You got promoted to a manager"
            "Some time later, you graduated and started a new company"
            "After a series of hard work and perseverance, you finally
    become a successful entrepeneur."
            "And you thank everyone for not giving up on yourself"
            "Including you"
            "Stay strong"
            "You can do it."
            "THE END"
            $ renpy.movie_cutscene("images/ending.webm", loops=0)
            stop music

    label act9:
        if choice_act7 == "act7_b":
            play music "audio/Escapism - Yung Logos.mp3"
            show bg ending2 with fade
            "Unfortunately, the debt collector caught you, and they took
    everything from you."
            "You lived your remaining life as a beggar."
            $ renpy.movie_cutscene("images/ending.webm", loops=0)
            stop music

    return  
