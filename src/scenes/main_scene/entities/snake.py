from visual.drawer import Drawer
from game_object import GameObject
from scenes.main_scene.resources.delta_time import DeltaTime
import math
import pygame
from events.snake_coord_event import SnakeCoordEvent
from events.event import EventServer
from events.keyboard_event import KeyBoardEvent
from events.snake_fruit_collision_event import SnakeFruitCollisionEvent
from events.snake_body_event import SnakeBodyEvent
from events.snake_size_event import SnakeSizeEvent
from scenes.main_scene.resources.growth_function import growth

class Snake(GameObject):
    def __init__(self):
        super().__init__()
        self.inputThreatement = _Snake_InputThreatement(self)
        self.movement = _Snake_Movement(self)
        self.body: list[list[0, 0]] = [[1, 1], [2, 2]]
        self.input = [0, 0]
            
    def setup(self):
        EventServer.bind(self.grow, SnakeFruitCollisionEvent)
        EventServer.bind(self.inputThreatement.threat, KeyBoardEvent)
        EventServer.bind(self.movement.speed_up, SnakeSizeEvent)

    def grow(self, event):
        x = self.body[len(self.body) - 1][0] - 1
        y = self.body[len(self.body) - 1][1] - 1
        self.body.append([x, y])

    def update(self):
        self.movement.update_speed()
        self.movement.walk_body()
        self.movement.walk_head()
        EventServer.pool(SnakeCoordEvent(self.body[0][0], self.body[0][1]))
        EventServer.pool(SnakeSizeEvent(len(self.body)))
        EventServer.pool(SnakeBodyEvent(self.body))

    def render(self, drawer: Drawer):
        for i in self.body:
            drawer.draw_pixel(i[0], i[1], (0, 50, 255))

class _Snake_Movement:
    def __init__(self, snake: Snake) -> None:
        self.snake = snake
        self.velocity = [0, 0]
        self.speed = 10
    
    def speed_up(self, event: SnakeSizeEvent):
        self.speed = 10 + growth(event.size, 55, 20)
    
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
        angle = self.__get_sin_cos(sk.body[i - 1], sk.body[i])
        sk.body[i][0] += angle[0] * self.speed * DeltaTime.get()
        sk.body[i][1] += angle[1] * self.speed * DeltaTime.get()
    
    def __get_sin_cos(self, a, b):
        xdis = a[0] - b[0] 
        ydis = a[1] - b[1]
        dis = math.sqrt(xdis * xdis + ydis * ydis)
        return [xdis / dis, ydis / dis]
            


class _Snake_InputThreatement:
    def __init__(self, snake: Snake) -> None:
        self.snake = snake

    def threat(self, event: KeyBoardEvent):
        self.snake.input = [0, 0]
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.snake.input[0] = 1
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.snake.input[0] = -1
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.snake.input[1] = -1
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.snake.input[1] = 1