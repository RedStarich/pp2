import pygame
from typing import Tuple
import math

width, height = 640,480


class Figure():
    layers = []
    def __init__(self, color:Tuple[int,int,int], screen : pygame.surface.Surface, draw_size : int):
        #set figure
        self.color = color
        self.layer = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        self.screen = screen
        self.drawn = False
        self.added_to_layers = False
        self.draw_size = draw_size

    def add_to_layers(self):
        Figure.layers.append(self)
        Figure.layers = Figure.layers[-500:]

    @classmethod
    def draw_all(cls):
        for inst in cls.layers:
            inst.screen.blit(inst.layer, (0,0))



class Circle(Figure):
    enable = False

    def __init__(self, color : Tuple[int, int, int], screen : pygame.surface.Surface, draw_size : int):
        super().__init__(color, screen, draw_size)
        self.radius = 0
        self.center = None
    
    def change_size(self, direction : int):
        #circle size control

        if direction > 0 and self.radius > 0:
            self.draw_size = min(math.ceil(self.radius), self.draw_size + 2)
        elif direction < 0 and self.radius > 0:
            self.draw_size = max(5, self.draw_size - 2)

    
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
        pygame.draw.circle(self.screen, self.color, self.center, self.radius, self.draw_size)
       
        
    def draw_on_layer(self):
        #drawing the current circle on its layer and adding it to the Figure class's layers list
        pygame.draw.circle(self.layer, self.color, self.center, self.radius, self.draw_size)
        self.add_to_layers()


class Palette():
    '''
    Palette class. Used to activate color selection by blitting a spectrum image and returning a color tuple on mouse click
    '''
    enable = False
    def __init__(self, screen : pygame.surface.Surface):
        self.screen = screen
        self.spectrum = pygame.image.load("rgb.jpg")
        self.spectrum_rect = self.spectrum.get_rect(center = (180, 196))
    
    def draw_spectrum(self):
        #creating an interactive color selection button
        self.spectrum_button = self.screen.blit(self.spectrum, self.spectrum_rect)
    def select_color(self, pressed : Tuple[bool, bool, bool], mouse_pos : Tuple[int, int], current_color : Tuple[int,int,int]):
        #if LMB is pressed on the position of the spectrum button, we return a color value at this point
        #then we automatically swithc off the palette and color selection
        if pressed[0] and self.spectrum_button.collidepoint(mouse_pos):
            Palette.enable = False
            color = self.spectrum.get_at((mouse_pos[0], mouse_pos[1]-80))
            if color == None:
                return current_color
            else:
                return color
        else:
            return current_color




class NRect(Figure):
    '''
    The class NRect - child class of Figure. Used to draw simple rectangles.
    Named NRect to avoid confusion with pygame's Rect class
    Has class var enable that turns on/off the drawing rectangles mode
    Has adjustable thickness
    '''
    enable = False

    def __init__(self, color : Tuple[int, int, int], screen : pygame.surface.Surface, draw_size : int):
        '''
        Initializing as a child of Figure class 
        Setting the start_point to None as we did not put the first point of the rectangle
        '''
        super().__init__(color, screen, draw_size)
        self.start_point = None

    def change_size(self, direction : int):
        '''
        Changes the thickness of border lines(affect only the next rects). The min value is 5, the max value of thickness is the largest side of the rectangle
        '''
        if direction > 0 and self.start_point != None:
            self.draw_size = min(max(self.rect.width, self.rect.height), self.draw_size + 2)
        elif direction < 0 and self.start_point != None:
            self.draw_size = max(5, self.draw_size - 2)


    def draw(self, mouse_pressed : bool):
        '''
        Function that draws a rectangle based on the current mosue position
        If the rectangle is drawn and is not added to the layers list of the parent class, we draw it on the layer and quit the function
        If we have already set the rectangle's size and its position is not empty, we mark it as a drawn rectangle
        '''
        if self.drawn and not self.added_to_layers:
            self.draw_on_layer()
            self.added_to_layers = True
            return

        if not mouse_pressed and self.start_point != None:
            self.drawn = True
            return
        #get the mouse's position
        pos = pygame.mouse.get_pos()

        #if we are setting the size for the first time, the mouse's position as the start point
        if self.start_point == None:
            self.start_point = pos
        
        #get the difference between the starting position and the current mouse position
        x = min(self.start_point[0], pos[0])
        y = min(self.start_point[1], pos[1])
        
        #setting the width and the height of the rect
        width = max(pos[0], self.start_point[0]) - x
        height = max(pos[1], self.start_point[1]) - y

        self.rect = pygame.Rect(x, y, width, height)   #adjustable rect
        pygame.draw.rect(self.screen, self.color, self.rect, self.draw_size)    #when we are in the adjusting/drawing/setting size mode we draw the rect on the screen, and only when we finished doing so, we draw everything on the corresponding layer

    def draw_on_layer(self):
        #drawing the current instance on its corresponding layer, and then adding it to the parent class' layers list
        pygame.draw.rect(self.layer, self.color, self.rect, self.draw_size)
        self.add_to_layers()



class Eraser(Figure):

    def __init__(self, bg_color : Tuple[int,int,int], screen : pygame.surface.Surface, draw_size : int):
        super().__init__(bg_color, screen, draw_size)
        self.enable = False
        self.radius = draw_size
        self.points = []

    def change_size(self, direction : int):
        if direction > 0:
            self.radius = min(self.radius, self.draw_size + 2)
        elif direction < 0:
            self.radius = max(15, self.draw_size - 2)
 

    def erase(self, mouse_pos : Tuple[int,int]):
        pygame.draw.circle(self.layer, self.color, mouse_pos, self.radius)
        

    def draw_on_layer(self):
        self.add_to_layers()

    
def drawLine(screen, index, start, end, width, color_mode):
    #default drawing function

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):            
        progress = 1.0 * i /iterations
        aprogress = 1 - progress

        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color_mode, (x,y), width)


def change_size_all(draw_size : int, circle : Circle, nrect : NRect, eraser : Eraser, direction : int):
    #every figure's size is changed correspondingly with their own function (polymorphism, i guess)
    for el in (circle, nrect, eraser):
        el.change_size(direction)
    #changin the size of the default mode
    if direction == 1:
        draw_size = min(40, draw_size + 2)
    elif direction == -1:
        draw_size =  max(5, draw_size - 2)
    return draw_size