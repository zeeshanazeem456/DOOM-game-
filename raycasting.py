import pygame as pg
import math
from settings import Settings

class RayCasting:
    def __init__(self,game):
        self.game = game
        self.settings = self.game.settings
        self.ray_casting_result = []
        self.objects_to_render = []
        self.textures = self.game.object_renderer.wall_textures

    def get_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, proj_height, texture, offset = values

            if proj_height < self.settings.HEIGHT:
                wall_column = self.textures[texture].subsurface(
                    offset * (self.settings.TEXTURE_SIZE - self.settings.SCALE), 0, self.settings.SCALE, self.settings.TEXTURE_SIZE
                )
                wall_column = pg.transform.scale(wall_column, (self.settings.SCALE, proj_height))
                wall_pos = (ray * self.settings.SCALE, self.settings.HALF_HEIGHT - proj_height // 2)
            else:
                texture_height = self.settings.TEXTURE_SIZE * self.settings.HEIGHT / proj_height
                wall_column = self.textures[texture].subsurface(
                    offset * (self.settings.TEXTURE_SIZE - self.settings.SCALE), self.settings.HALF_TEXTURE_SIZE - texture_height // 2,
                    self.settings.SCALE, texture_height
                )
                wall_column = pg.transform.scale(wall_column, (self.settings.SCALE, self.settings.HEIGHT))
                wall_pos = (ray * self.settings.SCALE, 0)

            self.objects_to_render.append((depth, wall_column, wall_pos))

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        self.ray_casting_result = []
        
        texture_vert,texture_hor = 1,1
        ray_angle = self.game.player.angle - self.settings.HALF_FOV + 0.0001

        for ray in range(self.settings.NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontal intersections
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for _ in range(self.settings.MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    texture_hor = self.game.map.world_map[tile_hor]
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # vertical intersections
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for _ in range(self.settings.MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    texture_vert = self.game.map.world_map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # choose closest intersection
            # depth, texture offset
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            """pg.draw.line(self.game.screen,'yellow',(62 * ox,62 * oy),
                         (62 * ox + 62 * depth * cos_a, 62 * oy + 62 * depth * sin_a),2)"""
            
            #Removing fishbowl effect
            depth *= math.cos(self.game.player.angle - ray_angle)
            #projection
            proj_height = self.settings.SCREEN_DIST / (depth + 0.0001)
            #Draw walls
            """intensity = 255 / (1 + depth ** 5 * 0.00002)
            color = (0,int(intensity),0)
            pg.draw.rect(self.game.screen,color,
                         (int(ray * self.settings.SCALE),int(self.settings.HALF_HEIGHT - proj_height // 2),self.settings.SCALE,int(proj_height)))"""
            #ray casting result
            self.ray_casting_result.append((depth,proj_height,texture,offset))

            ray_angle += self.settings.DELTA_ANGLE



    def update(self):
        self.ray_cast()
        self.get_objects_to_render()