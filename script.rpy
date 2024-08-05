init python:
    import math

    smogCountdown = "not started"

    def repulsor_update(st):

        # If we don't know where the mouse is, give up.
        if repulsor_pos is None:
            return .01

        px, py = repulsor_pos

        # For each sprite...
        for i in repulsor_sprites:

            # Compute the vector between it and the mouse.
            vx = i.x - px
            vy = i.y - py

            # Get the vector length, normalize the vector.
            vl = math.hypot(vx, vy)
            if vl >= 150:
                continue

            # Compute the distance to move.
            distance = 12.0 * (150 - vl) / 150

            # Move
            i.x += distance * vx / vl
            i.y += distance * vy / vl

            # Ensure we stay on the screen.
            if i.x < 2:
                i.x = 2

            if i.x > repulsor.width - 2:
                i.x = repulsor.width - 2

            if i.y < 2:
                i.y = 2

            if i.y > repulsor.height - 2:
                i.y = repulsor.height - 2

        return .01

    # On an event, record the mouse position.
    def repulsor_event(ev, x, y, st):
        store.repulsor_pos = (x, y)

    def truths_dragged(drags, drop):
        if not drop:
            return

        store.statement = drags[0].drag_name
        store.booleanChoice = drop.drag_name

        return True

    def recipe_dragged(drags, drop):
        if not drop:
            return

        store.gaelic = drags[0].drag_name
        store.english = drop.drag_name

        return True

    # This function will run a countdown of the given length. It will
    # be white until 5 seconds are left, and then red until 0 seconds are
    # left, and then will blink 0.0 when time is up.
    def countdown(st, at, length=0.0):
        global smogCountdown
        remaining = length - st

        if remaining > 2.0:
            return Text("%.1f" % remaining, color="#fff", size=72), .1
        elif remaining > 0.0:
            return Text("%.1f" % remaining, color="#f00", size=72), .1
        else:
            globals()['smogCountdown'] = "FINISHED"
            return anim.Blink(Text("0.0", color="#f00", size=72)), None

# Declare characters used by this game. The color argument colorizes the name of the character.
define audio.background = "audio/music_zapsplat_game_music_childrens_soft_warm_cuddly_calm_015.mp3"
define mom = Character(_("Mom"), color="#af208a")  # pink
define gmm = Character(_("Grandmama"), color="#af208a")  # pink
define gm = Character(_("Grandma"), color="#af208a")  # pink
define dad = Character(_("Dad"), color="#000033") # blue
define bil = Character(_("Billy"), color="#0ea709")   # green
define lin = Character(_("Linda"), color="#0ea709")   # green
define ixel = Character(_("Ixel"), color="#0ea709")   # green
define sister = Character(_("Sister"), color="#0000cc") # lighter blue
define ter = Character(_("Teresa"), color="#0ea709")   # green
define tea = Character(_("Teacher"), color="#af208a")  # pink
transform ixelZoom:  
    zoom 0.5                   
define gradeLinda = 0.0
define gradeIxel = 0.0
define gradeBilly = 0.0
define gradeTeresa = 0.0
define finalLinda = ""
define finalIxel = ""
define finalBilly = ""
define finalTeresa = ""
define procrastinated = False
define broken = False
define idkFlag = False
define TRUE = "TRUE"
define FALSE = "FALSE"
define snow_white = "snow_white.png"
define cuckoo = "cuckoo.png"
define napoleon = "napoleon.png"
define leaves = "leaves.png"
define hurricane = "hurricanes.png"
define ham = "ham.png"
define Recipe1 = "Recipe1.png"
define Recipe2 = "Recipe2.png"
define Recipe3 = "Recipe3.png"
define Recipe4 = "Recipe4.png"
define Recipe5 = "Recipe5.png"
define Recipe6 = "Recipe6.png"
define Recipe7 = "Recipe7.png"
define Recipe8 = "Recipe8.png"
define gal_recipe1 = "gal_recipe1.png"
define gal_recipe2 = "gal_recipe2.png"
define gal_recipe3 = "gal_recipe3.png"
define gal_recipe4 = "gal_recipe4.png"
define gal_recipe5 = "gal_recipe5.png"
define gal_recipe6 = "gal_recipe6.png"
define gal_recipe7 = "gal_recipe7.png"
define gal_recipe8 = "gal_recipe8.png"
define galRecipe1 = "gal_recipe1.png"
define galRecipe2 = "gal_recipe2.png"
define galRecipe3 = "gal_recipe3.png"
define galRecipe4 = "gal_recipe4.png"
define galRecipe5 = "gal_recipe5.png"
define galRecipe6 = "gal_recipe6.png"
define galRecipe7 = "gal_recipe7.png"
define galRecipe8 = "gal_recipe8.png"

image table = im.FactorScale("table.jpg", 0.8, 0.6)
image blackboard_intro = im.FactorScale("blackboard_intro.png", 0.8, 0.6)
image blackboard_grades = im.FactorScale("blackboard_grades.png", 0.8, 0.6)
image blackboard_forest = im.FactorScale("blackboard_forest.png", 0.8, 0.6)
image blackboard_scotland = im.FactorScale("blackboard_scotland.png", 0.8, 0.6)
image blackboard_empty = im.FactorScale("blackboard_empty.png", 0.8, 0.6)
image blackboard_linda = im.FactorScale("blackboard_linda2.png", 0.8, 0.6)
image blackboard_ixel = im.FactorScale("blackboard_ixel2.png", 0.8, 0.6)
image blackboard_billy = im.FactorScale("blackboard_billy2.png", 0.8, 0.6)
image blackboard_teresa = im.FactorScale("blackboard_teresa2.png", 0.8, 0.6)
image terKitchen = im.FactorScale("breakfasttable.jpg", 1.6, 1.4)
image kitchen_modern = im.FactorScale("modernKitchen.jpg", 0.8, 0.6)
image kitchen_old = im.FactorScale("kitchen.png", 0.8, 0.6)
image framed = im.FactorScale("framed.jpg", 0.8, 0.85)
image frame_broken = im.FactorScale("frame_broken.png", 0.8, 0.6)
image scotland = im.FactorScale("isle_of_skye.jpg", 0.4, 0.3)
image berlin = im.FactorScale("school.png", 0.8, 0.6)
image garage2 = im.FactorScale("garage2.png", 1.2, 1.4)
image globe = im.FactorScale("globe.jpg", 0.8, 0.6)
image globe4Game = im.FactorScale("globe4Game.jpg", 0.7, 0.6)
image terRPG = im.FactorScale("terRPG.png", 2.0, 2.0)
image stoolKalterHund = im.FactorScale("stoolKalterHund.png", 1.0, 1.2)
image stoolJeepney = im.FactorScale("stoolJeepney.png", 1.0, 1.2)
image stoolSungka = im.FactorScale("stoolSungka.png", 1.0, 1.2)
image stoolShortbread = im.FactorScale("stoolShortbread.png", 1.0, 1.2)
image stool2jugs = im.FactorScale("stool2jugs.png", 1.0, 1.2)
image stoolJug = im.FactorScale("stoolJug.png", 1.0, 1.2)
image sister = im.FactorScale("ixelGrandma.png", 0.5, 0.5)
image ixelGrandma = im.FactorScale("ixelGrandma.png", 0.5, 0.5)
image ixelGrandmama = im.FactorScale("ixelGrandma.png", 0.5, 0.5)
image ixelMom = im.FactorScale("ixelGrandma.png", 0.5, 0.5)
image lilbillsmile = im.FactorScale("lilbillsmile.png", 0.8, 0.8)
image lilbillsurprised = im.FactorScale("lilbillsurprised.png", 0.8, 0.8)
image lilteresaneutral = im.FactorScale("lilteresaneutral.png", 0.7, 0.7)
image lilteresanervous = im.FactorScale("lilteresanervous.png", 0.7, 0.7)
image lilteresasmile = im.FactorScale("lilteresasmile.png", 0.7, 0.7)
image lilteresasmiling = im.FactorScale("lilteresasmiling.png", 0.7, 0.7)
image lilteresatalk = im.FactorScale("lilteresatalk.png", 0.7, 0.7)
image linda = im.FactorScale("linda.png", 1.0, 1.0)
image linda_phone = im.FactorScale("linda.png", 1.0, 1.0)
image mom_phone = im.FactorScale("ixelGrandma.png", 0.5, 0.5)
image dj_dad = im.FactorScale("dj_dad.png", 0.6, 0.6)
image teacher = im.FactorScale("teacher.png", 0.8, 0.8)
image chippedJug = im.FactorScale("oldJugChipped.png", 0.8, 0.8)

screen start_UI:
    imagebutton auto "images/linda_%s.png" xpos 410 ypos 260 focus_mask True action Jump("linda")

    imagebutton auto "images/ixel2_%s.png" xpos 220 ypos 160 focus_mask True action Jump("ixel")

    imagebutton auto "images/billy_%s.png" xpos -150 ypos 400 focus_mask True action Jump("billy")

    imagebutton auto "images/teresa_%s.png" xpos 720 ypos 300 focus_mask True action Jump("teresa")

    imagebutton auto "images/teacher_%s.png" xpos 840 ypos 100 focus_mask True action Jump("end")

label start:
    play music background
    scene blackboard_intro
    call screen start_UI

################## LINDA #####################
label linda:
    scene blackboard_linda
    show linda at center

    lin "Hallo Freunde!  That's German for 'Hello friends!"
    lin "Today I'll be talking about my German heritage."
    lin "It was not long ago that Germany was two seperate countries - East & West Germany."
    lin "I had to call my Mom to see what life was like in East Germany."

    scene globe
    show linda_phone at left
    lin "Hallo Mutti!"

    show mom_phone at right
    mom "Linda!  So glad to hear from you!  How is school going?"
    lin "It is going well.  That is why I am calling."
    lin "I have to write a report on our family and our heritage."
    mom "That is a considerable amount of work."
    lin "Would you tell me again what it was like before the Berlin Wall came down?"

    scene berlin
    mom "Certainly.  As you know, I was born in the rural area around Berlin."
    mom "Compared to what we have today, life was hard.  But I never knew anything else, so it was normal to me."
    lin "Like what, Mom?"
    mom "Well… like having a bunker on the school grounds in case the Americans tried to drop a bomb on us.  I am glad you never had to live in fear like that."
    mom "But it was not all bad.  One of my favorite foods growing up was called ‘Kalter Hund’ or ‘cold dog’.  The dish was really popular since it was easy to make even with limited food supplies.  And of course, I had a family that loved me."
    mom "After the Wall fell in 1989, my sister and I came to Freiburg in the southern part of Germany to find a job.  We saved our extra money and, after a while, opened our own diner."

    scene diner
    lin "Grace!"
    mom "Yes, Grace.  And I am so glad we did because one night a young, handsome DJ came in for dinner.  You might know him."
    lin "Was it Dad?"

    show dj_dad
    mom "Yes.  Your father was quite charming.  And before I knew it, we were married and settled near the Black Forest.  And I think you know the rest of the story."
    lin "Thanks Mom!  Give Dad a hug for me.  I will call you this weekend."
    jump linda_tf

label linda_tf:

screen linda_UI:

    draggroup:
        drag:
            drag_name "Statement1"
            child snow_white
            droppable False
            dragged truths_dragged
            xpos 120 ypos 200

        drag:
            drag_name "Statement2"
            child cuckoo
            droppable False
            dragged truths_dragged
            xpos 120 ypos 250

        drag:
            drag_name "Statement3"
            child napoleon
            droppable False
            dragged truths_dragged
            xpos 120 ypos 300

        drag:
            drag_name "Statement4"
            child leaves
            droppable False
            dragged truths_dragged
            xpos 120 ypos 350

        drag:
            drag_name "Statement5"
            child hurricane
            droppable False
            dragged truths_dragged
            xpos 120 ypos 400

        drag:
            drag_name "Statement6"
            child ham
            droppable False
            dragged truths_dragged
            xpos 120 ypos 450

        drag:
            drag_name "TRUE"
            child "TRUE.png"
            draggable False
            xpos 1000 ypos 250

        drag:
            drag_name "FALSE"
            child "FALSE.png"
            draggable False
            xpos 1000 ypos 450

label sort_truths:
    scene blackboard_forest
    $ gradeLinda = 0.0
    $snow_white = "snow_white.png"
    $cuckoo = "cuckoo.png"
    $napoleon = "napoleon.png"
    $leaves = "leaves.png"
    $hurricane = "hurricanes.png"
    $ham = "ham.png"

    # would have a for loop here, but call doesn't work with loops
    call screen linda_UI
    call lindaLogic from _call_lindaLogic

    call screen linda_UI
    call lindaLogic from _call_lindaLogic_1

    call screen linda_UI
    call lindaLogic from _call_lindaLogic_2

    call screen linda_UI
    call lindaLogic from _call_lindaLogic_3

    call screen linda_UI
    call lindaLogic from _call_lindaLogic_4

    call screen linda_UI
    call lindaLogic from _call_lindaLogic_5

    if gradeLinda >= 4.0:
        $ lindaGrade = "That was a great A+ presentation!"
    elif gradeLinda >= 3.0:
        $ lindaGrade = "That was nice. B+ Linda!"
    else :
        $ lindaGrade = "We'll talk after class about your grade."

label endForest:
    scene blackboard_linda
    show linda at right
    show kalter_hund2:
        pos (400,300)
    show teacher at left
    lin "And here is some Kalter Hund for you all to try"
    tea "Thank you Linda. [lindaGrade]."

    jump start

################## IXEL #####################
label ixel:
    scene blackboard_ixel
    show ixel2

    ixel "Hola Todas!  That means 'Hi everyone!' in Spanish."
    ixel "My mom was born in the US, and my dad was born in Mexico, and both of my grandmothers were from Mexico, too."
    ixel "My report today will be discussing this family heirloom - a cantaro."

label ixelMenu:
    scene kitchen_modern
    menu:
        "Mama, can you tell me about Mexico?":
                jump momMexico
        "Papa, can you tell me about Mexico?":
                jump dadMexico
        "I’m going to go over to Grandmama’s. OK?":
                jump grandma

label momMexico:
    mom "Well Eishy, most of what I know is from our trips and from your Dad."
    mom "But I can tell you that you were named after the Mayan goddess of love."
    ixel "Really?  I never knew that.  So I’m a goddess?!"
    mom "To me, you are the world, the sun, the moon, and the stars!"
    ixel "I love you too, Mama.  I’m going to go ask Papa."
    jump ixelMenu

label dadMexico:
    ixel "Hey Papa!  I need to do a report on our family heritage."
    dad "Sure thing, lady.  What would you like to know?"
    ixel "What was it like growing up in Mexico?"
    dad "Well… when it comes down to what’s important – family – things were pretty much the same with a ton of family to meet."
    dad "There were always parties to go to and lots of cousins to see. Everyone was greeted with open arms. No matter how young or old, it was a custom to do so."
    ixel "Just like we do!"
    dad "That’s right!  One small difference was sometimes it was tough for my Dad to find work.  Some of our parties were just family sitting around talking.  Not like our big barbeque we had last weekend."
    dad "That is part of the reason my family came to California.  To build a future for me and your uncles.  And the feeling that I had to meet your Mom."
    ixel "You knew Mama from Mexico?"
    dad "No, but something in my heart told me I would find true love in America."
    ixel "What?! I don't believe you!"
    dad "No really!  I would dream of California being a magical place where I would find a beautiful princess to marry."
    dad "It might not be as magical as I dreamed it would be, but I thank God everyday to have you and Mom and your sister in my life."
    ixel "Aww Dad, I didn’t think you were such a big baby!"
    dad "Shhhhh… Don’t let that get around!"
    ixel "So what else do you remember about Mexico?"
    dad "Well… I remember how great my grandmother was at telling stories.  I don’t remember much of them.  I wish I had written them down."
    dad "Why don't you go ask your grandma? I know she has many relics of the past all around her house. You should go talk to her."
    jump ixelMenu

label grandma:
    scene kitchen_old
    ixel "Hola, Grandmama!"
    gmm "Oh Ixel! Hola mi preciosa, ¿cómo estás?"
    ixel "Bien Grandmama, ¿y tú?"
    gmm "Bien! Estoy cosiendo y limpiando. ¿Qué quieres?"
    ixel "Yo...mmm tarea para escuela...información de cultura...?"
    gmm "Nice try. Are you looking for information about my culture for homework?"
    ixel "Yes! A report actually, sorry my Spanish is rough."
    gmm "No te preocupes. At least you can still speak it today outside without being judged for it. It's my native language but at a young age I was assimilated to act and speak more like an American."
    ixel "I am working on a report for school and came here to ask about Mexico and your mom."
    gmm "Whatever the reason I am just so happy to see you.  Please have a seat.  Are you hungry? Oh let me get you something.  You and your sister are too skinny."
    ixel "Thank you Grandmama.  Are these pieces of pottery from Mexico?"
    gmm "Oh yes!  My Mom made most of these.  That bowl next to you is my favorite."
    ixel "It is pretty.  I have always liked it.  I like the flowers."
    gmm "Oh it is pretty, but that is not why it is my favorite.  My Mom and I made that bowl together.  It was one of the few pieces that survived from my trip here."
    ixel "That’s so cool!  Not that others broke, but that you made that with your Mom."
    gmm "Every time I see it, my heart flies back home and fills me with joy."
    gmm "Another piece is in your kitchen."
    ixel "Really? Um….. you mean the water jug?"
    gmm "Yes dear.  My Mom made the cantaro.  That’s the Spanish name for it."
    gmm "I got to paint it.  I was so excited.  It was probably one of the first pieces I got to help with."
    gmm "When I got married, my mom gave it to me and your grandfather.  When your mom got married to your dad, I gave it to them as my gift so that they would never be in need."
    gmm "I would guess when you or your sister gets married, the jug will become one of yours."
    ixel "But there’s only one jug and two of us.  How would that work?"
    gmm "That’s a great question, but I have a wonderful idea!"

menu:
    "Run home and claim the jug as yours since you are the oldest.":
        jump runHome
    "What’s your idea Grandmama?":
        jump makeCantaros

label runHome:
    scene kitchen_modern
    show ixelMom:
        pos (600, 250)
    show ixel2:
        pos (800, 400)
    mom "Hey Eishy!  What’s the rush?"
    ixel "Mama, you are planning to give me the cantaros when I get married, right?"
    mom "Well… I hadn’t thought about it."
    ixel "Since I’m the oldest, I should get it."
    show sister:
        pos (500, 200)
    sister "Hey!  Wait a minute! You said you didn’t want to get married!"
    ixel "Umm… well, I changed my mind.  Plus I said I didn’t want to get married to Billy!"
    ixel "Since I claimed it first, it’s mine!"
    sister "NO! It’s mine!"
    ixel "GASP!"
    scene kitchen_modern
    show chippedJug
    mom "Oh Ixel…"
    ixel "I’m so sorry…"
    $ broken = True
    scene kitchen_old
    gmm "Don’t worry.  I know what we can do."
    gmm "OK Ixel, why don’t you take that piece and break it some more into little pieces."
    ixel "What?!  Why?"
    jump makeCantaros2

label makeCantaros:
    scene kitchen_old
    gmm "I have some broken pottery under the sink.  Can you grab one of them?"
    ixel "OK.  Now what?"
    gmm "While we break that up into little pieces, I’ll have your father buy some clay and bring your sister over."

label makeCantaros2:
    show ixelGrandma at left
    show sister at center
    show ixel2 at right
    gmm "We will save the little pieces for painting while will wait for the fresh clay your father is buying at the craft store."
    gmm "I wish it was from my hometown, but climate change has made that clay unusable."
    gmm "Here... why don't we play a game and put these cards in order to make a new jug"

label cardgame:

    scene table

    python:
        c = Cards(1)
        c.show()

label continue:
    while True:
        python:
            ui.textbutton("DONE", ui.jumps("done"), xalign=.025, yalign=.05)
            event = c.interact()

            if event:
                renpy.checkpoint()

label done:

    menu:
        "Are you sure this is the order?"

        "Yes":
            jump gradeCards

        "No":
            jump continue

label gradeCards:
    $ gradeIxel = 0.0

    if c.order[0].__getitem__(0) == 1:
        $ gradeIxel += 0.67
    if c.order[1].__getitem__(0) == 2:
        $ gradeIxel += 0.67
    if c.order[2].__getitem__(0) == 3:
        $ gradeIxel += 0.67
    if c.order[3].__getitem__(0) == 4:
        $ gradeIxel += 0.67
    if c.order[4].__getitem__(0) == 5:
        $ gradeIxel += 0.67
    if c.order[5].__getitem__(0) == 6:
        $ gradeIxel += 0.67

    if gradeIxel >= 4.0:
        $ ixelGrade = "That was a great A+ presentation!"
    elif gradeIxel >= 3.0:
        $ ixelGrade = "That was nice. B+ Ixel!"
    else :
        $ ixelGrade = "We'll talk after class about your grade."

label endCards:
    scene blackboard_ixel
    show ixel2 at right
    show teacher at left
    if broken:
        show stool2jugs:
            pos (400,300)
        ixel "I brought two clay water jugs known as a cantaro."
        ixel "The one with the chip missing is my Mom's."
        ixel "The other one I made with the help of my Grandmother."
    else:
        show stoolJug:
            pos (400,300)
        ixel "I brought in a clay water jug known as a cantaro."    
    ixel "It cools water down without any electricity."    
    tea "Thank you Ixel. [ixelGrade]."
    jump start


################## TERESA #####################
label teresa:
    $ procrastinated = False
    $ idkFlag = False

    scene terRPG
    ter "Argh, come on! I need to level up and catch up with my friends!"

    menu:
        "Continue fighting Cellions":
            jump procrastinate
        "Start homework":
            jump workOnProject

label workOnProject:
    show lilteresaneutral
    ter "I’m kinda bored of fighting Cellions. I guess I should start my project since it’s due tomorrow."

    menu:
        "Look for Mom":
            jump lookForMom
        "Look for Dad":
            jump lookForDad

label lookForDad:
    ter "He’s probably outside.  He’s always tinkering in the garage."
    scene garage2
    show lilteresatalk:
        pos(800,300)
    ter "Daddy? Can you help me with my project?"
    show teresadadnervous:
        pos(50,60)
    dad "I’m a bit busy, but sure. What is it?"
    ter "We have to present about our culture so I thought I’d talk about Filipino culture."
    dad "I don’t know much about that. Your mom taught me how to say a few things in Tagalog, but that’s all I know. You gotta ask her."
    ter "Oh, okay."

label lookForMom:
    ter "Ooo, something smells good!"
    jump terKitchen

label procrastinate:
    $ procrastinated = True
    ter "I leveled up!"
    mom "Teresa! Can you come here?"

    menu:
        "I’ll be there in a second!":
            jump inASecond
        "Coming!":
            jump terKitchen

label inASecond:
    mom "I would like your help now, Teresa!"
    ter "Okay, okay!"

label terKitchen:
    scene terKitchen
    show teresamomneutral:
        pos (900, 100)
    mom "Can you grab me another egg please?"
    show lilteresasmile at left

    ter "Whatcha making?"
    mom "I’m making lumpia."
    ter "Oh, sounds yummy!"
    mom "Here, help me out"
    scene terKitchen
    if procrastinated:
        show lilteresatalk at left
        ter "I guess now is a good time to ask if she can help."

label terKitchen2:
    scene terKitchen
    show lilteresatalk at left
    ter "Can you help me with my project? We have to present about our culture so I thought I’d talk about Filipino culture."
    show teresamomsmile:
        pos (900, 100)
    mom "Oh, sure! What do you want to know?"

    menu:
        "I don’t know":
            jump idk
        "How about when you lived in the Philippines?":
            jump philippines

label idk:
    $ idkFlag = True
    mom "Well, we have some pretty fun games in the Philippines! There’s mancala—"
    ter "Oh, I love mancala!"
    mom "Yes, we call it Sungka! There’s also Tumbang preso, 'knock down the prisoner'. Players throw slippers at a can while one player, the 'tayà', tries to guard it."
    ter "That’s funny!"
    mom "Another activity we have is Tinikling, which is a traditional folk dance. Two people beat, tap, and slide bamboo poles on the ground and against each other as dancers step over and in between the poles while dancing."
    ter "That sounds really cool!"
    mom "Is there anything else you would like to know?"
    ter "What are some of your favorite memories from when you were living in the Philippines?"

label philippines:
    mom "I really enjoyed the fiestas around Christmas time. We would have the Maytinis Festival that took place every Christmas Eve, which was a dramatic re-enactment of the Virgin Mary and Joseph's search in Bethlehem for a place to stay called ‘Panunuluyan’."
    ter "I wish we had fiestas here!"
    mom "On November 1st, we would celebrate All Saints’ Day. We would go to the cemetery at night and everybody would decorate the graves with flowers and candles."
    mom "My dad was so strict. It was the only time we could go out at night, so I always looked forward to it."
    ter "Haha!"
    mom "Every year, for Tatay’s birthday, we would go to Antipolo and ride the Jeepneys which was a fun family tradition."
    ter "Jeepney? Like my toy bus!"
    mom "That’s right!"
    mom "Every afternoon, I would go over to my tita’s house for meriendas, which are afternoon snacks. In the Philippines, we would eat more than four meals a day."
    ter "We could have lumpia for a merienda!"
    mom "We can!"
    mom "We also don’t have four seasons in the Philippines."
    mom "We only have dry and rainy season."
    mom "We lived in an area that when it would rain, it would flood. So we liked it when it got flooded 'cause we got out of school."
    mom "It’s pretty sad now that I think about it. Everybody’s house is flooded."
    ## (Provide an option for players to read more about Philippine floods.)
    ter "Getting out of school is always fun!"
    mom "Well, we’re all done preparing the lumpia. I just have to fry them now. Thank you for helping me. Is there anything else you would like to ask?"
    ter "No, I think that’s all. Thank you for helping me with my project. I know just what to bring to class tomorrow!"

    call jeepneyGame from _call_jeepneyGame

label endJeepney:
    $ gradeTeresa = 4.0
    if gradeTeresa >= 4.0:
        $ teresaGrade = "That was a great A+ presentation!"
    elif gradeTeresa >= 3.0:
        $ teresaGrade = "That was nice. B+ Teresa!"
    else :
        $ teresaGrade = "We'll talk after class about your grade."
    scene blackboard_teresa
    show lilteresasmiling at right
    show teacher at left
    if idkFlag:
       ter "And to represent my culture today, I brought Sungka!"
       ter "It’s a game popular with my family which is played with cowrie shells and the objective is to capture your opponent’s pieces. It’s a lot of fun and I would love to show you guys how to play later!"
       show stoolSungka:
           pos (400,300)
    else :
       show stoolJeepney:
           pos (400,300)
       ter "And to represent my culture today, I brought my toy Jeepney!"
       ter "In the Philippines, Jeepneys are the most popular means of public transportation and are known for their decorations."
    ter "That’s the end of my presentation. Thank you for listening!"
    tea "Thank you Teresa. [teresaGrade]."
    jump start

################## BILLY #####################
label billy:
    scene blackboard_billy
    show lilbillsmile at center
    define foundShortbread = False

    bil "Fàilte! That means 'Welcome!' in Gaelic."
    bil "My Mom's family is from Scotland and Gaelic is their traditional language."

    scene framed

    bil "Mom, why do we have that tiny sword on the wall?"

    mom "Well Billy, that is a valuable family heirloom."

    menu:

        "What's an heirloom?":
            jump heirloom

        "Can we sell it?":
            jump sell

label heirloom:

    mom "An heirloom is something special handed down from one generation to another.  This pin was your great-great-great-great grandfather's.  He came to the United States from Scotland."

    bil "Wow!  Where is Scotland?"

label scotland:

    scene scotland

    mom "Scotland is across the ocean in Europe.  It is a beautiful, yet rugged, place."

    mom "Your great-great-great-great grandfather was also named William.  That's where we got your name."

    mom "When he was a young man, his family was very poor.  They had to sell most of their farmland to survive."

    mom "Since William's older brother would inherit the family farm, William decided to travel to the United States, a place he heard was full of opportunities."

    mom "William's dad gave him his kilt pin and his mom gave him some lace so that he would always remember Scotland."

    mom "And so, William left home, traveled to Edinburgh, and boarded a ship for America."

    mom "He arrived in New York City without a penny to his name, so he wandered the city looking for work."

    mom "Luckily for him (and I guess for all of us) he met a young woman named Rose."

    bil "Why'd you say, 'for all of us'?"

    mom "Well, you and I wouldn't exist if William and Rose didn't get married and have children."

    scene framed

    mom "On their wedding day, William gave Rose that pin and lace as his gift."

    mom "Rose then gave that to your great-great-great grandmother."

    mom "Eventually, that pin was given to me on my wedding day when I married Dad."

    bil "Wow.  That's a great story.  Will I get the pin next?"

    mom "Only if you get married!"

    bil "Well until then, can we take it out of the frame?"

    mom "No, I think it is fine where it is"

    menu:

        "But I want to touch a piece of history!":
            jump history

        "OK Mom.  Why don't you have some more wine?":
            jump wine1

    jump start

label history:

    mom "Well that's a touching thought, but I think we should keep it in the frame."

    menu:

        "Very punny Mom... I'm going to play some video games.":
            jump endGaelic

        "OK Mom.  Why don't you have some more wine?":
            jump wine1

label wine1:

    mom "Well if you insist.  It's five o'clock somewhere!"

    menu:

        "Can I see the pin now?":
            jump wine2

        "It's probably 6 in Scotland. Why don't you have some more wine?":
            jump wine2

label wine2:
    mom "You know... I have always wanted to see how pointy that pin is."

    mom "Hold tight there Billy-boy.  Let me get that frame now."

    scene frame_broken

    menu:
        "You OK Mom?":
            jump momCrash

        "Mom, look!  There's something behind the backing.":
            jump pinCrash

label momCrash:
    mom "Whew!  That frame was heavier than it looked."

label pinCrash:
    $ foundShortbread = True
    mom "What IS THAT behind the backing?"

    bil "Looks like a note but the letters are all jumbled."

    mom "Oh silly Billy, it's not jumbled, it's Gaelic."

screen billy_UI:
    draggroup:
        drag:
            drag_name "gal_recipe1.png"
            child gal_recipe1
            droppable True
            dragged recipe_dragged
            xpos 100 ypos 190

        drag:
            drag_name "gal_recipe2.png"
            child gal_recipe2
            droppable True
            dragged recipe_dragged
            xpos 100 ypos 230

        drag:
            drag_name "gal_recipe3.png"
            child gal_recipe3
            droppable True
            dragged recipe_dragged
            xpos 100 ypos 270

        drag:
            drag_name "gal_recipe4.png"
            child gal_recipe4
            droppable True
            dragged recipe_dragged
            xpos 100 ypos 310

        drag:
            drag_name "gal_recipe5.png"
            child gal_recipe5
            droppable True
            dragged recipe_dragged
            xpos 100 ypos 350

        drag:
            drag_name "gal_recipe6.png"
            child gal_recipe6
            droppable True
            dragged recipe_dragged
            xpos 100 ypos 380

        drag:
            drag_name "gal_recipe7.png"
            child gal_recipe7
            droppable True
            dragged recipe_dragged
            xpos 100 ypos 420

        drag:
            drag_name "gal_recipe8.png"
            child gal_recipe8
            droppable True
            dragged recipe_dragged
            xpos 100 ypos 455

        drag:
            drag_name "Recipe1"
            child Recipe1
            draggable False
            xpos 690 ypos 190

        drag:
            drag_name "Recipe2"
            child Recipe2
            draggable False
            xpos 700 ypos 230

        drag:
            drag_name "Recipe3"
            child Recipe3
            draggable False
            xpos 700 ypos 270

        drag:
            drag_name "Recipe4"
            child Recipe4
            draggable False
            xpos 700 ypos 310

        drag:
            drag_name "Recipe5"
            child Recipe5
            draggable False
            xpos 705 ypos 340

        drag:
            drag_name "Recipe6"
            child Recipe6
            draggable False
            xpos 700 ypos 380

        drag:
            drag_name "Recipe7"
            child Recipe7
            draggable False
            xpos 700 ypos 415

        drag:
            drag_name "Recipe8"
            child Recipe8
            draggable False
            xpos 700 ypos 450

label translate:
    $ gradeBilly = 0.0
    $ Recipe1 = "Recipe1.png"
    $ Recipe2 = "Recipe2.png"
    $ Recipe3 = "Recipe3.png"
    $ Recipe4 = "Recipe4.png"
    $ Recipe5 = "Recipe5.png"
    $ Recipe6 = "Recipe6.png"
    $ Recipe7 = "Recipe7.png"
    $ Recipe8 = "Recipe8.png"
    $ gal_recipe1 = "gal_recipe1.png"
    $ gal_recipe2 = "gal_recipe2.png"
    $ gal_recipe3 = "gal_recipe3.png"
    $ gal_recipe4 = "gal_recipe4.png"
    $ gal_recipe5 = "gal_recipe5.png"
    $ gal_recipe6 = "gal_recipe6.png"
    $ gal_recipe7 = "gal_recipe7.png"
    $ gal_recipe8 = "gal_recipe8.png"
    $ galRecipe1 = "gal_recipe1.png"
    $ galRecipe2 = "gal_recipe2.png"
    $ galRecipe3 = "gal_recipe3.png"
    $ galRecipe4 = "gal_recipe4.png"
    $ galRecipe5 = "gal_recipe5.png"
    $ galRecipe6 = "gal_recipe6.png"
    $ galRecipe7 = "gal_recipe7.png"
    $ galRecipe8 = "gal_recipe8.png"
    scene blackboard_scotland

    # would have a for loop here, but call doesn't work with loops
    call screen billy_UI
    call billyLogic from _call_billyLogic

    call screen billy_UI
    call billyLogic from _call_billyLogic_1

    call screen billy_UI
    call billyLogic from _call_billyLogic_2

    call screen billy_UI
    call billyLogic from _call_billyLogic_3

    call screen billy_UI
    call billyLogic from _call_billyLogic_4

    call screen billy_UI
    call billyLogic from _call_billyLogic_5

    call screen billy_UI
    call billyLogic from _call_billyLogic_6

    call screen billy_UI
    call billyLogic from _call_billyLogic_7

label endGaelic:
    if gradeBilly >= 4.0:
        $ billyGrade = "That was a great A+ presentation!"
    elif gradeBilly >= 3.0:
        $ billyGrade = "That was nice. B+ Billy!"
    else :
        $ billyGrade = "We'll talk after class about your grade."

    scene blackboard_billy
    show lilbillsmile at right
    show teacher at left
    if foundShortbread:
        show stoolShortbread:
            pos (400,300)
        bil "I brought Scottish shortbread for everybody!"
    else:
        bil "I was going to bring in a family heirloom, but it is too valuable for me to touch."
        bil "So I was thinking I would dance a jig.  But then I remembered I can't dance."

    tea "Thank you Billy. [billyGrade]."
    jump start

label sell:

      mom "Oh no! It is way too valuable to sell."

      bil "Why is it valuable?"

      mom "Well, Billy, that pin was your great-great-great-great grandfather's.  This family heirloom comes all the way from Scotland."

      menu:

        "What's an heirloom?":
            jump heirloom

        "Yawn.... I'm bored.  I'm going to play some video games.":
            jump endGaelic

label end:
    
#scene blackboard_grades


screen end_UI:
    if gradeLinda >= 4.0:
       imagebutton auto "images/gradeA_%s.png" xpos 350 ypos 160 action NullAction()
    elif gradeLinda >= 3.0:    
       imagebutton auto  "images/gradeB_%s.png" xpos 350 ypos 160 action NullAction()
    elif gradeLinda >= 2.0:    
       imagebutton auto "images/gradeC_%s.png" xpos 350 ypos 160 action NullAction()
    elif gradeLinda >= 1.0:
       imagebutton auto "images/gradeD_%s.png" xpos 350 ypos 160 action NullAction()
    else:
       imagebutton auto "images/gradeIncomplete_%s.png" xpos 350 ypos 160 action NullAction()

    if gradeIxel >= 4.0:
       imagebutton auto "images/gradeA_%s.png" xpos 350 ypos 210 action NullAction()
    elif gradeIxel >= 3.0:    
       imagebutton auto  "images/gradeB_%s.png" xpos 350 ypos 210 action NullAction()
    elif gradeIxel >= 2.0:    
       imagebutton auto "images/gradeC_%s.png" xpos 350 ypos 210 action NullAction()
    elif gradeIxel >= 1.0:
       imagebutton auto "images/gradeD_%s.png" xpos 350 ypos 210 action NullAction()
    else:
       imagebutton auto "images/gradeIncomplete_%s.png" xpos 350 ypos 210 action NullAction()

    if gradeBilly >= 4.0:
       imagebutton auto "images/gradeA_%s.png" xpos 350 ypos 250 action NullAction()
    elif gradeBilly >= 3.0:    
       imagebutton auto  "images/gradeB_%s.png" xpos 350 ypos 250 action NullAction()
    elif gradeBilly >= 2.0:    
       imagebutton auto "images/gradeC_%s.png" xpos 350 ypos 250 action NullAction()
    elif gradeBilly >= 1.0:
       imagebutton auto "images/gradeD_%s.png" xpos 350 ypos 250 action NullAction()
    else:
       imagebutton auto "images/gradeIncomplete_%s.png" xpos 350 ypos 250 action NullAction()

    if gradeTeresa >= 4.0:
       imagebutton auto "images/gradeA_%s.png" xpos 350 ypos 300 action NullAction()
    elif gradeTeresa >= 3.0:    
       imagebutton auto  "images/gradeB_%s.png" xpos 350 ypos 300 action NullAction()
    elif gradeTeresa >= 2.0:    
       imagebutton auto "images/gradeC_%s.png" xpos 350 ypos 300 action NullAction()
    elif gradeTeresa >= 1.0:
       imagebutton auto "images/gradeD_%s.png" xpos 350 ypos 300 action NullAction()
    else:
       imagebutton auto "images/gradeIncomplete_%s.png" xpos 350 ypos 300 action NullAction()

    imagebutton auto "gui/mm_quit_%s.png" xpos 260 ypos 350 focus_mask True action Quit(confirm=not main_menu) # hovered [ Play("sound", "audio/ring.wav") ]

    imagebutton auto "gui/mm_credits_%s.png" xpos 390 ypos 350 focus_mask True action ShowMenu("credits") # hovered [ Play("sound", "audio/ring.wav") ]

label end2:
    scene blackboard_grades
    call screen end_UI
    
    return

label jeepneyGame:
    python:
        # Create a sprite manager.
        repulsor = SpriteManager(update=repulsor_update, event=repulsor_event)
        repulsor_sprites = [ ]
        repulsor_pos = None

        # Ensure we only have one smog displayable.
        smog = Image("smog.png")

        # Add sprites.
        for i in range(800):
            repulsor_sprites.append(repulsor.create(smog))

        # Position the sprites.
        for i in repulsor_sprites:
            i.x = renpy.random.randint(2, 1198)
            i.y = renpy.random.randint(2, 558)

        del smog
        del i

    # Add the repulsor to the screen.
label smogGame:
    $ smogCountdown = "new game"
    scene globe4Game

    # Show a countdown for X seconds.
    show expression repulsor as repulsor
    image countdown = DynamicDisplayable(countdown, length=10.0)
    show countdown at Position(xalign=.05, yalign=.3)
    while smogCountdown <> "FINISHED":
        pause(1)

    "Unless we act fast, we are in trouble."

    hide repulsor

    # Clean up.
    python:
        del repulsor
        del repulsor_sprites
        del repulsor_pos
    return

label billyLogic:
    if "gal_recipe1.png" == gaelic:
        $ gal_recipe1 = "mini_green.png"
        if "Recipe8" == english:
            $ gradeBilly += 0.5
    if "gal_recipe2.png" == gaelic:
        $ gal_recipe2 = "mini_green.png"
        if "Recipe4" == english:
            $ gradeBilly += 0.5
    if "gal_recipe3.png" == gaelic:
        $ gal_recipe3 = "mini_green.png"
        if "Recipe7" == english:
            $ gradeBilly += 0.5
    if "gal_recipe4.png" == gaelic:
        $ gal_recipe4 = "mini_green.png"
        if "Recipe3" == english:
            $ gradeBilly += 0.5
    if "gal_recipe5.png" == gaelic:
        $ gal_recipe5 = "mini_green.png"
        if "Recipe6" == english:
            $ gradeBilly += 0.5
    if "gal_recipe6.png" == gaelic:
        $ gal_recipe6 = "mini_green.png"
        if "Recipe1" == english:
            $ gradeBilly += 0.5
    if "gal_recipe7.png" == gaelic:
        $ gal_recipe7 = "mini_green.png"
        if "Recipe5" == english:
            $ gradeBilly += 0.5
    if "gal_recipe8.png" == gaelic:
        $ gal_recipe8 = "mini_green.png"
        if "Recipe2" == english:
            $ gradeBilly += 0.5
    if "Recipe1" == english:
        $ Recipe1 = gaelic
    if "Recipe2" == english:
        $ Recipe2 = gaelic
    if "Recipe3" == english:
        $ Recipe3 = gaelic
    if "Recipe4" == english:
        $ Recipe4 = gaelic
    if "Recipe5" == english:
        $ Recipe5 = gaelic
    if "Recipe6" == english:
        $ Recipe6 = gaelic
    if "Recipe7" == english:
        $ Recipe7 = gaelic
    if "Recipe8" == english:
        $ Recipe8 = gaelic
    return

label lindaLogic:
    if "Statement1" == statement:
        $ snow_white = "mini_green.png"
        if TRUE == booleanChoice:
            $ gradeLinda += 1.0
    if "Statement2" == statement:
        $ cuckoo = "mini_green.png"
        if TRUE == booleanChoice:
            $ gradeLinda += 1.0
    if "Statement3" == statement:
        $ napoleon = "mini_green.png"
        if TRUE == booleanChoice:
            $ gradeLinda -= 1.0
    if "Statement4" == statement:
        $ leaves = "mini_green.png"
        if TRUE == booleanChoice:
            $ gradeLinda -= 1.0
    if "Statement5" == statement:
        $ hurricane = "mini_green.png"
        if TRUE == booleanChoice:
            $ gradeLinda += 1.0
    if "Statement6" == statement:
        $ ham = "mini_green.png"
        if TRUE == booleanChoice:
            $ gradeLinda += 1.0
    return
