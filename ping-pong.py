from pygame import * 


window = display.set_mode((700,500))
display.set_caption("Ping-Pong")

back = (213, 150, 255)
window.fill(back)

clock = time.Clock()
FPS = 60
run = True
finish = False

speed_x = 3
speed_y = 3

class Game_Sprite(sprite.Sprite):
    def __init__(self, x, y, img, speed, width, height):
        super().__init__()
        self.img = transform.scale(image.load(img), (width, height))
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
    def __init__(self, x, y, img, width, height, speed_x, speed_y ):
        super().__init__( x, y, img, 0, width, height)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def update_speeds(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

racketl = RacketL(50, 200, 'racket.png', 10, 30, 200 )
racketr = RacketR(600, 200, 'racket.png', 10, 30, 200 )
ball = Ball(300, 5, 'tenis_ball.png', 45, 45, speed_x, speed_y)

while run:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    racketl.render(window)
    racketl.update_position()
    racketr.render(window)
    racketr.update_position()
    ball.render(window)
    ball.update()
    

  
        


    if sprite.collide_rect(racketl, ball) or sprite.collide_rect(racketr, ball):
        speed_x *= -1
    

    if ball.rect.y > 500 - 45 or ball.rect.y < 0:
        speed_y *= -1
    ball.update_speeds(speed_x, speed_y)
    
    display.update()
    clock.tick(FPS)

