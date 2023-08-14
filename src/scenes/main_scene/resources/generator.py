from visual.drawer import Drawer
from game_object import GameObject
import random
from events.event import EventServer
from events.snake_fruit_collision_event import SnakeFruitCollisionEvent
from visual.visual import VisualComponents
from events.snake_size_event import SnakeSizeEvent
from scenes.main_scene.resources.growth_function import growth
from scenes.main_scene.entities.fruit import Fruit

class Generator(GameObject):
    def __init__(self, visual: VisualComponents, type):
        super().__init__()
        self.max = 100
        self.min = 0
        self.visual = visual
        self.type = type

    def update(self):
        if len(GameObject.get_type(self.type)) < self.max:
            x, y = self.__get_random_position()
            fruit = self.type(x, y)
            fruit.setup()
    
    def __get_random_position(self):
        width = self.visual.size[0] / self.visual.draw.scale
        x = random.randrange(1, int(width))

        height = self.visual.size[1] / self.visual.draw.scale
        y = random.randrange(1, int(height))

        return (x, y)