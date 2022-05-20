from cmu_graphics import *

#allow for random positions
import random as r

#space background
app.background = gradient('midnightBlue', 'darkSlateGrey', start = 'top')

#darken the background
Rect(0, 0, 400, 400, fill = 'black', opacity = 50)

#create stars in random positions
for x in range(10):
    Circle(r.randint(10, 390), r.randint(10, 390), 5, fill = 'white')

#glow behind player
glow = Circle(200, 200, 20, fill = 'white', opacity = 50)
glowGrow = True

#create player
player = Star(200, 200, 20, 5, fill = gradient('lightYellow', 'yellow'))

#score
score = Label(0, 375, 375, font = 'arial', fill = 'white', size = 15, bold = True)

#meteors to avoid (created offscreen to immediately give them new positions)
meteor1 = Circle(-50, r.randint(10, 390), 50, fill = 'saddleBrown', border = 'sienna')
meteor2 = Circle(-50, r.randint(10, 390), 50, fill = 'saddleBrown', border = 'sienna')
meteor3 = Circle(-50, r.randint(10, 390), 50, fill = 'saddleBrown', border = 'sienna')
meteor4 = Circle(r.randint(10, 390), -50, 50, fill = 'saddleBrown', border = 'sienna')
meteor5 = Circle(r.randint(10, 390), -50, 50, fill = 'saddleBrown', border = 'sienna')
meteor6 = Circle(r.randint(10, 390), -50, 50, fill = 'saddleBrown', border = 'sienna')

#update the glow's position
def updateGlow():
    glow.centerX = player.centerX
    glow.centerY = player.centerY
    
#reset meteor positions
def resetMeteors():
    meteor1.right = 0
    meteor2.right = 0
    meteor3.right = 0
    meteor4.bottom = 0
    meteor5.bottom = 0
    meteor6.bottom = 0
    
    meteor1.centerY = r.randint(10, 390)
    meteor2.centerY = r.randint(10, 390)
    meteor3.centerY = r.randint(10, 390)
    meteor4.centerX = r.randint(10, 390)
    meteor5.centerX = r.randint(10, 390)
    meteor6.centerX = r.randint(10, 390)
    
#check and do wraparound
def playerWrap():
    if(player.left > 400):
        player.right = 0
    elif(player.right < 0):
        player.left = 400
    if(player.bottom < 0):
        player.top = 400
    elif(player.top > 400):
        player.bottom = 0
    
#move the meteors, 3 going right and 3 going down
def updateMeteors():
    #meteor movement speed increases throughout the game
    speed = 3 + int(score.value / 250)
    
    #give points based on speed
    score.value += 1 + int(((speed - 3) / 2))
    
    #move the meteors
    meteor1.centerX += speed
    meteor2.centerX += speed
    meteor3.centerX += speed
    meteor4.centerY += speed
    meteor5.centerY += speed
    meteor6.centerY += speed
    
    #only check one meteor before reset since all move equally
    if(meteor1.left > 400):
        resetMeteors()
    

#control player
def onKeyHold(keys):
    #player speed to increase throughout the game
    playerSpeed = 3 + int(score.value / 250)
    
    #prevent opposite directions from being held, otherwise move
    if(not (('left' in keys) and ('right' in keys))):
        if('left' in keys):
            player.centerX -= playerSpeed
        elif('right' in keys):
            player.centerX += playerSpeed
    if(not (('up' in keys) and ('down' in keys))):
        if('up' in keys):
            player.centerY -= playerSpeed
        elif('down' in keys):
            player.centerY += playerSpeed
    
    #update player, glow, and try to wrap around the screen
    updateGlow()
    player.rotateAngle += 5
    playerWrap()
    
    #move the meteors
    updateMeteors()
    
    #check to see if touching a meteor and end game if true
    if(player.hitsShape(meteor1) or player.hitsShape(meteor2) or player.hitsShape(meteor3) or 
       player.hitsShape(meteor4) or player.hitsShape(meteor5) or player.hitsShape(meteor6)):
           app.stop()

cmu_graphics.run()