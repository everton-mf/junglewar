import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324

C_PURPLE = 185, 5, 175
C_WHITE = 255, 255, 255
C_ORANGE = 255, 128, 0
C_BLACK = 15, 0, 15

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P',
               'SCORE',
               'EXIT')

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Player1': 2,
    'Player2': 2,
    'Enemy1' : 2,
    'Enemy2': 3,
    'Player1Shot': 3,
    'Player2Shot': 3
}


PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_PRINT,
                    'Player2': pygame.K_RCTRL}

EVENTY_ENEMY= pygame.USEREVENT + 1

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1': 200,
    'Player2': 200,
    'Enemy1' : 100,
    'Enemy2': 100
}
