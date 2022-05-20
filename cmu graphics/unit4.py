from cmu_graphics import *

#the objective of this game is to avoid the falling blocks, but they only move down when a key is pressed

#needed for random block positions
import random as r

#background
app.background = 'skyBlue'

#ground
ground = Rect(0, 350, 400, 50, fill='green')

#blocks to avoid (given random x values)
block1 = Rect(r.randint(0, 400), 10, 20, 20, fill='red', border='crimson', align='center')
block2 = Rect(r.randint(0, 400), 10, 20, 20, fill='red', border='crimson', align='center')
block3 = Rect(r.randint(0, 400), 10, 20, 20, fill='red', border='crimson', align='center')
block4 = Rect(r.randint(0, 400), 10, 20, 20, fill='red', border='crimson', align='center')
block5 = Rect(r.randint(0, 400), 10, 20, 20, fill='red', border='crimson', align='center')
block6 = Rect(r.randint(0, 400), 10, 20, 20, fill='red', border='crimson', align='center')

#player to control
player = Rect(200, 340, 20, 20, fill='lightSteelBlue', border='steelBlue', align='center')

#score counter
score = Label(0, 25, 375)

#helper function to update block positions
def updateBlocks(moveAmount):
    #make the blocks move more with more points
    moveAmount += 20
    block1.centerY += moveAmount
    block2.centerY += moveAmount
    block3.centerY += moveAmount
    block4.centerY += moveAmount
    block5.centerY += moveAmount
    block6.centerY += moveAmount
    
    #check to see if they are touching the ground and move them to top with new x if they are
    #also gives the player a point
    if(block1.hitsShape(ground)):
        block1.centerX = r.randint(0,400)
        block1.centerY = 10
        score.value += 1
    if(block2.hitsShape(ground)):
        block2.centerX = r.randint(0,400)
        block2.centerY = 10
        score.value += 1
    if(block3.hitsShape(ground)):
        block3.centerX = r.randint(0,400)
        block3.centerY = 10
        score.value += 1
    if(block4.hitsShape(ground)):
        block4.centerX = r.randint(0,400)
        block4.centerY = 10
        score.value += 1
    if(block5.hitsShape(ground)):
        block5.centerX = r.randint(0,400)
        block5.centerY = 10
        score.value += 1
    if(block6.hitsShape(ground)):
        block6.centerX = r.randint(0,400)
        block6.centerY = 10
        score.value += 1
        
    #checks to see if block hits player and ends game if yes
    if(block1.hitsShape(player)):
        app.stop()
    if(block2.hitsShape(player)):
        app.stop()
    if(block3.hitsShape(player)):
        app.stop()
    if(block4.hitsShape(player)):
        app.stop()
    if(block5.hitsShape(player)):
        app.stop()
    if(block6.hitsShape(player)):
        app.stop()

#move the character and blocks
def onKeyPress(key):
    #modifier for how fast the blocks will fall on this key press, exponentially increases
    pace = (score.value/10)
    if(key == 'left'):
        player.centerX -= 10
        updateBlocks(pace)
    elif(key == 'right'):
        player.centerX += 10
        updateBlocks(pace)
    elif(key == 'down'):
        updateBlocks(pace)

cmu_graphics.run()