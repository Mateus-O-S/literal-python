from visual.drawer import Drawer
from game_object import GameObject
import random
from events.event import EventServer
from events.snake_fruit_collision_event import SnakeFruitCollisionEvent
from visual.visual import VisualComponents
from events.snake_size_event import SnakeSizeEvent
from scenes.main_scene.resources.growth_function import growth
from scenes.main_scene.resources.generator import Generator
from scenes.main_scene.entities.fruit import Fruit

class FruitGenerator(Generator):
    def __init__(self, visual: VisualComponents):
        super().__init__(visual, Fruit)
        self.max = 10
        self.min = 2