from scenes.scene import Scene
from game_object import GameObject
from visual.visual import VisualComponents
from default_resources.window_closing_handler import WindowClosingHandler
from default_resources.input_server import InputServer
from scenes.lose_scene.entities.title import Title
from scenes.lose_scene.entities.start_button import StartButton

class LoseScene(Scene):
    def __init__(self, visual: VisualComponents):
        super().__init__(visual)
        self.window_closing_handler = WindowClosingHandler()
        self.title = Title(visual)
        self.button = StartButton(visual)
        self.input_server = InputServer()
        GameObject.global_setup()        
    
    def update(self):
        super().update()
        GameObject.global_update()
        