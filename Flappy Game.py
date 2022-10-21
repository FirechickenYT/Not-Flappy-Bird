from sqlite3 import Timestamp
import pygame, sys
from pygame.locals import *
import random
from time import sleep


pygame.init()
width = int(input("Enter screen width"))
height = int(input("Enter screen height"))
DISPLAY=pygame.display.set_mode((width,height),0,32)

clock = pygame.time.Clock()

white=(255,255,255)
blue=(0,0,255)
red = (255, 0, 0)
green = (0, 255, 0)

DISPLAY.fill(white)

def drawPipes(w1):
    DISPLAY.fill(white)
    global y1
    global y2
    global points
    points += 1
    thing = -1

    y1 = random.randint(150, height-150)
    y2 = y1 + playerW * 4
    pygame.draw.rect(DISPLAY,green,(w1,0,50,y1))
    pygame.draw.rect(DISPLAY,green,(w1,y2,50,height*2))

def die(player_x_pos):
    global moving
    global sDown
    global player
    moving = False
    sDown = False
    DISPLAY.fill(white)
    player = pygame.draw.rect(DISPLAY,red,(player_x_pos,player_y_pos,playerW,playerH))
    pygame.display.update()
    return player_x_pos

pro = height/100
    
scoreFont = pygame.font.Font("/Users/Thomas/Documents/Assets/Charlie_Kingdom.ttf", 200)
speedFont = pygame.font.Font("/Users/Thomas/Documents/Assets/Charlie_Kingdom.ttf", 50)

player_x_pos = width/2 - 25
player_y_pos = height/2 - 25

downAcceleration  = 0.05
downSpeed = 0

sDown = False

playerW = width/19.2
playerH = playerW
player = pygame.draw.rect(DISPLAY,red,(player_x_pos,player_y_pos,playerW,playerH))

times = 0
timesThroughText = 0

speed = width / 425
if height > width:
    speed *= 1.5
thing = 500

w1 = width-50

done = False
moving = True

points = -1
drawPipes(w1)
currentX = player_x_pos
currentY = player_y_pos
while True:
    clock.tick(120)
    prevX = currentX
    currentX = player_x_pos
    currentY = player_y_pos
    xDiff = currentX - prevX
    prevY = currentY
    yDiff = currentY - prevY
    diff = xDiff + yDiff
    vel = diff * 120

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and moving == True:
            if event.key == K_SPACE:
                sDown = True
                downSpeed = 0
    if sDown == True and moving == True:
        pygame.draw.rect(DISPLAY,white,(player_x_pos,player_y_pos,playerW,playerH))
        times += 1
        stupid = height/8
        player_y_pos -= stupid / 30 - times/100
        if player_y_pos <= 0:
            player_y_pos = 0
            sDown = False
        if times >= 30:
            sDown = False
            times = 0
        downSpeed=0
    
    if downSpeed <= 5:
        downSpeed += downAcceleration
    
    if player_y_pos >= height - 25:
        player_y_pos = height - 25
        print(points)
        pygame.quit()
        sys.exit()
    if player_x_pos >= width - 25:
        speed = speed * -1
        w1 = 0
        thing = 0
        drawPipes(w1)
    if player_x_pos <= 0:
        speed = speed * -1
        w1 = width-50
        thing = 0
        drawPipes(w1)
    
    if w1 == 0 and done == False:
        if player_x_pos <= 50:
            if player_y_pos <= y1 or player_y_pos >= y2:
                if player_y_pos <= y1 + height/1.5:
                    print("1")
                if player_y_pos >= y2:
                    print("2")
                done = True
                player_x_pos = die(player_x_pos)
    if w1 == width-50 and done == False:
        if player_x_pos >= w1-25:
            if player_y_pos <= y1 or player_y_pos >= y2:
                if player_y_pos <= y1 + height/1.5:
                    print("1")
                if player_y_pos >= y2:
                    print("2")
                done = True
                player_x_pos = die(player_x_pos)
    if points >= 10:
        scoreFont = pygame.font.Font("/Users/Thomas/Documents/Assets/Charlie_Kingdom.ttf", 100)

    pygame.draw.rect(DISPLAY,white,(player_x_pos,player_y_pos,playerW,playerH))
    if sDown == False:
        player_y_pos += downSpeed
    if moving == True:
        player_x_pos += speed
    scoreText = scoreFont.render(str(points), True, (100, 100, 100))
    if points < 100:
        DISPLAY.blit(scoreText, (width/2 - 50, height/2 - 100))
    elif points >= 100:
        DISPLAY.blit(scoreText, (width/2 - 75, height/2 - 100))
    if timesThroughText >= 20:
        pygame.draw.rect(DISPLAY,white,(50,0,400,100))
        spdtxt = "Speed: " + str(round(vel + speed + downSpeed, 2))+ "m/s"
        speedText = speedFont.render(spdtxt, False, (100, 100, 100))
        DISPLAY.blit(speedText, (0, 0))
        timesThroughText = 0
    timesThroughText += 1
    player = pygame.draw.rect(DISPLAY,red,(player_x_pos,player_y_pos,playerW,playerH))
    pygame.display.update()

