import pygame

pygame.mixer.init()
pygame.mixer.music.load("mymusicfile.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    x = input('')
    if x == '+':
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
        print(pygame.mixer.music.get_volume())
    if x == '-':
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)
        print(pygame.mixer.music.get_volume())
    if x == 'start':
        pygame.mixer.music.unpause()
    if x == 'pauze':
        pygame.mixer.music.pause()
