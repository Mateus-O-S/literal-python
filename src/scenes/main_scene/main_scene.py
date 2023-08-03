import pygame
from scenes.main_scene.entities.window import Window
from scenes.main_scene.resources.drawer import Drawer
from game_object import GameObject
from scenes.main_scene.entities.snake import Snake
from scenes.main_scene.resources.counter import Counter
import time
from scenes.main_scene.resources.fruit_generator import FruitGenerator
from scenes.main_scene.resources.window_closing_handler import WindowClosingHandler
from scenes.main_scene.resources.input_server import InputServer
from scenes.main_scene.resources.snake_fruit_collision import SnakeFruitCollision
from scenes.scene import Scene

class MainScene(Scene):
    def __init__(self):
        self.size = (700, 700)
        self.scale = 20

        self.win = Window('a literal python kkkk', self.size)
        self.draw = Drawer(self.scale, self.win.screen)

    def setup(self):
        self.snake = Snake()
        
        self.fruit_generator = FruitGenerator()
        self.fruit_generator.size = (self.size[0] / self.scale,
                                self.size[1] / self.scale)
        
        self.snake_fruit_collision = SnakeFruitCollision()
        self.input_server = InputServer()

        self.window_event_handler = WindowClosingHandler()

        GameObject.global_setup()

    def update(self):
        Counter.set_start()
        self.win.update()
        self.win.screen.fill((0, 0, 0))
        Counter.set_end()
        GameObject.global_update()
        GameObject.global_render(self.draw)