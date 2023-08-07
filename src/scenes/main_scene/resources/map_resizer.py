from game_object import GameObject
from events.event import EventServer
from events.snake_size_event import SnakeSizeEvent
from visual.visual import VisualComponents
from scenes.main_scene.resources.growth_function import growth

class MapResizer(GameObject):
    def __init__(self, visual: VisualComponents):
        super().__init__()
        self.visual = visual
        EventServer.bind(self.on_snake_size, SnakeSizeEvent)

    def on_snake_size(self, event: SnakeSizeEvent):
        nscale = self.visual.max_scale * growth(-event.size, 40, 60)
        if nscale < self.visual.min_scale:
            self.visual.draw.scale = self.visual.min_scale
        else: 
            self.visual.draw.scale = nscale