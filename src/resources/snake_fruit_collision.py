from game_object import GameObject
from events.fruits_coord_event import FruitCoordEvent
from events.snake_coord_event import SnakeCoordEvent
from events.snake_fruit_collision_event import SnakeFruitCollisionEvent
from events.event import EventServer

class SnakeFruitCollision(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.fruit_positions = []
        self.snake_position = (0, 0)

    def setup(self):
        EventServer.bind(self.set_fruits_position, FruitCoordEvent)
        EventServer.bind(self.set_snake_position, SnakeCoordEvent)
    
    def set_fruits_position(self, event: FruitCoordEvent):
        self.fruit_positions = event.fruits
    
    def set_snake_position(self, event: SnakeCoordEvent):
        self.snake_position = (event.x, event.y)
    
    def update(self):
        for fruit in self.fruit_positions:
            if self.__colliding(fruit, self.snake_position):
                EventServer.pool(SnakeFruitCollisionEvent(fruit))
    
    def __colliding(self, fruit, snake):
        return abs(fruit[0] - snake[0]) < 1 and \
                abs(fruit[1] - snake[1]) < 1