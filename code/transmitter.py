import pygame
from settings import *
from ui import UI
from debug import debug
class Transmitter(pygame.sprite.Sprite):
    def __init__(self,player,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,y_offset)
        
        self.player = player
        self.isActive = False
        
        
        self.ui = UI()
        
    def get_player_distance_direction(self,player):
    
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        
        if distance >0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        
        return(distance,direction)
    
    def get_status(self,player):
        distance = self.get_player_distance_direction(player)[0]   
        if distance <= 100:
            self.Active = self.ui.show_interactions()
            if self.Active == True:
                self.isActive = True
                debug('Aktywny',HEIGTH/4, WIDTH/2.5)

    def update(self):
        self.get_status(self.player)