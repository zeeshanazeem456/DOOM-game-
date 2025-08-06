#settings:
import pygame as py

class Settings:
    def __init__(self):
        self.HEIGHT = 560
        self.WIDTH = 995
        self.FPS = 60
        #PLAYER settings:
        self.PLAYER_POS = 1.5, 5
        #0 radian means, our player is facing right
        self.PLAYER_ANGLE = 0
        self.PLAYER_SPEED = 0.004
        self.PLAYER_ROT_SPEED = 0.002