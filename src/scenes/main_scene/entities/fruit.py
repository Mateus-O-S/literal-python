from visual.drawer import Drawer
from game_object import GameObject
import random
from events.event import EventServer
from events.snake_fruit_collision_event import SnakeFruitCollisionEvent
from visual.visual import VisualComponents
from events.snake_size_event import SnakeSizeEvent
from scenes.main_scene.resources.growth_function import growth

class Fruit(GameObject):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
    
    def setup(self):
        EventServer.bind(self.remove_fruit, SnakeFruitCollisionEvent)
    
    def remove_fruit(self, event: SnakeFruitCollisionEvent):
        x = event.fruit.x == self.x
        y = event.fruit.y == self.y
        if x and y:
            self.destroy()

    def render(self, drawer: Drawer):
        drawer.draw_pixel(self.x, self.y, (44, 61, 230))