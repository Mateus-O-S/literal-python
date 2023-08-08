from events.event import Event

class SnakeBodyEvent(Event):
    def __init__(self, snake_body):
        self.snake_body = snake_body