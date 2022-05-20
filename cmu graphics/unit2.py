from cmu_graphics import *

# Background
app.background = 'skyBlue'

#button panel
Rect(0, 300, 400, 100, fill='grey')

#button
button = Oval(200, 350, 40, 30, fill='red', border='crimson')

#block being hit by hammer
def drawBlock(centerX, centerY):
    #background
    Rect(centerX, centerY, 100, 100, fill='maroon', align='center')
    #bricks
    Rect(centerX, centerY-30, 110, 60, fill='brown', align='center')
    Rect(centerX-30, centerY+40, 50, 60, fill='brown', align='center')
    Rect(centerX+30, centerY+40, 50, 60, fill='brown', align='center')
    
#coin
coinOutline = Oval(200, 75, 80, 100, fill='yellow', visible=False)
coinIn = Rect(200, 75, 20, 60, fill='gold', align='center', visible=False)

#hammer
hammerHandle = Rect(50, 200, 20, 80, align='center', fill='brown')
hammerHead = Rect(50, 170, 50, 20, align='center', fill='gainsboro')

#counter
count = 0
clicks = Label(count, 50, 350, fill='black', font='arial', size=25)

#set up brick
brick = drawBlock(200, 200)

#change image on mouse click and increment count
def onMousePress(mouseX, mouseY):
    hammerHandle.left+=75
    hammerHead.left+=75
    coinIn.visible=True
    coinOutline.visible=True
    button.fill='darkRed'
    clicks.value+=1
    
#revert image on mouse release
def onMouseRelease(mouseX, mouseY):
    hammerHandle.left-=75
    hammerHead.left-=75
    coinIn.visible=False
    coinOutline.visible=False
    button.fill='red'

cmu_graphics.run()