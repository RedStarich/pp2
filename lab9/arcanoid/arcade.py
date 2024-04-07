import pygame as pg 
import random
import sys
from button import Button

pg.init()

W, H = 1200, 700
FPS = 60
a = 600
b = 30
c = 6

#screen
screen = pg.display.set_mode((W, H), pg.RESIZABLE)
clock = pg.time.Clock()
done = False
bg = (0, 0, 0)



def get_font(size): # Returns Press-Start-2P in the desired size
    return pg.font.Font("assets/font.ttf", size)



def game_play(a, b, c):
    #paddle
    paddleW = a
    paddleH = 60
    initialpaddlespeed = 20
    paddleSpeed = 20
    paddle_x = W//2 - paddleW//2

    paddle = pg.Rect(paddle_x, H - paddleH - 30, paddleW, paddleH)


    #Ball
    ballRadius = b #30
    ballSpeed = c #6
    initialballspeed = 6
    INC_SPEED = pg.USEREVENT + 1
    pg.time.set_timer(INC_SPEED, 1000)

    ball_rect = int(ballRadius * 2 ** 0.5)
    ball = pg.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
    dx, dy = 1, -1

    #Game score
    game_score = 0
    game_score_fonts = pg.font.SysFont('comicsansms', 40)
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
    game_score_rect = game_score_text.get_rect()
    game_score_rect.center = (210, 20)

    #Catching sound
    collision_sound = pg.mixer.Sound('audio/catch.mp3')
    #detect collision
    def detect_collision(dx, dy, ball, rect):
        if dx > 5:
            delta_x = ball.right - rect.left
        else:
            delta_x = rect.right - ball.left
        if dy > 5:
            delta_y = ball.bottom - rect.top
        else:
            delta_y = rect.bottom - ball.top

        if abs(delta_x - delta_y) < 50:
            dx, dy = -dx, -dy
            pg.time.delay(10)
        if delta_x >= delta_y:
            pg.time.delay(10)
            dy = -dy
        elif delta_y >= delta_x:
            dx = -dx
            pg.time.delay(10)
        return dx, dy


    #block settings
    strong_blocks = [pg.Rect(120*i, 400, 50, 5) for i in range(2, 8)]
    bonus_blocks = [pg.Rect(10 + 120*i, 120, 110, 50) for i in range(10)]

    soft_blocks = [pg.Rect(10 + 120 * i, 50 + 70 * j,
            100, 50) for i in range(10) for j in range (2, 4)]
    color_list = [(random.randrange(0, 255), 
        random.randrange(0, 255),  random.randrange(0, 255))
                for i in range(10) for j in range(1, 4)] 

    #Game over Screen
    losefont = pg.font.SysFont('comicsansms', 40)
    losetext = losefont.render('Game Over', True, (255, 255, 255))
    losetextRect = losetext.get_rect()
    losetextRect.center = (W // 2, H // 2)

    #Win Screen
    winfont = pg.font.SysFont('comicsansms', 40)
    wintext = losefont.render('You win yay', True, (0, 0, 0))
    wintextRect = wintext.get_rect()
    wintextRect.center = (W // 2, H // 2)

    #pause function
    pause = False
    while True:
        for event in pg.event.get():
            if event.type == INC_SPEED and not pause:
                ballSpeed += 0.5
                paddleW -= 10 if paddleW > 90 else 0
                paddle = pg.Rect(paddle_x, H - paddleH - 30, paddleW, paddleH)
        
            if event.type == pg.QUIT:
                return

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    if not pause:  # If the game is not already paused
                        pause = True
                        ballSpeed = 0
                        paddleSpeed = 0
                    else:  # If the game is already paused
                        pause = False
                        ballSpeed = initialballspeed  # Restore original ball speed
                        paddleSpeed = initialpaddlespeed  # Restore original paddle speed



        screen.fill(bg)
        
        # print(next(enumerate(soft_blocks)))
        
        [pg.draw.rect(screen, color_list[color], block)
        for color, block in enumerate (soft_blocks)] #drawing blocks
        [pg.draw.rect(screen, (255,255,255), block)
        for block in (strong_blocks)] #drawing blocks
        [pg.draw.rect(screen, (0,255,0), block)
        for block in (bonus_blocks)] #drawing blocks
        pg.draw.rect(screen, pg.Color(255, 255, 255), paddle)
        pg.draw.circle(screen, pg.Color(255, 0, 0), ball.center, ballRadius)
        # print(next(enumerate (soft_blocks)))

        #Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        


        #Collision left
        if ball.centerx < ballRadius-5 or ball.centerx > W - ballRadius+5:
            dx = -dx
        #Collision top
        if ball.centery < ballRadius + 55: 
            dy = -dy
        #Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)
        #Collision blocks
        hitIndex = ball.collidelist(soft_blocks)
        hit_strong = ball.collidelist(strong_blocks)
        hit_bonus = ball.collidelist(bonus_blocks)

        if hit_strong != -1:
            hitRect = strong_blocks[-1]
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            collision_sound.play()

        if hit_bonus != -1:
            hitRect = bonus_blocks.pop(hit_bonus)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            ballSpeed /= 1.3
            collision_sound.play()
            

        if hitIndex != -1:
            hitRect = soft_blocks.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()
            
        #Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
        
        #Win/lose screens
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
        elif not len(soft_blocks):
            screen.fill((255,255, 255))
            screen.blit(wintext, wintextRect)

        #Paddle Control
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] and paddle.left > 0:
            paddle_x -= paddleSpeed
            paddle.left -= paddleSpeed
        if key[pg.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed
            paddle_x += paddleSpeed


        pg.display.flip()
        clock.tick(FPS)

def options():
    while True:
        OPTIONS_MOUSE_POS = pg.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT3 = get_font(75).render("HOW TO PLAY", True, "Black")
        OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(640, 120))

        OPTIONS_TEXT = get_font(45).render("Paddle: left & right key.", True, "Black")
        OPTIONS_TEXT2 = get_font(45).render("Pause on/off: press 'P'", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 290))
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 390))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        screen.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        screen.blit(OPTIONS_TEXT3, OPTIONS_RECT3)

        OPTIONS_BACK = Button(image=None, pos=(200, 600), 
                            text_input="BACK", font=get_font(25), base_color="Black", hovering_color="Green")
        HARDCORE = Button(image=None, pos=(1000, 600), 
                            text_input="HARDCORE MODE", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)
        HARDCORE.changeColor(OPTIONS_MOUSE_POS)
        HARDCORE.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if HARDCORE.checkForInput(OPTIONS_MOUSE_POS):
                    game_play(90, 5, 10)

        pg.display.update()

def main_menu():
    while True:
        screen.fill(bg)

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pg.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pg.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="HOW TO PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pg.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_play(600, 30, 6)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()

main_menu()