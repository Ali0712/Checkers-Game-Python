import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# RED = (255, 0, 0)
BLUE = (111, 182, 246)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DOT = (0, 0 , 255)
# GRAY = (128, 128, 128)
LIGHT_BLUE = (185, 222, 254)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (36, 18))
