from pygame import * 


window = display.set_mode((700,500))
display.set_caption("Ping-Pong")

back = (213, 150, 255)
window.fill(back)

clock = time.Clock()
FPS = 60
run = True
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
