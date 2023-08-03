from scenes.scene import Scene
from game_object import GameObject
from visual.visual import VisualComponents
from default_resources.window_closing_handler import WindowClosingHandler
from default_resources.input_server import InputServer
from scenes.initial_scene.entities.title import Title
from scenes.initial_scene.entities.button import Button

class InitialScene(Scene):
    def __init__(self, visual: VisualComponents):
        super().__init__(visual)
        self.window_closing_handler = WindowClosingHandler()
        self.title = Title(visual)
        self.button = Button(visual)
        self.input_server = InputServer()
        GameObject.global_setup()        
    
    def update(self):
        super().update()
        GameObject.global_update()
        