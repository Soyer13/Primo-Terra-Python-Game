import pygame, sys
from settings import *
from level import Level
from button import Button

class Game:
	
	def __init__(self):		 
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Primo Terra')
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	def run(self):
		Start_img = pygame.image.load('../graphics/buttons/Start.png').convert_alpha()
		StartButton =Button(WIDTH / 2.3, HEIGTH/3.6, Start_img, 0.8)
		isStart = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			
			if isStart == False:
				if StartButton.draw(self.screen):
					isStart = True
			if isStart == True:
				self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()
	
 


 

		