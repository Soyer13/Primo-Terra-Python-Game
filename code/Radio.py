import pygame
import os

class Radio():
    def __init__(self,folder_path):
        self.folder_path = folder_path
        self.play = True
        self.music_files = []
        for file in os.listdir(folder_path):
            if file.endswith('.mp3') or file.endswith('.wav'):
                self.music_files.append(os.path.join(folder_path, file))

        if len(self.music_files) == 0:
            print("Brak plików muzycznych w folderze.")
            return
        pygame.mixer.music.load(self.music_files[0])  # Załaduj pierwszy plik muzyczny
        pygame.mixer.music.play()
        self.current_track = 0  # Indeks aktualnie odtwarzanego utworu
    def play_music_from_folder(self,volume):
        
        pygame.mixer.music.set_volume(volume)
        if self.play == True:
            if pygame.mixer.music.get_busy():
                pass  # Czekaj na zakończenie odtwarzania
            else:
                
                print("Odtwarzanie:", self.music_files[self.current_track])
                self.current_track += 1
                if self.current_track >= len(self.music_files):
                    self.current_track = 0  # Wróć do początku listy utworów 
                pygame.mixer.music.load(self.music_files[self.current_track])
                pygame.mixer.music.play()
            
    def radioPlay(self):
        self.play = True
        pygame.mixer.music.play()
    def radioStop(self):
        self.play = False
        pygame.mixer.music.stop()