from resources.drawer import Drawer

class GameObject:
    __game_objects = []

    @staticmethod
    def global_setup():
        for obj in GameObject.__game_objects:
            obj.setup()
    
    @staticmethod
    def global_update():
        for obj in GameObject.__game_objects:
            obj.update()
    
    @staticmethod
    def global_render(drawer: Drawer):
        for obj in GameObject.__game_objects:
            obj.render(drawer)

    def __init__(self):
        GameObject.__game_objects.append(self)

    def setup(self):
        pass
    
    def update(self):
        pass

    def render(self, drawer: Drawer):
        pass