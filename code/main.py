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
		self.font_advice = pygame.font.Font(UI_FONT,14)

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

		#przyciski
		Start_img = pygame.image.load('../graphics/buttons/Start.png').convert_alpha()
		StartButton =Button(WIDTH / 2.3, HEIGTH/3.6, Start_img, 0.8)
		Exit_img = pygame.image.load('../graphics/buttons/Koniec.png').convert_alpha()
		ExitButton =Button(WIDTH / 2.3, HEIGTH/1.4, Exit_img, 0.8)
		isStart = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
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
	
 


 

		