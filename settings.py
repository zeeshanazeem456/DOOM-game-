#settings:
import pygame as py
import math

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

        #Field of View
        self.FOV = math.pi/3
        self.HALF_FOV = self.FOV / 2
        self.NUM_RAYS = self.WIDTH
        self.HALF_NUM_RAYS = self.NUM_RAYS//2
        self.DELTA_ANGLE = self.FOV / self.NUM_RAYS
        self.MAX_DEPTH = 20

        #Very Important
        self.TILE_SIZE = 62
