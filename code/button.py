
import pygame

#button class
'''
class Button():
	def __init__(self, image,pos):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect(midbottom = pos)
		self.clicked = False

	'''
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

'''
	def restartButton(self):
		if self.lives <= 0 :
			RestartButton_sprite = Button('../graphics/Restart.png', screen_width / 2,screen_height/4)
			self.RestartButton = pygame.sprite.GroupSingle(RestartButton_sprite)
			self.RestartButton.draw(screen)
'''
