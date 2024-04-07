#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
BONUS = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
restart_msg = font.render("Press 'space' to restart", True, BLACK)
 
#load background road
background = pygame.image.load("Road.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#Coins
#Coin 10 tenge
class Coin1(pygame.sprite.Sprite):
    #generation, spawn
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    #movement
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#Coin 50 tenge
class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
#Coin 100 tenge
class Coin3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin3.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#Enemy car
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#PLayer car
class Player(pygame.sprite.Sprite):
    #generation, spawn
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    #movement
    #left key - turn left
    #right key - turn right
    def move(self):
        pressed_keys = pygame.key.get_pressed()         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin1()
C2 = Coin2()
C3 = Coin3()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins1 = pygame.sprite.Group()
coins1.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


#Adding custom user event for Speed increment 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    #Text on screen
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    bonuses = font_small.render(str(BONUS), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(bonuses, (SCREEN_WIDTH-80,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill()
          time.sleep(2)
          pygame.quit()
          sys.exit()   

    #To be run if collision occurs between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins1):
        #if a player collects N number of bonus score or more, the speed becomes proportional to the score
        if BONUS >= 500:
            SPEED = BONUS/100 
        pygame.mixer.Sound('catch.mp3').play()
        coin = pygame.sprite.spritecollideany(P1, coins1)  # Get the collided coin
        if coin:
            if isinstance(coin, Coin1):
                BONUS += 10
            elif isinstance(coin, Coin2):
                BONUS += 50
            elif isinstance(coin, Coin3):
                BONUS += 100
            coin.kill()  # Remove the collided coin
            # Generate new coin that hasn't been collected yet and doesn't spawn inside the player
            available_coins = [C1, C2, C3]
            collected_coins = [sprite for sprite in coins1 if sprite.rect == coin.rect]
            available_coins = [coin for coin in available_coins if coin not in collected_coins]
            if available_coins:
                new_coin = random.choice(available_coins)
                new_coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
                # Check if new coin collides with the player
                while pygame.sprite.spritecollideany(new_coin, all_sprites):
                    new_coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
                coins1.add(new_coin)
                all_sprites.add(new_coin)

    
    #screen update
    pygame.display.update()
    FramePerSec.tick(FPS)