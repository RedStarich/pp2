import pygame as pg
pg.font.init()
songs=["1.mp3","2.mp3", "3.mp3"]

screen = pg.display.set_mode((800, 600))
ingame = True
onplay=False
q=0
bg = (0, 0, 0)
text_color = (255, 255, 255)
pg.display.set_caption('Music Player')
fontObj = pg.font.Font(None, 32)
textSufaceObj = fontObj.render('/play = Tab /back = left_arrow /next = right-arrow /pause = space', True, text_color, None)
screen.fill(bg)
screen.blit(textSufaceObj, (0, 0))
pg.display.update()
pg.mixer.init()
while ingame:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                ingame = False
            if event.type==pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                      exit()
                if event.key == pg.K_TAB:
                            pg.mixer.music.load(songs[q])
                            pg.mixer.music.play(0)
                            onplay=True
                if event.key ==pg.K_RIGHT and onplay==True:
                    q+=1
                    if q>len(songs)-1:
                        q=0
                    pg.mixer.music.stop()
                    pg.mixer.music.load(songs[q])
                    pg.mixer.music.play()
                if event.key ==pg.K_LEFT and onplay==True:
                    q-=1
                    if q<0:
                        q=len(songs)-1
                    pg.mixer.music.stop()
                    pg.mixer.music.load(songs[q])
                    pg.mixer.music.play()
                if event.key ==pg.K_SPACE:
                    pg.mixer.music.stop()