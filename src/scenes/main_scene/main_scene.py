import pygame
from game_object import GameObject
from scenes.main_scene.entities.player_snake import PlayerSnake
from scenes.main_scene.resources.delta_time import DeltaTime
import time
from scenes.main_scene.resources.fruit_generator import FruitGenerator
from default_resources.window_closing_handler import WindowClosingHandler
from default_resources.input_server import InputServer
from scenes.main_scene.resources.snake_fruit_collision import SnakeFruitCollision
from visual.visual import VisualComponents
from scenes.scene import Scene
from scenes.main_scene.resources.enemy_spawner import EnemySpawner
from scenes.main_scene.resources.map_resizer import MapResizer
from scenes.main_scene.resources.snake_map_collision import SnakeMapCollision
from scenes.main_scene.resources.snake_snake_collision import SnakeSnakeCollision
from scenes.main_scene.resources.snake_enemy_collision import SnakeEnemyCollision
from scenes.main_scene.resources.enemy_snake_collision import EnemySnakeCollision

class MainScene(Scene):
    def __init__(self, visual: VisualComponents):
        super().__init__(visual)
        
        self.snake = PlayerSnake()

        self.enemy_snake_collision = EnemySnakeCollision()

        self.snake_enemy_collision = SnakeEnemyCollision()

        self.enemy_spawner = EnemySpawner(visual)

        self.snale_snake_collision = SnakeSnakeCollision()

        self.snake_fruit_collision = SnakeFruitCollision()
        
        self.fruit_generator = FruitGenerator(visual)

        self.snake_map_collision = SnakeMapCollision(visual)
        
        self.map_resizer = MapResizer(visual)

        self.input_server = InputServer()

        self.window_event_handler = WindowClosingHandler()

        GameObject.global_setup()

    def update(self):
        DeltaTime.set_start()
        super().update()
        DeltaTime.set_end()
        GameObject.global_update()
        GameObject.global_render(self.visual.draw)