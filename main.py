from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, path, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(path), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((700, 500))
background = transform.scale(image.load('C:/Users/gavri/Desktop/Ping-Pong/Ping-Pong/242294.jpg'), (700, 500))
clock = time.Clock() 
game = True
while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(60)
