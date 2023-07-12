import pygame
pygame.init()
pygame.mixer.music.load('ex08.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print(pygame.ver)
