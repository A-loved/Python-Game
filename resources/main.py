import pygame
from pygame.locals import *
import time

size = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = size*3
        self.y = size*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()





class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.block_x = [40] * length
        self.block_y = [40] * length
        self.direction = "down"

    def draw(self):
        self.parent_screen.fill((168, 50, 96))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_right(self):
        self.direction = "right"

    def move_left(self):
        self.direction = "left"

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.block_x[i] = self.block_x[i-1]
            self.block_y[i] = self.block_y[i-1]

        if self.direction == "up":
            self.block_y[0] -= size
            self.draw()

        if self.direction == "down":
            self.block_y[0] += size
            self.draw()

        if self.direction == "right":
            self.block_x[0] += size

        if self.direction == "left":
            self.block_x[0] -= size

        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((600, 600))
        self.surface.fill((168, 50, 96))
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()





