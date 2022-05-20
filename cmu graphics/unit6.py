from cmu_graphics import *

 #import random for random obstacle positions
import random as r

#sky
app.background = 'dodgerBlue'

#game state
app.gameState = 'start'

#ground and score group
ground = Rect(0, 350, 400, 50, fill = 'forestGreen')
score = Label(0, 50, 375, font = 'arial', fill = 'white')
scoreText = Label('Score:', 50, 360, font = 'arial', fill = 'white')
hiScore = Label(0, 350, 375, font = 'arial', fill = 'white')
hiScoreText = Label('High Score:', 350, 360, font = 'arial', fill = 'white')

ui = Group(
    ground,
    score,
    scoreText,
    hiScore,
    hiScoreText
    )

#group of 5 obstacles of varying x, attempted to be snapped to the grid
block1 = Rect((50 + (r.randint(0, 3)*100)), -40, 80, 80, align = 'center', fill = 'red', border = 'crimson')
block2 = Rect((50 + (r.randint(0, 3)*100)), -160, 80, 80, align = 'center', fill = 'red', border = 'crimson')
block3 = Rect((50 + (r.randint(0, 3)*100)), -280, 80, 80, align = 'center', fill = 'red', border = 'crimson')

obstacles = Group(
    block1,
    block2,
    block3
    )
#set custom variable for speed
obstacles.speed = 3 + (int(score.value / 250))

#intro screen
introBox = Rect(200, 200, 225, 100, fill = 'lemonChiffon', border = 'moccasin', align = 'center')
introText1 = Label('Move purple with arrow keys!', 200, 185, font = 'arial', fill = 'black')
introText2 = Label('Yellow mirrors movement!', 200, 200, font = 'arial', fill = 'black')
introText3 = Label('Press space to start!', 200, 215, font = 'arial', fill = 'black')

intro = Group(
    introBox,
    introText1,
    introText2,
    introText3
    )
    
#end screen
endBox = Rect(200, 200, 225, 100, fill = 'lemonChiffon', border = 'moccasin', align = 'center')
endText = Label('Press r to restart!', 200, 200, font = 'arial', fill = 'black')

end = Group(
    endBox,
    endText
    )
    
#move ending box above screen to hide it
end.centerY = -200

#player is 2 circles that move opposite each other
player1 = Circle(200, 340, 10, fill = 'magenta', border = 'fuchsia')
player2 = Circle(200, 340, 10, fill = 'yellow', border = 'gold')

player = Group(
    player1,
    player2
    )

#move purple to front
player1.toFront()

#move players on key press and manage restarting 
def onKeyHold(keys):
    #allow different actions based on game state
    if(app.gameState == 'start'):
        if('space' in keys):
            app.gameState = 'playing'
            intro.centerY = -200
    elif(app.gameState == 'playing'):
        if('left' in keys):
            player1.centerX -= 5
            player2.centerX += 5
        elif('right' in keys):
            player1.centerX += 5
            player2.centerX -= 5
    elif(app.gameState == 'end'):
        if('r' in keys):
            app.gameState = 'playing'
            end.centerY = -200
            if(score.value > hiScore.value):
                hiScore.value = score.value
            score.value = 0

#move obstacles
def moveObstacles():
    #reset obstacles if they go below the screen
    if(obstacles.top > 400):
        obstacles.bottom = 0
        block1.centerX = (40 + (r.randint(0, 4)*80))
        block2.centerX = (40 + (r.randint(0, 4)*80))
        block3.centerX = (40 + (r.randint(0, 4)*80))
    #otherwise move the boxes down
    else:
        obstacles.centerY += obstacles.speed
    

#manage obstacles on step
def onStep():
    if(app.gameState == 'playing'):
        if(obstacles.hitsShape(player)):
            app.gameState = 'end'
            end.centerY = 200
            obstacles.centerY = -200
        else:
            moveObstacles()
            score.value += 1

cmu_graphics.run()