import pygame
from entities.window import Window
from resources.drawer import Drawer
import game_object
from entities.snake import Snake
from resources.counter import Counter
import time
from resources.fruit_generator import FruitGenerator
from resources.window_closing_handler import WindowClosingHandler
from resources.input_server import InputServer
from resources.snake_fruit_collision import SnakeFruitCollision

size = (700, 700)
scale = 20

win = Window('a literal python kkkk', size)
draw = Drawer(scale, win.screen)
snake = Snake()
fruit_generator = FruitGenerator()
snake_fruit_collision = SnakeFruitCollision()
fruit_generator.size = (size[0] / scale, size[1] / scale)
input_server = InputServer()

window_event_handler = WindowClosingHandler()
game_object.GameObject.global_setup()

while True:
    Counter.set_start()
    win.update()
    win.screen.fill((0, 0, 0))
    Counter.set_end()
    game_object.GameObject.global_update()
    game_object.GameObject.global_render(draw)
