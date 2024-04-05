from pygame import *
from time import sleep
window_width = 700
window_height = 500
background = (0, 0, 100)
run = True
scrtlvl = 0
restart = False
suzhet = 0
level = 1
not_ended = True
mixer.init()
font.init()
font = font.SysFont('Arial', 40)
mixer.music.load('scream.mp3')
lose = font.render('ВЫ НЕ СМОГЛИ СБЕЖАТЬ...', True, (255,0,0))
scrtlvlwin = font.render('ВЫ ПРОШЛИ!', True, (0,255,0))
scrtlvllose = font.render('ПОПРОБУЙТЕ ПОЗЖЕ', True, (255,0,0))
winimg = transform.scale(image.load('podval.jpg'), (700,500))
lehasm = transform.scale(image.load('leha.png'), (1200, 800))
playerimg = transform.scale(image.load('sanya.png'), (100, 100))
win = font.render('ВЫ СБЕЖАЛИ', True, (0,255,0))
window = display.set_mode((window_width, window_height))
display.set_caption('Escape from Lexia')
timer = time.Clock()
class Gamesprite(sprite.Sprite):
    def __init__(self,picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class player(Gamesprite):
    def __init__(self, picture, w, h, x, y, xspeed, yspeed):
        Gamesprite.__init__(self, picture, w, h, x, y)
        self.xspeed = xspeed
        self.yspeed = yspeed
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
zapiska1 = Gamesprite('zapiska.png', 50, 50, 135, 25 )
Player = player('sanya.png', 40, 40, 50, 450, 0, 0)
door1 = Gamesprite('door.png', 40, 40, 480, 380)
wall1 = Gamesprite('backgr.jpg', 200, 20, 150, 250)
wall2 = Gamesprite('backgr.jpg', 20, 450, 350, 70)
wall3 = Gamesprite('backgr.jpg', 300, 20, 450, 70)
wall4 = Gamesprite('backgr.jpg', 200, 20, 0, 400)
wall5 = Gamesprite('backgr.jpg', 20, 90, 200, 330)
wall6 = Gamesprite('backgr.jpg', 250, 20, 350, 150)
wall7 = Gamesprite('backgr.jpg', 260, 20, 440, 350)
wall8 = Gamesprite('backgr.jpg', 20, 80, 440, 350)
wall9 = Gamesprite('backgr.jpg', 200, 20, 440, 425)
Player2 = player('sanya.png', 40, 40, 20, 15, 0, 0)
door2 = Gamesprite('door.png', 40, 40, 20, 430)
wall10 = Gamesprite('backgr.jpg', 20, 60, 180, 0)
wall11 = Gamesprite('backgr.jpg', 250, 20, 0, 140)
wall12 = Gamesprite('backgr.jpg', 150, 20, 180, 60)
wall13 = Gamesprite('backgr.jpg', 20, 160, 330, 60)
wall14 = Gamesprite('backgr.jpg', 20, 20, 100, 400)
wall15 = Gamesprite('backgr.jpg', 400, 20, 350, 200)
wall16 = Gamesprite('backgr.jpg', 20, 80, 250, 140)
wall17 = Gamesprite('backgr.jpg', 270, 20, 0, 200)
wall18 = Gamesprite('backgr.jpg', 600, 20, 0, 380)
wall19 = Gamesprite('backgr.jpg', 20, 100, 100, 460)
wall20 = Gamesprite('backgr.jpg', 20, 60, 200, 400)
wall21 = Gamesprite('backgr.jpg', 20, 60, 280, 440)
wall22 = Gamesprite('backgr.jpg', 20, 60, 360, 400)
wall23 = Gamesprite('backgr.jpg', 20, 60, 440, 440)
Enemy2 = player('petr.png', 60, 90, 40, 220, 0, 0)
Enemy = player('leha.png', 50, 50, 500, 300, 0, 0)
scrtplayer1 = player('sanya.png', 20, 20, 350, 245, 0,0)
scrtwall1 = Gamesprite('backgr.jpg', 48, 12, 285, 222)
scrtwall2 = Gamesprite('backgr.jpg', 10, 66, 285, 222)
scrtwall3 = Gamesprite('backgr.jpg', 150, 10, 285, 288)
scrtwall4 = Gamesprite('backgr.jpg', 11, 66, 424, 222)
scrtwall5 = Gamesprite('backgr.jpg', 55, 12, 380, 222)
scrtwall6 = Gamesprite('backgr.jpg', 18, 149, 333, 85)
scrtwall7 = Gamesprite('backgr.jpg', 10, 95, 380, 127)
scrtwall8 = Gamesprite('backgr.jpg', 170, 13, 380, 127)
scrtwall9 = Gamesprite('backgr.jpg', 270, 10, 345, 85)
scrtwall10 = Gamesprite('backgr.jpg', 15, 285, 600,85)
scrtwall11 = Gamesprite('backgr.jpg', 25,185,525,127)
scrtwall12 = Gamesprite('backgr.jpg', 511, 21, 104, 349)
scrtwall13 = Gamesprite('backgr.jpg', 383, 8, 165, 304)
scrtwall14 = Gamesprite('backgr.jpg', 14, 303, 165, 0)
scrtwall15 = Gamesprite('backgr.jpg', 17, 350, 104, 0)
while run:
    window.fill(background)
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP or e.key == K_w:
                Player.yspeed = -5
                Player2.yspeed = -5
                scrtplayer1.yspeed = -5
            elif e.key== K_DOWN or e.key == K_s:
                Player.yspeed = 5
                Player2.yspeed = 5
                scrtplayer1.yspeed = 5
            elif e.key == K_LEFT or e.key == K_a:
                Player.xspeed = -5
                Player2.xspeed = -5
                scrtplayer1.xspeed = -5
            elif e.key == K_RIGHT or e.key == K_d:
                Player.xspeed = 5
                Player2.xspeed = 5
                scrtplayer1.xspeed = 5
        elif e.type == KEYUP:
            if e.key == K_UP or e.key == K_w:
                Player.yspeed = 0
                Player2.yspeed = 0
                scrtplayer1.yspeed = 0
            elif e.key == K_DOWN or e.key == K_s:
                Player.yspeed = 0
                Player2.yspeed = 0
                scrtplayer1.yspeed = 0
            elif e.key == K_LEFT or e.key == K_a:
                Player.xspeed = 0
                Player2.xspeed = 0
                scrtplayer1.xspeed = 0
            elif e.key == K_RIGHT or e.key == K_d:
                Player.xspeed = 0
                Player2.xspeed = 0
                scrtplayer1.xspeed = 0
    if not_ended != False:    
        if restart == True:
            level = 1
            scrtlvl = 0
            Player.rect.x = 50
            Player.rect.y = 450
            Player2.rect.x = 20
            Player2.rect.y = 15
            scrtplayer1.rect.x = 350
            scrtplayer1.rect.y = 245
            sleep(5)
            restart = False

        if level == 1:  
            
            window.fill(background)
            time.delay(5)          
            Player.reset()
            Player.update()
            Enemy.reset()
            Enemy.update()
            door1.reset()
            wall2.reset()
            wall4.reset()
            wall5.reset()
            wall6.reset()
            
            wall9.reset()
            wall8.reset()
            wall7.reset()
            wall1.reset()
            wall3.reset()
            
            
            if sprite.collide_rect(Player, Enemy):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            
            elif sprite.collide_rect(Player, door1):
                level = 2
            elif sprite.collide_rect(Player, wall1):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player, wall2):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player, wall3):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            
            elif sprite.collide_rect(Player, wall4):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player, wall5):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player, wall6):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player, wall7):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player, wall8):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player, wall9):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))

            if Enemy.rect.y >= 300:
                Enemy.yspeed = -3
            elif Enemy.rect.y <= 200:
                Enemy.yspeed = 3
            if Player.rect.y < 70 and Player.rect.y > 0 and Player.rect.x > 700:
                scrtlvl = 1
            elif Player.rect.y == 500:
                not_ended = False
                window.blit(lose,(250,350))
            elif Player.rect.y == -100:
                not_ended = False
                window.blit(lose,(250,350))
            elif Player.rect.x == -10:
                not_ended = False
                window.blit(lose,(250,350))
            elif Player.rect.x == 800:
                not_ended = False
                window.blit(lose,(250,350))

        if scrtlvl == 1:
            window.fill(background)
            time.delay(5)
            Player.xspeed = 0
            Player2.xspeed = 0
            Player2.yspeed = 0
            Player.yspeed = 0
            scrtplayer1.reset()
            scrtplayer1.update()
            zapiska1.reset()
            scrtwall1.reset()
            scrtwall2.reset()
            scrtwall3.reset()
            scrtwall4.reset()
            scrtwall5.reset()
            scrtwall6.reset()
            scrtwall7.reset()
            scrtwall8.reset()
            scrtwall9.reset()
            scrtwall10.reset()
            scrtwall11.reset()
            scrtwall12.reset()
            scrtwall13.reset()
            scrtwall14.reset()
            scrtwall15.reset()

            if scrtplayer1.rect.y == 500:
                not_ended = False
                window.blit(lose,(250,350))
            elif scrtplayer1.rect.y == -100:
                not_ended = False
                window.blit(lose,(250,350))
            elif scrtplayer1.rect.x == -10:
                not_ended = False
                window.blit(lose,(250,350))
            elif scrtplayer1.rect.x == 800:
                not_ended = False
                window.blit(lose,(250,350))
            if sprite.collide_rect(scrtplayer1, zapiska1):
                suzhet = 1
                window.blit(scrtlvlwin,(250,350))
                zapiska1.rect.x = 1000
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall1):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall2):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall3):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall4):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall5):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall6):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall7):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall8):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall9):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall10):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall11):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall12):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall13):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall14):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
            elif sprite.collide_rect(scrtplayer1, scrtwall15):
                window.blit(scrtlvllose, (250, 350))
                time.delay(500)
                scrtlvl = 0
                level = 1
        if level == 2:
            window.fill(background)
            time.delay(5)
            Player2.reset()
            Player2.update()
            Enemy2.reset()
            Enemy2.update()
            door2.reset()
            wall10.reset()
            wall11.reset()
            wall12.reset()
            wall13.reset()
            wall14.reset()
            wall15.reset()
            wall16.reset()
            wall17.reset()
            wall18.reset()
            wall19.reset()
            wall20.reset()
            wall21.reset()
            wall22.reset()
            wall23.reset()
            if sprite.collide_rect(Player2, Enemy2):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            
            elif sprite.collide_rect(Player2, door2):
                window.blit(winimg, (0,0))
                window.blit(playerimg, (400, 250))
                window.blit(win,(250,350))
                level = 2
            elif sprite.collide_rect(Player2, wall10):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall11):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall12):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall13):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall14):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall15):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall16):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall17):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall18):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall19):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall20):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall21):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall22):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            elif sprite.collide_rect(Player2, wall23):
                not_ended = False
                window.blit(lehasm,(-300,-300))
                mixer.music.play(0)
                window.blit(lose,(100,350))
            if Enemy2.rect.y >= 400:
                Enemy2.yspeed = -3
                time.delay(5)
            elif Enemy2.rect.y <= 200:
                Enemy2.yspeed = 3
                time.delay(5)
            if Enemy2.rect.x >= 650:
                Enemy2.xspeed = -7
                time.delay(5)
            elif Enemy2.rect.x <= 50:
                Enemy2.xspeed = 7
                time.delay(5)          
            if Player2.rect.y == 500:
                not_ended = False
                window.blit(lose,(250,350))
            elif Player2.rect.y == -100:
                not_ended = False
                window.blit(lose,(250,350))
            elif Player2.rect.x == -10:
                not_ended = False
                window.blit(lose,(250,350))
            elif Player2.rect.x == 700:
                not_ended = False
                window.blit(lose,(250,350))
        display.update()
        timer.tick(60)