import pygame
from math import sin, cos, radians


class SimplePendulum:
    gravity = 0.1
    friction = 10**-4
    starting_angle = -90

    def __init__(self, surface: pygame.Surface, position=pygame.Vector2(), length=300, color=0):
        self.position = position

        self.length = length
        self.angle = SimplePendulum.starting_angle

        self.velocity = 0
        self.acceleration = 0

        self.arm = pygame.Vector2()

        self.color = color
        self.surface = surface

    def draw(self):
        self.arm = pygame.Vector2(
            self.length*sin(radians(self.angle)),
            self.length*cos(radians(self.angle))
        )
        pygame.draw.line(self.surface, self.color, self.position, self.position+self.arm)
        pygame.draw.circle(self.surface, (0, 255, 0), self.position+self.arm, self.arm.magnitude()/10)
        bob = self.position + self.arm
        pygame.draw.circle(self.surface, (0, 255, 0), (bob.x, self.surface.get_height()), 10)

    def update(self):
        self.acceleration = -self.gravity * sin(radians(self.angle))/self.length
        self.velocity += self.acceleration - self.friction*self.velocity
        self.angle += self.velocity

