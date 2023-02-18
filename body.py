import pygame
import math
import random

class Body:
    def __init__(self, mass, x, y, vx=0, vy=0, color=[127, 0, 127]):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.speed = 0.2
        self.fg = 0

    def __str__(self):
        return f'body at <{self.x}, {self.y}>'


    def update(self):
        self.x += self.speed * self.vx
        self.y += self.speed * self.vy


    def calculate_force(self, x2, y2, m2, r):

        fg = self.mass * m2 * r / ((r**2) + 150**2)**(3/2) * 0.1 # dampening factor
        fg /= 9.81
        # print(next_fg)
        # print(self.fg)

        # fg = self.mass * m2 / (r ** 2)
        # print(fg)

        theta = 0
        if x2 - self.x != 0:
            theta = abs(math.atan((y2 - self.y) / (x2 - self.x)))
        
        
        if self.x < x2:
            self.vx += math.cos(theta) * fg / self.mass
        else:
            self.vx -= math.cos(theta) * fg / self.mass

        if self.y < y2:
            self.vy += math.sin(theta) * fg / self.mass
        else:
            self.vy -= math.sin(theta) * fg / self.mass


    def draw(self, screen):
        if self.mass > 30000:
            self.color = [219, 128, 31]
        pygame.draw.circle(screen, self.color, [self.x, self.y], math.log(self.mass, 10))
        # math.log(self.mass, 10)
