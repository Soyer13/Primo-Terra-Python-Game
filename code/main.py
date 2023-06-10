import pygame, sys
from settings import *
from level import Level
from button import Button
from intro import wyswietlintro
from slider import slider_function
import random
import cv2
from input import input_box
from Radio import Radio
from displeyEND import Napis

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
		self.isPause = False
		self.canDisMenu = True
		self.isOptions = False
		self.level = Level()
		self.isIntro = False
		
		#Muzyka
		self.MusicVolume = MusicVolume
		'''self.main_sound = pygame.mixer.Sound('../audio/main.ogg')
		self.main_sound.set_volume(self.MusicVolume)'''
		
		self.isENDGAME = False
  
		self.radio = Radio('../audio/Music')
		#self.slider = Slider(WIDTH/2)
		#FILM
		self.napis = Napis()
  
	def run(self):
		#tworzenuie tła
		self.MianBC_surf = pygame.image.load('../graphics/MainWallPaper.png').convert()
		self.MianBC_surf = pygame.transform.scale(self.MianBC_surf, (WIDTH, HEIGTH))
		self.MainBC_rect = self.MianBC_surf.get_rect(topleft = (0,0))

		 #Tytuł 
		PrimoTerra_surf = self.font.render(str('Primo Terra'),False,'#6AF468')
		PrimowTerra_rect = PrimoTerra_surf.get_rect(center=(WIDTH / 2, HEIGTH/6))
  
		#Ładowanie 
		Loading_surf = self.font.render(str('Ładowanie...'),False,'#6AF468')
		Loading_rect = PrimoTerra_surf.get_rect(center=(WIDTH / 3, HEIGTH/2))
	
		#Porady
		i = random.randint(0, len(Advice_menu) -1)
		Advice_surf = self.font_advice.render(str(Advice_menu[i]),False,'white')
		Advice_rect = Advice_surf.get_rect(center=(WIDTH/2, HEIGTH/1.2))
  
		#Powiadomienie Intro
		AdviceIntro_surf = self.font_advice.render(str('Ładowanie zajumje troche czasu'),False,'black')
		AdviceIntro_rect = Advice_surf.get_rect(center=(WIDTH / 1.9, HEIGTH/1.83))
		#Przycisk Intro
		Intro_surf = self.Button_Font.render(str('Intro'),False,'red')
		#Przyciks Kontynułuj 
		Continue_surf = self.Button_Font.render(str('kontynuj'),False,'white')
		#Przyciks Start
		Start_surf = self.Button_Font.render(str('Start'),False,'white')
		#Przyciks Opcjef
		Opcje_surf = self.Button_Font.render(str('Opcje'),False,'#6719b5')
		#Przyciks Koniec
		Konie_surf = self.Button_Font.render(str('Koniec'),False,'#75a832')
		#Menu
		Menu_surf = self.Button_Font.render(str('Menu'),False,'#75a832')
  
		#przyciski
		#Start_img = pygame.image.load('../graphics/buttons/Start.png').convert_alpha()
		ContinueButton =Button(WIDTH / 2.5, HEIGTH/3.5, Continue_surf, 0.8)
		StartButton =Button(WIDTH / 2.5, HEIGTH/3.5, Start_surf, 0.8)
  
		OptionsButton =Button(WIDTH / 2.5, HEIGTH/2.4, Opcje_surf, 0.8)
		IntroButton =Button(WIDTH / 2.5, HEIGTH/1.8, Intro_surf, 0.8)
		#Exit_img = pygame.image.load('../graphics/buttons/Koniec.png').convert_alpha()
		ExitButton =Button(WIDTH / 2.6, HEIGTH/1.5, Konie_surf, 0.8)
		#Menu
		MenuButton =Button(WIDTH / 2.5, HEIGTH/3, Menu_surf, 0.8)
  
		#Studios
		display_time = 2500
		start_time = pygame.time.get_ticks()
		self.Studios = True
		self.Studio_surf = pygame.image.load('../graphics/DisconnectedStudios.png').convert()
		self.Studio_surf = pygame.transform.scale(self.Studio_surf, (WIDTH, HEIGTH))
		self.Studio_rect = self.Studio_surf.get_rect(topleft = (0,0))
  
		#earth {#699,9}
		displayearth_time = 1500
		#startearth_time = pygame.time.get_ticks()
		self.earth = True
		self.earth_surf = pygame.image.load('../graphics/ZiemiaZanieczyszczona.png').convert()
		self.earth_surf = pygame.transform.scale(self.earth_surf, (WIDTH, HEIGTH))
		self.earth_rect = self.Studio_surf.get_rect(topleft = (0,0))
		self.earthisStart = False
  
		displayad_time = 3000
		self.ad = True
		self.ad_surf = pygame.image.load('../graphics/Reklama ECO BOT.png').convert()
		self.ad_surf = pygame.transform.scale(self.ad_surf, (WIDTH, HEIGTH))
		self.ad_rect = self.ad_surf.get_rect(topleft = (0,0))
		self.adisStart = False
  
		self.is1 = True
		self.is2 = True
		self.is3 = True
		self.is4 = True
		self.is5 = True
		self.is6 = True
		self.is7 = True
		self.is8 = True	
  
		isStart = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit() 
					sys.exit()

			self.radio.play_music_from_folder(self.MusicVolume)
			keys = pygame.key.get_pressed()
			
			if self.canDisMenu == True:
				if keys[pygame.K_ESCAPE]:
						self.isPause = not self.isPause
						displayInMenu_time = 300
						startinMenu_time = pygame.time.get_ticks()
						self.canDisMenu = False
			else:
				current_timeMenu = pygame.time.get_ticks()
				if current_timeMenu - startinMenu_time >= displayInMenu_time:
					self.canDisMenu = True
					
				else:
					self.canDisMenu = False
		
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
				if self.isENDGAME == False:
					# Menu Główne {#173, 24} 
					if isStart == False:
						if self.isOptions == False:
							if self.isIntro ==False:
								#Wyświetlanie Tytułu
								self.screen.blit(PrimoTerra_surf,PrimowTerra_rect )
								#Wyświetlenie Porady
								self.screen.blit(Advice_surf,Advice_rect )
								self.screen.blit(AdviceIntro_surf,AdviceIntro_rect )
								if StartButton.draw(self.screen):
									isStart = True
								if OptionsButton.draw(self.screen):
									self.isOptions = True
								if ExitButton.draw(self.screen):
									pygame.quit()
									sys.exit()
								if IntroButton.draw(self.screen):
									self.isIntro = True	
									self.radio.radioStop()
									self.screen.fill('black')
									self.screen.blit(Loading_surf,Loading_rect )
							else:
								self.isIntro = wyswietlintro(self.screen,self.clock)
								self.radio.radioPlay()
						else:
							# Opcje {#873, 7} 
							#self.MusicVolume = self.slider.slider(self.screen,event,self.MusicVolume,WIDTH/2,300,300)
							if MenuButton.draw(self.screen):
								self.isOptions = False
							#self.MusicVolume = input_box(self.screen, self.font_advice, 100, 100, 200, 32)
							
							
					if isStart == True:				
						# Menu W Grze 25252525
						if self.isOptions == False:
							if self.isPause == False:
								
								
								#earth {#699 ,10}
								if self.earth == True:
									if self.earthisStart == False:
										startearth_time = pygame.time.get_ticks()
										self.earthisStart = True
									currentearth_time = pygame.time.get_ticks()
									if currentearth_time - startearth_time >= displayearth_time:
										self.earth = False	
									self.screen.blit(self.earth_surf,self.earth_rect)
								else:
									if self.ad == True:
										if self.adisStart == False:
											startad_time = pygame.time.get_ticks()
											self.adisStart = True
										currentad_time = pygame.time.get_ticks()
										if currentad_time - startad_time >= displayad_time:
											self.ad = False	
										self.screen.blit(self.ad_surf,self.ad_rect)
									else:
										# uruchowniemie gry {#922 ,2}
										self.screen.fill(WATER_COLOR) 
										self.isENDGAME = self.level.run()
							else:
								self.screen.blit(PrimoTerra_surf,PrimowTerra_rect )
								if ContinueButton.draw(self.screen):
									self.isPause = False
								if OptionsButton.draw(self.screen):
									self.isOptions = True
								if ExitButton.draw(self.screen):
									pygame.quit()
									sys.exit()
						else:
							if MenuButton.draw(self.screen):
								self.isOptions = False

				else:
					if self.is1 == True:
						
						self.is1 =self.napis.napis(4000,'../graphics/Napisy/ZiemiaZanieczyszczona2.png',self.screen)
					elif self.is1 == False:

						if self.is2 == True:
							
							self.is2 =self.napis.napis(4000,'../graphics/Napisy/Napisy1.png',self.screen)
						elif self.is2 == False:	
	
							if self.is3 == True:
								
								self.is3 =self.napis.napis(4000,'../graphics/Napisy/Napisy2.png',self.screen)
							elif self.is3 == False:	
		
								if self.is4 == True:
									
									self.is4 =self.napis.napis(4000,'../graphics/Napisy/Napisy3.png',self.screen)
								elif self.is4 == False:	
			
									if self.is5 == True:
										
										self.is5 =self.napis.napis(4000,'../graphics/Napisy/Napisy4.png',self.screen)
									elif self.is5 == False:	
				
										if self.is6 == True:
											
											self.is6 =self.napis.napis(4000,'../graphics/Napisy/Napisy5.png',self.screen)
										elif self.is6 == False:	
					
											if self.is7 == True:
												
												self.is7 =self.napis.napis(4000,'../graphics/Napisy/Napisy6.png',self.screen)
											elif self.is7 == False:	
						
												if self.is8 == True:
													
													self.is8 =self.napis.napis(4000,'../graphics/Napisy/Napisy7.png',self.screen)
												else:
													pygame.quit()
					
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
	
 


 

		