from cmu_graphics import *

#import random to reposition grass randomly
import random as r

#set app background
app.background = 'limeGreen'

#create grass
grass1 = Polygon(125, 25, 150, 50, 175, 0, 200, 50, 225, 25, 212.5, 75, 137.5, 75, fill='green')
grass2 = Polygon(0, 25, 25, 50, 50, 0, 75, 50, 100, 25, 87.5, 75, 12.5, 75, fill='green')
grass3 = Polygon(275, 25, 300, 50, 325, 0, 350, 50, 375, 25, 362.5, 75, 287.5, 75, fill='green')

#create the ball
ball = Circle(200, 200, 50, fill=gradient('white', 'red', 'red', start='left-top'))

#helper function to move all the grass when the ball rolls to give the illusion of the ball moving
def moveGrass():
    
    #move all grass over 1 unit
    grass1.centerX -= 5
    grass2.centerX -= 5
    grass3.centerX -= 5
    
    randomGrass()
    
#helper function for a helper function
#its helper function-ception
def randomGrass():
    #move grass to the right and adjust its height randomly
    if(grass1.centerX < -100):
        grass1.centerX = 500
        grass1.centerY = r.randint(25, 375)
    if(grass2.centerX < -100):
        grass2.centerX = 500
        grass2.centerY = r.randint(25, 375)
    if(grass3.centerX < -100):
        grass3.centerX = 500
        grass3.centerY = r.randint(25, 375)
    
#'roll' the mall on mouse move
def onMouseMove(mouseX, mouseY):
    ball.rotateAngle += 5
    moveGrass()
    
#move the ball to the mouse on drag
def onMouseDrag(mouseX, mouseY):
    ball.centerX = mouseX
    ball.centerY = mouseY

cmu_graphics.run()