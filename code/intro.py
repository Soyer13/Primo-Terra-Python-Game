from settings import *
import pygame
import cv2

def wyswietlintro(screen,clock):
    #

  
    main_sound = pygame.mixer.Sound('../audio/Together-to-the-Stars.mp3')
    main_sound.set_volume(MusicVolume)
    main_sound.play()
    video = cv2.VideoCapture("../Film/FilmWstep.mp4")
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)

    screen = pygame.display.set_mode(video_image.shape[1::-1])
    clock = pygame.time.Clock()

    run = success
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
        else:
            run = False
        screen.blit(video_surf, (0, 0))
        pygame.display.flip()
    main_sound.stop()
    return False
