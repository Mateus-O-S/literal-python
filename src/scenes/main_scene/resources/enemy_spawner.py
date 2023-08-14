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
from events.snake_size_event import SnakeSizeEvent
from scenes.main_scene.resources.growth_function import growth
from scenes.main_scene.entities.enemy_snake import EnemySnake
from scenes.main_scene.resources.generator import Generator
from visual.visual import VisualComponents

class EnemySpawner(Generator):
    def __init__(self, visual: VisualComponents):
        super().__init__(visual, EnemySnake)
        self.min = 0
        self.max = 5