import pygame
from paint_module import *

rect_select_img = pygame.image.load("rectt.png")
circle_select_img = pygame.image.load("circ.png")
palette_select_img = pygame.image.load("palette.png")
eraser_select_img = pygame.image.load("eraser.png")

rect_select_rect = rect_select_img.get_rect(center = (40,40))
circle_select_rect = circle_select_img.get_rect(center = (120,40))
palette_select_rect = palette_select_img.get_rect(center = (200,40))
eraser_select_rect = eraser_select_img.get_rect(center = (280,40))

width = 800
height = 800

def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()
    
    #initial parameters
    draw_size = 5
    points = []
    draw_mode = True
    
    #color parameters
    color_mode = (0,255,0)
    bg_color = (0,0,0)
    

    #initializing the class instances
    canvas = Figure(bg_color, screen, draw_size)
    circle = Circle(color_mode, screen, draw_size)
    nrect = NRect(color_mode, screen, draw_size)
    palette = Palette(screen)
    eraser = Eraser(bg_color, screen, draw_size)
 
    while True:
        pressed_key = pygame.key.get_pressed()
        #hotkeys
        alt = pressed_key[pygame.K_LALT] or pressed_key[pygame.K_RALT]
        ctrl = pressed_key[pygame.K_LCTRL] or pressed_key[pygame.K_RCTRL]

        screen.fill(bg_color) 
        canvas.draw_all()

        #mouse parametes
        pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        
        if Circle.enable:
            #circle -> draw function
            circle.draw(pressed[0])
            #if circle is drawn -> create a new instance
            if circle.drawn and circle.added_to_layers:
                circle = Circle(color_mode, screen, draw_size)
        elif NRect.enable:
            #rectangle handle
            nrect.draw(pressed[0])
            if nrect.drawn and nrect.added_to_layers:
                nrect = NRect(color_mode, screen, draw_size)

        elif eraser.enable:
            #eraser
            if pressed[0]:
                eraser.erase(mouse_pos)
            else:
                eraser.draw_on_layer()

        elif Palette.enable:
            #choose color from pallette
            palette.draw_spectrum()
            #color select
            color_mode = palette.select_color(pressed, mouse_pos, color_mode)
            #delete last handle
            if color_mode != None:
                color_mode = color_mode[:3]
        else:
            #default mode
            draw_mode = True
            i = 0
            while i < len(points) - 1:
                drawLine(screen, i, points[i], points[i + 1], draw_size, color_mode)
                i += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl:
                    return
                if event.key == pygame.K_F4 and alt:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == 1:
                    draw_mode = True

            #buttons press handle 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if circle_select_button.collidepoint(event.pos):
                    #mode switch
                    Circle.enable = not Circle.enable
                    NRect.enable = eraser.enable = Palette.enable = draw_mode = False
                    points = []
                elif rect_select_button.collidepoint(event.pos):
                    NRect.enable = not NRect.enable
                    Circle.enable = eraser.enable = Palette.enable = draw_mode = False
                    points = []
                elif eraser_select_button.collidepoint(event.pos):
                    eraser = Eraser(bg_color, screen, draw_size)
                    eraser.enable = not eraser.enable
                    Circle.enable = NRect.enable = Palette.enable =  draw_mode = False
                    points = []
                elif palette_select_button.collidepoint(event.pos):
                    Palette.enable = not Palette.enable
                    Circle.enable = NRect.enable = eraser.enable = draw_mode =  False
                    points = []
              
            #brush handle
            elif event.type == pygame.MOUSEMOTION and draw_mode:
                if pressed[0]:
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]

            elif event.type == pygame.MOUSEWHEEL:
                #brush size
                draw_size = change_size_all(draw_size, circle, nrect, eraser, direction=event.dict["y"])
        

        #mode change - rect/circle/brush/eraser/palette
        pygame.draw.rect(screen, (0,0,0), (0,0,320,80))
        rect_select_button = screen.blit(rect_select_img, rect_select_rect)
        circle_select_button = screen.blit(circle_select_img, circle_select_rect)
        palette_select_button = screen.blit(palette_select_img, palette_select_rect)
        eraser_select_button = screen.blit(eraser_select_img, eraser_select_rect)

        pygame.display.flip()
        
        clock.tick(60)
main()