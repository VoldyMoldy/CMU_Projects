from cmu_graphics import *

#background
app.background = 'skyBlue'

#bubble gun
bubbleGun = Group(
    Polygon(240, 200, 280, 160, 280, 240, fill = 'darkGray'),
    Rect(200, 200, 100, 50, align = 'center', fill = 'gray')
    )
#reposition the bubble gun
bubbleGun.centerX = 25
bubbleGun.centerY = 375
bubbleGun.rotateAngle = -45

#accept user string
userString = app.getTextInput('Input the message you want to catch')

#bubble labels
speedLabel = Label('Bubble speed: 3', 200, 340, font = 'arial', fill = 'white')
angleLabel = Label('Bubble angle: 45', 200, 355, font = 'arial', fill = 'white')
spreadLabel = Label('Bubble spread: 20', 200, 370, font = 'arial', fill = 'white')
countLabel = Label('Bubble count: 3', 200, 385, font = 'arial', fill = 'white')

#bubble group
bubbles = Group()

#letter group
letters = Group()

#using labels for globals
speed = Label(3, -25, -25)
angle = Label(45, -25, -25)
spread = Label(20, -25, -25)

#change bubble gun properties
def changeBlaster():
    newSpeed = app.getTextInput('Input bubble speed')
    newAngle = app.getTextInput('Input blaster angle')
    newSpreadAngle = app.getTextInput('Input blaster spread angle')
    newBubbleCount = app.getTextInput('Input bubble count')
    speedLabel.value = 'Bubble speed: ' + newSpeed
    angleLabel.value = 'Bubble angle: ' + newAngle
    spreadLabel.value = 'Bubble spread: ' + newSpreadAngle
    countLabel.value = 'Bubble count: ' + newBubbleCount

#gets count because i cant use globals :(
def getCount():
    count = ''
    for l in countLabel.value:
        if(l.isdigit()):
            count += l
    return int(count)
    
#update bubble variables
def updateBubbleNums():
    #vars used to update values
    newspeed = ''
    newangle = ''
    newspread = ''
    #update values using label values
    for l in speedLabel.value:
        if(l.isdigit()):
            newspeed += l
    for l in angleLabel.value:
        if(l.isdigit()):
            newangle += l
    for l in spreadLabel.value:
        if(l.isdigit()):
            newspread += l
    #convert to int
    speed.value = newspeed
    angle.value = newangle
    spread.value = newspread
    
#fire the bubbles
def fireBubbles():
    #count doubled for some reason, half it with integer division
    count = getCount() // 2
    for x in range(count):
        bubble = Circle(bubbleGun.centerX, bubbleGun.centerY, 25, fill = gradient('white', 'blue', 'blue', start = 'left-top'), rotateAngle = (angle.value + randrange((spread.value * -1), spread.value + 1)))
        bubbles.add(bubble)
        
#rain letters from input string (all caps)
def rainLetters():
    for l in userString.upper():
        letters.add(Label(l, randrange(50, 351), randrange(-50, 0), fill = 'black', font = 'arial'))

#check letter collision and disappear if touching a bubble
def letterCollision():
    for l in letters:
        if(l.hitsShape(bubbles) or l.centerY > 400):
            letters.remove(l)
        else:
            l.centerY += 5
    #check if all letters are gone and if so refresh the letters
    lettercount = 0
    for l in letters:
        lettercount += 1
    if(lettercount == 0):
        rainLetters()
        
#update bubble positions
def updateBubbles(bubblespeed):
    #replace bubble values
    for bubble in bubbles:
        #try to get newx and newy based on angle
        newx, newy = getPointInDir(bubble.centerX, bubble.centerY, bubble.rotateAngle, bubblespeed)
        bubble.centerX = newx
        bubble.centerY = newy
        if(bubble.centerX > 400 or bubble.centerX < 0 or bubble.centerY > 400 or bubble.centerY < 0):
            bubbles.remove(bubble)
        
#set bubble limit
def limitBubbles():
    num = 0
    for i in bubbles:
        num += 1
        if(num > 100):
            bubbles.remove(i)
        
#controls
def onKeyHold(keys):
    if('space' in keys):
        changeBlaster()
    elif('n' in keys):
        fireBubbles()
        limitBubbles()
        
#start the letters
rainLetters()

#manage letters and bubbles
def onStep():
    letterCollision()
    updateBubbles(speed.value)
        
cmu_graphics.run()