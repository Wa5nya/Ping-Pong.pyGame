from pygame import * 


window = display.set_mode((700,500))
display.set_caption("Ping-Pong")

back = (213, 150, 255)
window.fill(back)

clock = time.Clock()
FPS = 60
run = True

speed_x = 3
speed_y = 3

class Game_Sprite(sprite.Sprite):
    def __init__(self, x, y, img, speed, wight, height):
        super().__init__()
        self.img = transform.scale(image.load(img), (60, 60))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y       
        self.speed = speed
    def render(self, window):
        window.blit(self.img, (self.rect.x, self.rect.y))

class RacketL(Game_Sprite):
    def update_position(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += 10
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 10

class RacketR(Game_Sprite):
    def update_position(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += 10
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 10


class Ball(Game_Sprite):
    def __init___(self, x, y, img, wight, height, speed_x, speed_y ):
        super().__init__( x, y, img, 0, wight, height)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def update_speeds(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

racketl = RacketL(300, 300, 'racket.png', 10 )



while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    


    display.update()
    clock.tick(FPS)

