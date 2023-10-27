import pygame, random, sys, copy, math, ctypes  # Imports libraries

pygame.init()
global WIDTH, HEIGHT  # sets all the global constants and variables

ctypes.windll.user32.SetProcessDPIAware()  # makes high PPI monitors aware of screen size change
WIDTH, HEIGHT = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)  # sets screen

print(WIDTH, HEIGHT)
if WIDTH / 16 > HEIGHT / 9:
    WIDTH = math.floor(16 * HEIGHT / 9)
elif WIDTH / 16 < HEIGHT / 9:
    HEIGHT = math.floor(9 * WIDTH / 16)
print(WIDTH, HEIGHT)


# dimensions by calling the ctypes library


def ratioConvert(axis, size):  # changes every size, to ensure that it fits screensize (in case of res change)
    newSize = 0
    if axis == "x":  # resizes horizontal size
        newSize = size * WIDTH / 1920
    elif axis == "y":  # resizes vertical size
        newSize = size * HEIGHT / 1080
    newSize = math.ceil(newSize)  # ensures all numbers are rounded up
    return newSize


def imageLoader(img, wid, hei):  # loads every image (simpler than rewriting single phrase)
    img = 'Images/' + img  # specifies folder
    image = pygame.image.load(img).convert_alpha()  # makes image transparent
    wid = ratioConvert("x", wid)  # sets variables for image size
    hei = ratioConvert("y", hei)
    image = pygame.transform.scale(image, (wid, hei))  # uses pygame library to change size of image
    return image


def audioLoader(sound):  # loads normal audio files
    sound = 'Audio/' + sound + '.ogg'
    sound = pygame.mixer.Sound(sound)  # locates file and sets it in the pygame mixer to play if needed
    sound.set_volume(0.25)
    return sound


def musicLoader(music):  # loads music files
    music = 'Audio/' + music + '.ogg'  # rewrites string to locate file
    return music


screen = pygame.display.set_mode((WIDTH, HEIGHT),
                                 pygame.FULLSCREEN | pygame.SCALED)  # sets screen to be full screen with correct
# dimensions
timer = pygame.time.Clock()  # Set a variable for the clock function
pygame.display.set_caption("Aprodite Adventure!")  # Title of game to be displayed top left of screen

MAP = imageLoader('New Map 6.png', 1920, 1080)  # All images for game
STARSBACK = imageLoader('NewBackground.png', 1920, 1080)  # Backgrounds
GAMETITLE = imageLoader('New Start Screen.png', 1920, 1080)
MAINMENU = imageLoader('New Main Menu.png', 1920, 1080)
GAMEOVERSCREEN = imageLoader('New Game Over.png', 1920, 1080)
LOADING = imageLoader('New Loading.png', 1920, 1080)
HIGHSCOREMENU = imageLoader('New High Scores List.png', 1920, 1080)
DIFFICULTY = imageLoader('New Difficulty.png', 1920, 1080)

PLAYERSP = imageLoader('New Player.png', 830 // 10, 513 // 10)  # Character Sprites
PLAYERFROZE = imageLoader('New Player Frozen.png', 830 // 10, 513 // 10)
PLAYERSPEED = imageLoader('New Player Speed.png', 840 // 10, 513 // 10)
PLAYERDEATH = imageLoader('New Player Death.png', 840 // 10, 513 // 10)
PLAYERINVIN = imageLoader('New Player Invincible.png', 840 // 10, 513 // 10)
PLAYERDUAL = imageLoader('New Player Dual.png', 840 // 10, 513 // 10)

ENEMYSP1 = imageLoader('Pathogen 1B.png', 70, 105)
ENEMYSP2 = imageLoader('Pathogen 2B.png', 70, 105)
ENEMYSP3 = imageLoader('Pathogen 3B.png', 70, 105)
ENEMYSP4 = imageLoader('Pathogen 4B.png', 70, 105)

HEALTH4 = imageLoader('4 Hearts.png', 272, 68)
HEALTH3 = imageLoader('3 Hearts.png', 272, 68)  # Healthbar images
HEALTH2 = imageLoader('2 Hearts.png', 272, 68)
HEALTH1 = imageLoader('1 Heart.png', 272, 68)
HEALTH0 = imageLoader('0 Hearts.png', 272, 68)
HEALTHI = imageLoader('Infinite Hearts.png', 272, 68)

ROCKVT = imageLoader('Vertical Wall 4.png', 28, 347)  # Wall images
ROCKHZ = imageLoader('Horizontal Wall 5.png', 628, 59)

CONTROLS = imageLoader('Controls.png', 1250, 85)  # UI images
HOWTOPLAYMENU = imageLoader('New How to Play Menu.png', 1920, 1080)
BLURIMG = imageLoader('Blur.png', 1920, 1080)

CLOSEDCHEST = imageLoader('New Chest Closed.png', 85, 66)  # Chests and powerup sprites
OPENCHEST = imageLoader('New Chest Open 2.png', 85, 66)
PWACE = imageLoader('New Ace TR.png', 85, 66)
PWANTINUKE = imageLoader('New Antibiotic Nuke TR.png', 85, 66)
PWAPROCREAM = imageLoader('New Aproderm Gel TR.png', 85, 66)
PWBARRIER = imageLoader('New Barrier Gel TR.png', 85, 66)
PWCOLLOIDAL = imageLoader('New Colloidal Oat Cream TR.png', 85, 66)
PWEMOLLIENT = imageLoader('New Emoillent Cream TR.png', 85, 66)
PWFREEZE = imageLoader('New Icicle TR.png', 85, 66)
PWNUT = imageLoader('New Acorn TR.png', 85, 66)
PWSCORE = imageLoader('New Score Boost TR.png', 85, 66)

TXTACE = imageLoader('Text AOC.png', 1624 // 3, 500 // 3)  # Text for powerup sprites
TXTANTINUKE = imageLoader('Text AN.png', 1624 // 3, 500 // 3)
TXTAPROCREAM = imageLoader('Text AG.png', 1411 // 3, 500 // 3)
TXTBARRIER = imageLoader('Text BG.png', 1411 // 3, 742 // 3)
TXTCOLLOIDAL = imageLoader('Text COC.png', 2109 // 3, 500 // 3)
TXTEMOLLIENT = imageLoader('Text EC.png', 1790 // 3, 500 // 3)
TXTFREEZE = imageLoader('Text FB.png', 1411 // 3, 500 // 3)
TXTNUT = imageLoader('Text NU.png', 925 // 3, 500 // 3)
TXTSCORE = imageLoader('Text SB.png', 1199 // 3, 500 // 3)

SCOREBOX = imageLoader('Text Score.png', 607 // 3, 258 // 3)

AUDCHESTOPEN = audioLoader('Chest Opening')  # .ogg file loading for sound effects
AUDDAMAGE = audioLoader('Hit')
AUDGOODPWR = audioLoader('Good')
AUDFREEZE = audioLoader('Freezing')
AUDGAMEEND = audioLoader('End Game')

MUSGAME = musicLoader('Gameplay Music')  # music files (.ogg loading)


class OnScreenObj(pygame.sprite.Sprite):  # Class for all elements, acts as super for more specific classes

    def __init__(self, xPos, yPos, img):  # Takes in x,y coordinates, size and image as parameters
        pygame.sprite.Sprite.__init__(self)
        self.image = img  # sets the sprites image
        self.rect = self.image.get_rect()  # sets a rectangle for sprite collisions
        self.rect.x = self.x = ratioConvert("x", xPos)  # determines the rectangle and sprite positions
        self.rect.y = self.y = ratioConvert("y", yPos)
        self.width = self.image.get_width()  # sets the width and height attributes by using the image
        self.height = self.image.get_height()

    def draw(self):  # subroutine which draws without requiring parameters
        self.customDraw(self.image, self.rect.x, self.rect.y)

    def customDraw(self, image, xPos, yPos):  # subroutine which draws if different arguments are needed
        screen.blit(image, (xPos, yPos))

    def setImage(self, newImage):  # allows sprite to have a new image if necessary
        self.image = newImage  # takes new image
        self.width = self.image.get_width()  # determines width and height of image
        self.height = self.image.get_height()


class PauseMenu(OnScreenObj):  # class for how to play screen on pause menu
    def __init__(self):
        super().__init__(0, 0, HOWTOPLAYMENU)
        self.menuState = False  # on or off menu
        self.tempFreezeTime = 0  # 4 temp variables to store info
        self.tempTextTime = 0
        self.tempPlayerVelocity = 0
        self.tempEnemyVelocity = 0

    def showPauseMenu(self):  # shows menu and sets time variables
        if self.menuState:  # checks whether to show pause menu or not
            player.setFreezeTime(0)  # freezes player time
            powerupInfo.setTime(0)  # stops power up information from disappearing
            for enemy in enemies.enemy_list:  # freezes all enemies
                enemy.setSpeed(0)
                enemy.setFreezeSelf(True)
            self.draw()  # draws the pause menu on screen

    def changeState(self):
        if not self.menuState:  # stores temp vars if P pressed and not in menu already
            self.tempFreezeTime = player.freezeTime
            self.tempTextTime = powerupInfo.textTime
            self.tempPlayerVelocity = player.velocity
            player.setSpeed(0)  # freezes player
            if len(enemies.enemy_list) > 0:  # makes sure list of enemies is not empty
                self.tempEnemyVelocity = enemies.enemy_list[0].velocity  # uses one of the enemy's velocity for temp
        else:  # restores previous vars if in menu currently and P pressed
            player.setSpeed(self.tempPlayerVelocity)  # sets player speed back to normal
            player.setFreezeTime(self.tempFreezeTime)  # sets the player freeze time back to normal
            powerupInfo.setTime(self.tempTextTime)  # allows text to disappear
            enemies.setSpeeds(self.tempEnemyVelocity)  # resets enemy speeds
        self.menuState = not self.menuState  # flips Boolean state


class ScoreSystem(OnScreenObj):  # score class
    def __init__(self):  # produces text
        super().__init__(1920 // 2, 1000, SCOREBOX)
        self.score = 0  # an attribute for the player's achievements
        self.enemyControl = 0  # an attribute to check how many enemies need to be spawned in

    def addScore(self, number):  # increases score
        self.score += number
        if self.score > 9999:  # sets maximum score of 9999
            self.score = 9999

    def displayScore(self):  # prints score on screen
        self.draw()
        scoreTextBox.showText(self.score, WHITE)  # uses white colour to show the text
        self.enemyCapControl()

    def enemyCapControl(self):  # determines how many enemies to spawn in during that round
        self.enemyControl = math.floor(math.log(self.score + 1, 2))  # logarithm to determine number of enemies
        self.enemyControl -= 1  # decreases the logarithmic output
        if self.enemyControl > 6:  # ensures only between 1 to 6 enemies spawn
            self.enemyControl = 6
        elif self.enemyControl < 1:
            self.enemyControl = 1
        enemies.setNormalEnemyCap(self.enemyControl)  # sets the enemy cap

    def resetScore(self):  # resets score at game launch to 0
        self.score = 0


class PowerText(OnScreenObj):  # class for text that explains what each power up does
    def __init__(self):
        super().__init__(100, 100, TXTACE)
        self.textTime = 90000

    def showInfo(self, changeInTime):  # prints text images to screen for set time period
        self.textTime += changeInTime  # increases time
        if self.textTime < 90000:  # makes sure there is enough time to show the text
            if player.rect.y < ratioConvert("y", 1080 // 2):  # checks which area of screen player is in...
                self.y = ratioConvert("y", 720)  # ...so that the text never overlaps the player
            else:
                self.y = ratioConvert("y", 200)
            if player.rect.x < ratioConvert("x", 1920 // 2):  # checks the horizontal way too
                self.x = ratioConvert("x", 1020)
            else:
                self.x = ratioConvert("x", 300)
            self.customDraw(self.image, self.x, self.y)  # draws text information to screen

    def setTime(self, newTime):
        self.textTime = newTime


class HealthSystem(OnScreenObj):  # class for health bar and health mechanics

    def __init__(self, health):
        super().__init__(37, 18, HEALTH3)
        self.health_list = {0: HEALTH0, 1: HEALTH1, 2: HEALTH2, 3: HEALTH3, 4: HEALTH4, 5: HEALTHI}  # dictionary for
        # different images
        self.health = health  # takes in health from input
        self.invincibility = False  # checks for invincibility powerups

    def changeHealth(self, deltaHealth):  # changes health based on
        if self.invincibility:  # if infinite health set healthbar to gold image
            self.health = 5  # restores full health
        else:
            self.health += deltaHealth
            if self.health > 4:  # Sets health to be maximum 3
                self.health = 4
        if self.health < 0:  # makes sure health does not reach a negative number
            self.health = 0
        self.setImage(self.health_list[self.health])  # set health image based on dictionary attribute
        if deltaHealth < 0 and not self.invincibility:  # checks if health has been subtracted
            game.setColourTime(0)  # starts timer for screen colour fill
            game.setFillScreen(True)  # fills screen with red colour
            AUDDAMAGE.play()  # plays damage sound

    def setInvincibility(self, Boolean):  # setter for invincibility
        self.invincibility = Boolean

    def resetHealth(self):  # sets health back to 4 at game load
        self.health = 4


class Chest(OnScreenObj):  # Class for chests inheriting from OnScreenObj

    def __init__(self, x, y):
        super().__init__(x, y, CLOSEDCHEST)
        self.powerUpList = [self.acePW, self.aproCreamPW, self.barrierPW,
                            self.emollientPW, self.colloidalPW, self.nukePW,
                            self.freezePW, self.nutPW, self.scorePW]  # creates list for powerup functions
        self.openState = False  # Boolean attribute for chest being open or closed
        self.powerContent = 0  # Integer attribute to implement powerup in chest
        self.powerImage = None  # image for powerup to overlay on chest
        self.refill = False  # Boolean attribute to check whether to refill chest or not
        self.waitBool = True

    def closeChest(self):  # changes chest attributes and image when closing chest
        self.openState = False
        self.powerImage = None

    def openChest(self, powerupPic, powerupText):  # changes chest attributes to show open chest
        self.openState = True  # sets chest to be open
        self.powerImage = powerupPic  # sets image to be argument
        powerupInfo.setTime(0)  # allows text to be displayed on screen based on powerup, resets counter
        powerupInfo.setImage(powerupText)  # selects text to display

    def chestImage(self):  # sets image for chests
        if not self.openState:
            self.image = CLOSEDCHEST  # sets closed image if openState is false
        else:
            self.image = OPENCHEST  # sets opened image if openState is true
            self.customDraw(self.powerImage, self.rect.x, self.rect.y)  # shows image on screen

    def setRefill(self, Boolean):  # setter for refill state
        self.refill = Boolean

    def acePW(self):  # sets refill all chests
        self.openChest(PWACE, TXTACE)
        chests.refillChests()  # methods to shuffle walls around, fill all chests
        walls.shuffleLists()
        chests.setRefillImageTime(0)  # resets timer so chests don't refill instantly
        AUDCHESTOPEN.play()

    def aproCreamPW(self):
        self.openChest(PWAPROCREAM, TXTAPROCREAM)
        healthBar.setInvincibility(True)  # sets invincibility to True
        player.setImage(PLAYERINVIN)  # sets image for invincible player
        AUDGOODPWR.play()

    def barrierPW(self):
        self.openChest(PWBARRIER, TXTBARRIER)
        healthBar.setInvincibility(True)  # sets invincibility to True
        player.setSpeed(player.normalPlayerSpeed * 2)  # doubles player speed
        player.setImage(PLAYERDUAL)  # sets image for barrier gel player
        AUDGOODPWR.play()

    def emollientPW(self):  # freezes all enemies
        self.openChest(PWEMOLLIENT, TXTEMOLLIENT)
        enemies.setIndividualFreeze()  # freezes all enemies
        enemies.setFreezeAllEnemies(True)  # sets Boolean condition to freeze enemies
        AUDFREEZE.play()

    def colloidalPW(self):
        self.openChest(PWCOLLOIDAL, TXTCOLLOIDAL)
        player.setSpeed(player.normalPlayerSpeed * 2)  # doubles player speed
        player.setImage(PLAYERSPEED)  # sets image for speed boost player
        AUDGOODPWR.play()

    def nukePW(self):
        self.openChest(PWANTINUKE, TXTANTINUKE)  # deletes all enemies
        enemies.setcurrentEnemyCap(0)  # forces no enemies to spawn during this period
        AUDGOODPWR.play()

    def freezePW(self):
        self.openChest(PWFREEZE, TXTFREEZE)
        player.setFreeze(PLAYERFROZE)  # sets player to be frozen
        AUDFREEZE.play()

    def nutPW(self):  # damages player by 1
        self.openChest(PWNUT, TXTNUT)
        game.addHealthDropCount(1)  # calls method to knock down health

    def scorePW(self):  # increases score
        self.openChest(PWSCORE, TXTSCORE)
        scoreSystem.addScore(4)  # adds 4 more score on top of 1st score point for every chest
        AUDGOODPWR.play()

    def powerUp(self):  # function to determine powerups
        if not self.openState:  # resets all powerups to ensure no effects carry over
            chests.resetPowers()  # resets all player and enemy effects
            scoreSystem.addScore(1)  # increase score
            self.powerUpList[self.powerContent - 1]()  # selects powerup method from list

    def refillChest(self):  # sets chest contents to be frozen
        if (chests.refillImageTime > 90000 or self.waitBool) and self.refill:  # waits time before closing chests
            self.closeChest()  # closes chests
            chests.setFilledCount(0)  # sets amount of filled chest number to 0
            self.refill = False  # disables refilling
            self.waitBool = False

    def setPowerContent(self, content):  # sets the powerup in the chest
        self.powerContent = content


class Character(OnScreenObj):  # Class for players and enemies inheriting from OnScreenObj

    def __init__(self, xPos, yPos, velocity, image):  # Constructor needs image, x, y, wid, hei coordinates as
        # parameters
        super().__init__(xPos, yPos, image)  # Calls parent class
        self.velocity = ratioConvert("x", velocity)  # Controls speeds (each object needs own as it'll change)
        self.moveUp = False  # movement conditions to allow diagonal movement
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False
        self.freezeSelf = False

    def resetMovement(self):  # sets all movement to still every loop to stop infinite velocity gain
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False

    def moving(self, axis, direction):
        moveVelocity = self.velocity * direction  # calculates which way to move the object in case of collision
        if axis == "x":
            self.rect.x += moveVelocity  # moves character in this direction
            if walls.wallCollision(self):
                self.rect.x -= moveVelocity  # pushes character back if colliding with wall
        if axis == "y":  # repeats previous section for y axis
            self.rect.y += moveVelocity
            if walls.wallCollision(self):
                self.rect.y -= moveVelocity

    def movement(self):
        if self.moveLeft and self.rect.x > ratioConvert("x", 33):  # checks character is within map bounds
            self.moving("x", -1)  # lets character move in this direction and axis
        if self.moveRight and self.rect.x < ratioConvert("x", 1803):
            self.moving("x", 1)
        if self.moveUp and self.rect.y > ratioConvert("y", 85):
            self.moving("y", -1)
        if self.moveDown and (self.rect.y + self.height) < ratioConvert("y", 995):
            self.moving("y", 1)

    def setSpeed(self, newSpeed):  # setter for speed
        self.velocity = newSpeed

    def freeze(self):  # freezes character
        self.setSpeed(0)  # changes character velocity
        self.setFreezeSelf(True)  # sets Boolean variable

    def setFreezeSelf(self, Boolean):  # setter for custom freeze condition
        self.freezeSelf = Boolean


class Player(Character):

    def __init__(self):
        super().__init__(740, 500, 0, PLAYERSP)
        self.freezeTime = 0  # freeze timer and condition
        self.normalPlayerSpeed = ratioConvert("x", 5)
        self.velocity = self.normalPlayerSpeed

    def playerMovement(self):  # movement for player - based on keyboard presses
        self.resetMovement()
        keys = pygame.key.get_pressed()  # creates list of all keys pressed
        if keys[pygame.K_a]:  # checks if any of the following keys in that list
            self.moveLeft = True  # sets direction variable to True to me player in that direction
        if keys[pygame.K_d]:
            self.moveRight = True
        if keys[pygame.K_w]:
            self.moveUp = True
        if keys[pygame.K_s]:
            self.moveDown = True
        self.movement()

    def setFreezeTime(self, time):  # setter for freeze time
        self.freezeTime = time

    def setFreeze(self, image):  # setter for freezing character
        self.setFreezeTime(0)
        self.freeze()
        self.image = image  # changes image

    def checkSpeed(self, changeInTime):  # checks if time has passed to undo freeze condition
        self.freezeTime += changeInTime  # adds time
        if self.freezeTime > 100000 and self.freezeSelf:  # checks if enough time has passed, checks if frozen
            self.setSpeed(self.normalPlayerSpeed)  # resets speed
            self.freezeSelf = False  # unfreezes character
            self.resetImage()  # changes image back to normal image

    def resetImage(self):  # sets image back to normal
        self.image = PLAYERSP

    def resetPos(self):  # resets player coordinates at game launch
        self.rect.x = ratioConvert("x", 780)  # player x coordinate
        self.rect.y = ratioConvert("y", 500)  # player starting y coordinate


class Enemy(Character):
    def __init__(self, xPos, yPos, velocity):
        self.textureList = [ENEMYSP1, ENEMYSP2, ENEMYSP3, ENEMYSP4]
        random.shuffle(self.textureList)
        super().__init__(xPos, yPos, velocity, self.textureList[1])

    def enemyMovement(self):  # movement for enemies - based on player position
        self.resetMovement()
        if self.rect.x < player.rect.x:  # checks if player is right of enemy
            self.moveRight = True
        if self.rect.x > player.rect.x:  # checks if enemy on right
            self.moveLeft = True
        if self.rect.y < player.rect.y:  # checks if enemy below
            self.moveDown = True
        if self.rect.y > player.rect.y:  # checks if enemy above
            self.moveUp = True  # sets Boolean variable to true if above
        if self.rect.x == player.rect.x:  # checks if enemy is on the same coordinate as player
            self.moveLeft = self.moveRight = False  # stops enemy moving perpendicular to player
        if self.rect.y == player.rect.y:
            self.moveUp = self.moveDown = False
        self.movement()


class EnemyCollection:  # class for all enemies
    def __init__(self):
        self.enemy_list = []  # instantiates empty list of enemies
        self.insertionCount = 0  # number of enemies to reinsert
        self.enemyCount = 0  # number of enemies alive
        self.freezeAllEnemies = False  # Boolean for enemy freeze
        self.spawn_locations = [(70, 125),
                                (70, 875),
                                (925, 125),
                                (925, 875),
                                (1780, 125),
                                (1780, 875)]  # generates location points for enemies to spawn
        self.reInsert = True  # Attribute to check whether to kill enemy or reinsert into list
        self.currentEnemyCap = self.normalEnemyCap = 1  # enemy cap for number of maximum enemies
        self.normalEnemySpeed = ratioConvert("x", 1)  # Normal speed to reset for powerups

    def setFreezeAllEnemies(self, Boolean):  # setters for enemy traits
        self.freezeAllEnemies = Boolean

    def setIndividualFreeze(self):  # ensures all enemies are frozen
        for enemy in self.enemy_list:
            enemy.freeze()

    def setcurrentEnemyCap(self, newCap):  # sets a new enemy cap for killing temporarily
        self.currentEnemyCap = newCap

    def setNormalEnemyCap(self, newCap):  # sets a new normal cap for the rest of the game
        self.normalEnemyCap = newCap

    def resetEnemyCap(self):  # sets enemy cap back to 1 at start of new game
        self.setNormalEnemyCap(1)

    def setSpeeds(self, speed):  # changes all the enemy speeds to desired velocity
        for enemy in self.enemy_list:
            enemy.setSpeed(speed)

    def spawn(self):  # respawns enemies
        xPos, yPos = random.choice(self.spawn_locations)
        self.newEnemy(xPos, yPos)  # enemy instantiated at random location

    def newEnemy(self, xPos, yPos):  # function to add new enemy
        if not self.freezeAllEnemies:
            useSpeed = self.normalEnemySpeed  # lets new enemy move if not frozen
        else:
            useSpeed = 0  # lets new enemy stay frozen if necessary
        self.enemy_list.append(Enemy(xPos, yPos, useSpeed))  # spawns new enemy at randomised location

    def enemySetup(self, healthDrop):
        self.insertionCount = 0
        self.enemyCount = 0

        for enemy in self.enemy_list[:]:  # goes through list of enemies
            self.reInsert = True
            self.reInsert = walls.wallIntrusion(enemy)  # removes enemy if stuck inside wall
            self.enemy_list.remove(enemy)  # pops enemy temporarily
            self.enemyCount += 1
            if pygame.sprite.collide_rect_ratio(0.75)(player, enemy):  # Checks if player collides with enemy
                self.reInsert = False  # removes enemy from object list
                healthDrop += 1  # increases health drop count
            for collEnemy in self.enemy_list:  # checks if enemy collides with any other enemy
                if pygame.sprite.collide_rect_ratio(0.5)(enemy, collEnemy):
                    self.reInsert = False  # stops enemy respawning if it does collide
            enemy.enemyMovement()
            enemy.draw()  # draws and allows enemy movement
            if self.reInsert:
                self.enemy_list.insert(self.insertionCount, enemy)  # pushes the enemy back into the list if required
                self.insertionCount += 1
        while self.enemyCount > self.currentEnemyCap:
            self.enemy_list.pop()  # if no. of enemies exceeds cap, delete enemies
            self.enemyCount -= 1
        if self.enemyCount < self.currentEnemyCap:  # otherwise spawn new enemies until cap reached
            self.spawn()
            self.enemyCount += 1
        return healthDrop

    def clearEnemies(self):
        self.enemy_list = []

    def setStartSpeed(self, event):
        self.normalEnemySpeed = event.key - 48  # determines enemy speed based on pygame event integer
        if 4 >= self.normalEnemySpeed >= 1:  # range check for enemy speed
            self.normalEnemySpeed = ratioConvert("x",
                                                 self.normalEnemySpeed)  # converts enemy speed for display resolution
            AUDDAMAGE.play()
            return True
        else:
            return False


class WallCollection:
    def __init__(self):  # creates all wall objects and wall lists
        self.wallh1 = OnScreenObj(22, 356, ROCKHZ)  # horizontal
        self.wallh2 = OnScreenObj(650, 356, ROCKHZ)
        self.wallh3 = OnScreenObj(1278, 356, ROCKHZ)
        self.wallh4 = OnScreenObj(22, 661, ROCKHZ)
        self.wallh5 = OnScreenObj(650, 661, ROCKHZ)
        self.wallh6 = OnScreenObj(1278, 661, ROCKHZ)

        self.wallv1 = OnScreenObj(628, 20, ROCKVT)  # vertical
        self.wallv2 = OnScreenObj(1257, 20, ROCKVT)
        self.wallv3 = OnScreenObj(628, 367, ROCKVT)
        self.wallv4 = OnScreenObj(1257, 367, ROCKVT)
        self.wallv5 = OnScreenObj(628, 715, ROCKVT)
        self.wallv6 = OnScreenObj(1257, 715, ROCKVT)

        self.wall_listbase = [self.wallv1, self.wallv2, self.wallv3, self.wallv4, self.wallv5, self.wallv6,
                              self.wallh1, self.wallh2, self.wallh3, self.wallh4, self.wallh5, self.wallh6]  # base
        self.wall_list1 = [self.wallv2, self.wallv5, self.wallh2, self.wallh5]  # level designs
        self.wall_list2 = [self.wallv1, self.wallv2, self.wallv5, self.wallv6]
        self.wall_list3 = [self.wallh1, self.wallh3, self.wallh4, self.wallh6]
        self.wall_list4 = [self.wallv1, self.wallv3, self.wallv4, self.wallh5]
        self.wall_list5 = [self.wallh1, self.wallh2, self.wallh5, self.wallh6]
        self.wall_list6 = [self.wallv3, self.wallv4, self.wallv5, self.wallv6]
        self.wall_list7 = [self.wallv2, self.wallv5, self.wallh1, self.wallh5]
        self.wall_list8 = [self.wallv3, self.wallv4, self.wallh2, self.wallh4]
        self.wall_list9 = [self.wallv2, self.wallv5, self.wallh2, self.wallh5]
        self.all_lists = [self.wall_list1, self.wall_list2, self.wall_list3, self.wall_list4, self.wall_list5,
                          self.wall_list6, self.wall_list7, self.wall_list8, self.wall_list9]  # list of levels

        self.current_list = random.choice(self.all_lists)  # selects a random layout

    def shuffleLists(self):  # randomises level layout
        self.current_list = random.choice(self.all_lists)

    def wallCollision(self, sprite):  # function to check if collisions occur
        for wall in self.current_list:
            if pygame.sprite.collide_rect_ratio(0.97)(sprite, wall):
                return True

    def wallIntrusion(self, sprite):  # checks if object is inside a wall, then kills
        for wall in self.current_list:
            if pygame.sprite.collide_rect_ratio(0.96)(sprite, wall):  # uses a ratio of 0.98 to determine if inside wall
                return False
        return True

    def wallDisplay(self):  # draws all walls
        for wall in self.current_list:
            wall.draw()


class ChestCollection:
    def __init__(self):
        self.chest_list = [Chest(300, 250),  # instantiates chests
                           Chest(300, 510),
                           Chest(300, 770),
                           Chest(918, 250),
                           Chest(918, 510),
                           Chest(918, 770),
                           Chest(1500, 250),
                           Chest(1500, 510),
                           Chest(1500, 770)]
        self.constant_powers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # a base powerup stack to use
        self.variable_powers = []  # stack which copies constant list
        self.filledCount = 0
        self.refillImageTime = 0

    def setRefillImageTime(self, newTime):  # sets the refill time to a new time
        self.refillImageTime = newTime

    def addRefillImageTime(self, changeInTime):  # adds to the refill image time
        self.refillImageTime += changeInTime

    def chestSetup(self):
        self.variable_powers = copy.copy(self.constant_powers)  # copy creates new memory location
        random.shuffle(self.variable_powers)  # shuffles data set for randomisation

        for chest in self.chest_list[:]:  # draws chests to screen
            chest.draw()
            if self.filledCount < 9:  # fills chests with stack
                chest.setPowerContent(self.variable_powers.pop())  # function to dispense from stack
                self.filledCount += 1
            if pygame.sprite.collide_rect_ratio(1.05)(player, chest):  # checks if player collides with chest ...
                chest.powerUp()  # ... using increased range for chest (1.15x)
            chest.chestImage()
            chest.refillChest()  # checks if chest needs refilling

    def refillChests(self):
        for chest in self.chest_list:  # sets all chests to refill state
            chest.setRefill(True)

    def resetWaitBool(self):
        for chest in self.chest_list:  # sets all chests to refill state
            chest.waitBool = True

    def setFilledCount(self, newCount):
        self.filledCount = newCount

    def resetPowers(self):  # sets all conditions to be normal, as though no powerups have effect
        healthBar.setInvincibility(False)  # stops invincibility
        player.setSpeed(player.normalPlayerSpeed)  # sets normal speed
        enemies.setcurrentEnemyCap(enemies.normalEnemyCap)  # sets current enemy cap
        enemies.setSpeeds(ratioConvert("x", enemies.normalEnemySpeed))  # resets enemy speeds
        enemies.setFreezeAllEnemies(False)  # unfreezes enemies
        player.resetImage()  # changes player image to normal


class TextBox(OnScreenObj):

    def __init__(self, textSize, xPos, yPos):
        super().__init__(xPos, yPos, PLAYERSP)
        self.font = pygame.font.Font(pygame.font.get_default_font(), ratioConvert("x", textSize))  # sets default font

    def showText(self, textInput, colour):
        self.image = self.font.render(str(textInput).upper(), True, colour)  # renders input text and draws it
        self.customDraw(self.image, self.rect.x + ratioConvert("x", 5), self.rect.y + ratioConvert("y", 7))


class HighScoreTextBox(TextBox):

    def __init__(self, yPos):
        super().__init__(56, 805, yPos)  # sets a predetermined position for the text box

    def displayHighScores(self, textInput):
        self.showText(textInput, PURPLE)  # sets purple text


class UsernameTextBox(TextBox):

    def __init__(self):
        super().__init__(48, 700, 530)  # input textbox
        self.rect = pygame.Rect(ratioConvert("x", 752), ratioConvert("y", 659), ratioConvert("x", 414),
                                ratioConvert("y", 55))

    def border(self, textInput):
        pygame.draw.rect(screen, PURPLE, self.rect, 4)  # prints rectangle for text
        self.showText(textInput, BLACK)  # renders text in black


class Product:  # class for the entire game structure

    def __init__(self):
        self.state = 0  # state to load
        self.states_list = [userName, selectionMenu, loading, game, gameOver, difficultySelect]  # states
        self.username = ""  # attribute for name
        self.score = 0  # attribute for score
        self.topFive = None

    def setState(self, number):  # set and run current game state
        self.state = number

    def runState(self):
        self.writeFile("")  # creates file every loop
        self.states_list[self.state].runtime()  # runs the correct state

    def setMusic(self, music):  # setters for different game elements
        pygame.mixer.music.load(music)  # loads and plays music
        pygame.mixer.music.play(-1)

    def setUsername(self, username):  # sets username
        self.username = username

    def setScore(self, score):  # sets score
        self.score = score

    def stopMusic(self):  # stops current track
        pygame.mixer.music.stop()

    def resetGame(self):  # refreshes all game elements
        chests.refillChests()  # refills and changes powerups
        chests.resetPowers()  # puts player and enemy back to default state
        enemies.resetEnemyCap()  # sets enemy cap back to 1
        scoreSystem.resetScore()  # sets score back to 0
        player.resetPos()  # sets player start coordinates
        enemies.clearEnemies()  # deletes all enemies
        healthBar.resetHealth()  # restores healthbar

    def writeFile(self, newLine):
        self.topFive = open("Leaderboard.txt", "a")  # creates file leaderboard.txt
        self.topFive.write(newLine)
        self.topFive.close()

    def readFile(self):
        self.topFive = open("Leaderboard.txt", "r")  # opens file for reading
        lines = self.topFive.readlines()  # reads lines
        self.topFive.close()
        return lines


class UserNameInput:  # class for entering username

    def __init__(self):
        self.text = ""

    def events(self, event):
        if event.type == pygame.KEYDOWN:  # checks if input is alphabet or number, and length of text already
            if (event.unicode.isalpha() or event.unicode.isdigit()) and len(self.text) < 9:
                self.text += event.unicode  # adds to the text
                AUDDAMAGE.play()
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # removes from the text if backspace entered
            elif event.key == pygame.K_RETURN and len(self.text) > 0:  # changes state if return pressed
                aproditeAdventure.setState(1)  # also checks text is present
                aproditeAdventure.setUsername(self.text)
                AUDGOODPWR.play()

    def quitGame(self, event):
        if event.type == pygame.QUIT:  # If user clicks X the application closes
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # if "ESC" pressed ends game
            sys.exit()

    def runtime(self):  # function to run every loop
        startupScreen.draw()
        for event in pygame.event.get():  # carries out all pygame events
            self.events(event)
            self.quitGame(event)
        usernameBox.border(self.text)  # displays text


class SelectMode:  # class for main menu

    def __init__(self):
        self.howToPlay = False
        self.instructions = OnScreenObj(0, 0, HOWTOPLAYMENU)  # image of HOWTOPLAY
        self.highScore = False
        self.highScoresImg = OnScreenObj(0, 0, HIGHSCOREMENU)  # image of HIGHSCORES
        self.highScore_list = [HighScoreTextBox(305),  # textboxes for each high score
                               HighScoreTextBox(412),
                               HighScoreTextBox(517),
                               HighScoreTextBox(624),
                               HighScoreTextBox(730)]
        self.lines = None
        self.loopCondition = 0

    def quitGame(self, event):
        if event.type == pygame.QUIT:  # If user clicks X the application closes
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # if "ESC" pressed ends game
            sys.exit()

    def events(self, event):  # checks key input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                aproditeAdventure.setState(5)  # sets state to difficulty select if s is pressed
                difficultySelect.setSwitchState(False)
                loading.setTime()
                AUDDAMAGE.play()
            elif event.key == pygame.K_p:
                self.howToPlay = not self.howToPlay  # swaps state to show instructions if p pressed
                self.highScore = False  # hides high scores
                AUDDAMAGE.play()
            elif event.key == pygame.K_h:  # swaps state to show high scores if h pressed
                self.highScore = not self.highScore  # hides instructions
                self.howToPlay = False
                AUDDAMAGE.play()
            elif event.key == pygame.K_c:
                aproditeAdventure.setState(0)  # returns to username menu
                AUDDAMAGE.play()

    def howToPlayScreen(self):  # draws pause screen to show player what to do
        if self.howToPlay:
            self.instructions.draw()

    def highScoresScreen(self):
        aproditeAdventure.writeFile("")  # checks file exists
        if self.highScore:
            self.highScoresImg.draw()
            self.lines = aproditeAdventure.readFile()  # reads all lines from file into array
            self.lines = sorted(self.lines, reverse=True)  # sorts lines from variable
            self.loopCondition = 0  # loop condition
            for line in self.lines:
                if self.loopCondition < 5:
                    self.highScore_list[self.loopCondition].displayHighScores(
                        line[:-1])  # shows the text from array onscreen
                    self.loopCondition += 1

    def runtime(self):  # main loop to run
        mainMenuPic.draw()
        for event in pygame.event.get():  # checks events
            self.quitGame(event)
            self.events(event)
        self.howToPlayScreen()
        self.highScoresScreen()  # completes main methods


class SelectDifficulty:  # class for selecting the appropriate game mode

    def __init__(self):
        self.selectionScreen = OnScreenObj(0, 0, DIFFICULTY)  # picture for menu
        self.switchState = False

    def quitGame(self, event):
        if event.type == pygame.QUIT:  # If user clicks X the application closes
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # if "ESC" pressed returns to main menu
            aproditeAdventure.setState(1)

    def events(self, event):  # checks key input
        if event.type == pygame.KEYDOWN:  # sets enemy speed depending on difficulty
            self.switchState = enemies.setStartSpeed(event)

    def setSwitchState(self, Boolean):  # setter for attribute
        self.switchState = Boolean

    def changeState(self):  # changes state if necessary
        if self.switchState:
            aproditeAdventure.setState(2)
            aproditeAdventure.stopMusic()  # starts loading screen but stops playing music

    def runtime(self):  # main loop for difficulty section
        self.selectionScreen.draw()
        for event in pygame.event.get():
            self.quitGame(event)
            self.events(event)
        self.changeState()


class Loading:

    def __init__(self):
        self.loadingScreen = OnScreenObj(0, 0, LOADING)  # image for loading screen
        self.tip_list = ["A certain powerup changes the walls around!",  # different tips to show on screen
                         "Invincibility powerups refill your health!",
                         "You have to keep moving to get a high score!",
                         "You turn blue if you're frozen!",
                         "Trapping pathogens behind walls slows them down!",
                         "More pathogens spawn as you get more points!",
                         "A gold health bar means you're invincible!",
                         "Pathogens only spawn on red spaces!",
                         "If pathogens collide one will die!",
                         "You can move in 8 different directions!",
                         "You turn green if you get a speed powerup!"]
        self.text = None
        self.time = 0
        self.chooseText = True

    def quitGame(self, event):
        if event.type == pygame.QUIT:  # If user clicks X the application closes
            sys.exit()

    def setTime(self):  # setter for time to show screen
        self.time = 0

    def increaseTimes(self, changeInTime):  # change timer
        self.time += changeInTime

    def runtime(self):  # runs the loading screen and places a tip on screen
        self.loadingScreen.draw()
        for event in pygame.event.get():
            self.quitGame(event)
        if self.chooseText:  # checks if necessary to choose new tip
            self.text = random.choice(self.tip_list)  # choose tip from array
            self.chooseText = False
        tipTextBox.showText(self.text, PURPLE)  # renders and shows tip in purple
        self.increaseTimes(deltaTime)
        if self.time > 100000:  # waits until enough time has passed
            aproditeAdventure.setMusic(MUSGAME)  # changes music
            pygame.mixer.music.set_volume(0.25)
            aproditeAdventure.setState(3)  # loads game
            aproditeAdventure.resetGame()  # resets game settings to default
            self.chooseText = True  # requires tip to be set to true


class Game:  # class for main game

    def __init__(self):
        self.colourTime = 0
        self.deathTime = 0
        self.fillScreen = False
        self.backgroundColour = RED
        self.healthDropCount = 0

    def addHealthDropCount(self, Add):  # increases damage taken
        self.healthDropCount += Add

    def increaseTimes(self, changeInTime):
        chests.addRefillImageTime(changeInTime)  # changes times
        self.colourTime += changeInTime  # controls loop times
        self.deathTime += changeInTime

    def screenFill(self):
        if self.fillScreen:
            screen.fill(self.backgroundColour)  # Screen drawing with certain background colour if necessary
        if self.colourTime > 6000:  # disables screen colouring
            self.fillScreen = False

    def setFillScreen(self, Boolean):  # setter for filling screen
        self.fillScreen = Boolean

    def setColourTime(self, Time):  # setter for colour time
        self.colourTime = Time

    def killPlayer(self):
        if healthBar.health > 0:  # reset timer if alive still
            self.deathTime = 0
        elif healthBar.health <= 0:  # ends game once player runs out of health
            player.setFreeze(PLAYERDEATH)  # changes player image to death image
            AUDGAMEEND.play()
            enemies.setcurrentEnemyCap(0)
            aproditeAdventure.stopMusic()  # stops music playing
            if self.deathTime >= 90000:  # ends game after enough time
                self.endGame()

    def events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:  # checks pause
            pauseScreen.changeState()

    def quitGame(self, event):
        if event.type == pygame.QUIT:  # If user clicks X the application closes
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # if "ESC" pressed ends game
            self.endGame()

    def endGame(self):
        aproditeAdventure.stopMusic()
        aproditeAdventure.setState(4)  # sets game to game over state and sets username and score
        aproditeAdventure.setScore(scoreSystem.score)  # sets score and username
        aproditeAdventure.setUsername(userName.text)
        scoreConcat_list = ["000", "00", "0", ""]  # creates list to attach details to
        if scoreSystem.score != 0:  # checks score isn't 0
            logScore = math.floor(math.log(scoreSystem.score, 10))  # uses logs to decide what to concatenate
            newScore = str(scoreConcat_list[logScore]) + str(scoreSystem.score)  # produces a new score string
        else:
            newScore = "0000"  # sets score to 0000 if score is originally 0
        aproditeAdventure.writeFile(str(newScore) + "  |  " + aproditeAdventure.username + "\n")

    def enemyCap(self):  # sets enemy cap to original
        if scoreSystem.score == 0:
            enemies.setcurrentEnemyCap(1)

    def runtime(self):  # main game loop, draws images and calls main methods
        self.enemyCap()
        for event in pygame.event.get():
            self.quitGame(event)
            self.events(event)
        self.healthDropCount = 0  # resets damage taken
        starsBackground.draw()
        self.screenFill()
        walls.wallDisplay()
        gamemap.draw()  # Displays elements on screen
        healthBar.draw()
        controls.draw()
        scoreSystem.displayScore()  # responsible for main methods
        chests.chestSetup()
        player.draw()
        player.playerMovement()
        self.healthDropCount = enemies.enemySetup(self.healthDropCount)
        powerupInfo.showInfo(deltaTime)  # checks if text needs to be displayed
        pauseScreen.showPauseMenu()
        healthBar.changeHealth(-self.healthDropCount)  # depletes health if necessary
        self.killPlayer()  # checks if need to kill player
        player.checkSpeed(deltaTime)
        self.increaseTimes(deltaTime)


class GameOver:  # class for game over screen

    def quitGame(self, event):
        if event.type == pygame.QUIT:  # If user clicks X the application closes
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # if "ESC" pressed ends game
            aproditeAdventure.setState(1)  # changes state and music
            aproditeAdventure.stopMusic()
            AUDDAMAGE.play()

    def displayDetails(self):
        resultsUsernameBox.showText(aproditeAdventure.username, PURPLE)  # renders text
        resultsScoreBox.showText("Score: " + str(aproditeAdventure.score), PURPLE)  # sets current text

    def runtime(self):  # draws screen and username, score
        gameOverPic.draw()
        self.displayDetails()
        for event in pygame.event.get():
            self.quitGame(event)


WHITE = (255, 255, 255)  # used colours
RED = (125, 0, 0)
BLACK = (0, 0, 0)
PURPLE = (147, 58, 103)

player = Player()  # Instantiate moving elements
enemies = EnemyCollection()

walls = WallCollection()  # instantiates still elements
chests = ChestCollection()
gamemap = OnScreenObj(0, 0, MAP)

healthBar = HealthSystem(4)  # instantiates UI elements
controls = OnScreenObj(450, 5, CONTROLS)
scoreSystem = ScoreSystem()

starsBackground = OnScreenObj(0, 0, STARSBACK)  # instantiates screens
pauseScreen = PauseMenu()
powerupInfo = PowerText()
startupScreen = OnScreenObj(0, 0, GAMETITLE)
mainMenuPic = OnScreenObj(0, 0, MAINMENU)
gameOverPic = OnScreenObj(0, 0, GAMEOVERSCREEN)

usernameBox = UsernameTextBox()  # instantiates text boxes
scoreTextBox = TextBox(55, 1170, 1018)
tipTextBox = TextBox(60, 40, 815)
resultsUsernameBox = TextBox(170, 230, 460)
resultsScoreBox = TextBox(170, 500, 635)

deltaTime = timer.tick(60)  # detects change in time

userName = UserNameInput()  # instantiates game state settings
game = Game()
loading = Loading()
selectionMenu = SelectMode()
gameOver = GameOver()
difficultySelect = SelectDifficulty()
aproditeAdventure = Product()

aproditeAdventure.stopMusic()  # sets starting music

gameLoop = True
while gameLoop:
    aproditeAdventure.runState()
    pygame.display.flip()  # reloads screen drawing
    timer.tick(60)  # Sets frame rate to 60fps

pygame.quit()  # ends game
sys.exit()

# Powerups
# 1 - Ace, refills all chests
# 2 - Aproderm Gel, invincible, health = 3
# 3 - Barrier Gel, invincible, speed up, health = 3
# 4 - Emollient Cream, freezes enemies
# 5 - Colloidal Oat Cream, speed up
# 6 - Antibiotic Nuke, clears enemies
# 7 - Freeze Bomb, freezes player temporarily
# 8 - Nuts, takes one health from player
# 9 - Score Boost, increases score
