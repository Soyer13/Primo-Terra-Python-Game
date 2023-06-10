import pygame
from settings import *

class Napis():
    def __init__(self):
        self.startad_time = 0
        self.adisStart = False
        
        self.ad = True
    def napis(self,displayad_time,path,screen):
        
        ad_surf = pygame.image.load(path).convert()
        ad_surf = pygame.transform.scale(ad_surf, (WIDTH, HEIGTH))
        ad_rect = ad_surf.get_rect(topleft = (0,0))
        if self.ad == True:
            if self.adisStart == False:
                self.startad_time = pygame.time.get_ticks()
                self.adisStart = True
            currentad_time = pygame.time.get_ticks()
            if currentad_time - self.startad_time >= displayad_time:
                self.ad = False	
            screen.blit(ad_surf,ad_rect)
        else:
            self.adisStart = False
            self.startad_time = 0
            self.ad = True
        
        if self.ad == False:
            
            return False
        return self.ad
    