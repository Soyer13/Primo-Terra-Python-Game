import pygame
from button import Button
from settings import *
class Slider():
    def __init__(self,posx):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.Button_Font = pygame.font.Font(UI_FONT,80)
        self.slider_position = posx
        self.is_dragging = False
        
    
    def draw_slider(self,window,posytion,positionX,positionY,length ):
        pygame.draw.line(window, 'green', (positionX, positionY), (positionX + length, positionY), 5)
        pygame.draw.circle(window, self.white, (50 + posytion, positionY), 15)

    def map_value(self,slider_pos, posx, length, StartValue, MaxValue):
        return StartValue + (MaxValue - StartValue) * ((slider_pos - posx) / (length - posx))


    def slider(self,window,event,slider_position,posx,posy,length):
        self.slider_position = float(posx) + float(slider_position)
        slider_positionX = posx
        slider_positionY = posy
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                if posx <= self.mouse_x <= posx + length and posy - 20 <= self.mouse_y <= posy + 20:
                    self.is_dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.is_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if self.is_dragging:
                    self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                    if posx <= self.mouse_x <= posx + length:
                        self.slider_position = self.mouse_x - posx
        ''' if IntroButton.draw(window):
        running =  False'''
        value = self.map_value(self.slider_position, slider_positionX, length, 0, 2)
        window.fill(self.black)
        self.draw_slider(window ,self.slider_position,slider_positionX,slider_positionY,length )
        pygame.display.update()

        print("Obecna wartość suwaka:", value)

        return value


