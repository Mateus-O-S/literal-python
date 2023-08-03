from visual.visual import VisualComponents
from scenes.main_scene.main_scene import MainScene
from scenes.initial_scene.initial_scene import InitialScene
from events.game_start_event import GameStartEvent 
from events.event import EventServer
from game_object import GameObject
from scenes.lose_scene.lose_scene import LoseScene
from events.game_over_event import GameOverEvent
import pygame
import time

pygame.init()

visual = VisualComponents()

class App:
    app = InitialScene(visual)
    
    @staticmethod
    def setup():
        EventServer.bind(App.enter_game, GameStartEvent)
        EventServer.bind(App.enter_post_game, GameOverEvent)

    @staticmethod
    def enter_game(event):
        time.sleep(0.3)
        GameObject.clear_objects()
        EventServer.clear()
        App.setup()
        App.app = MainScene(visual)
    
    @staticmethod
    def enter_post_game(event):
        time.sleep(0.3)
        GameObject.clear_objects()
        EventServer.clear()
        App.setup()
        App.app = LoseScene(visual)


App.setup()

while True:
    App.app.update()