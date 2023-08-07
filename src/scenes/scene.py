from visual.visual import VisualComponents
import pygame

class Scene:
    def __init__(self, visual: VisualComponents):
        self.visual = visual

    def update(self):
        self.visual.win.update()
        self.visual.win.screen.fill((100, 200, 0))