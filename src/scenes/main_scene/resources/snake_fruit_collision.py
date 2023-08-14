from game_object import GameObject
from events.snake_coord_event import SnakeCoordEvent
from events.snake_fruit_collision_event import SnakeFruitCollisionEvent
from scenes.main_scene.entities.fruit import Fruit
from events.event import EventServer

class SnakeFruitCollision(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.snake_position = (0, 0)

    def setup(self):
        EventServer.bind(self.set_snake_position, SnakeCoordEvent)
    
    def set_snake_position(self, event: SnakeCoordEvent):
        self.snake_position = (event.x, event.y)
    
    def update(self):
        for fruit in GameObject.get_type(Fruit):
            if self.__colliding([fruit.x, fruit.y], self.snake_position):
                EventServer.pool(SnakeFruitCollisionEvent(fruit))
    
    def __colliding(self, fruit, snake):
        return abs(fruit[0] - snake[0]) < 1 and \
                abs(fruit[1] - snake[1]) < 1