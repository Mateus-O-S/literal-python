from scenes.main_scene.resources.drawer import Drawer
from game_object import GameObject
import random
from events.event import EventServer
from events.fruits_coord_event import FruitCoordEvent
from events.snake_fruit_collision_event import SnakeFruitCollisionEvent

class FruitGenerator(GameObject):
    def __init__(self):
        super().__init__()
        self.__fruits = []
        self.max_fruits = 20
        self.size = (100, 100)
    
    def setup(self):
        EventServer.bind(self.remove_fruit, SnakeFruitCollisionEvent)
    
    def remove_fruit(self, event: SnakeFruitCollisionEvent):
            self.__fruits.remove(event.fruit)
    
    def update(self):
        EventServer.pool(FruitCoordEvent(self.__fruits))
        if len(self.__fruits) < self.max_fruits:
            x = random.randrange(1, self.size[0])
            y = random.randrange(1, self.size[1])
            self.__fruits.append((x, y))

    def render(self, drawer: Drawer):
        for f in self.__fruits:
            drawer.draw_pixel(f[0], f[1], (255, 127, 0))