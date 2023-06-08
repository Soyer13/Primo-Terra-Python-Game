import pygame, sys
from settings import *
from level import Level
from button import Button
import random

class Game:
	
	def __init__(self):		 
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Primo Terra')
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
		self.font_advice = pygame.font.Font(UI_FONT,16)
		self.Button_Font = pygame.font.Font(UI_FONT,80)

		self.level = Level()
	
	def run(self):
		#tworzenuie tła
		self.MianBC_surf = pygame.image.load('../graphics/MainWallPaper.png').convert()
		self.MianBC_surf = pygame.transform.scale(self.MianBC_surf, (WIDTH, HEIGTH))
		self.MainBC_rect = self.MianBC_surf.get_rect(topleft = (0,0))

		 #Tytuł 
		PrimoTerra_surf = self.font.render(str('Primo Terra'),False,'#6AF468')
		PrimowTerra_rect = PrimoTerra_surf.get_rect(center=(WIDTH / 2, HEIGTH/6))
	
		#Porady
		i = random.randint(0, len(Advice_menu) -1)
		Advice_surf = self.font_advice.render(str(Advice_menu[i]),False,'white')
		Advice_rect = Advice_surf.get_rect(center=(WIDTH/2, HEIGTH/1.2))
  
		#Przyciks Start
		Start_surf = self.Button_Font.render(str('Start'),False,'white')
		#Przyciks Opcje
		Opcje_surf = self.Button_Font.render(str('Opcje'),False,'#6719b5')
		#Przyciks Koniec
		Konie_surf = self.Button_Font.render(str('Koniec'),False,'#75a832')
  
		#przyciski
		#Start_img = pygame.image.load('../graphics/buttons/Start.png').convert_alpha()
		StartButton =Button(WIDTH / 2.5, HEIGTH/3.5, Start_surf, 0.8)
  
		OptionsButton =Button(WIDTH / 2.5, HEIGTH/2.1, Opcje_surf, 0.8)

		#Exit_img = pygame.image.load('../graphics/buttons/Koniec.png').convert_alpha()
		ExitButton =Button(WIDTH / 2.6, HEIGTH/1.5, Konie_surf, 0.8)
  
		#Studios
		display_time = 2500
		start_time = pygame.time.get_ticks()
		self.Studios = True
		self.Studio_surf = pygame.image.load('../graphics/DisconnectedStudios.png').convert()
		self.Studio_surf = pygame.transform.scale(self.Studio_surf, (WIDTH, HEIGTH))
		self.Studio_rect = self.Studio_surf.get_rect(topleft = (0,0))
		
		isStart = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit() 
					sys.exit()

			self.screen.fill('black') 
			#Wyświetlenie Studio
			current_time = pygame.time.get_ticks()
			if self.Studios == True:
				if current_time - start_time >= display_time:
					self.Studios = False
				self.screen.blit(self.Studio_surf,self.Studio_rect)
			else:
				#Wyświetlanie tła
				self.screen.blit(self.MianBC_surf,self.MainBC_rect)
				#Menu Główne
				if isStart == False:
					#Wyświetlanie Tytułu
					self.screen.blit(PrimoTerra_surf,PrimowTerra_rect )
					#Wyświetlenie Porady
					self.screen.blit(Advice_surf,Advice_rect )
					if StartButton.draw(self.screen):
						isStart = True
					if OptionsButton.draw(self.screen):
						pass
					if ExitButton.draw(self.screen):
						pygame.quit()
						sys.exit()
     
				# uruchowniemie gry
				if isStart == True:
					self.level.run()

			#przyciks Restat Po śmierci
			if self.level.player.isDead == True:
				Restart_img = pygame.image.load('../graphics/buttons/Restart.png').convert_alpha()
				Restart_Button =Button(WIDTH / 2.5, HEIGTH/1.8, Restart_img, 0.8)
				if Restart_Button.draw(self.screen):
					self.level = Level()
     
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()
	
 


 

		