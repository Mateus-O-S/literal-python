from events.event import Event

class SnakeEvent(Event):
    def __init__(self, snake_body):
        self.snake_body = snake_body