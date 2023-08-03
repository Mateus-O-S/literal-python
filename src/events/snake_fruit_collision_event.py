from events.event import Event

class SnakeFruitCollisionEvent(Event):
    def __init__(self, fruit):
        self.fruit = fruit