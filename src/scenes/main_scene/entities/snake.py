from visual.drawer import Drawer
from game_object import GameObject
from scenes.main_scene.resources.counter import Counter
import math
import pygame
from events.snake_coord_event import SnakeCoordEvent
from events.event import EventServer
from events.keyboard_event import KeyBoardEvent
from events.snake_fruit_collision_event import SnakeFruitCollisionEvent
from events.snake_event import SnakeEvent
from events.snake_size_event import SnakeSizeEvent
from scenes.main_scene.resources.growth_function import growth

class Snake(GameObject):
    def __init__(self):
        super().__init__()
        self.body: list[list[0, 0]] = [[1, 1], [2, 2]]
        self.velocity = [0, 0]
        self.input = [0, 0]
        self.speed = 10
            
    def setup(self):
        EventServer.bind(self.grow, SnakeFruitCollisionEvent)
        EventServer.bind(self.input_threatment, KeyBoardEvent)
        EventServer.bind(self.speed_up, SnakeSizeEvent)

    def grow(self, event):
        x = self.body[len(self.body) - 1][0] - 1
        y = self.body[len(self.body) - 1][1] - 1
        self.body.append([x, y])


    def input_threatment(self, event: KeyBoardEvent):
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.input = [1, 0]
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.input = [-1, 0]
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            self.input = [0, -1]
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.input = [0, 1]

    def speed_up(self, event: SnakeSizeEvent):
        self.speed = 10 + growth(event.size, 25, 80)

    def update(self):
        self.velocity[0] = (self.input[0] / math.sqrt(2)) * self.speed
        self.velocity[1] = (self.input[1] / math.sqrt(2)) * self.speed
        self.__walk_body()
        self.body[0][0] += float(self.velocity[0]) * Counter.delta_time()
        self.body[0][1] += float(self.velocity[1]) * Counter.delta_time()
        EventServer.pool(SnakeCoordEvent(self.body[0][0], self.body[0][1]))
        EventServer.pool(SnakeSizeEvent(len(self.body)))
        EventServer.pool(SnakeEvent(self.body))

    def __walk_body(self):
        for i in range(1, len(self.body)):
            xdis = self.body[i - 1][0] - self.body[i][0] 
            ydis = self.body[i - 1][1] - self.body[i][1]
            dis = math.sqrt(xdis * xdis + ydis * ydis)
            if dis > 1:
                self.body[i][0] += (xdis / dis) * self.speed * Counter.delta_time()
                self.body[i][1] += (ydis / dis) * self.speed * Counter.delta_time()
    
    def render(self, drawer: Drawer):
        for i in self.body:
            drawer.draw_pixel(i[0], i[1], (255, 0, 0))