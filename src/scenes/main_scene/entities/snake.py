from visual.drawer import Drawer
from game_object import GameObject
from scenes.main_scene.resources.delta_time import DeltaTime
import math
import pygame
from events.event import EventServer
from events.snake_coord_event import SnakeCoordEvent
from events.keyboard_event import KeyBoardEvent
from events.snake_body_event import SnakeBodyEvent
from events.snake_fruit_collision_event import SnakeFruitCollisionEvent
from events.destroy_enemy_part_event import DestroyEnemyPartEvent
from events.snake_size_event import SnakeSizeEvent
from scenes.main_scene.resources.growth_function import growth
from scenes.main_scene.resources.get_sin_cos import get_sin_cos

class Snake(GameObject):
    def __init__(self):
        super().__init__()
        self.movement = _Snake_Movement(self)
        self.body: list[list[5, 5]] = [[6, 6], [7, 7]]
        self.input = [0, 0]
        self.color = (0, 0, 0)
            
    def setup(self):
        EventServer.bind(self.grow, SnakeFruitCollisionEvent)

    def grow(self, event):
        x = self.body[len(self.body) - 1][0] - 1
        y = self.body[len(self.body) - 1][1] - 1
        self.body.append([x, y])

    def update(self):
        self.movement.update_speed()
        self.movement.walk_body()
        self.movement.walk_head()

    def render(self, drawer: Drawer):
        for i in self.body:
            drawer.draw_pixel(i[0], i[1], self.color)

class _Snake_Movement:
    def __init__(self, snake: Snake) -> None:
        self.snake = snake
        self.velocity = [0, 0]
        self.speed = 10
    
    def walk_head(self):
        sk = self.snake
        sk.body[0][0] += self.velocity[0] * DeltaTime.get()
        sk.body[0][1] += self.velocity[1] * DeltaTime.get()
        
    def update_speed(self):
        input = self.snake.input
        n_input = [input[0] / math.sqrt(2), input[1] / math.sqrt(2)]
        self.velocity[0] = n_input[0] * self.speed
        self.velocity[1] = n_input[1] * self.speed
    
    def walk_body(self):
        for i in range(1, len(self.snake.body)):
            if (self.__should_walk_part(i)):
                self.__walk_body_part(i)

    def __should_walk_part(self, i):
        xdis = self.snake.body[i][0] - self.snake.body[i - 1][0] 
        ydis = self.snake.body[i][1] - self.snake.body[i - 1][1]
        dis = math.sqrt(xdis * xdis + ydis * ydis)
        return dis > 1

    def __walk_body_part(self, i):
        sk = self.snake
        angle = get_sin_cos(sk.body[i - 1], sk.body[i])
        sk.body[i][0] += angle[0] * self.speed * DeltaTime.get()
        sk.body[i][1] += angle[1] * self.speed * DeltaTime.get()