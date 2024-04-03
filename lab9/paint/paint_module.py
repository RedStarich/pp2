import pygame
from typing import Tuple
import math

QW, QH = 640,480


class Figure():
    layers = []
    def __init__(self, color:Tuple[int,int,int], screen : pygame.surface.Surface, d_size : int):
        #set figure
        self.color = color
        self.layer = pygame.Surface((QW, QH), pygame.SRCALPHA, 32)
        self.screen = screen
        self.drawn = False
        self.added_to_layers = False
        self.d_size = d_size

    def add_to_layers(self):
        Figure.layers.append(self)
        Figure.layers = Figure.layers[-500:]

    @classmethod
    def draw_all(cls):
        for inst in cls.layers:
            inst.screen.blit(inst.layer, (0,0))

class Circle(Figure):
    enable = False

    def __init__(self, color : Tuple[int, int, int], screen : pygame.surface.Surface, d_size : int):
        super().__init__(color, screen, d_size)
        self.radius = 0
        self.center = None
    
    def change_size(self, dir : int):
        #circle size control

        if dir > 0 and self.radius > 0:
            self.d_size = min(math.ceil(self.radius), self.d_size + 2)
        elif dir < 0 and self.radius > 0:
            self.d_size = max(5, self.d_size - 2)

    
    def draw(self, mouse_pressed : bool):
        #create circle

        if self.drawn and not self.added_to_layers:
            self.draw_on_layer()
            self.added_to_layers = True
            return
        if not mouse_pressed and self.center != None:
            self.drawn = True
            return
        #getting the mouse position
        pos = pygame.mouse.get_pos()
        if self.center == None:
            #setting the mouse position as center if we have entered the function for the firss time for this instance
            self.center = pos
        
        #calculating the radius using the distance formula
        self.radius = math.sqrt((pos[0] - self.center[0])**2 + (pos[1] - self.center[1])**2)
        #drawing the circle on the screen not on its layaer yet to avoid creating too much layers
        pygame.draw.circle(self.screen, self.color, self.center, self.radius, self.d_size)
       
        
    def draw_on_layer(self):
        #drawing the current circle on its layer and adding it to the Figure class's layers list
        pygame.draw.circle(self.layer, self.color, self.center, self.radius, self.d_size)
        self.add_to_layers()


class RGB_thing():
    enable = False
    def __init__(self, screen : pygame.surface.Surface):
        self.screen = screen
        self.spectrum = pygame.image.load("rgb.jpg")
        self.spectrum_rect = self.spectrum.get_rect(center = (180, 196))
    
    def draw_spectrum(self):
        #creating an interactive color selection button
        self.spectrum_button = self.screen.blit(self.spectrum, self.spectrum_rect)
    def select_color(self, pressed : Tuple[bool, bool, bool], mouse_pos : Tuple[int, int], current_color : Tuple[int,int,int]):
        if pressed[0] and self.spectrum_button.collidepoint(mouse_pos):
            RGB_thing.enable = False
            color = self.spectrum.get_at((mouse_pos[0], mouse_pos[1]-80))
            if color == None:
                return current_color
            else:
                return color
        else:
            return current_color




class Quadr(Figure):
    enable = False

    def __init__(self, color : Tuple[int, int, int], screen : pygame.surface.Surface, d_size : int):
        super().__init__(color, screen, d_size)
        self.p_a = None

    def draw(self, mouse_pressed : bool):
        if self.drawn and not self.added_to_layers:
            self.draw_on_layer()
            self.added_to_layers = True
            return

        if not mouse_pressed and self.p_a != None:
            self.drawn = True
            return

        pos = pygame.mouse.get_pos()

        if self.p_a == None:
            self.p_a = pos
        
        #get the difference between the starting position and the current mouse position
        x = min(self.p_a[0], pos[0])
        y = min(self.p_a[1], pos[1])
        
        #setting the QW and the QH of the rect
        QW = max(pos[0], self.p_a[0]) - x
        QH = max(pos[1], self.p_a[1]) - y

        self.rect = pygame.Rect(x, y, QW, QH)   #adjustable rect
        pygame.draw.rect(self.screen, self.color, self.rect, self.d_size)    #when we are in the adjusting/drawing/setting size mode we draw the rect on the screen, and only when we finished doing so, we draw everything on the corresponding layer

    def draw_on_layer(self):
        #drawing the current instance on its corresponding layer, and then adding it to the parent class' layers list
        pygame.draw.rect(self.layer, self.color, self.rect, self.d_size)
        self.add_to_layers()



class Rubber(Figure):

    def __init__(self, bg_color : Tuple[int,int,int], screen : pygame.surface.Surface, d_size : int):
        super().__init__(bg_color, screen, d_size)
        self.enable = False
        self.radius = d_size
        self.points = []

    def change_size(self, dir : int):
        if dir > 0:
            self.radius = min(self.radius, self.d_size + 2)
        elif dir < 0:
            self.radius = max(15, self.d_size - 2)
 

    def erase(self, mouse_pos : Tuple[int,int]):
        pygame.draw.circle(self.layer, self.color, mouse_pos, self.radius)
        

    def draw_on_layer(self):
        self.add_to_layers()

    
def drawLine(screen, index, start, end, QW, col):

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):            
        progress = 1.0 * i /iterations
        aprogress = 1 - progress

        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, col, (x,y), QW)

