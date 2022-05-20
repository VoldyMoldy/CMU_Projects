from cmu_graphics import *

#import random
import random as r

#manage game speed and if it has been one second
app.stepsPerSecond = 30
second = Label(0, -50, -50)

#background
app.background = 'skyBlue'

#player
pacman1 = Arc(200, 200, 50, 50, 120, 300, fill = 'yellow')
pacman2 = Arc(200, 200, 50, 50, 120, 300, fill = 'green')
player = Group(
    pacman1,
    pacman2
    )

#score counter
timer = Label(20, 25, 25, fill = 'white', bold = True)

#pellets to eat
pellets = Group()
for x in range(12):
    pellet = Circle(r.randint(50, 350), r.randint(50, 350), 10, fill = 'white')
    pellet.dx = r.randint(-x, x)
    pellet.dy = r.randint(-x, x)
    pellets.add(pellet)

#manage pellets bouncing on a screen edge
def bouncePellets():
    for x in pellets.children:
        if(x.left < 0 or x.right > 400):
            x.dx *= -1
        if(x.top < 0 or x.bottom > 400):
            x.dy *= -1

#move the pellets
def movePellets():
    #amount of pellets left
    app.pellets = 0
    #check for pellets, if none end game
    for x in pellets.children:
        app.pellets += 1
    if(app.pellets == 0):
        app.stop()
    else:
        for x in pellets.children:
            x.centerX += x.dx
            x.centerY += x.dy
            if(x.hitsShape(player)):
                pellets.remove(x)
                app.pellets -= 1
        bouncePellets()
        
def onStep():
    movePellets()
    second.value += 1
    if(second.value >= 30):
        timer.value -= 1
        second.value = 0
    if(timer.value == 0):
        app.stop()
    
def onKeyHold(keys):
    if('left' in keys):
        pacman1.centerX -= 3
        pacman1.rotateAngle = 180
        pacman2.centerX += 3
        pacman2.rotateAngle = 0
    if('right' in keys):
        pacman1.centerX += 3
        pacman1.rotateAngle = 0
        pacman2.centerX -= 3
        pacman2.rotateAngle = 180
    if('up' in keys):
        pacman1.centerY -= 3
        pacman1.rotateAngle = 270
        pacman2.centerY += 3
        pacman2.rotateAngle = 90
    if('down' in keys):
        pacman1.centerY += 3
        pacman1.rotateAngle = 90
        pacman2.centerY -= 3
        pacman2.rotateAngle = 270

cmu_graphics.run()