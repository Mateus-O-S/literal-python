from events.event import EventServer
from events.snake_coord_event import SnakeCoordEvent
from events.enemy_coord_event import EnemyPartCoordEvent
from events.game_over_event import GameOverEvent

class SnakeEnemyCollision:
    def __init__(self) -> None:
        EventServer.bind(self.check_collision, EnemyPartCoordEvent)
        EventServer.bind(self.__set_snake, SnakeCoordEvent)
        self.snake_coord = [0, 0]

    def __set_snake(self, event: SnakeCoordEvent):
        self.snake_coord = [event.x, event.y]

    def check_collision(self, event: EnemyPartCoordEvent):
        if self.__is_colliding(self.snake_coord, [event.x, event.y]):
            EventServer.pool(GameOverEvent())
    
    def __is_colliding(self, a, b):
        return abs(a[0] - b[0]) < .5 and abs(a[1] - b[1]) < .5