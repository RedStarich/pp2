import pygame as pg 
import random
pg.init()

W, H = 1200, 700
FPS = 60

#screen
screen = pg.display.set_mode((W, H), pg.RESIZABLE)
clock = pg.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 400
paddleH = 25
paddleSpeed = 20
paddle_x = W//2 - paddleW//2

paddle = pg.Rect(paddle_x, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
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
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
strong_blocks = [pg.Rect(120*i, 400, 10, 10) for i in range(10)]
bonus_blocks = [pg.Rect(10 + 120*i, 120, 110, 50) for i in range(10)]

soft_blocks = [pg.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (2, 4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 

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


while not done:
    for event in pg.event.get():
        if event.type == INC_SPEED:
            ballSpeed += 0.5
            paddleW -= 10 if paddleW > 50 else 0
            paddle = pg.Rect(paddle_x, H - paddleH - 30, paddleW, paddleH)
    
        if event.type == pg.QUIT:
            done = True

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
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
    #Collision blocks
    hitIndex = ball.collidelist(soft_blocks)
    hit_strong = ball.collidelist(strong_blocks)
    hit_bonus = ball.collidelist(bonus_blocks)

    if hit_strong != -1:
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