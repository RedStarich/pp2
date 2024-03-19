import pygame as pg
import time
import datetime

pg.init()

screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()

pg.display.set_caption("Mickey Clock")

sec = pg.image.load("img/lefty.png").convert_alpha()
mins = pg.image.load("img/righty.png").convert_alpha()
rectsec = sec.get_rect()
rectmin = mins.get_rect()
rectmin.center = rectsec.center = 400, 400

background = pg.image.load("img/bodyclock.png")
ingame = True

pos1, pos2 = 0, 0

while ingame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            ingame = False

    time = datetime.datetime.now()
    minuteTime = time.minute
    secondTime = time.second

    pos1 = -minuteTime*6
    leg1 = pg.transform.rotate(mins, pos1)
    rect1 = leg1.get_rect()
    rect1.center = rectmin.center

    pos2 = -secondTime*6
    leg2 = pg.transform.rotate(sec, pos2)
    rect2 = leg2.get_rect()
    rect2.center = rectsec.center

    screen.blit(background, (-300, -150))
    screen.blit(leg1, rect1)
    screen.blit(leg2, rect2)
    
    pg.display.flip()
    clock.tick(60)