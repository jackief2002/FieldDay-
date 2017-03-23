from gamelib import *

game = Game(640, 480, "Field Day", 120)

bk = Image("GameProject\\picnicbackground.jpg", game)
bk.resizeTo(game.width, game.height)

ant = Animation("GameProject\\ant.png", 4, game, 256/4, 256/4, 3)

human = Image("GameProject\\human.png", game)

rock1 = Image("GameProject\\rocks.png", game)
rock1.moveTo(50, 100)
rock2 = Image("GameProject\\rocks.png", game)
rock2.moveTo(60, 250)
rock3 = Image("GameProject\\rocks.png", game)
rock3.moveTo(400, 200)
rock4 = Image("GameProject\\rocks.png", game)
rock4.moveTo(550, 300)
rock5 = Image("GameProject\\rocks.png", game)
rock5.moveTo(250, 123)
rock6 = Image("GameProject\\rocks.png", game)
rock6.moveTo(300, 400)
rock7 = Image("GameProject\\rocks.png", game)
rock7.moveTo(450, 150)
rock8 = Image("GameProject\\rocks.png", game)
rock8.moveTo(380, 264)
rock9 = Image("GameProject\\rocks.png", game)
rock9.moveTo(274, 416)
rock10 = Image("GameProject\\rocks.png", game)
rock10.moveTo(142, 423)

rock1.resizeBy(-75)
rock2.resizeBy(-75)
rock3.resizeBy(-75)
rock4.resizeBy(-75)
rock5.resizeBy(-75)
rock6.resizeBy(-75)
rock7.resizeBy(-75)
rock8.resizeBy(-75)
rock9.resizeBy(-75)
rock10.resizeBy(-75)

nuggets = []
regenTime = -1
regenTimeChicken = -1
regenTimeFries = -1
regenTimeSandwich = -1
regenTimeEtc = -1
regenTimeDonuts = -1
gametime = 120
antscore = 0
humanscore = 0

for times in range(2):
    nuggets.append( Animation("GameProject\\chickennuggets.png", 2, game, 172/2, 78, 15 ) )

for n in nuggets:
    n.resizeBy(-50)
    x = randint(50,550)
    y = randint(50,450)
    n.moveTo(x,y)

chicken = []

for times in range(2):
    chicken.append( Animation("GameProject\\chicken.png", 3, game, 227/3, 65, 15 ) )

for c in chicken:
    c.resizeBy(-50)
    x = randint(50,550)
    y = randint(50,450)
    c.moveTo(x,y)

etc = []

for times in range(2):
    etc.append( Animation("GameProject\\etc.png", 4, game, 600/3, 400/2, 15 ) )

for e in etc:
    e.resizeBy(-80)
    x = randint(50,550)
    y = randint(50,450)
    e.moveTo(x,y)

fries = []

for times in range(3):
    fries.append( Animation("GameProject\\frenchfry.gif", 2, game, 400/2, 200, 15 ) )

for f in fries:
    f.resizeBy(-80)
    x = randint(50,550)
    y = randint(50,450)
    f.moveTo(x,y)

sandwiches = []

for times in range(2):
    sandwiches.append( Animation("GameProject\\sandwiches.png", 8, game, 296/4, 147/2, 15 ) )

for s in sandwiches:
    s.resizeBy(-50)
    x = randint(50,550)
    y = randint(50,450)
    s.moveTo(x,y)

donuts = []

for times in range(2):
    donuts.append( Animation("GameProject\\donuts.png", 8, game, 287/4, 145/2, 15) )
    
for d in donuts:
    d.resizeBy(-50)
    x = randint(50,550)
    y = randint(50,450)
    d.moveTo(x,y)



foods = Animation("GameProject\\food.png", 36, game, 450/6, 450/6, 15 )
foods.resizeBy(-30)
x = randint(50, 550)
y = randint(50, 450)
foods.moveTo(x, y)

trophy =Image("GameProject\\trophy.png", game)
trophy.resizeBy(-80)
x = randint(50, 550)
y = randint(50, 450)
trophy.moveTo(x, y)


backgroundmusic = Sound("GameProject\\BackgroundMusic.wav", 1)
bite = Sound("GameProject\\Bite.wav", 2)
awalk = Sound("GameProject\\AntWalk.wav", 3)
hwalk = Sound("GameProject\\HumanWalk.wav", 4)

while not game.over:
    game.processInput()
    bk2 = Image("GameProject\\StartGame.png", game)
    game.setBackground(bk2)
    bk2.resizeTo(game.width, game.height)
    game.drawBackground()
    if keys.Pressed[K_UP]:
        awalk.play()
        ant.rotateTo(360)
        ant.y -= 4

    if keys.Pressed[K_DOWN]:
        awalk.play()
        ant.rotateTo(180)
        ant.y += 4

    if keys.Pressed[K_LEFT]:
        awalk.play()
        ant.rotateTo(90)
        ant.x -= 4

    if keys.Pressed[K_RIGHT]:
        awalk.play()
        ant.rotateTo(270)
        ant.x += 4

    if keys.Pressed[K_w]:
        hwalk.play()
        human.y -= 4

    if keys.Pressed[K_s]:
        hwalk.play()
        human.y += 4

    if keys.Pressed[K_a]:
        hwalk.play()
        human.x -= 4

    if keys.Pressed[K_d]:
        hwalk.play()
        human.x += 4
        

    foods.draw()
    if ant.collidedWith (foods):
        bite.play()
        f.visible = False
        antscore += 10
        game.over = True
    if human.collidedWith(foods):
        bite.play()
        f.visible = False
        humanscore += 10
        game.over = True

    ant.move()
    human.move()
    game.update(30)
    
game.over = False    
while not game.over:
    game.processInput()
    bk.draw()
    ant.move()
    human.move(True)
    rock1.draw()
    rock2.draw()
    rock3.draw()
    rock4.draw()
    rock5.draw()
    rock6.draw()
    rock7.draw()
    rock8.draw()
    rock9.draw()
    rock10.draw()

    backgroundmusic.play()

    for n in nuggets:
        n.draw()
        if n.collidedWith(ant) or n.collidedWith(human):
            regenTime = 100
        if n.collidedWith(ant):
            bite.play()
            n.visible = False 
            antscore += 10
        if n.collidedWith(human):
            bite.play()
            n.visible = False 
            humanscore += 10


    if regenTime >= 0:
        regenTime -= 1
    if regenTime == 0:
        nuggets.append( Animation("GameProject\\chickennuggets.png", 2, game, 172/2, 78, 15 ) )
        n = nuggets[len(nuggets)-1]
        n.resizeBy(-50)
        x = randint(50,550)
        y = randint(50,450)
        n.moveTo(x,y)
        regenTime = -1

    
    for c in chicken:
        c.draw()
        if c.collidedWith(ant) or c.collidedWith(human):
            regenTimeChicken = 150
        if c.collidedWith(ant):
            bite.play()
            c.visible = False 
            antscore += 10
        if c.collidedWith(human):
            bite.play()
            c.visible = False 
            humanscore += 10


    if regenTimeChicken >= 0:
        regenTimeChicken -= 1
    if regenTimeChicken == 0:
        chicken.append( Animation("GameProject\\chicken.png", 3, game, 227/3, 65, 15 ) )
        c = chicken[len(chicken)-1]
        c.resizeBy(-50)
        x = randint(50,550)
        y = randint(50,450)
        c.moveTo(x,y)
        regenTimeChicken = -1
    
    

    for f in fries:
        f.draw()
        if f.collidedWith(ant) or f.collidedWith(human):
            regenTimeFries = 150
        if f.collidedWith(ant):
            bite.play()
            f.visible = False 
            antscore += 10
        if f.collidedWith(human):
            bite.play()
            f.visible = False 
            humanscore += 10


    if regenTimeFries >= 0:
        regenTimeFries -= 1
    if regenTimeFries == 0:
        fries.append( Animation("GameProject\\frenchfry.gif", 2, game, 400/2, 200, 15 ) ) 
        f = fries[len(fries)-1]
        f.resizeBy(-80)
        x = randint(50,550)
        y = randint(50,450)
        f.moveTo(x,y)
        regenTimeFries = -1

    
    for s in sandwiches:
        s.draw()
        if s.collidedWith(ant) or s.collidedWith(human):
            regenTimeSandwich = 150
        if s.collidedWith(ant):
            bite.play()
            s.visible = False 
            antscore += 10
        if s.collidedWith(human):
            bite.play()
            s.visible = False 
            humanscore += 10


    if regenTimeSandwich >= 0:
        regenTimeSandwich -= 1
    if regenTimeSandwich == 0:
        sandwiches.append( Animation("GameProject\\sandwiches.png", 8, game, 296/4, 147/2, 15 ) )
        s = sandwiches[len(sandwiches)-1]
        s.resizeBy(-50)
        x = randint(50,550)
        y = randint(50,450)
        s.moveTo(x,y)
        regenTimeSandwich = -1

    
    for e in etc:
        e.draw()
        if e.collidedWith(ant) or e.collidedWith(human):
            regenTimeEtc = 150
        if e.collidedWith(ant):
            bite.play()
            e.visible = False 
            antscore += 10
        if e.collidedWith(human):
            bite.play()
            e.visible = False 
            humanscore += 10


    if regenTimeEtc >= 0:
        regenTimeEtc -= 1
    if regenTimeEtc == 0:
        etc.append( Animation("GameProject\\etc.png", 4, game, 600/3, 400/2, 15 ) )
        e = etc[len(etc)-1]
        e.resizeBy(-80)
        x = randint(50,550)
        y = randint(50,450)
        e.moveTo(x,y)
        regenTimeEtc = -1

    for d in donuts:
        d.draw()
        if d.collidedWith(ant) or d.collidedWith(human):
            regenTimeDonuts = 150
        if d.collidedWith(ant):
            bite.play()
            d.visible = False 
            antscore += 10
        if d.collidedWith(human):
            bite.play()
            d.visible = False 
            humanscore += 10


    if regenTimeDonuts >= 0:
        regenTimeDonuts -= 1
    if regenTimeDonuts == 0:
        donuts.append( Animation("GameProject\\donuts.png", 8, game, 287/4, 145/2, 15) )
        d = donuts[len(donuts)-1]
        d.resizeBy(-50)
        x = randint(50,550)
        y = randint(50,450)
        d.moveTo(x,y)
        regenTimeDonuts = -1

   

    
    if keys.Pressed[K_UP]:
        awalk.play()
        ant.rotateTo(360)
        ant.y -= 4

    if keys.Pressed[K_DOWN]:
        awalk.play()
        ant.rotateTo(180)
        ant.y += 4

    if keys.Pressed[K_LEFT]:
        awalk.play()
        ant.rotateTo(90)
        ant.x -= 4

    if keys.Pressed[K_RIGHT]:
        awalk.play()
        ant.rotateTo(270)
        ant.x += 4

    if keys.Pressed[K_w]:
        hwalk.play()
        human.y -= 4

    if keys.Pressed[K_s]:
        hwalk.play()
        human.y += 4

    if keys.Pressed[K_a]:
        hwalk.play()
        human.x -= 4

    if keys.Pressed[K_d]:
        hwalk.play()
        human.x += 4


    if ant.collidedWith (rock1) or ant.collidedWith (rock2) or ant.collidedWith (rock3) or ant.collidedWith (rock4) or ant.collidedWith (rock5) or ant.collidedWith (rock6) or ant.collidedWith (rock7) or ant.collidedWith (rock8) or ant.collidedWith (rock9) or ant.collidedWith (rock10):
        antscore -= 1

    if human.collidedWith (rock1) or human.collidedWith (rock2) or human.collidedWith (rock3) or human.collidedWith (rock4) or human.collidedWith (rock5) or human.collidedWith (rock6) or human.collidedWith (rock7) or human.collidedWith (rock8) or human.collidedWith (rock9) or human.collidedWith (rock10):
        humanscore -= 1

    

    if game.time <1:
        game.over = True

    
    game.drawText("Ant: " + str(antscore), 100, 0)
    game.drawText("Human: " + str(humanscore), 200, 0)
    game.displayTime()
    game.update(30)




game.over= False
while not game.over:
    game.processInput()
    bk3 = Image("GameProject\\youwin.png", game)
    game.setBackground(bk3)
    bk3.resizeTo(game.width, game.height)
    game.drawBackground()


    
    if keys.Pressed[K_w]:
        hwalk.play()
        human.y -= 4

    if keys.Pressed[K_s]:
        hwalk.play()
        human.y += 4

    if keys.Pressed[K_a]:
        hwalk.play()
        human.x -= 4

    if keys.Pressed[K_d]:
        hwalk.play()
        human.x += 4

    if keys.Pressed[K_UP]:
        awalk.play()
        ant.rotateTo(360)
        ant.y -= 4

    if keys.Pressed[K_DOWN]:
        awalk.play()
        ant.rotateTo(180)
        ant.y += 4

    if keys.Pressed[K_LEFT]:
        awalk.play()
        ant.rotateTo(90)
        ant.x -= 4

    if keys.Pressed[K_RIGHT]:
        awalk.play
        ant.rotateTo(270)
        ant.x += 4

    if humanscore > antscore:
        human.move()
        trophy.draw()
        if human.collidedWith (trophy):
            trophy.visible = False
            game.over = True

    if antscore > humanscore:
        ant.move()
        trophy.draw()
        if ant.collidedWith (trophy):
            trophy.visible = False
            game.over = True
    game.update(30)


game.update()
game.quit()
