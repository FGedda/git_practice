import pygame
from pygame.locals import *
import os
import sys
import math
import random
pygame.init()

walkRight = pygame.image.load("obj_box004.png")
walkLeft = pygame.image.load("obj_box004.png")
goblin = pygame.image.load("idle001.png")
win = pygame.display.set_mode((800,600))
bg = pygame.image.load("bg.jpg")
pygame.display.set_caption("Munkfångaren Sara")
font = pygame.font.SysFont("comicsans", 30)
font1 = pygame.font.SysFont("comicsans", 30)
font2 = pygame.font.SysFont("comicsans", 45)
youLose = font2.render("You Lose!", 1, (255,255,255))
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()
c = True
c1 = True
score = 0
score1 = 0
liv = 3
liv1 = 3
level = 0
level1 = 0

class Bucket():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.left = False
        self.right = False
        self.standing = True
        self.walkCount = 0
        self.hitbox = (self.x, self.y, 60, 60)


    def draw(self,win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if not(self.standing):    
            if self.right:
                win.blit(walkRight, (self.x,self.y))
                self.walkCount += 1
            elif self.left:
                win.blit(walkLeft, (self.x,self.y))
                self.walkCount += 1
        else:
            win.blit(walkLeft, (self.x,self.y))
        #pygame.draw.rect(win, (255,0,0), (self.hitbox[0],self.hitbox[1],self.hitbox[2],self.hitbox[3]), 2)
        self.hitbox = (self.x, self.y, 60, 60)
        
            
class Munk():
    def __init__(self, width, height, x):
        global score
        self.x = x
        self.y = -50
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 40, 40)

    def draw(self,win):
        win.blit(pygame.transform.scale(goblin,(60,60)),(self.x,self.y))
        #pygame.draw.rect(win, (0,255,0), (self.hitbox[0],self.hitbox[1],self.hitbox[2],self.hitbox[3]), 2)
        self.hitbox = (self.x+15, self.y+7, 30, 50)
        if self.y <= 690+self.height and score >= 0 and score < 5:
            self.y += 2
        if self.y <= 690+self.height and score >= 5 and score < 10:
            self.hitbox = (self.x+15, self.y+8, 30, 50)
            self.y += 3
        if self.y <= 690+self.height and score >= 10 and score < 15:
            self.hitbox = (self.x+15, self.y+9, 30, 50)
            self.y += 4
        if self.y <= 690+self.height and score >= 15 and score < 20:
            self.hitbox = (self.x+15, self.y+10, 30, 50)
            self.y += 5
        if self.y <= 690+self.height and score >= 20 and score < 25:
            self.hitbox = (self.x+15, self.y+11, 30, 50)
            self.y += 6
        if self.y <= 690+self.height and score >= 25 and score < 30:
            self.hitbox = (self.x+15, self.y+12, 30, 50)
            self.y += 7
        if self.y <= 690+self.height and score >= 30:
            self.hitbox = (self.x+15, self.y+13, 30, 50)
            self.y += 8

class Munk1():
    def __init__(self, width, height, x):
        global score1
        self.x = x - 15
        self.y = -50
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 40, 40)

    def draw(self,win):
        win.blit(pygame.transform.scale(goblin,(60,60)),(self.x,self.y))
        #pygame.draw.rect(win, (0,255,0), (self.hitbox[0],self.hitbox[1],self.hitbox[2],self.hitbox[3]), 2)
        self.hitbox = (self.x+15, self.y+7, 30, 50)
        if self.y <= 690+self.height and score1 >= 0 and score1 < 5:
            self.y += 2
        if self.y <= 690+self.height and score1 >= 5 and score1 < 10:
            self.hitbox = (self.x+15, self.y+8, 30, 50)
            self.y += 3
        if self.y <= 690+self.height and score1 >= 10 and score1 < 15:
            self.hitbox = (self.x+15, self.y+9, 30, 50)
            self.y += 4
        if self.y <= 690+self.height and score1 >= 15 and score1 < 20:
            self.hitbox = (self.x+15, self.y+10, 30, 50)
            self.y += 5
        if self.y <= 690+self.height and score1 >= 20 and score1 < 25:
            self.hitbox = (self.x+15, self.y+11, 30, 50)
            self.y += 6
        if self.y <= 690+self.height and score1 >= 25 and score1 < 30:
            self.hitbox = (self.x+15, self.y+12, 30, 50)
            self.y += 7
        if self.y <= 690+self.height and score1 >= 30:
            self.hitbox = (self.x+15, self.y+13, 30, 50)
            self.y += 8
            
def updateFile():
    f = open("scores.txt","r")
    file = f.readlines()
    last = int(file[0])

    if last < int(score) and score > score1:
        f.close()
        file = open("scores.txt", "w")
        file.write(str(score))
        file.close()

    if last < int(score1) and score1 > score:
        f.close()
        file = open("scores.txt", "w")
        file.write(str(score1))
        file.close()

        return score
               
    return last


def endScreen():
    global pause, score, circle
    
    go = True
    while go:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    circle = []
                    circle1 = []
                    go = False
                
                
        win.blit(bg, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        smallFont = pygame.font.SysFont('comicsans', 40)
        lastScore = largeFont.render('Highscore: ' + str(updateFile()),1,(255,255,255))
        playerOneWin = largeFont.render("Player 1 wins!",1,(255,255,255))
        playerTwoWin = largeFont.render("Player 2 wins!",1,(255,255,255))
        playAgain = smallFont.render('Klicka R för att spela igen',1,(255,255,255))
        win.blit(lastScore, (400 - lastScore.get_width()/2,150))
        if score > score1:
            win.blit(playerOneWin, (400 - playerOneWin.get_width()/2, 240))
        else:
            win.blit(playerTwoWin, (400 - playerTwoWin.get_width()/2, 240))
        win.blit(playAgain, (400 - playAgain.get_width()/2, 330))
        pygame.display.update()


def drawWindow():
    global score, liv, level, score1, liv1, level1, c1, c
    
    levelNr = font.render("Level: " + str(level), 1, (0,0,0))
    scoreNr = font.render("Score: " + str(score), 1, (0,0,0))
    livNr = font.render("Life: " + str(liv), 1, (0,0,0))
    playerOne = font2.render("Player 1", 1, (255,255,255))
    
    
    levelNr1 = font.render("Level: " + str(level1), 1, (0,0,0))
    scoreNr1 = font.render("Score: " + str(score1), 1, (0,0,0))
    livNr1 = font.render("Life: " + str(liv1), 1, (0,0,0))
    playerTwo = font2.render("Player 2", 1, (255,255,255))
    

    win.blit(bg, (0,0))
    pygame.draw.line(win, (0,0,0), (395,0), (395,600), 5)

    win.blit(scoreNr,(400, 20))
    win.blit(levelNr, (400,0))
    win.blit(livNr, (400,40))

    win.blit(scoreNr1,(0, 20))
    win.blit(levelNr1, (0,0))
    win.blit(livNr1, (0,40))
    
    bucket.draw(win)
    bucket1.draw(win)

    if c:
        win.blit(playerOne, (525,300))
        circle[0].draw(win)
        if circle[0].y >= 300:
            circle[1].draw(win)


    if c1:
        win.blit(playerTwo, (125,300))
        circle1[0].draw(win)
        if circle1[0].y >= 300:
            circle1[1].draw(win)
            
    if liv == 0 and liv1 > 0:
        liv == 0
        win.blit(youLose, (525,300))
    elif liv > 0 and liv1 == 0:
        liv1 == 0
        win.blit(youLose, (125,300))
        
    pygame.display.update()
        
        


def game():
    clock.tick(60)
    global liv,score,circle,level, liv1, score1, circle1, level1, c, c1
    

    keys = pygame.key.get_pressed()

    if liv == 0:
        c = False
    if liv1 == 0:
        c1 = False
        

    if keys[pygame.K_LEFT] and bucket.x - 395 > bucket.vel:
        bucket.x -= bucket.vel
        bucket.left = True
        bucket.right = False
        bucket.standing = False

    elif keys[pygame.K_RIGHT] and bucket.x < 785 - bucket.width - bucket.vel:
        bucket.x += bucket.vel
        bucket.left = False
        bucket.right = True
        bucket.standing = False

    if keys[pygame.K_a] and bucket1.x + 5 > bucket1.vel:
        bucket1.x -= bucket1.vel
        bucket1.left = True
        bucket1.right = False
        bucket1.standing = False

    elif keys[pygame.K_d] and bucket1.x < 380 - bucket1.width - bucket1.vel:
        bucket1.x += bucket1.vel
        bucket1.left = False
        bucket1.right = True
        bucket1.standing = False
        

    #Munk under skärmen
    if circle[0].y+12 >= 650 and circle[1].y+12 <= 650:
        liv -= 1
        circle.pop(0)
        circle.append(Munk(40, 40, random.randint(375,755)))
            

    #Fånga Munk
    if circle[0].y+52 >= bucket.y and circle[0].y+55 <= bucket.y+15 and circle[0].x+15 <= bucket.x+60 and circle[0].x+45 >= bucket.x:
        circle.pop(0)
        score += 1
        circle.append(Munk(40, 40, random.randint(375,755)))

        

    #Munk1 under skärmen
    if circle1[0].y+12 >= 650 and circle1[1].y+12 <= 650:
        liv1 -= 1
        circle1.pop(0)
        circle1.append(Munk1(40, 40, random.randint(0,350)))
            

    #Fånga Munk1
    if circle1[0].y+52 >= bucket1.y and circle1[0].y+55 <= bucket1.y+15 and circle1[0].x+15 <= bucket1.x+60 and circle1[0].x+45 >= bucket1.x:
        circle1.pop(0)
        score1 += 1
        circle1.append(Munk1(40, 40, random.randint(0,350)))

    if score >= 0 and score < 5:
        level = 1
    if score >= 5 and score < 10:
        level = 2
    if score >= 10 and score < 15:
        level = 3
    if score >= 15 and score < 20:
        level = 4
    if score >= 20 and score < 25:
        level = 5
    if score >= 25:
        level = 6

    if score1 >= 0 and score1 < 5:
        level1 = 1
    if score1 >= 5 and score1 < 10:
        level1 = 2
    if score1 >= 10 and score1 < 15:
        level1 = 3
    if score1 >= 15 and score1 < 20:
        level1 = 4
    if score1 >= 20 and score1 < 25:
        level1 = 5
    if score1 >= 25:
        level1 = 6
    
    

    
bucket = Bucket(600-60, 520, 40, 40)
bucket1 = Bucket(200-60, 520, 40, 40)
circle = [Munk(40,40,random.randint(375,750)), Munk(40,40,random.randint(375,750))]
circle1 = [Munk1(40, 40, random.randint(0,350)), Munk1(40, 40, random.randint(0,350))]
run = True
while run:

    
    if liv == 0 and liv1 == 0:
        endScreen()
        circle1 = [Munk1(40, 40, random.randint(0,350)), Munk1(40, 40, random.randint(0,350))]
        circle = [Munk(40,40, random.randint(400,750)),Munk(40,40, random.randint(400,750))]
        liv1 = 3
        score1 = 0
        liv = 3
        score = 0
        c = True
        c1 = True
        drawWindow()
        game()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawWindow()
    game()

pygame.quit()
