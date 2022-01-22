import random
import sys
import pygame
from pygame import transform
from pygame.locals import * 

#Global variables for the game
FPS = 32
SCREENWIDTH = 321
SCREENHEIGHT = 611
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallary/sprites/bird.png'
BACKGROUND = 'gallary/sprites/backgroung.png'
PIPE = 'gallary/sprites/pipe.png'


if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by AryanJagarwal')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallary/sprites/0.png').convert_alpha(),
        pygame.image.load('gallary/sprites/1.png').convert_alpha(),
        pygame.image.load('gallary/sprites/2.png').convert_alpha(),
        pygame.image.load('gallary/sprites/3.png').convert_alpha(),
        pygame.image.load('gallary/sprites/4.png').convert_alpha(),
        pygame.image.load('gallary/sprites/5.png').convert_alpha(),
        pygame.image.load('gallary/sprites/6.png').convert_alpha(),
        pygame.image.load('gallary/sprites/7.png').convert_alpha(),
        pygame.image.load('gallary/sprites/8.png').convert_alpha(),
        pygame.image.load('gallary/sprites/9.png').convert_alpha(),
    )


GAME_SPRITES['message'] = pygame.image.load('gallary/sprites/message.png').convert_alpha()
GAME_SPRITES['base'] = pygame.image.load('gallary/sprites/base.png').convert_alpha()
GAME_SPRITES['pipe'] = (
pygame.transform.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
pygame.image.load(PIPE).convert_alpha()
)

GAME_SOUNDS['die'] = pygame.mixer.sound('gallary/audio/die.wav')
GAME_SOUNDS['hit'] = pygame.mixer.sound('gallary/audio/hit.wav')
GAME_SOUNDS['point'] = pygame.mixer.sound('gallary/audio/point.wav')
GAME_SOUNDS['swoosh'] = pygame.mixer.sound('gallary/audio/swoosh.wav')
GAME_SOUNDS['wing'] = pygame.mixer.sound('gallary/audio/wing.wav')

GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

while True:
    welcomeScreen()
    mainGame()