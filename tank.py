from os import environ
from  pygame import *
import random
import pygame as pg
import time, sys
import  random , math
from pygame import mixer
bullet2_state = 'ready'
bullet_state = 'ready'
pg.mixer.pre_init(44100,-16,2,512)
pg.init()
screen = pg.display.set_mode((800, 600))
def menu():
    a = 0
    icon = pg.image.load('akm.jpg')
    pg.display.set_icon(icon)
    button_sound = pg.mixer.Sound('button.mp3')
    click_sound = pg.mixer.Sound('click.mp3')
    music1 = [pg.mixer.Sound('music1.mp3'),pg.mixer.Sound('music2.mp3'),pg.mixer.Sound('music3.mp3')]
    music1[0].set_volume(0.3)
    music1[1].set_volume(0.3)
    music1[2].set_volume(0.3)
    music_timer = 0
    start = pg.Rect(250, 160, 300, 60)
    exit = pg.Rect(250, 260, 300, 60)
    credit = pg.Rect(100, 360, 250, 60)
    music = pg.Rect(450, 360, 250, 60)
    stop = pg.Rect(710,360,50,60)
    control = pg.Rect(250, 460, 300, 60)
    startfont = pg.font.Font('freesansbold.ttf', 40)
    exitfont = pg.font.Font('freesansbold.ttf', 40)
    creditfont = pg.font.Font('freesansbold.ttf',40)
    musicfont = pg.font.Font('freesansbold.ttf', 25)
    stopfont = pg.font.Font('freesansbold.ttf', 40)
    controlfont = pg.font.Font('freesansbold.ttf', 40)
    click = False
    while True:
        if music_timer > 0:
            music_timer -= 1
        pg.display.set_caption('Home')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                click_sound.play()
                if event.button == 1:
                    click = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        screen.fill((100, 100, 100))
        startfontrender = startfont.render('Start', True, (255, 255, 255))
        exitfontrender = exitfont.render('Exit', True, (255, 255, 255))
        creditfontrender = creditfont.render('Author',True,(255,255,255))
        musicfontrender = musicfont.render('play some music :))', True, (255, 255, 255))
        stopfontrender = stopfont.render('l l', True, (255, 255, 255))
        controlfontrender = controlfont.render('Control',True,(255,255,255))
        mx, my = pg.mouse.get_pos()
        mouse = pg.Rect(mx, my, 1, 1)
        pg.draw.rect(screen, (0, 100, 0), start)
        pg.draw.rect(screen, (100, 0, 0), exit)
        pg.draw.rect(screen,(0,100,0),credit)
        pg.draw.rect(screen,(0,100,0),music)
        pg.draw.rect(screen,(100,0,0),stop)
        pg.draw.rect(screen, (0, 100, 0), control)
        # check if the mouse touch a button
        if control.contains(mouse):
            if a == 0:
                a = 1
                button_sound.play()
            pg.draw.rect(screen, (16, 176, 16), control)
            if click:
                pg.draw.rect(screen, (7, 125, 10), control)
                controls()
        if stop.contains(mouse):
            if a == 0:
                a = 1
                button_sound.play()
            pg.draw.rect(screen, (227, 5, 27), stop)
            if click:
                mixer.fadeout(1000)
                pg.draw.rect(screen, (163, 13, 13), stop)
        if exit.contains(mouse):
            if a == 0:
                a = 1
                button_sound.play()
            pg.draw.rect(screen, (227, 5, 27), exit)
            if click:
                pg.draw.rect(screen, (163, 13, 13), exit)
                pg.quit()
                sys.exit()
        if start.contains(mouse):
            if a == 0:
                a = 1
                button_sound.play()
            pg.draw.rect(screen, (16, 176, 16), start)
            if click:
                pg.draw.rect(screen, (7, 125, 10), start)
                game()
        if credit.contains(mouse):
            if a == 0:
                a = 1
                button_sound.play()
            pg.draw.rect(screen, (16, 176, 16),credit)
            if click:
                pg.draw.rect(screen, (7, 125, 10), credit)
                author()
        if music.contains(mouse):
            if a == 0:
                a = 1
                button_sound.play()
            pg.draw.rect(screen, (16, 176, 16), music)
            if click:
                pg.draw.rect(screen, (7, 125, 10), music)
                if music_timer == 0:
                    mixer.stop()
                    music_timer = 120
                    random.choice(music1).play()
                    click_sound.play()
        # check if the mouse doesn't touch a button
        if control.contains(mouse)== False and stop.contains(mouse) == False and exit.contains(mouse) == False and start.contains(mouse) ==False and credit.contains(mouse) == False and music.contains(mouse) == False:
            a =0
        screen.blit(musicfontrender,(455,375))
        screen.blit(exitfontrender, (350, 270))
        screen.blit(startfontrender, (350, 170))
        screen.blit(creditfontrender,(155,375))
        screen.blit(stopfontrender, (718, 372))
        screen.blit(controlfontrender, (320, 470))
        pg.display.update()

def game():
    global bullet_state
    global bullet2_state
    button_sound = pg.mixer.Sound('button.mp3')
    click_sound = pg.mixer.Sound('click.mp3')
    clock = pg.time.Clock()
    pg.init()
    a = 900
    pg.display.set_caption('Game bắn tank đỉnh cao :))')
    icon = pg.image.load('akm.jpg')
    pg.display.set_icon(icon)
    #background
    background = pg.image.load('road.png')
    mixer.music.load('background.mp3')
    mixer.music.play(-1)


    #player1
    playerimg = pg.image.load('tank.png')
    playerX =random.randint(0,500)
    playerY = random.randint(220,460)
    playerX_changeL = 0
    playerX_changeR = 0
    playerY_changeU = 0
    playerY_changeD = 0
    player1_rect = pg.Rect(playerX,playerY,playerimg.get_width(),playerimg.get_height())
    #player2
    player2img = pg.image.load('tank1.png')
    player2X = random.randint(600,780)
    player2Y = random.randint(220,460)
    player2X_changeL = 0
    player2X_changeR = 0
    player2Y_changeU = 0
    player2Y_changeD = 0
    player2_rect = pg.Rect(player2X,player2Y,player2img.get_width(),player2img.get_height())
    #bullet
    bulletimg = pg.image.load('bullet.png')
    bulletX = 0
    bulletY = 0
    bullet_state = 'ready'
    bullet1_rect = pg.Rect(bulletX,bulletY,bulletimg.get_width(),bulletimg.get_height())
    #bullet2
    bullet2img = pg.image.load('bullet2.png')
    bullet2X = 0
    bullet2Y = 0
    bullet2_state = 'ready'
    bullet2_rect = pg.Rect(bullet2X,bullet2Y,bullet2img.get_width(),bullet2img.get_height())

    #media
    shot = mixer.Sound("tankshot.wav")
    score_player1 = 0
    font1 = pg.font.Font('freesansbold.ttf',16)
    score_player2 = 0
    font2 = pg.font.Font('freesansbold.ttf',16)
    #bang
    bangimg = pg.image.load('bang.png')
    bangsound = mixer.Sound('bang.wav')

    def bang(x,y):
        screen.blit(bangimg,(x,y))

    def player1(x,y):
        screen.blit(playerimg,(x,y))
    def player2(x,y):
        screen.blit(player2img, (x, y))
    def bullet(x,y):
        global bullet_state
        bullet_state = 'fire'
        screen.blit(bulletimg,(x,y))
    def bullet2(x,y):
        global bullet2_state
        bullet2_state = 'fire'
        screen.blit(bullet2img, (x, y))

    def score():
        score = font1.render("Player1: "+str(score_player1), True,(255,255,255))
        screen.blit(score,(0,0))
        score2 = font2.render("Player2: "+str(score_player2),True,(255,255,255))
        screen.blit(score2,(0,18))
    running = True
    exitfont = pg.font.Font('freesansbold.ttf',40)
    exit = pg.Rect(110,0,50,35)
    click = False
    while running:


        mx, my = pg.mouse.get_pos()
        mouse = pg.Rect(mx, my, 1, 1)
        player1_rect.x = playerX
        player1_rect.y = playerY
        player2_rect.x = player2X
        player2_rect.y = player2Y
        bullet1_rect.x = bulletX
        bullet1_rect.y = bulletY
        bullet2_rect.x = bullet2X
        bullet2_rect.y = bullet2Y
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            #Điều Khiển
            if event.type == pg.KEYDOWN:


                #up down1

                if event.key == pg.K_s:
                    playerY_changeD = 3.5
                if event.key == pg.K_w:
                    playerY_changeU = -3.5

                #left right1

                if event.key == pg.K_a:
                    playerX_changeL = -3.5
                if event.key == pg.K_d:
                    playerX_changeR = 3.5

                #bullet
                if event.key == pg.K_n or event.key == pg.K_SPACE:
                    if bullet_state == 'ready':
                        bulletX = playerX +11
                        bulletY = playerY +14
                        bullet(bulletX, bulletY)
                        shot.play()
                #bullet2
                if event.key == pg.K_BACKSPACE or event.key == pg.K_RETURN:
                    if bullet2_state == 'ready':
                        bullet2X = player2X +11
                        bullet2Y = player2Y +14
                        bullet2(bullet2X, bullet2Y)
                        shot.play()


                #up down2

                if event.key == pg.K_DOWN:
                    player2Y_changeD = 3.5
                if event.key == pg.K_UP:
                    player2Y_changeU = -3.5

                # left right2

                if event.key == pg.K_LEFT:
                    player2X_changeL = -3.5
                if event.key == pg.K_RIGHT:
                    player2X_changeR = 3.5

                #keyup

            if event.type == pg.KEYUP:
                if event.key == pg.K_s :
                    playerY_changeD = 0
                if event.key == pg.K_w:
                    playerY_changeU = 0
                if event.key == pg.K_a :
                    playerX_changeL = 0
                if event.key == pg.K_d:
                    playerX_changeR =0

                if event.key == pg.K_DOWN :
                    player2Y_changeD = 0
                if event.key == pg.K_UP:
                    player2Y_changeU = 0
                if event.key == pg.K_LEFT :
                    player2X_changeL = 0
                if event.key == pg.K_RIGHT:
                    player2X_changeR = 0

        screen.blit(background,(0,0))
        exitfontrender = exitfont.render("X",True,(255,255,255))
        pg.draw.rect(screen,(100,0,0),exit)

        if exit.contains(mouse):
            pg.draw.rect(screen,(227, 5, 27),exit)
            if click:
                mixer.music.stop()
                running = False
        playerX += playerX_changeR
        playerX += playerX_changeL
        if playerX <= 0:
            playerX = 0
        elif playerX >= 320:
            playerX = 320
        playerY += playerY_changeU
        playerY += playerY_changeD
        if playerY <= 200:
            playerY = 200
        elif playerY >= 460:
            playerY = 460
        player1(playerX,playerY)

        # bullet1
        if bulletX >= 800:
            bulletX = 0
            bullet_state ='ready'
        if bullet_state == 'fire':
            bulletX += 15
            bullet(bulletX,bulletY)
        #bullet2
        if bullet2X <= 0:
            bullet2X = 800
            bullet2_state ='ready'
        if bullet2_state == 'fire':
            bullet2X += -15
            bullet2(bullet2X,bullet2Y)



        player2X += player2X_changeR
        player2X += player2X_changeL
        if player2X >=800 -64 :
            player2X =800 - 64
        elif player2X <= 420:
            player2X = 420
        player2Y += player2Y_changeU
        player2Y += player2Y_changeD
        if player2Y <= 200:
            player2Y = 200
        elif player2Y >= 460:
            player2Y = 460
        player2(player2X,player2Y)

        #hit player1

        if bullet1_rect.colliderect(player2_rect):
            bulletX = playerX
            bullet_state = 'ready'
            score_player1 += 1
            bangX, bangY = player2X, player2Y
            player2X = random.randint(600, 780)
            player2Y = random.randint(220, 460)
            a = 0
            bangsound.play()

        #hit player2

        if bullet2_rect.colliderect(player1_rect):
            bullet2X = player2X
            bullet2_state = 'ready'
            score_player2 += 1
            bangX, bangY = playerX, playerY
            playerX = random.randint(0, 500)
            playerY = random.randint(220, 460)
            a = 0
            bangsound.play()
        #bang
        if a <150:
            bang(bangX,bangY)
        a +=5
        screen.blit(exitfontrender, (120, 0))
        score()
        pg.display.update()
        clock.tick(60)

def author():
    a = 0
    button_sound = pg.mixer.Sound('button.mp3')
    click_sound = pg.mixer.Sound('click.mp3')
    screen = pg.display.set_mode((800,600))
    authotimg = pg.image.load('author.jpg')
    back = pg.Rect(60,60,200,60)
    backfont = pg.font.Font('freesansbold.ttf',40)
    click = False
    running = True
    while running:
        screen.fill((100, 100, 100))
        screen.blit(authotimg,(0,0))
        mx,my = pg.mouse.get_pos()
        mouse = pg.Rect(mx,my,1,1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                click_sound.play()
                if event.button == 1:
                    click = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        backfontrender= backfont.render('Back',True,(255,255,255))
        pg.draw.rect(screen, (100, 0, 0), back)
        #check if the mouse touch a button
        if back.contains(mouse):
            if a == 0:
                a = 1
                button_sound.play()
            pg.draw.rect(screen, (227, 5, 27), back)
            if click:
                pg.draw.rect(screen, (163, 13, 13), back)
                running = False
        #check if the mouse doesn't touch a button
        if back.contains(mouse) == False:
            a = 0
        screen.blit(backfontrender,(110,70))
        pg.display.update()
def controls():
    a = 0
    button_sound = pg.mixer.Sound('button.mp3')
    click_sound = pg.mixer.Sound('click.mp3')
    screen = pg.display.set_mode((800,600))
    controltimg = pg.image.load('control.png')
    back = pg.Rect(60,60,200,60)
    backfont = pg.font.Font('freesansbold.ttf',40)
    click = False
    running = True
    while running:
        screen.fill((100, 100, 100))
        screen.blit(controltimg,(0,0))
        mx,my = pg.mouse.get_pos()
        mouse = pg.Rect(mx,my,1,1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                click_sound.play()
                if event.button == 1:
                    click = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
        backfontrender= backfont.render('Back',True,(255,255,255))
        pg.draw.rect(screen, (100, 0, 0), back)
        #check if the mouse touch a button
        if back.contains(mouse):
            if a == 0:
                a = 1
                button_sound.play()
            pg.draw.rect(screen, (227, 5, 27), back)
            if click:
                pg.draw.rect(screen, (163, 13, 13), back)
                running = False
        #check if the mouse doesn't touch a button
        if back.contains(mouse) == False:
            a = 0
        screen.blit(backfontrender,(110,70))
        pg.display.update()
menu()

