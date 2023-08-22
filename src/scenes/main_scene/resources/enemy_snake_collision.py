from events.event import EventServer
from events.snake_coord_event import SnakeCoordEvent
from events.snake_body_event import SnakeBodyEvent
from events.enemy_event import EnemyEvent
from events.game_over_event import GameOverEvent
from events.destroy_enemy_part_event import DestroyEnemyPartEvent
from game_object import GameObject

class EnemySnakeCollision:
    def __init__(self) -> None:
        EventServer.bind(self.check_collision, EnemyEvent)
        EventServer.bind(self.__set_snake, SnakeBodyEvent)
        self.snake_body = []

    def __set_snake(self, event: SnakeBodyEvent):
        self.snake_body = event.snake_body

    def check_collision(self, event: EnemyEvent):
        for part in self.snake_body:
            for e_part in event.body:
                if self.__is_colliding(part, e_part):
                    EventServer.pool(DestroyEnemyPartEvent(e_part))
    
    def __is_colliding(self, a, b):
        return abs(a[0] - b[0]) < .5 and abs(a[1] - b[1]) < .5