import pygame as pg
from settings import Settings

class ObjectRenderer:
    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.settings = Settings()
        self.wall_textures = self.load_wall_textures()
        self.TEXTURE_SIZE = self.game.settings.TEXTURE_SIZE
        self.sky_image = self.get_texture(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\DOOM\resources\textures\sky.png",(self.settings.WIDTH,self.settings.HALF_HEIGHT))
        self.sky_offset = 0 

    def draw(self):
        self.draw_bg()
        self.render_game_objects()

    def draw_bg(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % self.settings.WIDTH
        self.screen.blit(self.sky_image,(-self.sky_offset,0))
        self.screen.blit(self.sky_image,(-self.sky_offset+self.settings.WIDTH,0))
        pg.draw.rect(self.screen,self.settings.FLOOR_COLOR,(0,self.settings.HALF_HEIGHT,self.settings.WIDTH,self.settings.HEIGHT))

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path,res = (256,256)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture,res)
    
    def load_wall_textures(self):
        return {
            1: self.get_texture(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\DOOM\resources\textures\1.png"),
            2: self.get_texture(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\DOOM\resources\textures\2.png"),
            3: self.get_texture(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\DOOM\resources\textures\3.png"),
            4: self.get_texture(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\DOOM\resources\textures\4.png"),
            5: self.get_texture(r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\DOOM\resources\textures\5.png"),
        }