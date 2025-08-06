import pygame as pg
from settings import Settings
import math

class Player:
    def __init__(self,game):
        self.game = game
        self.settings = self.game.settings
        #I store x and y co-ordinates of my player
        self.x,self.y = self.settings.PLAYER_POS
        #Here, i initialize the angle: Angle tell us where our player is looking! (0 radians mean he is looking right)
        #For example. if our angle is 0
        #player_camera.x = cos(angle) = cos(0) = 1
        #player_camera.y = sin(angle) = sin(0) = 0
        #This means our player is looking at +ve x or right
        self.angle = self.settings.PLAYER_ANGLE

    def movement(self):
        #sin_a is y-component of the direction, our player is facing.
        sin_a = math.sin(self.angle)
        #cos_a is x-component of the direction, our player is facing.
        cos_a = math.cos(self.angle)
        #initializing change in x and y as 0
        dx,dy = 0,0
        #This is to limite how far the player should move this frame
        speed = self.settings.PLAYER_SPEED * self.game.delta_time
        #This calculates the direction and the speed
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        #keys captures the key presses
        keys = pg.key.get_pressed()
        # "W" is to move forward
        if keys[pg.K_w]:
            #dx += (1 * speed)
            dx += speed_cos
            #dy += (0 * speed)
            dy += speed_sin
        # "S" is to move backwards
        if keys[pg.K_s]:
            #dx += (-1 * speed)
            dx -= speed_cos
            #dy += (0 * speed)
            dy -= speed_sin
        # "A" is to move left
        if keys[pg.K_a]:
            #dx += (0 * speed)
            dx += speed_sin
            #dy += (1 * speed)
            dy -= speed_cos
        # "D" is to move right
        if keys[pg.K_d]:
            dx -= speed_sin
            dy += speed_cos
        #self.x = dx
        #self.y = dy
        self.check_wall_collision(dx,dy)

        #Rotation logic
        if keys[pg.K_LEFT]:
            self.angle -= self.settings.PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += self.settings.PLAYER_ROT_SPEED * self.game.delta_time

    def check_wall(self,x,y):
        #This will return true if the (x,y) are not inside the wall
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self,dx,dy):
        #This check if the x co-ordinate of our player is inside the wall
        if self.check_wall(int(self.x + dx),int(self.y)):
            #if the future co-ordinates of x (self. + dx) are not inside the wall
            #dx which is the change in position gets added to x
            self.x  += dx
        if self.check_wall(int(self.x),int(self.y + dy)):
            self.y += dy

    def draw(self):
        tile = self.game.map.TILE_SIZE
        #x = (0.### * 64)
        x = self.x * tile
        y = self.y * tile

        # Draw direction line
        pg.draw.line(
            self.game.screen, 'yellow',
            (x, y),
            (x + self.settings.WIDTH * math.cos(self.angle),
            y + self.settings.WIDTH * math.sin(self.angle)),
            2
        )

        # Draw player circle
        pg.draw.circle(self.game.screen, 'green', (x, y), 15)
        
    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x,self.y
    @property
    def map_pos(self):
        return int(self.x),int(self.y)

    