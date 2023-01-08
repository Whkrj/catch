import pygame
import random
pygame.init()

screen_width = 1290
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('몬스터 잡기')

background = pygame.image.load('qorud.png')
background = pygame.transform.scale(background, (1290,700))
rlqhs = pygame.image.load('rlqhs1.png')
rlqhs = pygame.transform.scale(rlqhs, (100,100.4))
rlqhs1 = pygame.image.load('rlqhs1.png')
rlqhs1 = pygame.transform.scale(rlqhs1, (100,100.4))
rlqhs2 = pygame.image.load('rlqhs2.png')
rlqhs2 = pygame.transform.scale(rlqhs2, (100,100.4))
rlqhs3 = pygame.image.load('rlqhs3.png')
rlqhs3 = pygame.transform.scale(rlqhs3, (100,100.4))
rlqhs4 = pygame.image.load('rlqhs4.png')
rlqhs4 = pygame.transform.scale(rlqhs4, (100,100.4))
wjr = pygame.image.load('wjr1.png')
wjr = pygame.transform.scale(wjr, (131.5,115))
wjrr = pygame.image.load('wjr1.png')
wjrr = pygame.transform.scale(wjrr, (131.5,115))
wjr1 = pygame.image.load('wjr1.png')
wjr1 = pygame.transform.scale(wjr1, (131.5,115))
wjr2 = pygame.image.load('wjr2.png')
wjr2 = pygame.transform.scale(wjr2, (131.5,115))
wjr3 = pygame.image.load('wjr3.png')
wjr3 = pygame.transform.scale(wjr3, (131.5,115))
wjr4 = pygame.image.load('wjr4.png')
wjr4 = pygame.transform.scale(wjr4, (131.5,115))
wjr5 = pygame.image.load('wjr5.png')
wjr5 = pygame.transform.scale(wjr5, (131.5,115))

rlqhs_X_pos = 100
rlqhs_Y_pos = 403
to_x = 0
to_y = 0
wjr_X_pos = random.randint(200,1200)
wjr_Y_pos = random.randint(90,650)
wjrr_X_pos = random.randint(200,1200)
wjrr_Y_pos = random.randint(90,650)
gold = 0
kill = 0

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 10
                rlqhs = rlqhs4
            elif event.key == pygame.K_RIGHT:
                to_x += 10
                rlqhs = rlqhs4
            elif event.key == pygame.K_DOWN:
                to_y += 9
                rlqhs = rlqhs4
            elif event.key == pygame.K_UP:
                to_y -= 9
                rlqhs = rlqhs4
            elif event.key == pygame.K_RSHIFT:
                rlqhs = rlqhs2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            rlqhs = rlqhs1

    if rlqhs == rlqhs2:
        if wjr_X_pos <= rlqhs_X_pos+100 and wjr_X_pos+110 >= rlqhs_X_pos:
            if wjr_Y_pos <= rlqhs_Y_pos+100 and wjr_Y_pos+100 >= rlqhs_Y_pos:
                gold += random.randint(1,60)
                kill += 1
                wjr_X_pos = random.randint(1,1200)
                wjr_Y_pos = random.randint(1,600)
                q = random.randint(1,5)
                if q == 1:
                    wjr = wjr1
                elif q == 2:
                    wjr = wjr2
                elif q == 3:
                    wjr = wjr3
                elif q == 4:
                    wjr = wjr4
                elif q == 5:
                    wjr = wjr5
    if rlqhs == rlqhs2:
        if wjrr_X_pos <= rlqhs_X_pos+100 and wjrr_X_pos+110 >= rlqhs_X_pos:
            if wjrr_Y_pos <= rlqhs_Y_pos+100 and wjrr_Y_pos+100 >= rlqhs_Y_pos:
                gold += random.randint(1,60)
                kill += 1
                wjrr_X_pos = random.randint(1,1200)
                wjrr_Y_pos = random.randint(1,600)
                w = random.randint(1,5)
                if w == 1:
                    wjrr = wjr1
                elif w == 2:
                    wjrr = wjr2
                elif w == 3:
                    wjrr = wjr3
                elif w == 4:
                    wjrr = wjr4
                elif w == 5:
                    wjrr = wjr5

    rlqhs_X_pos += to_x
    rlqhs_Y_pos += to_y
    if rlqhs_X_pos < 0:
        rlqhs_X_pos = 0
    if rlqhs_X_pos > 1200:
        rlqhs_X_pos = 1200
    if rlqhs_Y_pos < 0:
        rlqhs_Y_pos = 0
    if rlqhs_Y_pos > 650:
        rlqhs_Y_pos = 650
    screen.blit(background, (0,0))
    screen.blit(wjr, (wjr_X_pos,wjr_Y_pos))
    screen.blit(wjrr, (wjrr_X_pos,wjrr_Y_pos))
    screen.blit(rlqhs, (rlqhs_X_pos,rlqhs_Y_pos))

    myFont = pygame.font.SysFont("Arial", 30, True, False)
    text_point = myFont.render("GOLD : " + str(gold), True, (255,255,255))
    screen.blit(text_point, (1,1))
    text_point2 = myFont.render("KILL : " + str(kill), True, (255,255,255))
    screen.blit(text_point2, (200,1))

    pygame.display.update()

pygame.quit()