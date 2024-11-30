import pgzrun
import random

#variables
HEIGHT=500
WIDTH=500
TITLE="B.O.B"
texts=0
level=0
drawcomputer=False
saladinfo=False
troll=False
riddleactivate=False
display_riddle=False
stage=0
price_display_tomato=False
cash=3600
start_earning=False
tomato_owned=False
inventory=[]
move_tomato=False
toothbrush_owned=False
carrot_owned=False
onion_owned=False
wood_count=0
wood_purchase=False
filterd_inv=[]
salad_launcher_owned=False
cabbage_owned=False
knife_owned=False
reflist=[]
can_advance=False
cut=False
selection="NONE"

tomatoiscut=False
cabbageiscut=False
onioniscut=False
#actors
bank=Actor('bank')
background=Actor("healthgamebg")
computer=Actor("computer")
info_display_unit=Actor("infodisplay")
salad=Actor("salad")
house=Actor("house")
houses=[]
mainhouse=Actor("big3house")
paper=Actor("paper")
paper_on_table=Actor('paperontable')
nex_button=Actor("nextbutton")
main_character=Actor("robot_idle")
main_character.x=250
main_character.y=250
tomato=Actor('tomato')
cabbage=Actor('cabbage1')
target_store=Actor('targetstore')
walmart=Actor("walmart")
costcos=Actor("costcos")
shelves=Actor('shelves')
shelve_list=[]
wrong_house_anim=Actor("wrong_house1")
clock=0
houseanim=["wrong_house1", "wrong_house2", "wrong_house3"]
earn_button=Actor('button')
money_sack=Actor('money_sack')
coin=Actor('coin_gold')
toothbrush=Actor('toothbrush')
carrot=Actor('carrot')
onion=Actor('onion')
wood=Actor("wood")
salad_launcher=Actor("salad_launcher")
knife=Actor("knife")
cutting_board_button=Actor("cuttingboard_button")
cuttingboardscreendispunit=Actor("cutting_board")
knife1=Actor("knife")
knife1.x=250
knife1.y=410

#craft stuff
craftbutton=Actor("craft")
craft=False
wood1=Actor("wood")
wood1clicked=False
wood1.x=random.randint(100,400)
wood1.y=random.randint(100,400)
wood2=Actor("wood")
wood2clicked=False
wood2.x=random.randint(100,400)
wood2.y=random.randint(100,400)
wood3=Actor("wood")
wood3clicked=False
wood3.x=random.randint(100,400)
wood3.y=random.randint(100,400)

allcrafted=False
#cut stuff

cuttomato=Actor("tomato")
cuttomato.x=150
cuttomato.y=150
cutcabbage=Actor("cabbage1")
cutcabbage.x=350
cutcabbage.y=150
cutonion=Actor("onion")
cutonion.x=250
cutonion.y=350
allcut=False

#boss fight
burger_lord=Actor("burgerking")
mainchar2=Actor("mc")
def bossfight():
    x=random.randint(1,20)
    burger_lord.y=x*35  

bullet=Actor("frybullet")
mainchar2.x=1100
mainchar2.y=350
bosshp=20
playerhp=20
lim_usg_healing=5
playerbullet=Actor("saladbullet")
weak=False
def draw():
    global texts
    global level
    global cash
    global tomato_owned
    global move_tomato
    global toothbrush_owned
    global carrot_owned
    global onion_owned
    global wood_purchase
    global salad_launcher_owned
    global cabbage_owned
    global knife_owned
    global can_advance
    global craft
    global WIDTH
    global HEIGHT
    if level==0:
        
        if texts==0:  
            screen.clear()  
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("Long ago, there lived 4 chefs...",color="white",center=(250,250))   
        if texts==1:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("the 4th chef named Bob had no money...", color="white",center=(250,250))        
        if  texts==2:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("One day after a long day of work...", color="white", center=(250,250))
        if texts==3:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("Bob had a loaf of bread, some lettuce", color="white", center=(250,250))
            screen.draw.text("sauce and some grilled beef...", color="white", center=(250,280))
        if texts==4:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("so Bob put the grilled beef,", color="white", center=(250,250))
            screen.draw.text(" sauce and lettuce between the 2 buns...", color="white", center=(250,280))
        if texts==5:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("After 1 bite, Bob knew he had made a masterpeice", color="white", center=(250,250))
        if texts==6:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("Bob sold his creation across stores world-wide..", color="white", center=(250,250))
        if texts==7:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("World Health Officials noticed a major drop in health...", color="white", center=(250,250))
        if texts==8:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("Bob's Burgers caused people to get sick...", color="white", center=(250,250))
        if texts==9:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("the other chefs were inventing a better dish...", color="white", center=(250,250))
        if texts==10:
            screen.clear()
            screen.draw.text("(Press space to continue)", color="white",topleft=(20,20))
            screen.draw.text("But Bob fed them so many bugers that they died...", color="white", center=(250,250))
        if texts>=11:
            level=1

    if level==1:
        screen.clear()
        screen.fill("green")
        screen.draw.text("Task: find the house of the BIG 3", color="white", topleft=(20,20))
        mainhouse.draw()
        mainhouse.x=random.randint(50,450)
        mainhouse.y=random.randint(50,450)
        for i in range(2):
            house.draw()
            house.x=random.randint(50, 450)
            house.y=random.randint(50,450)
            houses.append(house)   
        

        if troll==True:
            screen.clear()                 
            for i in range(3):
                if i==1:
                    wrong_house_anim.image="wrong_house1"
                    wrong_house_anim.draw()
                if i==2:
                    wrong_house_anim.image="wrong_house2"
                    wrong_house_anim.draw()
                if i==3:
                    wrong_house_anim.image="wrong_house3"
                    wrong_house_anim.draw()
            screen.draw.text("Nothing in this house :), click 'e' to leave ", color="white", topleft=(20,20))
               
    if level==2:
        screen.clear()        
        screen.blit("healthgamebg",(0,0))
        screen.draw.text("Task: find the cure's recepie", color="black", topleft=(20,20))
        computer.x=255
        computer.y=215
        nex_button.draw()
        nex_button.x=(450)
        nex_button.y=(50)
        paper_on_table.draw()
        paper_on_table.x=315
        paper_on_table.y=380
        computer.draw()
        if riddleactivate == True:
                    screen.clear()
                    screen.fill("black")
                    paper.draw()
                    paper.x=250
                    paper.y=250
                    screen.draw.text("The Riddle of the Three", color="black", topleft=(60,20))
                    screen.draw.text("_________________________", color="black", topleft=(60,25))
                    screen.draw.text("In the market,", color="black", topleft=(60,50))
                    screen.draw.text("Most of your needs you shall find,", color="black", topleft=(60,70))
                    screen.draw.text("The ingredients you must pick:", color="black", topleft=(60,90))
                    screen.draw.text("1) The vegetable that makes you go blind.", color="black", topleft=(60,110))
                    screen.draw.text("2) Squished to make sauce, Red like the sun,", color="black", topleft=(60,150))
                    screen.draw.text("3) Green leafs resembles a fan", color="black", topleft=(60,170))
                    screen.draw.text("4) Cut, Mince, don't burn", color="black", topleft=(60,190))
                    screen.draw.text("5) Place in a vessel, ", color="black", topleft=(60,210))
                    screen.draw.text("6) and let it wrestle, ", color="black", topleft=(60,230))
                    screen.draw.text("7) the toxins of the burger", color="black", topleft=(60,350))
        if drawcomputer==True:
            info_display_unit.draw()
            info_display_unit.x=250
            screen.draw.text("NEWS HEADLINES: BOB KILLS MILLIONS", color="black", topleft=(40,40))
            screen.draw.text("___________________________________________", color="black", topleft=(40,42))
            screen.draw.text("Bob's burgers strike again, this time a small", color="black", topleft=(40,60))
            screen.draw.text("town in Boston gets hit by burgers, nearly 235", color="black", topleft=(40,80))
            screen.draw.text("people are sickend by the Burger Syndrome", color="black", topleft=(40,100))
            salad.draw()
            salad.x=100
            salad.y=260
            screen.draw.text("Research on a cure by the BIG 3", color="black", topleft=(180,200))
            screen.draw.text("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_", color="black", topleft=(180,210))
            if saladinfo==True:
                screen.clear()
                screen.fill("cyan")
                screen.draw.text('"-A salad a day keeps the burger syndrome away"', color="black", topleft=(20,20))
                screen.draw.text("Our discoveries have shown us that eating #--@^$@! food", color="black", topleft=(20,60))
                screen.draw.text("is good, ^%&^@! food is good for you because of the #!$*_!($)", color="black", topleft=(20,80))
                screen.draw.text("there are many types of $&!@^*, but the most important part", color="black", topleft=(20,100))
                screen.draw.text("of all $!!$*&@ has to be the fact that it is %$@#*/!.", color="black", topleft=(20,120))
                screen.draw.text("Now I shall reveal the key to health", color="black", topleft=(20,140))
                screen.draw.text("Anyways, yesterday I discoverd that the key to health was:", color="black", topleft=(20,160))
                screen.draw.text("1) get some to*%!*&, P!#&tos, 0n1075, and some 6833Eg%", color="black", topleft=(20,200))
                screen.draw.text("2) make sure to !$!&5%3 the ingredients finely", color="black", topleft=(20,220))
                screen.draw.text("3) Place in a %#4l and drizzle some !393", color="black", topleft=(20,240))
                screen.draw.text("Update (3 years ago): bob is trying to exterminate us three", color="black", topleft=(20,280))
                screen.draw.text("in case he gets us and hacks our website i made a paper ", color="black", topleft=(20,300))
                screen.draw.text("document of the recipie", color="black", topleft=(20,320))
    if level==3:
        screen.clear() 
        screen.blit("grass",(0,0))
        main_character.draw()
        walmart.draw()
        costcos.draw()
        target_store.draw()
        bank.draw()
        screen.draw.text("Task: Find ingredients,(click 'f' for riddle, 'g' to close)", color="white", topleft=(20,20))
        screen.draw.text("arrow keys to move", color="black", topleft=(20,40))
        screen.draw.text('Cash: '+str(cash), color="black", topleft=(20,60))
        target_store.x=60
        target_store.y=450
        walmart.x=450
        walmart.y=450
        costcos.x=450
        costcos.y=60
        bank.x=250
        bank.y=450
        for i in inventory:
            if i in inventory:
                reflist.append(i)
                if "tomato" in reflist and "cabbage" in reflist and "onion" in reflist and "knife" in reflist and "3x wood" in reflist:
                    screen.fill("white")
                    screen.draw.text("You have found your ingredients, now cook them!", color="black", center=(WIDTH//2,HEIGHT//2))
                    screen.draw.text("'space to continue'", color="black", topleft=(20,20))
                    can_advance=True
            if i in reflist:
                pass
        if stage=="bank":
            screen.clear()
            screen.fill('white')
            money_sack.x=random.randint(50,450)
            money_sack.y=random.randint(50,450)
            money_sack.draw()
            screen.draw.text("You have "+str(cash)+" USD", color="black", topleft=(20,20))
        if stage=="costcos":
            screen.clear()
            screen.fill("grey")
            screen.draw.text('Cash: '+str(cash), color="black", topleft=(20,60))
            shelves.draw()
            tomato.draw()
            carrot.draw()
            toothbrush.draw()
            shelves.x=250
            shelves.y=200
            toothbrush.x=180
            toothbrush.y=180
            carrot.y=180
            carrot.x=300
            tomato.x=60
            tomato.y=180
            screen.draw.text("50 USD", color='black',center=(60,230))
            screen.draw.text("30 USD", color="black", center=(180,230))
            screen.draw.text("50 USD", color="black", center=(300,230))
            if price_display_tomato==True and tomato_owned==True:
                tomato.x=900
                tomato.y=900
                inventory.append('tomato')
                tomato_owned=False
                move_tomato=True
            if toothbrush_owned==True:
                inventory.append("toothbrush")
                toothbrush_owned=False
            if carrot_owned==True:
                inventory.append("carrot")
                carrot_owned=False
        screen.draw.text("Inventory"+str(inventory), color="black", topleft=(20,80))    
        if stage=="target":
            screen.fill("green")
            shelves.draw()
            shelves.x=250
            shelves.y=200
            onion.draw()
            wood.draw()
            salad_launcher.draw()
            salad_launcher.x=300
            salad_launcher.y=180
            wood.x=180
            wood.y=180
            onion.x=60
            onion.y=180
            screen.draw.text("Cash: "+str(cash), color="black", topleft=(20,20))
            screen.draw.text("Inventory"+str(inventory), color="black", topleft=(20,40))
            screen.draw.text("70 USD", color="black", center=(60,230))
            screen.draw.text("120 USD", color="black", center=(180,230))
            screen.draw.text("300 USD", color="black", center=(300,230))
            if onion_owned==True:
                inventory.append("onion")
                onion_owned=False
            if wood_count==1 and wood_purchase==True:
                inventory.append("1x wood")
                wood_purchase=False
            if wood_count==2 and wood_purchase==True:
                inventory.remove("1x wood")
                inventory.append("2x wood")
                wood_purchase=False
            if wood_count==3 and wood_purchase==True:
                inventory.remove("2x wood")
                inventory.append("3x wood")
                wood_purchase=False
            if salad_launcher_owned==True:
                
                salad_launcher_owned==False
                salad_launcher_owned=False
                
        if stage=="walmart":
            screen.clear()
            screen.fill("light blue")
            shelves.draw()
            cabbage.draw()
            knife.draw()
            knife.x=180
            knife.y=180
            cabbage.x=60
            cabbage.y=180
            shelves.x=250
            shelves.y=200
            screen.draw.text("Cash: "+str(cash), color="black", topleft=(20,20))
            screen.draw.text("Inventory: "+str(inventory), color="black", topleft=(20,40))
            screen.draw.text("80", color="black", center=(60,230))
            screen.draw.text("60", color="black", center=(180,230))
            if cabbage_owned==True:       
                cabbage_owned=False 
                inventory.append("cabbage")  
            if knife_owned==True:
                knife_owned=False
                inventory.append("knife")   

        if riddleactivate == True:
            screen.clear()
            screen.fill("black")
            paper.draw()
            paper.x=250
            paper.y=250
            screen.draw.text("The Riddle of the Three", color="black", topleft=(60,20))
            screen.draw.text("_________________________", color="black", topleft=(60,25))
            screen.draw.text("In the market,", color="black", topleft=(60,50))
            screen.draw.text("Most of your needs you shall find,", color="black", topleft=(60,70))
            screen.draw.text("The ingredients you must pick:", color="black", topleft=(60,90))
            screen.draw.text("1) The vegetable that makes you go blind.", color="black", topleft=(60,110))
            screen.draw.text("2) Squished to make sauce, Red like the sun,", color="black", topleft=(60,150))
            screen.draw.text("3) Green leafs resembles a fan", color="black", topleft=(60,170))
            screen.draw.text("4) Cut, Mince, don't burn", color="black", topleft=(60,190))
            screen.draw.text("5) Place in a vessel, ", color="black", topleft=(60,210))
            screen.draw.text("6) and let it wrestle, ", color="black", topleft=(60,230))
            screen.draw.text("7) the toxins of the burger", color="black", topleft=(60,350))
    if level==4:
        screen.clear()
        screen.fill("white")
        screen.draw.text("Level 4: ",color="black", topleft=(20,20))
        screen.draw.text("Objective: Make a salad", color="black", topleft=(20,40))
        nex_button.draw()
        nex_button.x=250
        nex_button.y=250
        screen.draw.text("Perform the rigorous task of making a salad", color="black", center=(250,370))
        '''cutting_board_button.draw()
        screen.draw.text("Cutting Board", color="black", center=(150,360))
        cutting_board_button.x=150
        cutting_board_button.y=250
        craftbutton.draw()
        screen.draw.text("Craft", color="black", center=(350,360))
        craftbutton.x=350
        craftbutton.y=250
      
        if cut==True and craft==False:
            screen.clear()
            screen.blit("cutting_board",(0,0))
            cutonion.draw()
            cutcabbage.draw()
            cuttomato.draw()
            screen.draw.text("Chop the vegetables ('e' to return)", color="black", topleft=(20,20))'''
        '''if selection=="Tomato":
                screen.draw.text("Ingredient selected: TOMATO", color="black", topleft=(20,60))
                screen.clear()
            if selection=="Onion":
                screen.draw.text("Ingredient selected: ONION", color="black", topleft=(20,60))
            if selection=="Cabbage":
                screen.draw.text("Ingredient selected: CABBAGE", color="black", topleft=(20,60))
            else:
                screen.draw.text("Ingredient selected: NONE", color="black", topleft=(20,60))'''
        '''if craft==True and cut==False:
            screen.clear()
            wood1.draw()
            wood2.draw()
            wood3.draw()
            if wood1clicked==True:
                wood1.x=9999
            if wood2clicked==True:
                wood2.x=9999
            if wood3clicked==True:
                wood3.x=9999'''
        
    if level==5:
        screen.fill("dim grey")
        screen.draw.text("You have made a salad,", color="black", topleft=(20,20))
        screen.draw.text("Now, you must feed it to bob", color="black", topleft=(20,40))
        screen.draw.text("If you are dying...", color="black", topleft=(20,80))
        screen.draw.text("Use your salad...", color="black", topleft=(20,100))
        screen.draw.text("Controls:", color="black", bottomright=(480,250))
        screen.draw.text("'e' to fire", color="black", bottomright=(480,270))
        screen.draw.text("'r' to consume", color="black", bottomright=(480,290))
        screen.draw.text("up and down arrow keys to move", color="black", bottomright=(480,310))
        screen.draw.text("SPACE TO START BOSS FIGHT", color="black", bottomright=(480,480))
    if level==6:
        wood3.draw()
        screen.fill("blue")
        WIDTH=1200
        HEIGHT=700
        burger_lord.draw()
        if wood3.x==300:
            bossfight()
            bullet.y=burger_lord.y
            bullet.x=burger_lord.x+100
            bullet.draw()
        bullet.draw()
        screen.draw.text("Boss HP: "+str(bosshp), color="black", topleft=(20,20))
        screen.draw.text("Player HP: "+str(playerhp), color="black", topright=(WIDTH-20,20))
        mainchar2.draw()
        playerbullet.draw()
        if bosshp<0:
            wood3.x=9999
        if weak==True:
            screen.draw.text("BOB IS WEAKEND, HIT HIM WITH SALAD", color="black", center=(WIDTH//2,HEIGHT//2))
        if bosshp<-4:
            level="win"
    if level=="lose":
        screen.clear()
        screen.draw.text("You Lost", color="white", center=(WIDTH//2,HEIGHT//2))
    if level=="win":
        screen.clear()
        screen.draw.text("You WON!!!!!", color="white", center=(WIDTH//2,HEIGHT//2))
def placecutgame():
    tomato.y=90
    cabbage.y=90
    onion.y=90
    tomato.x=random.randint(90,410)
    cabbage.x=random.randint(90,410)
    onion.x=random.randint(90,410)

 
def place_money():
    money_sack.x=random.randint(50,450)
    money_sack.y=random.randint(50,450)

                
    
def on_mouse_down(pos):
    global inventory
    global texts
    global price_display_tomato
    global level
    global drawcomputer
    global saladinfo
    global troll
    global riddleactivate
    global display_riddle
    global start_earning
    global cash
    global toothbrush_owned
    global carrot_owned
    global onion_owned
    global tomato_owned
    global wood_count
    global wood_purchase
    global salad_launcher_owned
    global cabbage_owned
    global knife_owned
    global cut
    global selection
    global onioniscut
    global tomatoiscut
    global cabbageiscut
    global craft
    global wood1clicked
    global wood2clicked
    global wood3clicked
    if computer.collidepoint(pos) and level==2:
        drawcomputer=True
    if salad.collidepoint(pos) and level==2:
        saladinfo=True
    if house.collidepoint(pos) and level==1:
        troll=True
    if mainhouse.collidepoint(pos) and level==1:
        level=2
    if paper_on_table.collidepoint(pos) and level==2:
        riddleactivate=True
        display_riddle=True
    if nex_button.collidepoint(pos) and display_riddle==True and level==2:
        level=3
        riddleactivate=False
    if tomato.collidepoint(pos) and level==3 and stage=="costcos":
        price_display_tomato=True
    if money_sack.collidepoint(pos) and level==3 and stage=="bank":
        cash=cash+10
    if tomato.collidepoint(pos) and level==3 and stage=="costcos" and cash>40:
        cash=cash-50
        tomato_owned=True
    if toothbrush.collidepoint(pos) and level==3 and stage=="costcos" and cash>20:
        toothbrush_owned=True
        cash=cash-30
    if carrot.collidepoint(pos) and level==3 and stage=="costcos" and cash>40:
        cash=cash-50
        carrot_owned=True
    if onion.collidepoint(pos) and level==3 and stage=="target" and cash>60:
        cash=cash-70
        onion_owned=True
    if wood.collidepoint(pos) and level==3 and stage=="target" and cash>110:
        cash=cash-120
        wood_count=wood_count+1
        wood_purchase=True
    if salad_launcher.collidepoint(pos) and level==3 and stage=="target" and cash>290:
        salad_launcher_owned=True
        cash=cash-300
        inventory.append("salad launcher")
    if cabbage.collidepoint(pos) and level==3 and stage=="walmart" and cash>70:
        cash=cash-80
        cabbage_owned=True
    if knife.collidepoint(pos) and level==3 and stage=="walmart" and cash>50:
        knife_owned=True
        cash=cash-60
    if nex_button.collidepoint(pos) and level==4:
        level=5
    '''if cutting_board_button.collidepoint(pos) and level==4:
        cut=True
    if cutting_board_button.collidepoint(pos) and level==4:
        cut=True
    if cuttomato.collidepoint(pos) and level==4 and cut==True:
        cuttomato.x=9999
        tomatoiscut=True
    if cutcabbage.collidepoint(pos) and level==4 and cut==True:
        cutcabbage.x=9999
        cabbageiscut=True
    if cutonion.collidepoint(pos) and level==4 and cut==True:
        cutonion.x=9999
        onioniscut=True
    if craftbutton.collidepoint(pos) and level==4:
        craft=True
    if wood1.collidepoint(pos) and level==4 and craft==True:
        wood1clicked=True
    if wood2.collidepoint(pos) and level==4 and craft==True:
        wood2clicked=True
    if wood3.collidepoint(pos) and level==4 and craft==True:
        wood3clicked=True'''
def update():
    global level
    global saladinfo
    global drawcomputer
    global troll
    global riddleactivate
    global price_display_tomato
    global stage
    global cut
    global craft
    global allcut
    global allcrafted
    global playerhp
    global bosshp
    global lim_usg_healing
    global weak
    if level==0:
        global texts
        if keyboard.space:
            texts=texts+0.25
    if level==1:
        if troll==True and level==1 and keyboard.e:
            troll=False
    if level==2:
        if saladinfo==True and level==2 and keyboard.e:
            saladinfo=False
        if drawcomputer==True and level==2 and keyboard.e:
            drawcomputer=False
        if riddleactivate==True and level==2 and keyboard.e:
            riddleactivate=False
    if level==3:
        if level==3 and riddleactivate==False and keyboard.f:
            riddleactivate=True
        if level==3 and riddleactivate==True and keyboard.g:
            riddleactivate=False
        if level==3 and riddleactivate==False and keyboard.right and main_character.x<500:
            main_character.x=main_character.x+2
            main_character.image="robot_right"
        if level==3 and riddleactivate==False and keyboard.left and main_character.x>0:
            main_character.x=main_character.x-2
            main_character.image="robot_left"
        if level==3 and riddleactivate==False and keyboard.up and main_character.y>0:
            main_character.y=main_character.y-2
            main_character.image="robot_idle"
        if level==3 and riddleactivate==False and keyboard.down and main_character.y<500:
            main_character.y=main_character.y+2
            main_character.image="robot_idle"
        if main_character.colliderect(costcos):
            stage="costcos"
        if main_character.colliderect(target_store):
            stage="target"
        if main_character.colliderect(bank):
            stage="bank"
        if main_character.colliderect(walmart):
            stage="walmart"
        if stage == "costcos" and keyboard.e:
            stage=0
            main_character.x=250
            main_character.y=250
            price_display_tomato=False
        if stage == "walmart" and keyboard.e:
            stage=0
            main_character.x=250
            main_character.y=250
        if stage == "target" and keyboard.e:
            stage=0
            main_character.x=250
            main_character.y=250
        if stage=="bank" and keyboard.e:
            stage=0
            main_character.x=250
            main_character.y=250
        if can_advance==True:
            level=4
    if level==4:
        '''if cut==True and keyboard.e:     
            cut=False
        if craft==True and keyboard.e:
            craft=False
        if wood2clicked==True and wood1clicked==True and wood3clicked==True:
            allcrafted==True
        if tomatoiscut==True and cabbageiscut==True and onioniscut==True:
            allcut=True
        if allcrafted==True and allcut==True:
            level=5
    if level==5:
        pass'''
    if level==5:
        if keyboard.space:
            level=6
    if level==6:
        wood3.x=wood3.x-10
        if wood3.x<0:
            wood3.x=300
        if wood3.x<99999:
            bullet.x=bullet.x+40
        if keyboard.up:
            mainchar2.y=mainchar2.y-5
        if keyboard.down:
            mainchar2.y=mainchar2.y+5
        if keyboard.e:
            #fire
            playerbullet.x=mainchar2.x-100
            playerbullet.y=mainchar2.y
        playerbullet.x=playerbullet.x-40
        
        if keyboard.r and lim_usg_healing>0:
            #consume
            lim_usg_healing=lim_usg_healing-1
            playerhp=playerhp+5
            if playerhp>20:
                playerhp=20
        if bullet.colliderect(mainchar2):
            playerhp=playerhp-1
        if playerbullet.colliderect(burger_lord):
            bosshp=bosshp-2
        if playerhp<0:
            level="lose"
        if bosshp<-4:
            level="win"
        if bosshp<0:
            weak=True





'''****READ ME****
    I HAVE LEFT THE VALUE OF CASH AT 3600 FOR EASE OF PLAYTESTING THE GAME, 
    CONTROLS:
        E TO EXIT
        SPACE TO EXIT(IF WRITTEN ON SCREEN)
        ARROW KEYS TO MOVE
        MOUSEBUTTON1 TO CLICK
    
'''

pgzrun.go()