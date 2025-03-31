import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324

C_PURPLE = 185, 5, 175
C_WHITE = 255, 255, 255
C_ORANGE = 255, 128, 0
C_BLACK = 15, 0, 15
C_GREY = 106, 106, 106
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P',
               'SCORE',
               'EXIT')

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Player1': 2,
    'Player2': 2,
    'Enemy1': 2,
    'Enemy2': 2,
    'Player1Shot': 3,
    'Player2Shot': 3,
    'Enemy1Shot': 5,
    'Enemy2Shot': 4,
}

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_LCTRL}

EVENTY_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1

}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 40,
    'Enemy2': 40
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 1,
    'Player2': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Player1Shot': 20,
    'Player2Shot': 20,
    'Enemy1Shot': 20,
    'Enemy2Shot': 15

}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 50,
    'Enemy2': 60,
    'Player1Shot': 0,
    'Player2Shot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0

}

EVENT_TIMEOUT = pygame.USEREVENT + 2

SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'Entername': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210)

             }
