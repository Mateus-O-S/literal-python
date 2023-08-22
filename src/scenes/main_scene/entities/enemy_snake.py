from scenes.main_scene.entities.snake import Snake
from events.keyboard_event import KeyBoardEvent
from events.event import EventServer
from events.snake_coord_event import SnakeCoordEvent
from events.keyboard_event import KeyBoardEvent
from events.snake_body_event import SnakeBodyEvent
from events.snake_size_event import SnakeSizeEvent
from events.enemy_event import EnemyEvent
from scenes.main_scene.resources.get_sin_cos import get_sin_cos
from scenes.main_scene.resources.generator import Generator
from events.destroy_enemy_part_event import DestroyEnemyPartEvent
from visual.visual import VisualComponents
import pygame
import math
import random

class EnemySnake(Snake):
    def __init__(self, x, y):
        super().__init__()
        super().__init__()
        self.body: list[list[-1, -1]] = [[0, 0], [1, 1]]
        self.__apply(x, y)
        self.movement.speed = 10
        self.color = (14, 27, 153)
        self.target = [10, 10]
    
    def __apply(self, x, y):
        for b in range(len(self.body)):
            self.body[b] = [x + self.body[b][0], y + self.body[b][1]]
    
    def setup(self):
        super().setup()
        EventServer.bind(self.remove_part, DestroyEnemyPartEvent)

    def remove_part(self, event: DestroyEnemyPartEvent):
        if event.part in self.body:
            self.body.remove(event.part)    
    
    def update(self):
        super().update()
        if len(self.body) > 1:
            EventServer.pool(EnemyEvent(self.body))

            self.input = get_sin_cos(self.target, self.body[0])

            if (self.__reached_target()):
                self.target = self.__generate_target()
    
    def __reached_target(self):
        x = abs(self.body[0][0] - self.target[0]) < .5
        y = abs(self.body[0][1] - self.target[1]) < .5
        return x and y

    def __generate_target(self):
        visual = VisualComponents.instance
        
        width = visual.size[0] / visual.draw.scale
        x = random.randrange(1, int(width))

        height = visual.size[1] / visual.draw.scale
        y = random.randrange(1, int(height))

        return [x, y]
