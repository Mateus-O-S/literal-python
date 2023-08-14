from events.event import Event

class EnemyPartCoordEvent(Event):
    def __init__(self, x, y):
        self.x = x
        self.y = y