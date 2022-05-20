from cmu_graphics import *

#space background
app.background = 'midnightBlue'

#group of ships
ships = Group()

#create background stars
for x in range(25, 401, 50):
    for y in range(25, 401, 50):
        temp = Star(x + randrange(-25, 26), y + randrange(-10, 11), 10, 5, roundness = 40, fill = 'white')
        temp.toBack()

#manage amount of ships
app.ships = 5

#label to show ship count
countLabel = Label(app.ships, 25, 25, font = 'arial', bold = True, fill = 'crimson', size = 30)

#planet ships orbit
planet = Group(
    #main body
    Circle(200, 200, 65, fill = gradient('gray', 'gray', 'darkSlateGray')),
    
    #craters
    Circle(randrange(170,231), randrange(170,231), randrange(5, 26), fill = gradient('darkGray', 'dimGray')),
    Circle(randrange(170,231), randrange(170,231), randrange(5, 26), fill = gradient('darkGray', 'dimGray')),
    Circle(randrange(170,231), randrange(170,231), randrange(5, 26), fill = gradient('darkGray', 'dimGray')),
    Circle(randrange(170,231), randrange(170,231), randrange(5, 26), fill = gradient('darkGray', 'dimGray')),
    Circle(randrange(170,231), randrange(170,231), randrange(5, 26), fill = gradient('darkGray', 'dimGray'))
    )

#draws a ship    
def drawShip():
    ship = Group(
        Arc(200, 100, 10, 10, 0, 180, fill = 'red'),
        Rect(190, 95, 10, 10, fill = 'red')
        )
    ship.centerX, ship.centerY = getPointInDir(200, 200, randrange(0, 360), randrange(75, 106))
    ship.rotateAngle = angleTo(200, 200, ship.centerX, ship.centerY)
    ship.speed = randrange(2, 6)
    ships.add(ship)

#helper function to update ship count and redraw the group
def updateShipCount():
    ships.clear()
    countLabel.value = app.ships
    for x in range(app.ships):
        drawShip()

#change the number of ships when arrows are pressed
def onKeyPress(key):
    if(key == 'up'):
        app.ships += 1
    elif(key == 'down'):
        app.ships -= 1
    updateShipCount()
    
#rotate the ships around the planet and have them move slightly in and out
def updateShips():
    for ship in ships:
        distToCenter = distance(200, 200, ship.centerX, ship.centerY)
        angle = angleTo(200, 200, ship.centerX, ship.centerY)
        distToCenter += randrange(-2, 3)
        if(distToCenter < 70):
            distToCenter = 70
        angle += ship.speed
        ship.centerX, ship.centerY = getPointInDir(200, 200, angle, distToCenter)
        ship.rotateAngle = angle
    
def onStep():
    updateShips()
    
updateShipCount()

cmu_graphics.run()