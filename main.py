import pygame as pg
import sys
from settings import Settings
from map import Map
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectRenderer

class Game:
    def __init__(self):
        """Contructor for the main game class"""
        pg.init()

        #Here i made an instance of my settings class
        self.settings = Settings()
        #Here i made the window of my game
        self.screen = pg.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        #Everyone,this is very important. This variable is used to calculate the amount of time that has passed
        #since the last frame
        self.delta_time = 1
        #Here, i initialize the clock for my game
        self.clock = pg.time.Clock()
        #####Start the game here#####
        pg.mouse.set_visible(False)
        pg.mouse.set_pos(self.settings.HALF_WIDTH, self.settings.HALF_HEIGHT)
        pg.event.set_grab(True)  # Lock mouse to the game window
        self.new_game()

    def new_game(self):
        #here, i make an instance for map
        self.map = Map(self)
        #here, i make an instance of player class
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)


    def update(self):
        self.player.update()
        self.raycasting.update()
        #this shows the screen
        pg.display.flip()
        self.delta_time = self.clock.tick(self.settings.FPS)
        #This is used to shows FPS on the title bar
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        #self.screen.fill('black')
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        #Our GAMELOOP:
        while True:
            #First,I check events that occur in my game 
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()