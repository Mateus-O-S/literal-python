from visual.drawer import Drawer
from visual.window import Window

class VisualComponents:
    instance = None

    def __init__(self) -> None:
        VisualComponents.instance = self
        
        self.size = (700, 700)
        self.max_scale = 20
        self.min_scale = 6.5
        
        self.win = Window('a literal python kkkk', self.size)
        self.draw = Drawer(self.max_scale, self.win.screen)