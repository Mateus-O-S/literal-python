from events.event import EventServer
from events.snake_body_event import SnakeBodyEvent
from events.game_over_event import GameOverEvent

class SnakeSnakeCollision:
    def __init__(self) -> None:
        EventServer.bind(self.check_collision, SnakeBodyEvent)

    def check_collision(self, event: SnakeBodyEvent):
        head = event.snake_body[0]
        for part in range(2, len(event.snake_body) - 1):
            if (self.__is_colliding(head, event.snake_body[part])):
                EventServer.pool(GameOverEvent())
    
    def __is_colliding(self, a, b):
        return abs(a[0] - b[0]) < .5 and abs(a[1] - b[1]) < .5