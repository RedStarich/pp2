import pygame as pg
pg.init()
screen = pg.display.set_mode((400, 400))
ingame = True
x = 25
y = 25
clock = pg.time.Clock()
while ingame:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        ingame = False
        pressed = pg.key.get_pressed()
        if pressed[pg.K_ESCAPE]: done=True
        if pressed[pg.K_UP]: y -= 20
        if pressed[pg.K_DOWN]: y += 20
        if pressed[pg.K_LEFT]: x -= 20
        if pressed[pg.K_RIGHT]: x += 20
        if x>=375: x-=20
        if x<=25: x+=20
        if y>=375: y-=20
        if y<=25: y+=20
        screen.fill((255,255,255))
        pg.draw.circle(screen,(255,0,0),(x,y), 25)
        pg.display.flip()
        clock.tick(60)