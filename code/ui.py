import pygame
from settings import * 
from player import *
from button import Button

class UI:
	def __init__(self):
		
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
		self.Gamefont = pygame.font.Font(Game_FONT,Game_FONT_SIZE)

		# bar setup 
		self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)

		# convert weapon dictionary
		self.weapon_graphics = []
		for weapon in weapon_data.values():
			path = weapon['graphic']
			weapon = pygame.image.load(path).convert_alpha()
			self.weapon_graphics.append(weapon)



	def show_bar(self,current,max_amount,bg_rect,color):
		# draw bg 
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface,color,current_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
  
  
	def show_Dead(self):
		text_surf = self.font.render(str('KONIEC'),False,TEXT_COLOR)
		x = self.display_surface.get_size()[0] /1.5
		y = self.display_surface.get_size()[1] /1.7
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(40,40))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(40,40),3)

	def show_interactions(self):
			text_surf = self.Gamefont.render(str('E'),False,TEXT_COLOR)

			'''screen_pos = (pos[0] , pos[1] + 100)
			text_rect = text_surf.get_rect(bottomright = screen_pos)'''
			x = self.display_surface.get_size()[0] /13
			y = self.display_surface.get_size()[1] /1.5
			text_rect = text_surf.get_rect(bottomright = (x,y))
   
			isE = False
			keys = pygame.key.get_pressed()
			if keys[pygame.K_e]:
				isE =True
				print('interakcja')
			else:
				isE = False
    
			if isE  == True:
				Color = '#6e6867'
			else:
				Color = UI_BG_COLOR

			pygame.draw.rect(self.display_surface,Color,text_rect.inflate(20,20))
			self.display_surface.blit(text_surf,text_rect)
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),2)
   
	def displayGameControls(self):
			'''text_surfW = self.Gamefont.render(str('W'),False,TEXT_COLOR)
			text_surfA = self.Gamefont.render(str('W'),False,TEXT_COLOR)
			text_surfS = self.Gamefont.render(str('W'),False,TEXT_COLOR)
			text_surfD = self.Gamefont.render(str('W'),False,TEXT_COLOR)
			text_surfSPACE = self.Gamefont.render(str('W'),False,TEXT_COLOR)
			posW = (self.display_surface.get_size()[0] /10,self.display_surface.get_size()[1] /1.4)
			text_rect = text_surfW.get_rect(bottomright = posW)

			pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
			self.display_surface.blit(text_surfW,text_rect)
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),2)'''

			keys = pygame.key.get_pressed()
			isW = False
			isA = False
			isS = False
			isD = False
			isSPACE = False
			self.isE = False
			# movement input
			if keys[pygame.K_w]:
				isW = True
			elif keys[pygame.K_s]:
				isS = True
			elif keys[pygame.K_d]:
				isD = True
			elif keys[pygame.K_a]:
				isA = True
			elif keys[pygame.K_SPACE]:
				isSPACE = True
			else:
				isW = False
				isA = False
				isS = False
				isD = False
				isSPACE = False
				self.isE = False


			self.KEYS('W',13,1.3,isW)
			self.KEYS('A',20,1.2,isA)
			self.KEYS('S',13,1.2,isS)
			self.KEYS('D',9.6,1.2,isD)
			self.KEYS('     ',10,1.112,isSPACE)
   
	def KEYS(self,name ,x,y,isPress = False):
		Color = UI_BG_COLOR
		if isPress == True:
			Color = '#6e6867'
   
		text_surf = self.Gamefont.render(str(name),False,TEXT_COLOR)
		pos = (self.display_surface.get_size()[0] /x,self.display_surface.get_size()[1] /y)
		text_rect = text_surf.get_rect(bottomright = pos)
  
		pygame.draw.rect(self.display_surface,Color,text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),2)	
	def display(self,player):
		self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)

	def displayDead(self,isDead):
		if isDead == True:
			self.show_Dead()


