from events.event import EventServer
from events.snake_coord_event import SnakeCoordEvent
from events.game_over_event import GameOverEvent
from visual.visual import VisualComponents

class SnakeMapCollision:
    def __init__(self, visuals: VisualComponents):
        self.visuals = visuals
        self.snake_coord = (1, 1)
        EventServer.bind(self.set_snake_coord, SnakeCoordEvent)

    def set_snake_coord(self, event: SnakeCoordEvent):
        xout = event.x < 0 or event.x > self.visuals.size[0]
        yout = event.y < 0 or event.y > self.visuals.size[1]
        if xout or yout:
            EventServer.pool(GameOverEvent())
            print("soap")