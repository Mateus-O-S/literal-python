from events.event import Event

class SnakeCoordEvent(Event):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y