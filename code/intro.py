from settings import *
import pygame
from PIL import Image
def wyswietlintro(screen):
    # Inicjalizacja biblioteki Pygame
    pygame.init()

    # Wczytanie animacji GIF jako listy klatek
    gif_path = "../graphics/FilmWstep.gif"
    gif = Image.open(gif_path)
    frames = []
    try:
        while True:
            frames.append(gif.copy())
            gif.seek(len(frames))
    except EOFError:
        pass
    
  
    main_sound = pygame.mixer.Sound('../audio/Together-to-the-Stars.mp3')
    main_sound.set_volume(MusicVolume)
    main_sound.play()
    
   
    
    # Konwersja klatek na format zrozumiały dla Pygame
    pygame_frames = []
    for frame in frames:
        pygame_frame = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
        pygame_frames.append(pygame_frame)

    # Ustawienie indeksu bieżącej klatki
    current_frame_index = 0

    # Główna pętla programu
    running = True
    clock = pygame.time.Clock()
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Wyświetlanie bieżącej klatki na ekranie
            screen.blit(pygame_frames[current_frame_index], (0, 0))
            pygame.display.flip()

            # Zwiększanie indeksu bieżącej klatki i cykliczne odtwarzanie animacji
            current_frame_index = (current_frame_index + 1) % len(pygame_frames)
            clock.tick(30)  # Możesz dostosować wartość FPS według własnych potrzeb
        except IndexError:
            running = False
            main_sound.stop()
            # Ustalenie liczby klatek na sekundę (FPS)
            

    # Zakończenie programu
    pygame.quit()