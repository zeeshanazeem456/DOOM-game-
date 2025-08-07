import pygame as pg

class Map:
    def __init__(self, game):
        self.game = game
        #Here underscore is initialized to be 0
        _ = 0
        #Here, i have generated a small map
        #1 represent walls and underscores represent free space
        self.mini_map = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
            [1,_,_,1,1,1,1,_,_,_,1,1,1,_,_,1],
            [1,_,_,_,_,_,1,_,_,_,_,_,1,_,_,1],
            [1,_,_,_,_,_,1,_,_,_,_,_,1,_,_,1],
            [1,_,_,1,1,1,1,_,_,_,_,_,_,_,_,1],
            [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
            [1,_,_,1,_,_,_,1,_,_,_,_,_,_,_,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        #Here i have set the tile size which satisfies my resolution
        self.TILE_SIZE = self.game.settings.TILE_SIZE
        #This is basically a dictionary
        #It stores all the co-ordinate of the walls in the game
        self.world_map = {}
        #This funnstion helps world_map to store all the co-ordinates
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):  
            for i, value in enumerate(row):     
                if value: 
                    self.world_map[(i, j)] = value

    def draw(self):
        #this function draws out the boxes
        for pos in self.world_map:
            pg.draw.rect(
                self.game.screen,
                'darkgray',
                (
                    #This places boxes at different positions which are seperated by the distance of TILE_SIZE
                    pos[0] * self.TILE_SIZE,
                    pos[1] * self.TILE_SIZE,
                    self.TILE_SIZE,
                    self.TILE_SIZE
                ),
                2 
            )
