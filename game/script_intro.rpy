label intro:

    # script_intro declared variables
    $ joinedTheTeam = False
    $ joinedTheTeamLate = False
    $ freeStuffCollector = False

    scene campus

    "Freshman year."
    "Your final year of high school, spent worrying about SATs, getting into college, prom, and having a final summer with old friends has culminated into
    the next four years to come."
    "What awaits are four years of excitement, debauchery, fun, and maybe, if you're lucky, love."
    "Oh, and education. Can't forget about that."
    "But so far, the first week has only been filled with orientation and syllabi."
    "Having finished your final class for the day, you make the walk across the quad back to your dorm room."
    "You swipe your key card, trudge up the stairs, and find your room."

    scene dorm

    "You look at the door, adorned with two cute decals. One for you, one for your roommate."

    $ name = renpy.input("What's your name?")

    "[name] and Justin, both written in puffy paint on separate miniature records. Your RA is pretty creative."
    "You step into your room and are greeted with a smile from your roommate. You toss your syllabi onto your desk beside your textbooks."
    "What are you studying?"

    menu:
        "English":
            $ major = "English"
            "Among various textbooks lies an old favorite from your AP Liturature class: All the King's Men."
        "Business":
            $ major = "Business"
            "The image on your business textbook is straight out of a stocks meme, and you can't help but laugh every time you see it."
        "Science":
            $ major = "Science"
            "One textbook you bought used has an odd chemical stain on the cover. You will have to be more careful than the last owner in your labs."
        "Engineering":
            $ major = "Engineering"
            "You had skimmed through one of your textbooks upon purchase, and the formulas you were presented with already gave you a headache."
        "Law":
            $ major = "Law"
            "Amongside textbooks were printouts of court cases you'd have to be reviewing over the semester."
        "Undeclared":
            $ major = "Undeclared"
            "Your textbooks were standard for first year students. You figure it's best to get gen eds out of the way before committing to the rest of your life."

    "You barely have time to sit on your bed before Justin is motioning for the two of you to leave again."

    show j

    j "Alright, now that you're back, let's get out there. The club fair's getting set up, and I want to get as much free stuff as I can before it gets taken."
    j "Plus, I wanted to check out what sports I can do. Not trying to get the Freshman 15 this early in the year!"

    menu:
        "As long as we stop by Ultimate first. I want to sign up.":
            j "Ultimate? We used to play that occasionally in gym class at my high school. I could definitely get into that!"
            $ joinedTheTeam = True
        "Sure! It's college, might as well meet friends with similar interests.":
            j "That's the spirit! And hey, we can go to club parties instead of buying our way into frat ones."
        "There's nothing I really want to do, but might as well check out what clubs there are.":
            j "Alright, then let's get going! I've been waiting for you since 2:00, dude!"
        "Free stuff? I'm in.":
            j "Right? If I'm paying tuition to go here, might as well reap the benefits!"
            $ freeStuffCollector = True

    scene clubfairground

    "And so you and Justin head out to the club fair together."
    "Various booths are set up along the main path in the quad, filled with excited college students waving signs and other advertisements for their extracurricular activity."
    if joinedTheTeam:
        "But you ignore most of them, making a beeline to the only club that piques your interest: Ultimate Frisbee."
        "With Justin in tow, you arrive at the booth."
    elif freeStuffCollector:
        "You and Justin stop by as many booths as possible, collecting tee shirts, water bottles, and candy before they're picked clean."
        "Once the mad dash for free stuff ends, Justin begins his hunt for a sport, and stops the two of you at the Ultimate Frisbee booth."
    else:
        "You and Justin stop by a few booths and listen to the pitches, but aren't swayed. After a bit, Justin begins his hunt for a sport."
        "The two of you stop at the Ultimate Frisbee booth."

    "All around are various students in light blue and seafoam green uniforms, calling out to passerbys and tossing discs to and fro."
    "Manning the station is a guy with thick eyebrows waving sign up sheets, a second with sharp eyes speaking to the crowd, and a third with a manbun and a pen in his hand."

    show so at slightleft
    show v
    show sd at slightright

    soUnknown "Dude, SD, stop waving those around and give me one. How are freshman going to sign up if they can't grab a sheet?"
    "The man with thick eyebrows who you can assume is called SD laughs."
    sd "Well, if they're playing with us they're going to have to get used to my defensive stance!"
    "Sharp eyes sighs and rubs a temple, as manbun swipes a sign up sheet with a deft hand and passes it to an onlooker. He then turns his attention to you."
    vUnknown "Hey guys, looking to join campus's one and only premier flatball team?"

    if joinedTheTeam:
        hide so
        hide v
        hide sd
        show v at left
        show j at right
    else:
        menu:
            "Heck yeah, sign me up!":
                hide so
                hide v
                hide sd
                show v at left
                show j at right
                $ joinedTheTeam = True
            "Can you give me a bit more information?":
                hide so
                hide sd
                vUnknown "Sure thing! Our ultimate team is a club team, but we do compete with other club teams. We've only got one 'team' and we're open to all skill levels. However, if you want to compete in matches
                and tournaments, we're going to expect you at practice."
                vUnknown "There are three practices a week usually, on Monday, Tuesday, and Thursday. Fridays and Saturdays usually have 'club bonding activities', but those aren't associated with the university,
                if you catch my drift. Anyway, you interested?"
                menu:
                    "Heck yeah, sign me up!":
                        hide v
                        show v at left
                        show j at right
                        $ joinedTheTeam = True
                    "I think I'm going to pass.":
                        hide v
                        show v at left
                        show j at right
                        vUnknown "Well, that's your loss, man, but I can't force you. How about the guy behind you?"
                        j "Honestly, it seems like Ultimate's going to be my jam. Bummed about [name], but he's his own man."

            "I think I'm going to pass.":
                hide so
                hide v
                hide sd
                show v at left
                show j at right
                vUnknown "Well, that's your loss, man, but I can't force you. How about the guy behind you?"
                j "Honestly, it seems like Ultimate's going to be my jam. Bummed about [name], but he's his own man."

    if joinedTheTeam:
        "You enthusically nod and are handed a sign-up sheet. You immediately fill out your information."
        j "Yeah, if [name] is joining, I might as well too! Roommates got to stick together."
        vUnknown "Oh, you guys are roommates? Man, now I can't get you to drag another two guys to practice!"
        vUnknown "Speaking of which, first practice will be this Thursday. Meet up at the side of the business building nearest the main street. Juniors and seniors
        will be waiting with vehicles to drive you up to our practice field."
        v "I'm Vegeta, by the way. The dudes behind me are SD and Snakeoil. Snakeoil's captain of the team, and I'm second-in-command, so you're getting in with the right guys!"
        "Vegeta shouts back to the two gentlemen behind him."
        v "SD, Snake, two more recruits!"
        hide v
        show sd at left
        show so at right
        so "Hell yeah Vegeta! Nice to meet you two. Looking forward to seeing you on the field."
        "Snakeoil turns to SD and offers him a big, toothy grin."
        so "With the rookies signing up, it looks like we'll be leaving the team in good hands."
        "SD gently punches Snakeoil in the arm."
        sd "They must have heard about the legendary Snakeoil, captain of the Ultimate Team, and came flocking over!"
        "Snakeoil lets out an exasperated sigh and smacks SD as various other members of the team laugh and begin a chant for the captain."
        hide sd
        hide so
        if freeStuffCollector:
            "With the two of you signed up for Ultimate, you and Justin continue on your way. You scour tables for any last remaining free goodies before heading back to your dorm room."
        else:
            "With the two of you signed up for Ultimate, you and Justin continue on your way. Other clubs catch your eye, but the two of you have dedicated yourselves to frisbee, and ignore
            their siren songs."
    else:
        hide v
        hide j
        "Justin fills out the form while you stand behind him. Around you students toss discs and laugh amongst themselves. You wonder if this is really what you want."
        "With Justin signed up for Ultimate, the two of you continue on your way. Justin's dedication to frisbee causes him to skip over the remaining booths, and you two find yourselves back
        at your dorm room before you can decide on another club."

    scene campus

    "Now that the club fair is over, you and Justin hang out in your dorm room playing videogames until far too late into the evening. The next day finds you dragging through yet more
    syllabi and introductions."
    "The first week of the 'four best years of your life' sure have been boring so far."
    if joinedTheTeam:
        "However, the thought of your first college Ultimate practice waiting you at the end of the day gets you through."

    scene dorm
    show j

    "You return to your dorm room. Justin is already there, having finished his classes before yours. He's in the middle of changing into atheletic clothes."
    if joinedTheTeam != True:
        j "Hey dude! Just getting ready to meet the upper classmen to head up to Ultimate practice. You sure you aren't interested? Vegeta said we could bring people to
        the first few practices. They'll have sign up sheets available."
        menu:
            "Heck yeah! I was kind of regretting not signing up":
                $ joinedTheTeam = True
                $ joinedTheTeamLate = True
                j "I could kind of tell, which is why I asked. Hell yeah, dude! I'm hyped!"
            "Alright alright, I'll come with. It looked pretty fun.":
                $ joinedTheTeam = True
                $ joinedTheTeamLate = True
                j "Hell yeah, dude! It's gonna be lit. I'm hyped you're joining with us."
            "Nah, I'm sure. Have a good time though!":
                j "Alright alright, I won't press it. Have a good one, man."
                call noFrisbeeEnding
    #pick out body type, go to practice, enter practice1!
