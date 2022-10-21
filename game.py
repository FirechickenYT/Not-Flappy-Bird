import pygame, sys
from pygame.locals import *
import random
from time import sleep


pygame.init()
width = 640
height = 480
DISPLAY=pygame.display.set_mode((width,height),0,32)

white=(255,255,255)
blue=(0,0,255)
red = (255, 0, 0)
green = (0, 255, 0)

DISPLAY.fill(white)

def setNone():
    return

def drawPipes(w1):
    DISPLAY.fill(white)
    global y1
    global y2
    global points
    points += 1

    y1 = random.randint(-240, 70)
    y2 = y1 + 350
    pygame.draw.rect(DISPLAY,green,(w1,y1,50,250))
    pygame.draw.rect(DISPLAY,green,(w1,y2,50,400))
    if y1 > 0:
        pygame.draw.rect(DISPLAY,green,(w1,0,50,250))

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
    
scoreFont = pygame.font.Font("/Users/Thomas/Documents/Assets/Charlie_Kingdom.ttf", 200)

player_x_pos = 295
player_y_pos = 215

downAcceleration  = 0.05
downSpeed = 0

sDown = False

playerW = 25
playerH = 25
player = pygame.draw.rect(DISPLAY,red,(player_x_pos,player_y_pos,25,25))

times = 0
speed = 1.5

thing = 500

w1 = 590

done = False
moving = True

points = -1
drawPipes(w1)

while True:
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
        player_y_pos -= 2
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
        speed = -1.5
        w1 = 0
        thing = 0
        drawPipes(w1)
    if player_x_pos <= 0:
        speed = 1.5
        w1 = 590
        thing = 0
        drawPipes(w1)

    if w1 == 0 and done == False:
        if player_x_pos <= 50:
            if player_y_pos <= y1+250 or player_y_pos >= y2:
                done = True
                player_x_pos = die(player_x_pos)
    if w1 == 590 and done == False:
        if player_x_pos >= 565:
            if player_y_pos <= y1+250 or player_y_pos >= y2:
                done = True
                player_x_pos = die(player_x_pos)


    pygame.draw.rect(DISPLAY,white,(player_x_pos,player_y_pos,playerW,playerH))
    if sDown == False:
        player_y_pos += downSpeed
    if moving == True:
        player_x_pos += speed
    scoreText = scoreFont.render(str(points), True, (100, 100, 100))
    DISPLAY.blit(scoreText, (250, 100))
    player = pygame.draw.rect(DISPLAY,red,(player_x_pos,player_y_pos,playerW,playerH))
    pygame.display.update()

