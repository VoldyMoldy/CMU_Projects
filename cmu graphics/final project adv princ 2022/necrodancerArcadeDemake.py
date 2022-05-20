#Based on the game: Crypt of the Necrodancer
#uses a grid-based system of movement
#you play as Melody with the golden lute which attacks evey cardinal tile around you on move
#stay alive for as many beats as possible
#enemies spawn on edge every 4 measures

#monster ai:
#bat - blue moves in a random direction every 2nd beat red moves every beat and will attack player if next to them
#skeleton - moves towards player every second beat, favors vertical alignment
#dragon - moves every other beat towards player, favors horizontal alignment

from cmu_graphics import *

#background
Rect(0, 0, 400, 400, fill = 'darkSlateBlue')

#disco board
for x in range(9):
    for y in range(9):
        if((x + y) % 2 == 0):
            color = 'slateBlue'
            edge = 'mediumSlateBlue'
        else:
            color = 'purple'
            edge = 'darkMagenta'
        Rect(50 + (x*(34 - (4/9))), 50 + (y*(34 - (4/9))), 34 - (4/9), 34 - (4/9), fill = color, border = edge)

#bpm: 123
app.stepsPerSecond = 123
app.count = 0
#check if close enought to beat to move
app.canMove = False

#game setup
level = makeList(9, 9)
song = Sound('https://vgmsite.com/soundtracks/crypt-of-the-necrodancer/cwvewilp/18%20-%20Knight%20to%20C-Sharp%20%28Deep%20Blues%29.mp3')
hurtSound = Sound('https://archive.org/download/necrodancer_sfx/en_general_hit.mp3')
attackSound = Sound('https://archive.org/download/necrodancer_sfx/en_general_death.mp3')
metronomeTick = Sound('https://archive.org/download/necrodancer_sfx/TEMP_tick.mp3')
app.makeMetronome = False

#player
player = Image('https://www.spriters-resource.com/resources/sheet_icons/78/81345.png', 185, 185)
player.width = 34 - (4/9)
player.height = 34 - (4/9)
player.hp = 6
player.x = 4
player.y = 4
level[4][4] = player

#score label
score = Label(0, 25, 25, fill = 'white', bold = True)

#hp label
health = Label('Health: ' + str(player.hp), 350, 25, fill = 'white', bold = True)

#make a position for enemy to fill on spawn
def getOpenEdge():
    #check all edges for None
    open = []
    
    for x in range(len(level)):
        for y in range(len(level[x])):
            if(x == 0 or y == 0):
                if(level[x][y] == None):
                    open.append([x, y])
    return open

#hurt player
def hugrtPlayer(dmg):
    player.hp -= dmg
    hurtSound.play(restart = True)

#make bats and ai
def makeBlueBat():
    spaces = getOpenEdge()
    if(len(spaces) > 0):
        index = randrange(0, len())
        x = open[index][0]
        y = open[index][1]
        
        #make the bat with 1hp
        bat = Image('http://clipart-library.com/img1/1421622.png', x*(34 - (4/9)), y*(34 - (4/9)))
        bat.x = x
        bat.y = y
        
        #place bat
        level[x][y] = bat
        
def makeRedBat():
    spaces = getOpenEdge()
    if(len(spaces) > 0):
        index = randrange(0, len())
        x = open[index][0]
        y = open[index][1]
        
        #make red bat
        bat = Image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTB496fv3QMEHLlBQJ8lBTQqqCWYdw3o7ubNwY-mdRFcArSBwfO&s', x*(34 - (4/9)), y*(34 - (4/9)))
        bat.x = x
        bat.y = y
        
        #place bat
        level[x][y] = bat
        
def batAI(bat):
    choices = []
    if(bat == 'blueBat'):
        if(app.count % 120 == 0):
            #check nearby tiles and radomly pick from those with None or player
            if(level[bat.x - 1][bat.y] == None or level[bat.x - 1][bat.y] == player):
                choices.append([bat.x - 1, bat.y])
            if(level[bat.x + 1][bat.y] == None or level[bat.x + 1][bat.y] == player):
                choices.append([bat.x + 1, bat.y])
            if(level[bat.x][bat.y - 1] == None or level[bat.x][bat.y - 1] == player):
                choices.append([bat.x, bat.y - 1])
            if(level[bat.x - 1][bat.y] == None or level[bat.x][bat.y + 1] == player):
                choices.append([bat.x - 1, bat.y])
            if(len(choices) > 0):
                #randomly pick avalible tile, attack or update vars and delete old bat
                index = randrange(0, len(choices))
                x = choices[index][0]
                y = choices[index][1]
                if(level[x][y] == player):
                    hurtPlayer(1)
                else:
                    level[bat.x][bat.y] = None
                    bat.x = x
                    bat.y = y
                    level[x][y] = bat
        bat.centerX = 67 + player.x*(34 - (4/9))
        bat.centerY = 67 + player.y*(34 - (4/9))
    else:
        #if player is within one cardinal tile try to attack them
        if((abs(bat.x - player.x) == 1)^(abs(bat.y - player.y) == 1)):
            hurtPlayer(2)
        else:
            #random move otherwise
            if(level[bat.x - 1][bat.y] == None):
                choices.append([bat.x - 1, bat.y])
            if(level[bat.x - 1][bat.y] == None):
                choices.append([bat.x - 1, bat.y])
            if(level[bat.x - 1][bat.y] == None):
                choices.append([bat.x - 1, bat.y])
            if(level[bat.x - 1][bat.y] == None):
                choices.append([bat.x - 1, bat.y])
            if(len(choices) > 0):
                index = randrange(0, len(choices))
                x = choices[index][0]
                y = choices[index][1]
                level[bat.x][bat.y] = None
                bat.x = x
                bat.y = y
                level[x][y] = bat
                bat.centerX = 67 + player.x*(34 - (4/9))
                bat.centerY = 67 + player.y*(34 - (4/9))        
                
#skeleton and ai
def makeSkeleton():
    spaces = getOpenEdge()
    if(len(spaces) > 0):
        index = randrange(0, len(spaces))
        x = spaces[index][0]
        y = spaces[index][0]
        
        #make skeleton
        skeleton = Image('http://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/ddada31b1def25c.png', x*(34 - (4/9)), y*(34 - (4/9)))
        skeleton.x = x
        skeleton.y = y
        
        #place skeleton
        level[x][y] = skeleton
        
def skeletonAI(skeleton):
    choices = []
    if(app.count % 120 == 0):
        #if player is within one cardinal tile try to attack them
        if((abs(skeleton.x - player.x) == 1)^(abs(skeleton.y - player.y) == 1)):
            hurtPlayer(1)
        else:
            #check for target x and y and move with y favored
            if(skeleton.y > player.y):
                x = skeleton.x
                y = skeleton.y - 1
                if(level[x][y] == None):
                    level[skeleton.x][skeleton.y] = None
                    skeleton.x = x
                    skeleton.y = y
                    level[x][y] = skeleton
            elif(skeleton.y < player.y):
                x = skeleton.x
                y = skeleton.y + 1
                if(level[x][y] == None):
                    level[skeleton.x][skeleton.y] = None
                    skeleton.x = x
                    skeleton.y = y
                    level[x][y] = skeleton
            elif(skeleton.x > player.x):
                x = skeleton.x - 1
                y = skeleton.y
                if(level[x][y] == None):
                    level[skeleton.x][skeleton.y] = None
                    skeleton.x = x
                    skeleton.y = y
                    level[x][y] = skeleton
            elif(skeleton.x < player.x):
                x = skeleton.x + 1
                y = skeleton.y
                if(level[x][y] == None):
                    level[skeleton.x][skeleton.y] = None
                    skeleton.x = x
                    skeleton.y = y
                    level[x][y] = skeleton
            skeleton.centerX = 67 + player.x*(34 - (4/9))
            skeleton.centerY = 67 + player.y*(34 - (4/9))
        
#controls
def onKeyHold(keys):
    if(app.canMove):
        if('up' in keys):
            if(player.y > 0 and level[player.x][player.y - 1] == None):
                level[player.x][player.y] = None
                player.y -= 1
                level[player.x][player.y] = player
            app.canMove = False
        elif('down' in keys):
            if(player.y < 8 and level[player.x][player.y + 1] == None):
                level[player.x][player.y] = None
                player.y += 1
                level[player.x][player.y] = player
            app.canMove = False
        elif('left' in keys):
            if(player.x > 0 and level[player.x - 1][player.y] == None):
                level[player.x][player.y] = None
                player.x -= 1
                level[player.x][player.y] = player
            app.canMove = False
        elif('right' in keys):
            if(player.x < 8 and level[player.x + 1][player.y - 1] == None):
                level[player.x][player.y] = None
                player.x += 1
                level[player.x][player.y] = player
            app.canMove = False
        player.centerX = 67 + player.x*(34 - (4/9))
        player.centerY = 67 + player.y*(34 - (4/9))
    if('m' in keys):
        if(app.makeMetronome):
            app.makeMetronome = False
        else:
            app.makeMetronome = True
            
#run the ai of every monster on the board
def tickAI():
    for x in range(len(level)):
        for y in range(len(level[x])):
            if(level[x][y] != None):
                monster = level[x][y]
                if(monster == 'blueBat'or monster == 'redBat'):
                    batAI(monster)
                else:
                    skeletonAI(monster)
            
#spawn a wave of monsters
def spawnMonsters():
    for x in range(2, randrange(3, 5)):
        makeBlueBat()
    makeRedBat()
    for x in range(2, randrange(3, 5)):
        makeSkeleton()

#attack monsters around player on move
def checkAttacks(x, y):
    if(level[x - 1][y] != None):
        level[x - 1][y] = None
    if(level[x + 1][y] != None):
        level[x + 1][y] = None
    if(level[x][y - 1] != None):
        level[x][y - 1] = None
    if(level[x][y + 1] != None):
        level[x][y + 1] = None

def onStep():
    #toggle move once at start of hit window
    if(app.count % 60 == 50):
        app.canMove = True
    elif(app.count % 60 == 0):
        tickAI()
        metronomeTick.play()
        score.value += 1
    elif(app.canMove and app.count % 60 == 10):
        app.canMove = False
    #create a new wave of enemies every 4 waves
    if(app.count % 480 == 0):
        spawnMonsters()
    app.count += 1