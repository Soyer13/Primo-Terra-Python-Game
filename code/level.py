from typing import Iterable, Union
import pygame
from pygame.sprite import AbstractGroup 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from enemy import Enemy
from npc import NPC
from weapon import Weapon
from ui import UI
from debug import debug
class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()
  
		# attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()
  
		# sprite group setup
		self.visible_sprites = YSortCamerGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()
  
		# user interface 
		self.ui = UI()

		
	def create_map(self):
		
		layouts = {
			'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
			'grass': import_csv_layout('../map/map_Grass.csv'),
			'object': import_csv_layout('../map/map_Objects.csv'),
   			'entities': import_csv_layout('../map/map_Entities.csv')
		}
		graphics = {
			'grass': import_folder('../graphics/Grass'),
			'objects': import_folder('../graphics/objects')
		}
		self.player = Player((1,1),
		[self.visible_sprites],
		self.obstacle_sprites,
		self.create_attack,
		self.destroy_attack)
  
		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							print(col,"-b")
							Tile((x,y),[self.obstacle_sprites],'invisible')
						if style == 'grass':
							print(col,"-g")
							random_grass_image = choice(graphics['grass'])
							Tile(
								(x,y),
								[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
								'grass',
								random_grass_image)

						if style == 'object':
							# co = graphics['objects'][27]
							# print(x)
							


							# exit(0)

							print(col)
							#print(graphics['objects'][int(col)],"daedjoi")
							surf = graphics['objects'][int(col)] 
						
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)

						if style == 'entities':
							if col == '394':
								self.player.kill()
								self.player = Player((x,y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack)
							else:
								if col == '390' or col == '391' or col == '392':
									if col == '390': monster_name = 'trashbagEnemy'
									elif col == '391': monster_name = 'spirit'
									elif col == '392': monster_name = 'trashcanEnemy'
									Enemy(
										monster_name,
										(x,y),
										[self.visible_sprites,self.attackable_sprites],
										self.obstacle_sprites,
										self.damage_player)
								else:
									NPC('ROBOT',(x,y),[self.visible_sprites,self.obstacle_sprites],self.obstacle_sprites,self.player)
        
	def create_attack(self):
		self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])
  
	def destroy_attack(self):
			if self.current_attack:
				self.current_attack.kill()
			self.current_attack = None
   
	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type == 'grass':
							target_sprite.kill()
						else:
							target_sprite.get_damage(self.player,attack_sprite.sprite_type)

	def damage_player(self,amount,attack_type):
		if self.player.vulnerable:
			self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			# spawn particles

	def run(self):
		
			# update and draw the game
			self.visible_sprites.custom_draw(self.player)
			self.visible_sprites.update()
			self.visible_sprites.enemy_update(self.player)
			self.player_attack_logic()
			self.ui.display(self.player)
			self.ui.displayDead(self.player.isDead)
			debug(self.player.health,10,0)

class YSortCamerGroup(pygame.sprite.Group):
	def __init__(self):
		# general setup

		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2 
		self.half_height = self.display_surface.get_size()[1] // 2 
		self.offset = pygame.math.Vector2()

		#tworzenuie tła
		self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):
		#getting the offset
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		#Wyświetlanie tła
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)
  
		#for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
   
	def enemy_update(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)