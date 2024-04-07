import pygame as pg
from paint_module import *

#load images
quadro_png = pg.image.load("quadro.png")
circ_png = pg.image.load("circ.png")
rgb_png = pg.image.load("rgb.png")
rubber_png = pg.image.load("rubber.png")
squar = pg.image.load("square.png")
e_tring = pg.image.load("triangle.png")
rho = pg.image.load("rhomb.png")
r_tring = pg.image.load("r_triangle.png")

#get shapes as rectangles
quadrad = quadro_png.get_rect(center = (40,40))
circ = circ_png.get_rect(center = (120,40))
rgb_choice = rgb_png.get_rect(center = (200,40))
clearer = rubber_png.get_rect(center = (280,40))
squared = squar.get_rect(center = (360,40))
e_triangled = e_tring.get_rect(center = (440,40))
rhombed = rho.get_rect(center = (520,40))
r_triangled = r_tring.get_rect(center = (600,40))


W = 700
H = 700

def main():
    pg.init()
    screen = pg.display.set_mode((W,H))
    clock = pg.time.Clock()
    
    #initial parameters
    d_size = 10
    dots = []
    brush = True
    
    #color parameters
    col = (0,255,0)
    bg_color = (0,0,0)
    

    #initializing the class instances
    canvas = Figure(bg_color, screen, d_size)
    circle = Circle(col, screen, d_size)
    quadr = Quadr(col, screen, d_size)
    rgb = RGB_thing(screen)
    rubber = Rubber(bg_color, screen, d_size*4)
    square = Square(col, screen, d_size)
    r_triangle = R_Triangle(col, screen, d_size)
    e_triangle = E_Triangle(col, screen, d_size)
    rhombus = Rhombus(col, screen, d_size)
 
    while True:
        klava = pg.key.get_pressed()
        #hotkeys
        alt = klava[pg.K_LALT] or klava[pg.K_RALT]
        ctrl = klava[pg.K_LCTRL] or klava[pg.K_RCTRL]

        screen.fill(bg_color) 
        canvas.draw_all()

        #mouse parametes
        pressed = pg.mouse.get_pressed()
        mouse_pos = pg.mouse.get_pos()


        if rubber.enable:
            #rubber
            if pressed[0]:
                rubber.erase(mouse_pos)
            else:
                rubber.draw_on_layer()   

        elif Circle.enable:
            #circle
            circle.draw(pressed[0])
            if circle.drawn and circle.added_to_layers:
                circle = Circle(col, screen, d_size)
        
        elif Rhombus.enable:
            #Rhombus
            rhombus.draw(pressed[0])
            if rhombus.drawn and rhombus.added_to_layers:
                rhombus = Rhombus(col, screen, d_size)
        
        elif R_Triangle.enable:
            #Right Triangle
            r_triangle.draw(pressed[0])
            if r_triangle.drawn and r_triangle.added_to_layers:
                r_triangle = R_Triangle(col, screen, d_size)
        
        elif Square.enable:
            #Square
            square.draw(pressed[0])
            if square.drawn and square.added_to_layers:
                square = Square(col, screen, d_size)
        
        elif E_Triangle.enable:
            #Equaliteral Triangle
            e_triangle.draw(pressed[0])
            if e_triangle.drawn and e_triangle.added_to_layers:
                e_triangle = E_Triangle(col, screen, d_size)

        elif Quadr.enable:
            #Rectangle
            quadr.draw(pressed[0])
            if quadr.drawn and quadr.added_to_layers:
                quadr = Quadr(col, screen, d_size)

        elif RGB_thing.enable:
            #choose color from pallette
            rgb.draw_spectrum()
            #color select
            col = rgb.select_color(pressed, mouse_pos, col)
            #delete last handle
            if col != None:
                col = col[:3]
        else:
            #default mode
            brush = True
            i = 0
            while i < len(dots)-1:
                drawLine(screen, i, dots[i], dots[i+1], d_size, col)
                i += 1

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and ctrl:
                    return
                if event.key == pg.K_F4 and alt:
                    return
                if event.key == pg.K_ESCAPE:
                    return
                if event.key == 1:
                    brush = True

            #buttons press handle 
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if button_circ.collidepoint(event.pos):
#Circle             #mode switch
                    Circle.enable = not Circle.enable
                    Quadr.enable = rubber.enable = RGB_thing.enable = brush = False
                    E_Triangle.enable = R_Triangle.enable = Rhombus.enable = Square.enable = False
                    dots = []
                elif button_quadrant.collidepoint(event.pos):
#Rectangle
                    Quadr.enable = not Quadr.enable
                    Circle.enable = rubber.enable = RGB_thing.enable = brush = False
                    E_Triangle.enable = R_Triangle.enable = Rhombus.enable = Square.enable = False
                    dots = []
                elif button_clearer.collidepoint(event.pos):
#Eraser, rubber
                    rubber = Rubber(bg_color, screen, d_size)
                    rubber.enable = not rubber.enable
                    Circle.enable = Quadr.enable = RGB_thing.enable =  brush = False
                    E_Triangle.enable = R_Triangle.enable = Rhombus.enable = Square.enable = False
                    dots = []
#Palette
                elif button_rgb.collidepoint(event.pos):
                    RGB_thing.enable = not RGB_thing.enable
                    Circle.enable = Quadr.enable = rubber.enable = brush =  False
                    E_Triangle.enable = R_Triangle.enable = Rhombus.enable = Square.enable = False

                    dots = []
                elif button_rhomb.collidepoint(event.pos):
#Rhombus
                    Rhombus.enable = not Rhombus.enable
                    Circle.enable = Quadr.enable = rubber.enable = brush =  False
                    E_Triangle.enable = R_Triangle.enable = Square.enable = False
                    dots = []
                elif button_r_tr.collidepoint(event.pos):
#Right Triangle 
                    R_Triangle.enable = not R_Triangle.enable
                    Circle.enable = Quadr.enable = rubber.enable = brush =  False
                    E_Triangle.enable = Square.enable = Rhombus.enable = False
                    dots = []
                elif button_e_tr.collidepoint(event.pos):
#Equaliterate Trianlge 
                    E_Triangle.enable = not E_Triangle.enable
                    Circle.enable = Quadr.enable = rubber.enable = brush =  False
                    Square.enable = R_Triangle.enable = Rhombus.enable = False
                    dots = []
                elif button_sq.collidepoint(event.pos):
#Square                    
                    Square.enable = not Square.enable
                    Circle.enable = Quadr.enable = rubber.enable = brush =  False
                    E_Triangle.enable = R_Triangle.enable = Rhombus.enable = False
                    dots = []
              
            #brush handle
            elif event.type == pg.MOUSEMOTION and brush:
                if pressed[0]:
                    position = event.pos
                    dots = dots + [position]
                    dots = dots[-256:]


        #mode change - rect/circle/brush/rubber/rgb
        pg.draw.rect(screen, (0,0,0), (0,0,320,80))
        button_quadrant = screen.blit(quadro_png, quadrad)
        button_circ = screen.blit(circ_png, circ)
        button_rgb = screen.blit(rgb_png, rgb_choice)
        button_clearer = screen.blit(rubber_png, clearer)
        button_rhomb = screen.blit(rho, rhombed)
        button_r_tr = screen.blit(r_tring, r_triangled)
        button_e_tr = screen.blit(e_tring, e_triangled)
        button_sq = screen.blit(squar,squared)



        pg.display.flip()
        
        clock.tick(60)
main()