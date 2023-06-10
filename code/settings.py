# game setup
WIDTH    = 1280
HEIGTH   = 720
FPS      = 60
TILESIZE = 64

HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}
#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 90
Game_FONT = '../graphics/font/joystix.ttf'
Game_FONT_SIZE = 18

# general colors
WATER_COLOR = '#177446'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#Poziom Głośności 
SoundEffectVolume = 0.2
MusicVolume = 0.3

#Bron 
weapon_data = {'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'}}

 #enemy
 #atack radius nie może być mniejsz niż 50 (lub obecnie ustawaiona wartość w enemy.py get_status() )
monster_data = {
	'trashcanEnemy': {'health': 120,'damage':15,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 1, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400,'health_recovered': 50},
	'trashbagEnemy': {'health': 60,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300,'health_recovered': 5}}

npc_data = {
	'ROBOT': {'health': 100, 'speed': 3,  'notice_radius': 120,}}

Advice_menu = ['Oszczędzaj energię!',
               'Unikaj plastikowych opakowań i wybieraj produkty o minimalnym wpływie na środowisko!',
               'Praktykuj segregację odpadów i recykling!','Unikaj marnowania jedzenia i dbaj o to, aby kupować i spożywać tylko tyle, ile jest niezbędne!',
               'Edukuj innych na temat ekologii!',
               'Oszczędzaj wodę!',
               'Nie marnowaniuj jedzenia !',
               'WIECEJ DRZEW WIECEJ KWIATÓW !!'
               'Noś swój kubek do kawiarni.',
       			'Uszyj sobie worki na warzywa.',
          		'Wyhoduj kilka własnych warzyw na balkonie.',
            	'Stare koce i pościel oddaj do schroniska dla zwierząt.',
             	'Nie bierz ulotek.',]

NPCquotes = 	['My w eco Corp Wierzymy w zielona prszyszłość',
				'Jestem ECOBOT. Moim celem jest uczyć o ekologi',
    			'Oszczędzaj energię!',
				'Unikaj plastikowych opakowań i wybieraj produkty o minimalnym wpływie na środowisko!',
				'Praktykuj segregację odpadów i recykling!',
    			'Unikaj marnowania jedzenia i dbaj o to, aby kupować i spożywać tylko tyle, ile jest niezbędne!',
				'Edukuj innych na temat ekologii!',
				'Oszczędzaj wodę!',
				'Nie marnowaniuj jedzenia !',
				'WIECEJ DRZEW WIECEJ KWIATÓW !!',
    			'Noś swój kubek do kawiarni.',
       			'Uszyj sobie worki na warzywa.',
          		'Wyhoduj kilka własnych warzyw na balkonie.',
            	'Stare koce i pościel oddaj do schroniska dla zwierząt.',
             	'Nie bierz ulotek.',
              	'Segreguj śmieci.']