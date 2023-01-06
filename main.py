import sys
import pygame
import simple_pendulum

pygame.init()

width, height = (700, 500)
screen = pygame.display.set_mode((width, height))

fps = 1000
clock = pygame.time.Clock()


def draw():
    screen.fill((255, 255, 255))
    p.draw()
    pygame.display.update()


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    p.update()
    # clock.tick(fps)


p = simple_pendulum.SimplePendulum(screen, (width/2, 100))
go = True
while go:
    update()
    draw()



