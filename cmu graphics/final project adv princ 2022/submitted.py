from cmu_graphics import *
#Based on the game: Crypt of the Necrodancer
#uses a grid-based system of movement
#you play as Melody with the golden lute which attacks evey cardinal tile around you on move
#stay alive for as many beats as possible
#enemies spawn on edge every 6 measures

#monster ai:
#bat - blue moves in a random direction every 2nd beat red moves every beat

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
player = Group(Image('https://www.spriters-resource.com/resources/sheet_icons/78/81345.png', 185, 185))
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
            if(x == 0 or y == 0 or x == 8 or y == 8):
                if(level[x][y] == None):
                    open.append([x, y])
    return open

#hurt player
def hurtPlayer(dmg):
    player.hp -= dmg
    hurtSound.play(restart = True)
    health.value = 'Health: ' + str(player.hp)
    if(player.hp < 1):
        app.stop()

#make bats and ai
def makeBlueBat():
    spaces = getOpenEdge()
    if(len(spaces) > 0):
        index = randrange(0, len(spaces))
        x = spaces[index][0]
        y = spaces[index][1]
        
        #make the bat with 1hp
        monster = Image('http://clipart-library.com/img1/1421622.png', 50 + x*(34 - (4/9)), 50 + y*(34 - (4/9)))
        monster.id = 0
        monster.x = x
        monster.y = y
        monster.width = 34 - (4/9)
        monster.height = 34 - (4/9)
        
        #place bat
        level[x][y] = monster
        
def makeRedBat():
    spaces = getOpenEdge()
    if(len(spaces) > 0):
        index = randrange(0, len(spaces))
        x = spaces[index][0]
        y = spaces[index][1]
        
        #make red bat
        monster = Image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTB496fv3QMEHLlBQJ8lBTQqqCWYdw3o7ubNwY-mdRFcArSBwfO&s', 50 + x*(34 - (4/9)), 50 + y*(34 - (4/9)))
        monster.id = 1
        monster.x = x
        monster.y = y
        monster.width = 34 - (4/9)
        monster.height = 34 - (4/9)
        
        #place bat
        level[x][y] = monster
        
def batAI(monster):
    choices = []
    if(monster.id == 0):
        if(app.count % 120 == 0):
            #check nearby tiles and radomly pick from those with None or player
            if(monster.x > 0):
                if(level[monster.x - 1][monster.y] == None):
                    choices.append([monster.x - 1, monster.y])
            if(monster.x < 8):
                if(level[monster.x + 1][monster.y] == None):
                    choices.append([monster.x + 1, monster.y])
            if(monster.y > 0):
                if(level[monster.x][monster.y - 1] == None):
                    choices.append([monster.x, monster.y - 1])
            if(monster.y < 8):
                if(level[monster.x][monster.y + 1] == None):
                    choices.append([monster.x, monster.y + 1])
            if(len(choices) > 0):
                #randomly pick avalible tile, attack or update vars and delete old bat
                index = randrange(0, len(choices))
                x = choices[index][0]
                y = choices[index][1]
                level[monster.x][monster.y] = None
                monster.x = x
                monster.y = y
                level[x][y] = monster
        monster.centerX = 67 + monster.x*(34 - (4/9))
        monster.centerY = 67 + monster.y*(34 - (4/9))
    else:
        #if player is within one cardinal tile try to attack them
        if(monster.x > 0):
            if(level[monster.x - 1][monster.y] == player):
                hurtPlayer(2)
            else:
                choices.append([monster.x - 1, monster.y])
        if(monster.x < 8):
            if(level[monster.x + 1][monster.y] == player):
                hurtPlayer(2)
            else:
                choices.append([monster.x + 1, monster.y])
        if(monster.y > 0):
            if(level[monster.x][monster.y - 1] == player):
                hurtPlayer(2)
            else:
                choices.append([monster.x, monster.y - 1])
        if(monster.y < 8):
            if(level[monster.x][monster.y + 1] == player):
                hurtPlayer(2)
            else:
                choices.append([monster.x, monster.y + 1])
        if(len(choices) > 0):
            index = randrange(0, len(choices))
        x = choices[index][0]
        y = choices[index][1]
        level[monster.x][monster.y] = None
        monster.x = x
        monster.y = y
        #print('[' + str(x) + ', ' + str(y) + ']')
        level[x][y] = monster
        monster.centerX = 67 + monster.x*(34 - (4/9))
        monster.centerY = 67 + monster.y*(34 - (4/9))        

#controls
def onKeyHold(keys):
    if(app.canMove):
        if('up' in keys):
            if(player.y > 0 and level[player.x][player.y - 1] == None):
                level[player.x][player.y] = None
                player.y -= 1
                level[player.x][player.y] = player
                checkAttacks(player.x, player.y)
            app.canMove = False
        elif('down' in keys):
            if(player.y < 8 and level[player.x][player.y + 1] == None):
                level[player.x][player.y] = None
                player.y += 1
                level[player.x][player.y] = player
                checkAttacks(player.x, player.y)
            app.canMove = False
        elif('left' in keys):
            if(player.x > 0 and level[player.x - 1][player.y] == None):
                level[player.x][player.y] = None
                player.x -= 1
                level[player.x][player.y] = player
                checkAttacks(player.x, player.y)
            app.canMove = False
        elif('right' in keys):
            if(player.x < 8 and level[player.x + 1][player.y - 1] == None):
                level[player.x][player.y] = None
                player.x += 1
                level[player.x][player.y] = player
                checkAttacks(player.x, player.y)
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
            if(level[x][y] != None and level[x][y] != player):
                monster = level[x][y]
                if(monster.id == 0 or monster.id == 1):
                    batAI(monster)
                else:
                    skeletonAI(monster)
            
#spawn a wave of monsters
def spawnMonsters():
    for x in range(2, randrange(4, 7)):
        makeBlueBat()
    for x in range(1, randrange(2, 5)):
        makeRedBat()

#attack monsters around player on move
def checkAttacks(x, y):
    if(x > 0):
        if(level[x - 1][y] != None):
            level[x - 1][y].toBack()
            level[x - 1][y] = None
            score.value += 1
            attackSound.play(restart = True)
    if(x < 8):
        if(level[x + 1][y] != None):
            level[x + 1][y].toBack()
            level[x + 1][y] = None
            score.value += 1
            attackSound.play(restart = True)
    if(y > 0):
        if(level[x][y - 1] != None):
            level[x][y - 1].toBack()
            level[x][y - 1] = None
            score.value += 1
            attackSound.play(restart = True)
    if(y < 8):
        if(level[x][y + 1] != None):
            level[x][y + 1].toBack()
            level[x][y + 1] = None
            score.value += 1
            attackSound.play(restart = True)

def onStep():
    #create a new wave of enemies every 6 measures and heal the player for 2hp
    if(app.count % 1440 == 0):
        spawnMonsters()
        player.hp += 2
        health.value = 'Health: ' + str(player.hp)
    #toggle move once at start of hit window
    if(app.count % 60 == 45):
        app.canMove = True
    elif(app.count % 60 == 0):
        tickAI()
        metronomeTick.play()
        score.value += 1
    elif(app.canMove and app.count % 60 == 15):
        app.canMove = False
        hurtPlayer(1)
    app.count += 1

cmu_graphics.run()